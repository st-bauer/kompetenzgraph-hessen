"""Liest die Schwerpunkt-Übersicht (vierspaltige Tabelle in Kap. 7.2 bzw. 7.3) aus quellen/txt als Entwurf.

Beispiel:
  python3 scripts/schwerpunkte_auslesen.py biologie_realschule 41 48 Biologie

Ausgabe: CSV-Zeilen (Inhaltsfeld, Spalte 1 oder 2, Schwerpunkt, Seite) zum Prüfen von Hand.
Spalte 1 ist die frühe Stufe, Spalte 2 die Stufe bis zum Abschluss. Kürzen und Prüfen am PDF bleibt Handarbeit.
"""
import csv, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def felder(fach):
    rows = csv.DictReader(open(os.path.join(ROOT, "data", "inhaltsfelder_sek1.csv"), encoding="utf-8"))
    return [r["inhaltsfeld"] for r in rows if r["fach"] == fach]


def norm(s):
    return re.sub(r"[\s’']+", "", s).lower()


def main():
    name, von, bis, fach = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    pages = open(glob.glob(os.path.join(ROOT, "quellen", "txt", name + "_kerncurriculum.txt"))[0], encoding="utf-8").read().replace("\uf0b7", "•").split("\f")  # U+F0B7: Aufzählungspunkt aus Symbolschrift
    titel = {norm(f): f for f in felder(fach)}
    feld, grenzen = None, None
    items = []  # [feld, spalte, text, seite]
    offen = {1: None, 2: None}
    for s in range(von, bis + 1):
        for z in pages[s - 1].splitlines():
            if z.count("Inhaltliche Schwerpunkte") == 2:
                a = z.index("Inhaltliche"); b = z.index("Bezüge"); c = z.index("Inhaltliche", a + 5); d = z.index("Bezüge", b + 5)
                grenzen = (b - 1, c - 9, d - 7)
                continue
            if not grenzen or not z.strip():
                continue
            if re.search(r"K A P|Kerncurriculum Hessen|Kultusministerium|Jahrgangsstufe|Lernjahr|Bezüge zu Kompetenz", z):
                continue
            t = norm(z)
            treffer = [v for k, v in titel.items() if k and (t == k or (len(t) > 12 and k.startswith(t)))]
            if treffer and len(z) - len(z.lstrip()) > 20:
                feld = treffer[0]; offen = {1: None, 2: None}
                continue
            if feld is None or re.match(r"^\s*\d+\s*$", z):
                continue
            for sp, (x0, x1) in ((1, (0, grenzen[0])), (2, (grenzen[1], grenzen[2]))):
                teil = re.sub(r"(\s{2,}\S)+$", "", z[x0:x1]).strip()  # Einzelbuchstaben aus senkrechtem Seitentext
                if not teil:
                    continue
                if teil.startswith("•"):
                    offen[sp] = [feld, sp, teil.lstrip("• ").strip(), s]
                    items.append(offen[sp])
                elif offen[sp] is not None:
                    alt = offen[sp][2]
                    if alt.endswith("-") and teil[:1].islower():
                        offen[sp][2] = alt[:-1] + teil
                    elif teil.startswith("–"):
                        offen[sp][2] = alt + (" " if alt.endswith(":") else "; ") + teil.lstrip("– ").strip()
                    else:
                        offen[sp][2] = alt + " " + teil
    w = csv.writer(sys.stdout)
    for f, sp, text, seite in items:
        w.writerow([f, sp, re.sub(r"\s+", " ", text), f"S. {seite}"])


if __name__ == "__main__":
    main()
