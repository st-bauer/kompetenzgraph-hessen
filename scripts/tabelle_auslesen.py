"""Liest Schwerpunkt-Tabellen mit Spalten über Wortkoordinaten (pdftotext -bbox) als Entwurf.

  felder: Spalten sind Inhaltsfelder, Abschnitte „Lernzeitbezogen 6/8“ wechseln die Stufe (Kath. Religion, Kap. 8.3)
  stufen: Spalten sind Jahrgangsstufen, links stehen die Inhaltsfelder (Mathematik, Kap. 7.3)

Spalten werden an der Lage der Aufzählungspunkte erkannt.
Beispiel:
  python3 scripts/tabelle_auslesen.py katholische_religion_realschule 35 37 "Katholische Religion" felder
  python3 scripts/tabelle_auslesen.py mathematik_realschule 26 29 Mathematik stufen
Ausgabe: CSV-Zeilen (Inhaltsfeld, Stufe, Schwerpunkt, Seite).
"""
import csv, glob, html, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUNKTE = ("•", "", "■")


def norm(s):
    return re.sub(r"[^a-zäöüß0-9]", "", s.lower())


def woerter(pdf, s):
    out = subprocess.run(["pdftotext", "-bbox", "-f", str(s), "-l", str(s), pdf, "-"], capture_output=True, text=True).stdout
    return [(float(a), float(b), float(c), html.unescape(t)) for a, b, c, t in
            re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="[\d.]+">(.*?)</word>', out)]


def spalten_von(ws):
    xs = sorted(x for x, y, x2, t in ws if t in PUNKTE)
    starts = []
    for x in xs:
        if not starts or x - starts[-1][-1] > 15:
            starts.append([x])
        else:
            starts[-1].append(x)
    return [min(g) for g in starts if len(g) >= 2]


def zeilen(ws):
    """Wörter einer Spalte zu Zeilen zusammenfassen: erst nach Höhe bündeln, dann von links nach rechts."""
    out = []
    for w in sorted(ws, key=lambda w: w[1]):
        if out and abs(out[-1][0] - w[1]) < 4.5:  # Aufzählungspunkt sitzt etwas tiefer als sein Text
            out[-1][1].append(w)
        else:
            out.append([w[1], [w]])
    return [(y, " ".join(t for x, yy, x2, t in sorted(g))) for y, g in out]


def main():
    name, von, bis, fach, modus = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
    felder = [r["inhaltsfeld"] for r in csv.DictReader(open(os.path.join(ROOT, "data", "inhaltsfelder_sek1.csv"), encoding="utf-8")) if r["fach"] == fach]
    pdf = glob.glob(os.path.join(ROOT, "quellen", "pdf", name + "_kerncurriculum.pdf"))[0]
    items, stufe, titel_spalten, stufen, letztes = [], "Abschluss", None, [], None
    for s in range(von, bis + 1):
        ws = [w for w in woerter(pdf, s) if 60 < w[1] < 790 and w[3] != str(s)]  # Kopf- und Fußzeile, Seitenzahl weg
        lz = [i for i, w in enumerate(ws) if w[3] == "Lernzeitbezogen"]
        cols = spalten_von(ws)
        if len(cols) < 2:
            continue
        rand = cols[0] - 4
        # Abschnittsmarken „Lernzeitbezogen 6/8“ (nur Modus felder)
        marken = sorted((y, f"am Ende der Jahrgangsstufe {ws[i + 1][3]}") for i, (x, y, x2, t) in enumerate(ws[:-1]) if t == "Lernzeitbezogen")
        if modus == "felder":
            kopf = [(x, t) for x, y, x2, t in ws]
            zeilen_kopf = zeilen([w for w in ws if w[3] not in PUNKTE])
            for y, text in zeilen_kopf:
                treffer = sum(1 for f in felder if f in text)
                if treffer >= 4:
                    titel_spalten = None  # Spaltentitel aus Reihenfolge der Inhaltsfelder
            titel = felder if len(cols) == len(felder) else None
            if not titel:
                continue
        # Wörter den Spalten zuordnen
        spalte = {i: [] for i in range(len(cols))}
        links = []
        for j, w in enumerate(ws):
            if any(j in (i, i + 1) for i in lz):
                continue  # Abschnittsmarke gehört zu keiner Spalte
            if w[0] < rand:
                links.append(w)
                continue
            i = max(j for j, c in enumerate(cols) if w[0] >= c - 4)
            spalte[i].append(w)
        # Zeilenbeschriftung links (Modus stufen): Inhaltsfelder mit y-Position
        reihe = []
        if modus == "stufen":
            for y, text in zeilen(links):
                t = [f for f in felder if norm(text) and norm(f).startswith(norm(text))]
                if t:
                    reihe.append((y, max(t, key=len)))
            if letztes and (not reihe or reihe[0][0] > 90):
                reihe.insert(0, (0, letztes))  # Inhaltsfeld läuft von der Vorseite weiter
            kopfzeile = [w for w in ws if w[3] == "Jahrgangsstufe" and ws.index(w) + 1 < len(ws) and re.match(r"[\d/]+$", ws[ws.index(w) + 1][3])]
            if len(kopfzeile) >= 2:
                stufen = [f"Jahrgangsstufe {ws[ws.index(w) + 1][3]}" for w in sorted(kopfzeile)]  # sonst Stufen der Vorseite
        for i, c in enumerate(cols):
            cur = None
            for y, text in zeilen(spalte[i]):
                if modus == "felder":
                    feld = titel[i]
                    st = next((m for my, m in reversed(marken) if my < y), stufe if not marken or y < marken[0][0] else stufe)
                    st = [m for my, m in marken if my < y][-1] if [m for my, m in marken if my < y] else stufe
                else:
                    r = [f for ry, f in reihe if ry <= y + 3]
                    feld = r[-1] if r else None
                    st = stufen[i] if i < len(stufen) else f"Spalte {i + 1}"
                if text.startswith(PUNKTE):
                    cur = [feld, st, text.lstrip("•■ ").strip(), s]
                    items.append(cur)
                elif cur is not None and cur[0] == feld:
                    cur[2] = (cur[2][:-1] if cur[2].endswith("-") and text[:1].islower() else cur[2] + " ") + text
        if modus == "stufen" and reihe:
            letztes = reihe[-1][1]
        if marken and modus == "felder":
            stufe = marken[-1][1]
    w = csv.writer(sys.stdout)
    for feld, st, text, seite in items:
        if feld:
            w.writerow([feld, st, re.sub(r"\s+", " ", text).strip().rstrip(",;"), f"S. {seite}"])


if __name__ == "__main__":
    main()
