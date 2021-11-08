# %% Ne pas modifier ########################

import inspect
import os

os.chdir(os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda: 0))))

###########################################


def benford(d):
    ...


def loi_benford():
    ...


def chiffre_significatif(s):
    """chiffre_significatif(s:string) -> int

Prends en entrée une chaîne de caractères représentant un
nombre strictement positif et retourne l'entier correspondant
à son chiffre significatif.

Son fonctionnement est très simple : elle convertit la chaîne de
caractère en flottant, puis à nouveau en chaîne de caractère en 
notation scientifique, récupère le premier caractère, et le 
convertit en entier.

Par exemple,
>>> chiffre_significatif('0.00023')
2
"""
    return int(f"{float(s):e}"[0])


def données_boursières():
    with open("bourse.csv", "r") as fichier:
        données = csv.DictReader(fichier, delimiter=";")
        for ligne in données:
            print(ligne)
            break


données_boursières()
