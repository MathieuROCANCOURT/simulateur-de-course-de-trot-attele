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
ALL_DISTANCE = 2400


def init_harness_racing(nb_horses):
    return {(key + 1): [0, 0] for key in range(nb_horses)}


def next_lap(horses_dictionary, is_dq_or_arrived):
    for key, [speed, distance] in horses_dictionary.items():
        if not is_dq_or_arrived[int(key) - 1]:
            dice_value = secrets.randbelow(6)
            add_speed = ARRAY_SPEED_DICE[speed][dice_value]

            if add_speed == 'D':
                is_dq_or_arrived[int(key) - 1] = True
            else:
                horses_dictionary[key] = [speed + add_speed, distance + ARRAY_SPEED_DISTANCE[speed]]

    return horses_dictionary, is_dq_or_arrived


def race_status(horses_dictionary):
    for key, [speed, distance] in horses_dictionary.items():
        if distance == 'D':
            print(f"Le cheval n°{key} est disqualifié.")
        elif distance >= ALL_DISTANCE:
            print(f"Le cheval n°{key} est arrivé")
        else:
            print(f"Le cheval n°{key} est à vitesse {speed} avec {distance}m parcouru.")


def loop_harness_racing(horses_dictionary):
    time_race = 0
    input("Veuillez appuyer sur Entrée pour commancer la course.")
    is_dq_or_arrived = [False for _ in range(len(horses_dictionary))]
    while True:
        horses_dictionary, is_dq_or_arrived = next_lap(horses_dictionary, is_dq_or_arrived)
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

    loop_harness_racing(init_harness_racing(inputUserHorses))

    exit(0)
