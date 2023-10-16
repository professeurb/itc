"""
unitaire.py

Tests unitaire simples et rapides pour fonctions, avec
une liste d'arguments/résultats.

La fonction testeur prends deux arguments :

 i. la fonction à tester
ii. une liste de couples de la forme (liste d'arguments, résultat attendu)

La fonction vérifie pour tous les couples que le résultat de la fonction
appelée avec les arguments donnés par la liste est égal à celui attendu.

Si un résultat obtenu n'est pas le bon, l'évaluation s'arrête et 
et affiche un message d'erreur.

En cas d'erreur d'exécution, l'évaluation s'arrête et l'erreur est affichée.

Exemples d'utilisation :

>>> def f(x):
...     return x + 1
...
>>> testeur(f, [([1], 2), ([2], 3)])
Test 2/2
= Ok ===================================

>>> def g(x):
...     return x + 2
...
>>> testeur(g, [([1], 2), ([2], 3)])
Test 1/2
= Erreur (AssertionError) ==============
Expression : g(1)
Résultat attendu : 2
Résultat obtenu  : 3

>>> testeur(min, [([1, 2, 3], 1), (["b", "a", "c"], "a")])
Test 2/2
= Ok ===================================

>>> testeur(min, ([([], 1)]))
Test 1/1
= Erreur (TypeError) ===================
min expected 1 arguments, got 0

:copyright: Olivier Brunet, 2019, professeurb.github.io
:license: CC-BY-NC
"""

import sys

def _test_equality(f, args, excepted_result):
    actual_result = f(*args)
    assert(actual_result == excepted_result), (
        "Expression : {}({})\n"
        "Résultat attendu : {}\n"
        "Résultat obtenu  : {}"
    ).format(
        f.__name__,
        repr(args)[1:-1],
        repr(excepted_result),
        repr(actual_result)
    )


def _test_equalities(f, l):
    size = repr(len(l))
    placeholder = "Test {{:{}}}/{}\r".format(len(size), size)
    for i in range(len(l)):
        print(placeholder.format(i + 1), end="")
        args, res = l[i]
        _test_equality(f, args, res)


def testeur(f, l):
    """
    Teste la fonction f en comparant, pour chaque couple (arguments, résultat) de la liste,
    si la valeur retournée par f en l'appelant avec les arguments est bien égale à résultat.
    """
    try:
        _test_equalities(f, l)
        print("\n= {:=<38s}".format("Ok "))
    except:
        exc = sys.exc_info()
        print("\n= {:=<38s}".format("Erreur ({}) ".format(exc[0].__name__)))
        print(exc[1])
