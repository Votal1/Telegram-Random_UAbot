from random import randint
from config import r
from datetime import datetime


def spirit(value, uid, c):
    if c == 4 or c == 14 or c == 24:
        r.hincrby(uid, 'spirit', value * 3)
    else:
        r.hincrby(uid, 'spirit', value)
    if int(r.hget(uid, 'spirit')) > 10000:
        r.hset(uid, 'spirit', 10000)
    if int(r.hget(uid, 'spirit')) < 0:
        r.hset(uid, 'spirit', 0)


def vodka(uid):
    ran = randint(10, 70)
    increase = ran * int(r.hget(uid, 's1'))
    spirit(increase, uid, 0)
    r.hincrby(uid, 'vodka', 1)
    return str(increase)


def intellect(value, uid):
    if value > 0:
        r.hincrby(uid, 'intellect', value)
        if int(r.hget(uid, 'intellect')) > 20:
            r.hset(uid, 'intellect', 20)
    if value < 0:
        r.hincrby(uid, 'intellect', value)
        if int(r.hget(uid, 'intellect')) <= 0:
            r.hset(uid, 'intellect', 1)


def injure(uid, s, bd, fi):
    if fi:
        r.hincrby(uid, 'injure', -1)
    return int(s * (1 / 3)), int(bd * (1 / 2))


def schizophrenia(uid, i, bd, fi):
    if fi:
        r.hincrby(uid, 'sch', -1)
    return int(i * (1 / 3)), int(bd * (1 / 2))


def trance(uid, s, bd, fi):
    if fi:
        r.hincrby(uid, 'buff', -1)
    return int(s * 1.2), int(bd * 1.8)


def increase_trance(value, uid):
    r.hincrby(uid, 'buff', value)
    mind = int(r.hget(uid, 'intellect'))
    if int(r.hget(uid, 'buff')) > mind:
        r.hset(uid, 'buff', mind)


def hp(value, uid):
    if value > 0:
        r.hincrby(uid, 'hp', value)
        if int(r.hget(uid, 'hp')) > 100:
            r.hset(uid, 'hp', 100)
    if value < 0:
        r.hincrby(uid, 'hp', value)
        if int(r.hget(uid, 'hp')) < 0:
            r.hset(uid, 'hp', 0)


def damage_weapon(uid, cl):
    r.hincrby(uid, 's_weapon', -1)
    if int(r.hget(uid, 's_weapon')) <= 0:
        if cl == 6 or cl == 16 or cl == 26:
            r.hset(uid, 'weapon', 16)
        else:
            r.hset(uid, 'weapon', 0)


def damage_defense(uid, d):
    r.hincrby(uid, 's_defense', -1)
    if int(r.hget(uid, 's_defense')) <= 0:
        r.hset(uid, 'defense', 0)
        if d == 9:
            r.hincrby(uid, 'money', 4)


def damage_support(uid):
    r.hincrby(uid, 's_support', -1)
    if int(r.hget(uid, 's_support')) <= 0:
        r.hset(uid, 'support', 0)

