import json, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "data"))
import kerncurricula as b

FACH_KEY = {"Biologie": "bio", "Chemie": "che", "Physik": "phy", "Erdkunde": "erd", "Politik und Wirtschaft": "pow"}
EARLY = {b.B56, b.C1, b.P1}

nodes, links = [], []
for f, k in FACH_KEY.items():
    nodes.append({"id": "F-" + k, "t": "fach", "f": k, "label": f, "url": b.URL[f]})

if_id = {}
for i, (fach, bk, feld, seite, hin) in enumerate(b.IF, 1):
    nid = f"IF-{i:02d}"
    if_id[(fach, feld)] = nid
    nodes.append({"id": nid, "t": "if", "f": FACH_KEY[fach], "label": feld, "bk": bk,
                  "seite": seite, "hin": hin})
    links.append({"s": "F-" + FACH_KEY[fach], "t": nid, "k": "hat"})

for i, (fach, feld, stufe, sp, seite) in enumerate(b.SP, 1):
    nid = f"SP-{i:03d}"
    st = "frueh" if stufe in EARLY else ("spaet" if stufe == b.B910 else "ohne")
    nodes.append({"id": nid, "t": "sp", "f": FACH_KEY[fach], "label": sp, "feld": feld,
                  "stufe": stufe, "st": st, "seite": seite})
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

out = {"nodes": nodes, "links": links, "querbezuege": [list(q) for q in b.QB]}
p = os.path.join(ROOT, "output", "data.json")
json.dump(out, open(p, "w"), ensure_ascii=False)
from collections import Counter
print(Counter(n["t"] for n in nodes), Counter(l["k"] for l in links))

# Webseite bauen: Daten in Vorlage einsetzen
tpl = open(os.path.join(ROOT, "web", "template.html"), encoding="utf-8").read()
html = tpl.replace("/*__DATA__*/null", json.dumps(out, ensure_ascii=False))
os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
open(os.path.join(ROOT, "docs", "index.html"), "w", encoding="utf-8").write(html)
open(os.path.join(ROOT, "docs", ".nojekyll"), "w").close()
print("docs/index.html geschrieben (wird von GitHub Pages ausgeliefert)")
