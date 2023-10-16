from unitaire import testeur

# Exercice 1: Factorielle


def exercice1(f):
    essais = [([1], 1), ([2], 2), ([3], 6), ([10], 3628800)]
    print("Exercice 1: Factorielle")
    testeur(f, essais)


# Exercice 2: Occurences


def exercice2(f):
    essais = [
        ([[5, 2, 4, 8, 7, 4, 1, 2, 5, 4], 4], 3),
        ([[5, 2, 4, 8, 7, 4, 1, 2, 5, 4], 6], 0),
        ([[], 10], 0),
        ([[2, 4, 6, 4], 1], 0),
        ([[2, 4, 6, 4], 2], 1),
        ([[2, 4, 6, 4], 4], 2),
    ]
    print("Exercice 2: Occurences")
    testeur(f, essais)


# Exercice 3: Maximum


def exercice3(f):
    essais = [
        ([[123]], 123),
        ([[20, 15, 18]], 20),
        ([[20, 28, 15, 18]], 28),
        ([[20, 15, 18, 39]], 39),
        ([[-10]], -10),
    ]
    print("Exercice 3: Maximum")
    testeur(f, essais)


# Exercice 4: Position du maximum


def exercice4(f):
    essais = [
        ([[5, 2, 4, 8, 7, 4, 1, 2, 5, 4]], 3),
        ([[5, 7, 2, 6, 4, 7, 3, 1, 6]], 1),
        ([[123]], 0),
        ([[20, 15, 18]], 0),
        ([[20, 28, 15, 18]], 1),
        ([[20, 15, 18, 39]], 3),
        ([[28, 28]], 0),
        ([[20, 28, 15, 18, 28]], 1),
    ]
    print("Exercice 4: Position du maximum")
    testeur(f, essais)


# Exercice 5: Position des 2 maximums


def exercice5(f):
    essais = [
        ([[3, 5, 1, 2, 5, 4, 5]], (1, 4)),
        ([[3, 2, 5, 2, 6, 4, 5]], (4, 2)),
        ([[28, 27]], (0, 1)),
        ([[27, 28]], (1, 0)),
        ([[123, 123]], (0, 1)),
        ([[20, 15, 18]], (0, 2)),
        ([[20, 28, 15, 18]], (1, 0)),
        ([[20, 21, 18, 39]], (3, 1)),
        ([[20, 28, 15, 18, 28]], (1, 4)),
        ([[20, 28, 15, 28, 28]], (1, 3)),
        ([[20, 28, 15, 20, 18]], (1, 0)),
        ([[13, 28, 15, 20, 20]], (1, 3)),
        ([[20, 28, 15, 20, 20]], (1, 0)),
        ([[13, 20, 15, 20, 28]], (4, 1)),
    ]
    print("Exercice 5: Position des 2 maximums")
    testeur(f, essais)


# Exercice 6: Présence


def exercice6(f):
    essais = [
        ([[4, 1, 2, 5], 3], False),
        ([[4, 1, 2, 5], 1], True),
        ([[], 5], False),
        ([[10], 15], False),
        ([[10], 10], True),
        ([[10, 15], 15], True),
        ([[10, 15], 10], True),
        ([[0, 15], 0], True),
        ([[15, 0], 0], True),
    ]
    print("Exercice 6: Test de présence")
    testeur(f, essais)


# Exercice 7: Croissance


def exercice7(f):
    essais = [
        ([[2, 4, 4, 5, 7]], True),
        ([[5, 7, 3, 4, 8]], False),
        ([[]], True),
        ([[10]], True),
        ([[10, 12]], True),
        ([[10, 12, 15]], True),
        ([[10, 12, 12]], True),
        ([[10, 12, 12, 15]], True),
        ([[12, 12, 12, 12]], True),
        ([[10, 12, 12, 12]], True),
        ([[15, 12, 12, 12]], False),
        ([[15, 10, 11, 12]], False),
        ([[10, 11, 13, 12]], False),
        ([[-10, -8]], True),
        ([[-10, -10]], True),
    ]
    print("Exercice 7: Test de croissance")
    testeur(f, essais)


# Exercice 8: Modalité


def exercice8(f):
    essais = [
        ([[2, 3, 3, 4, 5, 5, 3, 3, 1]], True),
        ([[1, 2, 3, 2, 3, 4]], False),
        ([[]], True),
        ([[10]], True),
        ([[10, 12]], True),
        ([[10, 12, 15]], True),
        ([[15, 12, 10]], True),
        ([[10, 12, 12]], True),
        ([[10, 12, 12, 10]], True),
        ([[10, 12, 12, 15]], True),
        ([[12, 12, 12, 12]], True),
        ([[10, 12, 12, 12]], True),
        ([[15, 12, 12, 12]], True),
        ([[15, 10, 11, 12]], False),
        ([[10, 11, 13, 12]], True),
        ([[10, 11, 13, 12, 11, 12]], False),
        ([[-10, -8, -10]], True),
        ([[-10, -12, -10]], False),
        ([[3, 2, 2, 3]], False),
    ]
    print("Exercice 8: Test de modalité")
    testeur(f, essais)


# Exercice 9: Somme croissante


def exercice9(f):
    essais = [
        ([[2, 4, 4, 5, 7]], 22),
        ([[5, 7, 3, 4, 8]], 12),
        ([[4, 3, 2, 1]], 4),
        ([[4, 5, 6, 5, 4]], 14),
        ([[4, 3, 2, 3, 4]], 4),
        ([[5, 5, 6, 5]], 16),
        ([[4, 5, 5, 6, 5]], 20),
        ([[4, 5, 6, 6, 5]], 21),
        ([[4, 4, 3, 2, 1]], 8),
    ]
    print("Exercice 9: Somme croissante")
    testeur(f, essais)
