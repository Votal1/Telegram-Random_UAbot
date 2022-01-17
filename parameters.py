from random import randint


def spirit(value, uid, c, fi, r):
    if fi is True:
        if c == 4 or c == 14 or c == 24:
            if value < 0 and c == 4:
                r.hincrby(uid, 'spirit', value * 2)
            elif value < 0 and c == 14:
                r.hincrby(uid, 'spirit', value)
            elif value < 0 and c == 24:
                r.hincrby(uid, 'spirit', int(value / 2))
            else:
                r.hincrby(uid, 'spirit', value * 3)
            if int(r.hget(uid, 'spirit')) > 20000:
                r.hset(uid, 'spirit', 20000)
        else:
            r.hincrby(uid, 'spirit', value)
            if int(r.hget(uid, 'spirit')) > 10000:
                r.hset(uid, 'spirit', 10000)
        if int(r.hget(uid, 'spirit')) < 0:
            r.hset(uid, 'spirit', 0)
    elif fi is False:
        r.hincrby(uid, 'spirit', value)
        if c == 4 or c == 14 or c == 24:
            if int(r.hget(uid, 'spirit')) > 20000:
                r.hset(uid, 'spirit', 20000)
        elif int(r.hget(uid, 'spirit')) > 10000:
            r.hset(uid, 'spirit', 10000)
        if int(r.hget(uid, 'spirit')) < 0:
            r.hset(uid, 'spirit', 0)


def vodka(uid, cl, r):
    ran = randint(10, 70)
    increase = ran * int(r.hget(uid, 's1'))
    spirit(increase, uid, cl, False, r)
    r.hincrby(uid, 'vodka', 1)
    return str(increase)


def intellect(value, uid, r):
    if value > 0:
        r.hincrby(uid, 'intellect', value)
        if int(r.hget(uid, 'intellect')) > 20:
            r.hset(uid, 'intellect', 20)
    if value < 0:
        r.hincrby(uid, 'intellect', value)
        if int(r.hget(uid, 'intellect')) <= 0:
            r.hset(uid, 'intellect', 1)


def injure(uid, s, bd, fi, r):
    if fi:
        r.hincrby(uid, 'injure', -1)
    return int(s * (1 / 3)), int(bd * (1 / 2))


def schizophrenia(uid, i, bd, fi, r):
    if fi:
        r.hincrby(uid, 'sch', -1)
    return int(i * (1 / 3)), int(bd * (1 / 2))


def hp(value, uid, r):
    if value > 0:
        r.hincrby(uid, 'hp', value)
        if int(r.hget(uid, 'hp')) > 100:
            r.hset(uid, 'hp', 100)
    if value < 0:
        r.hincrby(uid, 'hp', value)
        if int(r.hget(uid, 'hp')) < 0:
            r.hset(uid, 'hp', 0)


def weapon(uid, r):
    r.hincrby(uid, 's_weapon', -1)
    if int(r.hget(uid, 's_weapon')) <= 0:
        r.hset(uid, 'weapon', 0)
