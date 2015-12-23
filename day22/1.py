#!/usr/bin/env python

import random


def fight(attacks, p_hp, p_mana, boss_hp, boss_damage):
    hp = p_hp
    mana = p_mana
    b_hp = boss_hp
    b_dam = boss_damage
    att_stack = {}
    index = 1
    mana_usage = 0
    while hp > 0 and b_hp > 0:
        ret = turn(index, att_stack, attacks, hp, mana, b_hp, b_dam, mana_usage)
        att_stack = ret[0]
        hp = ret[1]
        mana = ret[2]
        b_hp = ret[3]
        mana_usage = ret[4]
        index += 1
        # print '%s %s' % (hp, b_hp)

    if hp > 0:
        # print "player won with mana usage %s" % mana_usage
        return mana_usage
    else:
        return 1000000


def turn(index, att_stack, attacks, hp, mana, b_hp, b_dam, mana_usage):
    a = random.choice(attacks.keys())

    mana_usage += attacks[a][0]
    mana -= attacks[a][0]
    for t in range(attacks[a][5]):
        if index + t not in att_stack:
            att_stack[index + t] = []
        att_stack[index + t].append(a)

    hit = 0
    arm = 0
    rec = 0
    for b in att_stack[index]:
        hit += attacks[b][1]
        arm += attacks[b][2]
        rec += attacks[b][3]
        mana += attacks[b][4]

    b_hp -= hit
    hp += rec

    hp -= (b_dam - arm)

    if b_hp > 0 and mana < attacks[0][0]:
        return [att_stack, 0, mana, b_hp, mana_usage]

    return [att_stack, hp, mana, b_hp, mana_usage]

attacks_init = {
    # mana, attack, armor, heal, recharge, turns
    0: [53, 4, 0, 0, 0, 1],
    1: [73, 2, 0, 2, 0, 1],
    2: [113, 0, 7, 0, 0, 6],
    3: [173, 3, 0, 0, 0, 6],
    4: [229, 0, 0, 0, 101, 5]
}

player_hp = int(50)
player_mana = int(500)
boss_hp_init = int(55)
boss_damage_init = int(8)

lowest_mana = int(1000001)
stable = 0
while stable < 100000:
    man = fight(attacks_init, player_hp, player_mana, boss_hp_init, boss_damage_init)
    if man < lowest_mana:
        lowest_mana = man
        stable = 0
    else:
        stable += 1
print lowest_mana
