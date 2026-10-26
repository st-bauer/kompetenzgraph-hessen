"""Lädt Kerncurricula aus data/quellen_sek1.csv und extrahiert den Text.

Beispiel:
  python3 scripts/fetch_pdfs.py --fach Biologie --schulform Realschule
  python3 scripts/fetch_pdfs.py --alle

PDFs landen in quellen/pdf/, Text in quellen/txt/ (braucht pdftotext aus poppler-utils).
"""
import argparse, csv, os, re, shutil, subprocess, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "quellen", "pdf")
TXT = os.path.join(ROOT, "quellen", "txt")


def slug(s):
    s = s.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fach")
    ap.add_argument("--schulform")
    ap.add_argument("--dokument", default="Kerncurriculum")
    ap.add_argument("--alle", action="store_true")
    a = ap.parse_args()
    os.makedirs(PDF, exist_ok=True)
    os.makedirs(TXT, exist_ok=True)
    rows = list(csv.DictReader(open(os.path.join(ROOT, "data", "quellen_sek1.csv"), encoding="utf-8")))
    if not a.alle:
        rows = [r for r in rows
                if (not a.fach or r["fach"] == a.fach)
                and (not a.schulform or r["schulform"].startswith(a.schulform))
                and r["dokument"] == a.dokument]
    has_pdftotext = shutil.which("pdftotext") is not None
    for r in rows:
        name = slug(f'{r["fach"]}_{r["schulform"]}_{r["dokument"]}')
        p = os.path.join(PDF, name + ".pdf")
        if not os.path.exists(p):
            print("lade", r["url"])
            urllib.request.urlretrieve(r["url"], p)
        if has_pdftotext:
            subprocess.run(["pdftotext", "-layout", p, os.path.join(TXT, name + ".txt")], check=True)
    print(f"{len(rows)} Dokument(e) verarbeitet." + ("" if has_pdftotext else " Hinweis: pdftotext fehlt, kein Text extrahiert."))


if __name__ == "__main__":
    main()
