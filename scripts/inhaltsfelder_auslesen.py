"""Liest beschriebene Inhaltsfelder (Kap. 6, 7.1, 7.2) aus quellen/txt und leitet Schwerpunkte als Entwurf ab.

Beispiel:
  python3 scripts/inhaltsfelder_auslesen.py ethik_realschule 22 23 Ethik

Je Inhaltsfeld: vorhandene Aufzählungspunkte, sonst der Satz „Im Mittelpunkt … steht/stehen …“
und „Bezugspunkte sind …“. Ausgabe als CSV-Zeilen (Inhaltsfeld, Schwerpunkt, Seite) zum Prüfen.
"""
import csv, glob, os, re, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KOPF = re.compile(r"K A P|Kerncurriculum Hessen|Kultusministerium|Sekundarstufe I –|^\s*\d+\s*$|^\s*[A-ZÄÖÜ](\s?[A-ZÄÖÜ]){3,}\s*$")
PUNKT = re.compile("^\\s*([•\\-–\\x02]|[\uf000-\uf8ff])\\s*")  # auch Aufzählungszeichen aus Symbolschriften (U+0002, Privatbereich)


def norm(s):
    return re.sub(r"[^a-zäöüß]", "", s.lower())


def bloecke(name, von, bis, fach):
    felder = [r["inhaltsfeld"] for r in csv.DictReader(open(os.path.join(ROOT, "data", "inhaltsfelder_sek1.csv"), encoding="utf-8")) if r["fach"] == fach]
    pages = open(glob.glob(os.path.join(ROOT, "quellen", "txt", name + "_kerncurriculum.txt"))[0], encoding="utf-8").read().split("\f")
    zeilen = [(s, z) for s in range(von, bis + 1) for z in pages[s - 1].splitlines() if z.strip() and not KOPF.search(z)]
    start = [i for i, (s, z) in enumerate(zeilen) if z.strip() == "Inhaltsfelder"]
    zeilen = zeilen[start[-1] + 1:] if start else zeilen  # erst ab der Tabellenüberschrift „Inhaltsfelder“
    # Spaltenbeginn der Beschreibung: häufigster Einzug der Folgezeilen
    einz = Counter(len(z) - len(z.lstrip()) for s, z in zeilen if z.startswith("   "))
    c = max((k for k in einz if 12 <= k <= 40), key=lambda k: einz[k], default=28)
    # Beginn einer rechten Randspalte (z. B. „Bezüge zu Kompetenzbereichen“): häufigste Startposition nach großer Lücke
    rechts = Counter(m.start(1) for s, z in zeilen for m in re.finditer(r"\s{2,}(\S)", z) if m.start(1) > c + 60)
    r = max(rechts, key=rechts.get) - 2 if rechts and max(rechts.values()) >= 4 else 10 ** 4

    def kopf_von(links):
        w = links.split()
        for k in range(len(w), 0, -1):
            n = norm(" ".join(w[:k]))
            t = [f for f in felder if len(n) >= 4 and norm(f).startswith(n)]
            if t:
                return max(t, key=len), " ".join(w[:k]), " ".join(w[k:])
        return None, "", links

    out, akt, kopf = [], None, ""
    for s, z in zeilen:
        z = z[:r]
        if z[:1].strip():
            teile = re.split(r"\s{2,}", z.strip(), maxsplit=1)
            links, rest = (teile[0], teile[1] if len(teile) > 1 else "")
            probe = norm(kopf + links)
            if akt and probe and norm(akt["feld"]).startswith(probe) and len(probe) <= len(norm(akt["feld"])):
                kopf += links
                mitte = rest
            else:
                feld, k, ueber = kopf_von(links)
                if feld:
                    akt = {"feld": feld, "seite": s, "text": []}
                    out.append(akt)
                    kopf = k
                    mitte = (ueber + " " + rest).strip()
                else:
                    mitte = z.strip()
        else:
            mitte = z.strip()
        if akt and mitte:
            akt["text"].append(mitte)
    return out


def schwerpunkte(text):
    zeilen = text
    punkte, cur = [], None
    for z in zeilen:
        if PUNKT.match(z):
            cur = PUNKT.sub("", z).strip()
            punkte.append(cur)
        elif cur is not None and (z[:1].islower() or not punkte[-1].rstrip().endswith((",", ";", ".", ":"))):
            punkte[-1] = (punkte[-1][:-1] if punkte[-1].endswith("-") else punkte[-1] + " ") + z.strip()
        else:
            cur = None
    voll = re.sub(r"(\w)- (\w+)", lambda m: m.group(1) + ("- " if m.group(2) in ("und", "oder", "bzw", "sowie") else "-" if m.group(2)[0].isupper() else "") + m.group(2), " ".join(zeilen))
    voll = re.sub(r"\s+", " ", voll)
    if len(punkte) >= 2:
        return [re.sub(r"\s+", " ", p).rstrip(",;.") for p in punkte]
    erg = []
    for satz in re.split(r"(?<=[.:])\s+(?=[A-ZÄÖÜ])", voll):
        m = re.search(r"Im Mittelpunkt[^.]*?\b(?:steht|stehen)\s+(.*)", satz)
        if m:
            erg.append(m.group(1).rstrip(". :"))
        m = re.search(r"Bezugspunkte sind (?:dabei )?(?:insbesondere )?(.*)", satz)
        if m:
            erg.append("Bezugspunkte: " + m.group(1).rstrip(". "))
    if not erg:
        erg = [re.split(r"(?<=\.)\s", voll)[0][:180]]
    return [e[:1].upper() + e[1:] for e in erg]


def main():
    name, von, bis, fach = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    w = csv.writer(sys.stdout)
    for b in bloecke(name, von, bis, fach):
        for sp in schwerpunkte(b["text"]):
            w.writerow([b["feld"], sp, f"S. {b['seite']}"])


if __name__ == "__main__":
    main()
