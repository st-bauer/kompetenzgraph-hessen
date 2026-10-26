"""Zeigt Text aus quellen/txt mit Seitenzahl am Zeilenanfang, als Hilfe beim Erfassen.

Beispiele:
  python3 scripts/kc_seiten.py geschichte_hauptschule 21-24
  python3 scripts/kc_seiten.py geschichte_hauptschule 21-24 --breite 60
  python3 scripts/kc_seiten.py geschichte_hauptschule --kapitel
Die Seitenzahl ist die PDF-Seite. Sie stimmt bei den hessischen KC mit der gedruckten Seitenzahl überein.
"""
import argparse, glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def seiten(name):
    pfad = glob.glob(os.path.join(ROOT, "quellen", "txt", name + "*kerncurriculum.txt"))[0]
    return open(pfad, encoding="utf-8").read().split("\f")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("name")
    ap.add_argument("bereich", nargs="?")
    ap.add_argument("--breite", type=int, default=0)
    ap.add_argument("--kapitel", action="store_true")
    a = ap.parse_args()
    s = seiten(a.name)
    if a.kapitel:
        # Kapitelanfänge 6, 7, 7.x, 8 nach dem Inhaltsverzeichnis
        for i, t in enumerate(s[4:], 5):
            for z in t.splitlines():
                if re.match(r"\s{0,8}(6|7|7\.\d|8)\s{2,}\S", z) and "..." not in z:
                    print(i, z.strip()[:100])
        return
    von, _, bis = a.bereich.partition("-")
    for i in range(int(von), int(bis or von) + 1):
        for z in s[i - 1].splitlines():
            z = z.rstrip()
            if a.breite:
                z = z[:a.breite].rstrip()
            if z.strip():
                print(f"{i}: {z}")


if __name__ == "__main__":
    main()
