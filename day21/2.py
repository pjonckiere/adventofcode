#!/usr/bin/env python

import itertools

health = int(100)
damage = int(0)
armor = int(0)
boss = int(109)
boss_damage = int(8)
boss_armor = int(2)


def get_player_stats():
    global health, damage, armor
    return [health, damage, armor]


def set_player_stats(d, a):
    global health, damage, armor
    health = int(100)
    damage = d
    armor = a


def set_player_health(h):
    global health
    health = h


def get_boss_stats():
    global boss, boss_damage, boss_armor
    return [boss, boss_damage, boss_armor]


def set_boss_health(h):
    global boss
    boss = h


def turn():
    pl = get_player_stats()
    bo = get_boss_stats()

    # player attack
    d = pl[1] - bo[2]
    set_boss_health(bo[0] - d)
    # print "boss: %d" % (bo[0] - d)
    if bo[0] - d <= 0:
        return

    # boss attack
    d = bo[1] - pl[2]
    set_player_health(pl[0] - d)
    # print "player: %d" % int(pl[0] - d)


shop = {
    'weapons': {
        0: [8, 4, 0],
        1: [10, 5, 0],
        2: [25, 6, 0],
        3: [40, 7, 0],
        4: [74, 8, 0]
    },
    'armor': {
        0: [0, 0, 0],
        1: [13, 0, 1],
        2: [31, 0, 2],
        3: [53, 0, 3],
        4: [75, 0, 4],
        5: [102, 0, 5]
    },
    'rings': {
        0: [25, 1, 0],
        1: [50, 2, 0],
        2: [100, 3, 0],
        3: [20, 0, 1],
        4: [40, 0, 2],
        5: [80, 0, 3],
    }
}

lowest_gold = 1000
highest_gold = 0
rings_combo = [x for l in range(3) for x in itertools.combinations(shop['rings'], l)]
for weapon in shop['weapons']:
    for armo in shop['armor']:
        for rings in rings_combo:
            # print "combination %s %s %s" % (weapon, armo, rings)
            attack = shop['weapons'][weapon][1]
            defence = shop['armor'][armo][2]
            rings_attack = 0
            rings_armor = 0
            if len(rings) >= 1:
                rings_attack += shop['rings'][rings[0]][1]
                rings_armor += shop['rings'][rings[0]][2]
            if len(rings) == 2:
                rings_attack += shop['rings'][rings[1]][1]
                rings_armor += shop['rings'][rings[1]][2]

            set_player_stats(attack + rings_attack, defence + rings_armor)
            set_boss_health(int(109))
            while get_boss_stats()[0] > 0 and get_player_stats()[0] > 0:
                turn()

            player_stats = get_player_stats()
            gold = shop['weapons'][weapon][0]
            gold += shop['armor'][armo][0]
            if len(rings) == 1:
                gold += shop['rings'][rings[0]][0]
            if len(rings) == 2:
                gold += shop['rings'][rings[0]][0]
                gold += shop['rings'][rings[1]][0]

            if get_boss_stats()[0] <= 0:
                lowest_gold = min(lowest_gold, gold)
            else:
                highest_gold = max(highest_gold, gold)
                # print "combination %s %s %s for %s" % (weapon, armo, rings, highest_gold)
print highest_gold
