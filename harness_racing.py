#!/usr/bin/env python
# -*- coding: utf-8 -*-

ARRAY_SPEED_DICE = (
    (0, 1, 1, 1, 2, 2),
    (0, 0, 1, 1, 1, 2),
    (0, 0, 1, 1, 1, 2),
    (-1, 0, 0, 1, 1, 1),
    (-1, 0, 0, 0, 1, 1),
    (-2, -1, 0, 0, 0, 1),
    (-2, -1, 0, 0, 0, "D")
)
ARRAY_SPEED_DISTANCE = (0, 23, 46, 69, 92, 115, 138)


def init_harness_racing(nb_horses):
    return dict.fromkeys(nb_horses, 0)


def print_ranking(ranking, type_rank):
    output, dict_type = "", {"tiercé": 3, "quarté": 4, "quinté": 5}
    top_ranking = dict_type[type_rank]
    for rank in range(top_ranking):
        output += str(ranking[rank]) + " - "
    return output[:-3]


if __name__ == "__main__":
    inputUserHorses = input("Saisir le nombre de chevaux entre 12 et 20 ou 'stop' pour arrêter le programme:")
    while inputUserHorses not in [str(validValue) for validValue in range(12, 21)]:
        inputUserHorses = input(
            "SAISIE INCORRECT !\nSaisir le nombre de chevaux entre 12 et 20 ou 'stop' pour arrêter le programme:")
    inputUserHorses = int(inputUserHorses)

    inputUserType = input("Voulez-vous un tiercé, un quarté ou un quinté ? Ou 'stop' pour arrêter le programme:")
    while inputUserType != 'tiercé' and inputUserType != 'quarté' and inputUserType != 'quinté':
        inputUserType = input("SAISIE INCORRECT !\nSaisir 'tiercé' ou 'quarté' ou 'quinté':")

    exit(0)
