import csv, json, sys, os
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "data"))
import kerncurricula as b


def lies(name):
    return list(csv.DictReader(open(os.path.join(ROOT, "data", name), encoding="utf-8")))


# Fächer in Reihenfolge der Anordnung im Kreis (benachbarte Fächer liegen nebeneinander)
FAECHER = [(r["key"], r["fach"], r["kurz"], r["farbe"]) for r in lies("faecher.csv")]
GRUPPE = {r["key"]: r["gruppe"] for r in lies("faecher.csv")}
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

# Suchwörter je Inhaltsfeld für die Themenwerkstatt (scripts/build_suchindex.py)
ip = os.path.join(ROOT, "data", "suchindex.json")
SUCH = json.load(open(ip, encoding="utf-8")) if os.path.exists(ip) else {}

if_id = {}
for i, r in enumerate(lies("inhaltsfelder_sek1.csv"), 1):
    fach, feld = r["fach"], r["inhaltsfeld"]
    seiten = {sf: r["seite_" + sf] for sf in SF if r["seite_" + sf]}
    bk, hin = pilot.get((fach, feld), (r["bereich"], ""))
    hin = "; ".join(x for x in (r["hinweis"], hin) if x)
    nid = f"IF-{i:03d}"
    if_id[(fach, feld)] = nid
    nodes.append({"id": nid, "t": "if", "f": KEY[fach], "label": feld, "bk": r["bereich"] or bk,
                  "sf": list(seiten), "seiten": seiten, "hin": hin, "w": SUCH.get(f"{fach}|{feld}", "")})
fehlt = [k for k in pilot if k not in if_id]
assert not fehlt, f"Pilot-Inhaltsfelder fehlen in inhaltsfelder_sek1.csv: {fehlt}"

for k, fach, kurz, farbe in FAECHER:
    sf = sorted({s for n in nodes if n["t"] == "if" and n["f"] == k for s in n["sf"]}, key=list(SF).index)
    nodes.append({"id": "F-" + k, "t": "fach", "f": k, "label": fach, "kurz": kurz, "farbe": farbe,
                  "sf": sf, "url": url.get(fach, {})})
for n in list(nodes):
    if n["t"] == "if":
        links.append({"s": "F-" + n["f"], "t": n["id"], "k": "hat"})

# Schwerpunkte Gymnasium (Pilot). Erdkunde und PoWi: Stichworte aus Kap. 6, das in allen drei Fassungen wortgleich ist
KAP6_ALLE = {"Erdkunde", "Politik und Wirtschaft"}
sp_nodes = []
for fach, feld, stufe, sp, seite in b.SP:
    st = "frueh" if stufe in EARLY else ("spaet" if stufe == b.B910 else "ohne")
    sfs = list(SF) if fach in KAP6_ALLE else ["gy"]
    hin = "Stichwort aus Kap. 6, das in allen drei KC-Fassungen gleich lautet" if fach in KAP6_ALLE else ""
    sp_nodes.append({"f": KEY[fach], "label": sp, "feld": feld, "st": st, "sf": sfs, "hin": hin,
                     "stufen": {s: stufe for s in sfs}, "seiten": {s: seite for s in sfs}})

# Schwerpunkte Haupt- und Realschule; gleich lautende Zeilen werden ein Knoten
gruppe = {}
for r in lies("schwerpunkte_sek1.csv"):
    key = (r["fach"], r["inhaltsfeld"], r["schwerpunkt"], r["stufe_typ"])
    if key not in gruppe:
        gruppe[key] = {"f": KEY[r["fach"]], "label": r["schwerpunkt"], "feld": r["inhaltsfeld"], "st": r["stufe_typ"],
                       "sf": [], "hin": r["hinweis"], "stufen": {}, "seiten": {}}
        sp_nodes.append(gruppe[key])
    g = gruppe[key]
    g["sf"].append(r["schulform"]); g["stufen"][r["schulform"]] = r["stufe"]; g["seiten"][r["schulform"]] = r["seite"]

for i, n in enumerate(sp_nodes, 1):
    n.update({"id": f"SP-{i:03d}", "t": "sp"})
    nodes.append(n)
    fach = next(f for k, f, _, _ in FAECHER if k == n["f"])
    links.append({"s": if_id[(fach, n["feld"])], "t": n["id"], "k": "hat"})

