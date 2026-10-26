import csv, json, sys, os
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "data"))
import kerncurricula as b


def lies(name):
    return list(csv.DictReader(open(os.path.join(ROOT, "data", name), encoding="utf-8")))


# Fächer in Reihenfolge der Anordnung im Kreis (benachbarte Fächer liegen nebeneinander)
FAECHER = [(r["key"], r["fach"], r["kurz"], r["farbe"]) for r in lies("faecher.csv")]
KEY = {f: k for k, f, _, _ in FAECHER}
SF = {"hs": "Hauptschule", "rs": "Realschule", "gy": "Gymnasium"}
EARLY = {b.B56, b.C1, b.P1}

# PDF-Adressen je Fach und Schulform
url = {}
for q in lies("quellen_sek1.csv"):
    if q["dokument"] == "Kerncurriculum" and q["fach"] in KEY:
        sf = {"Hauptschule": "hs", "Realschule": "rs"}.get(q["schulform"], "gy")
        url.setdefault(q["fach"], {})[sf] = q["url"]

nodes, links = [], []
pilot = {(fach, feld): (bk, hin) for fach, bk, feld, seite, hin in b.IF}

if_id = {}
for i, r in enumerate(lies("inhaltsfelder_sek1.csv"), 1):
    fach, feld = r["fach"], r["inhaltsfeld"]
    seiten = {sf: r["seite_" + sf] for sf in SF if r["seite_" + sf]}
    bk, hin = pilot.get((fach, feld), (r["bereich"], ""))
    hin = "; ".join(x for x in (r["hinweis"], hin) if x)
    nid = f"IF-{i:03d}"
    if_id[(fach, feld)] = nid
    nodes.append({"id": nid, "t": "if", "f": KEY[fach], "label": feld, "bk": r["bereich"] or bk,
                  "sf": list(seiten), "seiten": seiten, "hin": hin})
fehlt = [k for k in pilot if k not in if_id]
assert not fehlt, f"Pilot-Inhaltsfelder fehlen in inhaltsfelder_sek1.csv: {fehlt}"

for k, fach, kurz, farbe in FAECHER:
    sf = sorted({s for n in nodes if n["t"] == "if" and n["f"] == k for s in n["sf"]}, key=list(SF).index)
    nodes.append({"id": "F-" + k, "t": "fach", "f": k, "label": fach, "kurz": kurz, "farbe": farbe,
                  "sf": sf, "url": url.get(fach, {})})
for n in list(nodes):
    if n["t"] == "if":
        links.append({"s": "F-" + n["f"], "t": n["id"], "k": "hat"})

# Schwerpunkte: bisher nur Pilot, Fassung Gymnasium
for i, (fach, feld, stufe, sp, seite) in enumerate(b.SP, 1):
    nid = f"SP-{i:03d}"
    st = "frueh" if stufe in EARLY else ("spaet" if stufe == b.B910 else "ohne")
    nodes.append({"id": nid, "t": "sp", "f": KEY[fach], "label": sp, "feld": feld,
                  "stufe": stufe, "st": st, "seite": seite, "sf": ["gy"]})
    links.append({"s": if_id[(fach, feld)], "t": nid, "k": "hat"})

for j, (thema, items) in enumerate(b.AK, 1):
    tid = f"TH-{j:02d}"
    nodes.append({"id": tid, "t": "thema", "f": "thema", "label": thema})
    for fach, feld, stich, stufe in items:
        links.append({"s": tid, "t": if_id[(fach, feld)], "k": "vorschlag", "stich": stich, "stufe": stufe})

