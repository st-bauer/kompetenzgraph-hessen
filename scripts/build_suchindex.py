"""Erzeugt data/suchindex.json für die Themenwerkstatt.

Je Inhaltsfeld die Wörter aus der Beschreibung in Kap. 6 (alle KC-Fassungen zusammen), ohne Reihenfolge
und ohne Füllwörter. Die Seite zeigt diese Wörter nicht an, sie dienen nur der Suche.
Braucht quellen/txt (scripts/fetch_pdfs.py --alle).
"""
import csv, importlib.util, json, os, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("ia", os.path.join(ROOT, "scripts", "inhaltsfelder_auslesen.py"))
ia = importlib.util.module_from_spec(spec); spec.loader.exec_module(ia)

SLUG = lambda f: f.lower().replace(" ", "_").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
SFN = {"hs": "hauptschule", "rs": "realschule", "gy": "gymnasium"}
STOPP = set("""aber alle allem allen aller alles also auch auf aus bei beim bereits bzw dabei dadurch dafür daher damit dann darauf
darin darüber das dass dem den denen der deren des dessen die dies diese diesem diesen dieser dieses doch dort durch eine einem
einen einer eines einige etwa für gegen hier hierbei ihre ihrem ihren ihrer ihres immer indem insbesondere jedoch jeweils kann
können lernenden mehr mit nach neben nicht noch nur ob oder ohne schülerinnen schüler sehr sich sie sind sowie sowohl über um
und uns unter vom von vor wann was weise welche welchen welcher werden wie wird wobei zum zur zwischen inhaltsfeld inhaltsfeldes
inhaltsfelder mittelpunkt stehen steht dieses grundlage bezug bezüge kompetenzbereichen kompetenzbereiche standards angaben
bereich jede jeder hessen hessisches kultusministerium kerncurriculum hauptschule realschule gymnasium sekundarstufe
kapitel entfällt entwurf fach faches""".split())
FELDER = list(csv.DictReader(open(os.path.join(ROOT, "data", "inhaltsfelder_sek1.csv"), encoding="utf-8")))


def roh(datei, von, bis):
    """Text ohne Spaltenlayout: die Beschreibung folgt dort direkt auf den Titel des Inhaltsfelds."""
    pdf = os.path.join(ROOT, "quellen", "pdf", datei + "_kerncurriculum.pdf")
    t = subprocess.run(["pdftotext", "-f", str(von), "-l", str(bis), pdf, "-"], capture_output=True, text=True).stdout
    return re.sub(r"\s+", " ", re.sub(r"-\n(?=[a-zäöü])", "", t))


def abschnitt(text, fach, feld):
    n = lambda x: re.escape(re.sub(r"\s+", " ", x.split(" – ")[0][:18]))
    m = re.search(n(feld), text)
    if not m:
        return ""
    rest = text[m.end():]
    ende = [x.start() for f in FELDER if f["fach"] == fach and f["inhaltsfeld"] != feld for x in [re.search(n(f["inhaltsfeld"]), rest)] if x]
    return rest[:min(ende + [2500])]

index = {}
for r in FELDER:
    fach, feld = r["fach"], r["inhaltsfeld"]
    woerter = set()
    for sf, name in SFN.items():
        seiten = [int(x) for x in re.findall(r"\d+", r["seite_" + sf])]
        datei = f"{SLUG(fach)}_{name}" + ("_wahlunterricht" if fach == "Informatik" else "")
        if not seiten or not os.path.exists(os.path.join(ROOT, "quellen", "txt", datei + "_kerncurriculum.txt")):
            continue
        try:
            for b in ia.bloecke(datei, seiten[0], seiten[-1] + 1, fach):
                if b["feld"] == feld:
                    text = re.sub(r"(\w)-\s+(\w)", r"\1\2", " ".join(b["text"])).lower()
                    woerter |= {w for w in re.findall(r"[a-zäöüß]{4,}", text) if w not in STOPP}
        except Exception as e:  # Informatik und Sonderformate: dann nur Titel und Schwerpunkte durchsuchen
            print("übersprungen:", fach, sf, e)
        if not woerter and fach != "Informatik":
            text = abschnitt(roh(datei, seiten[0], seiten[-1] + 1), fach, feld).lower()
            woerter |= {w for w in re.findall(r"[a-zäöüß]{4,}", text) if w not in STOPP}
    index[f"{fach}|{feld}"] = " ".join(sorted(woerter))
p = os.path.join(ROOT, "data", "suchindex.json")
json.dump(index, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
leer = [k for k, v in index.items() if not v]
print(p, len(index), "Inhaltsfelder,", sum(len(v.split()) for v in index.values()), "Wörter; ohne Text:", leer)
