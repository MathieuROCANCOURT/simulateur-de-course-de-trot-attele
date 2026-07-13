#!/usr/bin/env python
# -*- coding: utf-8 -*-
import secrets

ARRAY_SPEED_DICE = (
    (0, 1, 1, 1, 2, 2),
    (0, 0, 1, 1, 1, 2),
    (0, 0, 1, 1, 1, 2),
    (-1, 0, 0, 1, 1, 1),
    (-1, 0, 0, 0, 1, 1),
    (-2, -1, 0, 0, 0, 1),
    (-2, -1, 0, 0, 0, 'D')
)
ARRAY_SPEED_DISTANCE = (0, 23, 46, 69, 92, 115, 138)


def init_harness_racing(nb_horses):
    return {(key + 1): [0, 0] for key in nb_horses}


def next_lap(horses_dictionary):
    for key, [speed, distance] in horses_dictionary.items():
        if distance != 'D':
            dice_value = secrets.randbelow(6)
            if dice_value == 6 and speed == 6:
                horses_dictionary[key] = ['D', 'D']
            else:
                horses_dictionary[key] = [dice_value, ARRAY_SPEED_DICE[speed][dice_value]]
    return horses_dictionary


def race_status(horses_dictionary):
    for key, [speed, distance] in horses_dictionary.items():
        if distance == 'D':
            print(f"Le cheval n°{key} est disqualifié.")
        else:
            print(f"Le cheval n°{key} est à vitesse {speed} avec {distance}m parcouru.")


def loop_harness_racing(horses_dictionary):
    time_race = 0
    input("Veuillez appuyer sur Entrée pour commancer la course.")
    while True:
        horses_dictionary = next_lap(horses_dictionary)
        time_race += 10
        print(f"Après {time_race}\" de course, voici l'état de la course:")
        race_status(horses_dictionary)


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