# belegte Querbezüge zwischen Fächern
beleg = [
    ("bio", "che", "Einheitlich definierte Kompetenzbereiche der Naturwissenschaften", "Kap. 3"),
    ("bio", "phy", "Einheitlich definierte Kompetenzbereiche; Basiskonzept Energie auch in Biologie", "Ph Kap. 3, Kap. 5 S. 18"),
    ("che", "phy", "Einheitlich definierte Kompetenzbereiche; Basiskonzept Energie auch in Chemie", "Ph Kap. 3, Kap. 5 S. 18"),
    ("phy", "erd", "Zusammenarbeit mit Erdkunde bietet sich an (System Erde und Weltraum)", "Ph Kap. 3, S. 12"),
    ("erd", "pow", "Gemeinsames gesellschaftswissenschaftliches Aufgabenfeld, Lernbereich Gesellschaftslehre möglich", "Ek S. 12 f., PoWi S. 13 f."),
]
for a, c, txt, fund in beleg:
    links.append({"s": "F-" + a, "t": "F-" + c, "k": "beleg", "stich": txt, "fund": fund})

# BNE: Aufgabengebiet nach § 6 Abs. 4 HSchG, Belege aus dem KC, SDG-Zuordnung als Vorschlag
nodes.append({"id": "BNE", "t": "bne", "f": "bne", "label": "Bildung für nachhaltige Entwicklung"})
for r in lies("bne_belege.csv"):
    seiten = {sf: r["seite_" + sf] for sf in SF if r["seite_" + sf]}
    quelle = if_id[(r["fach"], r["inhaltsfeld"])] if r["inhaltsfeld"] else "F-" + KEY[r["fach"]]
    links.append({"s": quelle, "t": "BNE", "k": "bne", "stich": r["zitat"], "seiten": seiten})
for r in lies("bne_sdg.csv"):
    nodes.append({"id": "SDG-" + r["nr"], "t": "sdg", "f": "sdg", "nr": int(r["nr"]),
                  "label": r["titel"], "farbe": r["farbe"]})
for r in lies("bne_vorschlaege.csv"):
    links.append({"s": "SDG-" + r["sdg"], "t": if_id[(r["fach"], r["inhaltsfeld"])], "k": "sdg", "stich": r["stichwort"]})

out = {
    "stand": "26.10.2026",
    "faecher": [{"k": k, "label": f, "kurz": kurz, "farbe": c} for k, f, kurz, c in FAECHER],
    "schulformen": SF,
    "nodes": nodes, "links": links,
    "querbezuege": [list(q) for q in b.QB],
    "bne": {
        "grundlage": "§ 6 Abs. 4 Hessisches Schulgesetz",
        "text": "Besondere Bildungs- und Erziehungsaufgaben der Schulen werden in Aufgabengebieten erfasst. "
                "Diese sind insbesondere Umweltbildung und Bildung für nachhaltige Entwicklung, … "
                "Aufgabengebiete werden fachübergreifend unterrichtet. Sie können in Form themenbezogener Projekte "
                "unter Berücksichtigung der fachbezogenen Lernziele und Methoden auch jahrgangs- und schulformübergreifend unterrichtet werden.",
        "quelle": "Nichtamtliche Lesefassung des HSchG, Stand 01.08.2026",
        "url": "https://kultus.hessen.de/sites/kultus.hessen.de/files/2026-08/nichtamtliche_lesefassung_schulgesetz_stand_20260801_.pdf",
        "info": "https://kultus.hessen.de/unterricht/bildung-fuer-nachhaltige-entwicklung",
    },
}
p = os.path.join(ROOT, "output", "data.json")
json.dump(out, open(p, "w"), ensure_ascii=False)
print(Counter(n["t"] for n in nodes), Counter(l["k"] for l in links))

# Webseite bauen: Daten in Vorlage einsetzen
tpl = open(os.path.join(ROOT, "web", "template.html"), encoding="utf-8").read()
html = tpl.replace("/*__DATA__*/null", json.dumps(out, ensure_ascii=False))
os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
open(os.path.join(ROOT, "docs", "index.html"), "w", encoding="utf-8").write(html)
open(os.path.join(ROOT, "docs", ".nojekyll"), "w").close()
print("docs/index.html geschrieben (wird von GitHub Pages ausgeliefert)")