# Themenvorschläge (eigene Bündelung, nicht im KC)
th_id = {}
for r in lies("themen.csv"):
    if r["thema"] not in th_id:
        th_id[r["thema"]] = f"TH-{len(th_id) + 1:02d}"
        nodes.append({"id": th_id[r["thema"]], "t": "thema", "f": "thema", "label": r["thema"]})
    links.append({"s": th_id[r["thema"]], "t": if_id[(r["fach"], r["inhaltsfeld"])], "k": "vorschlag",
                  "stich": r["stichwort"], "stufe": r["stufe"], "seite": r["seite"]})

# belegte Querbezüge zwischen Fächern (stehen ausdrücklich im KC)
QBN = lies("querbezuege.csv")
for r in QBN:
    links.append({"s": "F-" + KEY[r["von"]], "t": "F-" + KEY[r["nach"]], "k": "beleg", "stich": r["aussage"], "fund": r["fundstelle"]})

# BNE: Aufgabengebiet nach § 6 Abs. 4 HSchG, Belege aus dem KC, SDG-Zuordnung als Vorschlag
nodes.append({"id": "BNE", "t": "bne", "f": "bne", "label": "Bildung für nachhaltige Entwicklung"})
for r in lies("bne_belege.csv"):
    seiten = {sf: r["seite_" + sf] for sf in SF if r["seite_" + sf]}
    quelle = if_id[(r["fach"], r["inhaltsfeld"])] if r["inhaltsfeld"] else "F-" + KEY[r["fach"]]
    links.append({"s": quelle, "t": "BNE", "k": "bne", "stich": r["zitat"], "seiten": seiten})
UZ = lies("bne_unterziele.csv")
for r in lies("bne_sdg.csv"):
    nodes.append({"id": "SDG-" + r["nr"], "t": "sdg", "f": "sdg", "nr": int(r["nr"]), "label": r["titel"], "farbe": r["farbe"],
                  "ziel": r["ziel"], "uz": [{"nr": u["nr"], "text": u["text"]} for u in UZ if u["sdg"] == r["nr"]]})
for r in lies("bne_vorschlaege.csv"):
    links.append({"s": "SDG-" + r["sdg"], "t": if_id[(r["fach"], r["inhaltsfeld"])], "k": "sdg", "stich": r["stichwort"], "uz": r["unterziel"]})

out = {
    "stand": "26.10.2026",
    "faecher": [{"k": k, "label": f, "kurz": kurz, "farbe": c, "gruppe": GRUPPE[k]} for k, f, kurz, c in FAECHER],
    "gruppen": [{"k": r["key"], "label": r["label"], "farbe": r["farbe"], "x": int(r["x"]), "y": int(r["y"])} for r in lies("aufgabenfelder.csv")],
    "schulformen": SF,
    "nodes": nodes, "links": links,
    "querbezuege": [list(q) for q in b.QB] + [[r["von"], r["nach"], r["aussage"], r["fundstelle"]] for r in QBN[5:]],
    "bne": {
        "grundlage": "§ 6 Abs. 4 Hessisches Schulgesetz",
        "text": "Besondere Bildungs- und Erziehungsaufgaben der Schulen werden in Aufgabengebieten erfasst. "
                "Diese sind insbesondere Umweltbildung und Bildung für nachhaltige Entwicklung, … "
                "Aufgabengebiete werden fachübergreifend unterrichtet. Sie können in Form themenbezogener Projekte "
                "unter Berücksichtigung der fachbezogenen Lernziele und Methoden auch jahrgangs- und schulformübergreifend unterrichtet werden.",
        "quelle": "Nichtamtliche Lesefassung des HSchG, Stand 01.08.2026",
        "url": "https://kultus.hessen.de/sites/kultus.hessen.de/files/2026-08/nichtamtliche_lesefassung_schulgesetz_stand_20260801_.pdf",
        "info": "https://kultus.hessen.de/unterricht/bildung-fuer-nachhaltige-entwicklung",
        "sdg_quelle": UZ[0]["quelle"],
        "sdg_url": "https://sdg-indikatoren.de/",
        "uz47": next(u["text"] for u in UZ if u["nr"] == "4.7"),
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
