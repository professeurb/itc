# %% Ne pas modifier ######################

import test_tp1
import inspect
import os

os.chdir(os.path.dirname(os.path.abspath(inspect.getsourcefile(lambda: 0))))

###########################################

### II. Parcours ##########################

### II.1. Parcours complet ################

### Exercice 1


def factorielle(n):
    ...


test_tp1.exercice1(factorielle)

### Exercice 2


def occurences(t, e):
    ...


# test_tp1.exercice2(occurences)

### Exercice 3


def maximum(t):
    ...


# test_tp1.exercice3(maximum)

### Exercice 4


def position_maximum(t):
    ...


# test_tp1.exercice4(position_maximum)

### Exercice 5


def position_2_maximums(t):
    ...


# test_tp1.exercice5(position_2_maximums)

### II.2. Parcours partiel ################

### Exercice 6


def est_présent(t, e):
    ...
    i = 0
    while i < len(t) and ...:
        ...
        i = i + 1
    ...


# test_tp1.exercice6(est_présent)

### Exercice 7


def est_croissant(t):
    ...


# test_tp1.exercice7(est_croissant)

### Exercice 8


def est_modal(t):
    ...


# test_tp1.exercice8(est_modal)

### Exercice 9


def somme_croissante(t):
    ...


# test_tp1.exercice9(somme_croissante)
