from unitaire import testeur

# Exercice 1: Factorielle


def exercice1(f):
    essais = [
        ([5], [1, -1, 1, -1, 1]),
        ([10], [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]),
        ([0], []),
    ]
    print("Exercice 1: Alternance")
    testeur(f, essais)


# Exercice 2: Sommes des préfixes


def exercice2(f):
    essais = [
        ([[4, -2, 1, 5, -3, -1]], [4, 2, 3, 8, 5, 4]),
        ([[]], []),
    ]
    print("Exercice 2: Sommes des préfixes")
    testeur(f, essais)


# Exercice 3: Syracuse


def exercice3(f):
    essais = [
        ([3], [3, 10, 5, 16, 8, 4, 2, 1]),
        ([1], [1]),
        ([32], [32, 16, 8, 4, 2, 1]),
        ([11], [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
        (
            [77],
            [
                77,
                232,
                116,
                58,
                29,
                88,
                44,
                22,
                11,
                34,
                17,
                52,
                26,
                13,
                40,
                20,
                10,
                5,
                16,
                8,
                4,
                2,
                1,
            ],
        ),
    ]
    print("Exercice 3: Syracuse")
    testeur(f, essais)


# Exercice 5: Présence à une position donnée


def exercice5_1(f):
    essais = [
        (["abracadabra", "acada", 1], False),
        (["abracadabra", "acada", 3], True),
        (["un cheval, des chevaux", "", 5], True),
        (["un cheval, des chevaux", "chev", 2], False),
        (["un cheval, des chevaux", "chev", 3], True),
        (["un cheval, des chevaux", "cheval", 3], True),
        (["un cheval, des chevaux", "chevaux", 3], False),
    ]
    print("Exercice 5.1: Présence à une position donnée")
    testeur(f, essais)


# Exercice 5: Recherche de motif


def exercice5_2(f):
    essais = [
        (["abracadabra", "acada"], True),
        (["abracadabra", "poulet"], False),
        (["abracadabra", ""], True),
        (["", "bonjour"], False),
        (["bananes et ananas", "bananes"], True),
        (["aaaaa", "ab", False]),
        (["aaaaa", "aa", True]),
        (["aa", "aaaaa", False]),
        (["aa", "aa", True]),
    ]
    print("Exercice 5.2: Présence d'un motif")
    testeur(f, essais)


# Exercice 6: Catalan


def exercice6(f):
    essais = [
        ([0], []),
        ([1], [1]),
        ([2], [1, 1]),
        ([10], [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]),
    ]
    print("Exercice 6: Nombres de Catalan")
    testeur(f, essais)


# Exercice 7: Diamètre d'un ensemble


def exercice7_1(f):
    essais = [
        ([[4, 7, 2, -4, 6], -1], 8),
        ([[0], 0], 0),
        ([[1], 0], 1),
        ([[-1], 0], 1),
        ([[0], 1], 1),
        ([[0], -1], 1),
        ([[-4, 0, 4], 3], 7),
        ([[0, -4, 4], 3], 7),
        ([[-4, 4, 0], 3], 7),
        ([[0, 4, -4], 3], 7),
        ([[4, -4, 0], 3], 7),
        ([[4, 0, -4], 3], 7),
    ]
    print("Exercice 7.1: Distance maximale")
    testeur(f, essais)


def exercice7_2(f):
    essais = [
        ([[4, 7, 2, -4, 6]], 11),
        ([[42]], 0),
        ([[42, 5]], 37),
        ([[-5, 42]], 47),
        ([[1, 4, 13]], 12),
        ([[4, 1, 13]], 12),
        ([[13, 1, 4]], 12),
        ([[13, 4, 1]], 12),
        ([[1, 13, 4]], 12),
        ([[4, 13, 1]], 12),
    ]
    print("Exercice 7.2: Diamètre")
    testeur(f, essais)


# Exercice 8: Ératosthène


def exercice8(f):
    essais = [
        ([1], []),
        ([2], [2]),
        ([3], [2, 3]),
        ([4], [2, 3]),
        ([10], [2, 3, 5, 7]),
        (
            [100],
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
            ],
        ),
    ]
    print("Exercice 8: Ératosthène")
    testeur(f, essais)
