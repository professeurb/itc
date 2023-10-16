# %% Imports

from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt

# %% Exercice 1


def bizarre(n):
    s = 0
    i = 1
    while i < premier(n):
        s = s + 1
        i = i + bizarre2(i)
    return s


# Il faut modifier cette fonction


def bizarre_rapide(n):
    s = 0
    i = 1
    while i < premier(n):
        s = s + 1
        i = i + bizarre2(i)
    return s


# %% Expérimentations


def somme(t):
    s = 0
    for i in range(len(t)):
        s = s + t[i]
    return s


def plus_proches(t):
    d = abs(t[1] - t[0])
    for i in range(len(t)):
        for j in range(i):
            d = min(d, abs(t[i] - t[j]))
    return d


def chrono(f, x):
    t0 = timer()
    r = f(x)
    t1 = timer()
    return t1 - t0


def chrono_somme(n, f):
    ...


def trace_somme():
    longueurs = list(range(10, 210, 10))
    for i in range(20):
        # on calcule des temps pour différentes longueurs
        temps = [chrono_somme(l, 1000) for l in longueurs]
        # on les affiche
        plt.plot(longueurs, temps)
    plt.show()


# %% Recherche dichotomique


def recherche_dichotomique(t, e):
    deb = 0
    fin = len(t) - 1
    while ...:
        mil = (deb + fin) // 2
        if t[mil] == e:
            return ...
        elif t[mil] > e:
            ...
        else:
            ...
    # on n'a pas trouvé e
    return -1


# %% Fonctions supplémentaires


def premier(n):
    if n == 1:
        return 2
    prems = [2]
    cand = 3
    while len(prems) < n:
        i = 0
        est_compose = False
        while i < len(prems) and not est_compose:
            if cand % prems[i] == 0:
                est_compose = True
            else:
                i = i + 1
        if not est_compose:
            prems.append(cand)
        cand += 2
    return prems[-1]


def bizarre2(i):
    r = 0
    while i > 0:
        r += i % 2
        i = i // 2
    return r
