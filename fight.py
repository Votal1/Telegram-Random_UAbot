from random import randint, choice, choices
from datetime import datetime
from time import sleep
from parameters import spirit, vodka, intellect, injure, schizophrenia, hp
from variables import names, icons


def fight(uid1, uid2, un1, un2, t, r, bot, mid):
    info, wins1, wins2 = '', 0, 0
    for loop in range(t):
        if loop / 2 != 0 and t == 5:
            uid = uid1
            uid1 = uid2
            uid2 = uid

        weapon, defense = '', ''
        stats1 = r.hmget(uid1, 'name', 'class', 'weapon', 'defense')
        stats2 = r.hmget(uid2, 'name', 'class', 'weapon', 'defense')
        name1, name2 = int(stats1[0]), int(stats2[0])
        c1, c2 = int(stats1[1]), int(stats2[1])
        weapon1, weapon2 = int(stats1[2]), int(stats2[2])
        defense1, defense2 = int(stats1[3]), int(stats2[3])

        hach1, hach2, hach, worker, meat, cop, fsb, m1, m2, inj1, inj2 = 0, 0, '', '', '', '', '', '', '', '', ''
        if c1 == 1 or c1 == 11 or c1 == 21:
            if weapon2 == 0:
                hach1 = 1
        if c2 == 1 or c2 == 11 or c2 == 21:
            if weapon1 == 0:
                hach2 = 1
        if c1 == 21:
            if c2 == 1 or c2 == 11 or c2 == 21:
                if int(r.hget(uid1, 'hach_time2')) != datetime.now().day:
                    hach += '\n' + names[name1] + ': брат за брата! \U0001F919\n\U0001F4AA + 10 \U0001F54A +1000\n'
                    r.hset(uid1, 'hach_time2', datetime.now().day)
                    r.hincrby(uid1, 'strength', 10)
                    spirit(1000, uid1, 21, False, r)
        if c2 == 21:
            if c1 == 1 or c1 == 11 or c1 == 21:
                if int(r.hget(uid2, 'hach_time2')) != datetime.now().day:
                    hach += '\n' + names[name2] + ': брат за брата! \U0001F919\n\U0001F4AA + 10 \U0001F54A +1000\n'
                    r.hset(uid2, 'hach_time2', datetime.now().day)
                    r.hincrby(uid2, 'strength', 10)
                    spirit(1000, uid2, 21, False, r)
        if c1 == 22:
            if int(r.hget(uid1, 'worker')) != datetime.now().day and int(r.hget(uid1, 'time')) == datetime.now().day:
                alcohol = int(r.hget(uid1, 's1'))
                ran = choices([0, 1], weights=[100 - int(alcohol/2), int(alcohol/2)])
                if ran == [1]:
                    worker += '\n\U0001F9F0 ' + names[name1] + ' отримує від начальника талон на їжу.\n'
                    r.hset(uid1, 'worker', datetime.now().day)
                    r.hset(uid1, 'time', 0)
        if c2 == 22:
            if int(r.hget(uid2, 'worker')) != datetime.now().day and int(r.hget(uid2, 'time')) == datetime.now().day:
                alcohol = int(r.hget(uid2, 's1'))
                ran = choices([0, 1], weights=[100 - int(alcohol/2), int(alcohol/2)])
                if ran == [1]:
                    worker += '\n\U0001F9F0 ' + names[name2] + ' отримує від начальника талон на їжу.\n'
                    r.hset(uid2, 'worker', datetime.now().day)
                    r.hset(uid2, 'time', 0)
        if c1 == 26:
            if c2 != 6 and c2 != 16 and c2 != 26:
                if weapon2 != 0:
                    cop1 = choices([1, 0], weights=[20, 80])
                    if cop1 == [1]:
                        if weapon2 == 15 or weapon2 == 17:
                            r.hset(uid2, 'weapon', 0)
                            r.hset(uid2, 'defense', 0)
                            r.hset(uid2, 's_weapon', 0)
                            r.hset(uid2, 's_defense', 0)
                        else:
                            r.hset(uid2, 'weapon', 0)
                            r.hset(uid2, 's_weapon', 0)
                        if defense1 == 0:
                            r.hset(uid1, 'defense', 16)
                            r.hset(uid1, 's_defense', 10)
                        elif defense1 == 16:
                            r.hincrby(uid1, 's_defense', 10)
                        cop += '\n\U0001F46E ' + names[name1] + \
                               ' вилучив у ворога зброю! За це він отримав поліцейський щит.\n'
        if c2 == 26:
            if c1 != 6 and c1 != 16 and c1 != 26:
                if weapon1 != 0:
                    cop2 = choices([1, 0], weights=[20, 80])
                    if cop2 == [1]:
                        if defense1 == 15 or defense1 == 17:
                            r.hset(uid1, 'weapon', 0)
                            r.hset(uid1, 'defense', 0)
                            r.hset(uid1, 's_weapon', 0)
                            r.hset(uid1, 's_defense', 0)
                        else:
                            r.hset(uid1, 'defense', 0)
                            r.hset(uid1, 's_defense', 0)
                        if defense2 == 0:
                            r.hset(uid2, 'defense', 16)
                            r.hset(uid2, 's_defense', 10)
                        elif defense2 == 16:
                            r.hincrby(uid2, 's_defense', 10)
                        cop += '\n\U0001F46E ' + names[name2] + \
                               ' вилучив у ворога захисне спорядження! За це він отримав поліцейський щит.\n'

        if c1 == 27 and c2 == 0:
            fsb1 = choices([1, 0], weights=[5, 95])
            if fsb1 == [1]:
                r.hset(uid2, 'class', 7)
                r.hset(uid2, 'photo', randint(31, 35))
                r.hincrby(uid1, 'money', 20)
                fsb += '\n\U0001F921 ' + names[name1] + ' завербував ворога!\n\U0001F4B5 +20\n'
        if c2 == 27 and c1 == 0:
            fsb2 = choices([1, 0], weights=[5, 95])
            if fsb2 == [1]:
                r.hset(uid1, 'class', 7)
                r.hset(uid1, 'photo', randint(31, 35))
                r.hincrby(uid2, 'money', 20)
                fsb += '\n\U0001F921 ' + names[name2] + ' завербував ворога!\n\U0001F4B5 +20\n'

        if weapon2 == 1 and int(r.hget(uid1, 'spirit')) >= 300:
            foc = 1
            if c1 == 3 or c1 == 13 or c1 == 23:
                foc = choice([0, 0, 0, 0, 1])
            if foc == 1:
                if int(r.hget(uid1, 'spirit')) <= 1000:
                    r.hset(uid1, 'spirit', 0)
                elif 1000 < int(r.hget(uid1, 'spirit')) < 2500:
                    r.hincrby(uid1, 'spirit', -1000)
                else:
                    chance = choice([2.5, 3.333, 5])
                    r.hincrby(uid1, 'spirit', -int(int(r.hget(uid1, 'spirit')) / chance))
                r.hset(uid2, 'weapon', 0)
                weapon = '\n\n\U0001F5E1 ' + names[name2] + ' приніс на бій колючий дрин, опонента це' \
                                                            ' неабияк злякало!'
            else:
                weapon = '\n\n\U0001F52E ' + names[name1] + ' ухилився від дрина!'

        if weapon2 == 4 and int(r.hget(uid1, 'spirit')) >= 300:
            if int(r.hget(uid1, 'spirit')) <= 1000:
                r.hset(uid1, 'spirit', 0)
            elif 1000 < int(r.hget(uid1, 'spirit')) < 2500:
                r.hincrby(uid1, 'spirit', -1000)
            else:
                chance = choice([2.5, 3.333, 5])
                r.hincrby(uid1, 'spirit', -int(int(r.hget(uid1, 'spirit')) / chance))
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)
            weapon = '\n\n\U0001F5E1\U0001F5FF ' + names[name2] + ' прийшов на бій з битою, опонента це' \
                                                                  ' неабияк злякало!'

        if defense1 == 1 and int(r.hget(uid2, 'spirit')) >= 300:
            if int(r.hget(uid2, 'spirit')) <= 1000:
                r.hset(uid2, 'spirit', 0)
            elif 1000 < int(r.hget(uid2, 'spirit')) < 2500:
                r.hincrby(uid2, 'spirit', -1000)
            else:
                chance = choice([2.5, 3.333, 5])
                r.hincrby(uid2, 'spirit', -int(int(r.hget(uid2, 'spirit')) / chance))
            r.hset(uid1, 'defense', 0)
            defense = '\n\n\U0001F6E1 ' + names[name1] + ' захистився колючим щитом, опонент розгубився!'

        if int(r.hget(uid1, 'support')) == 1:
            hp(10, uid1, r)
            r.hincrby(uid1, 's_support', -1)
            if int(r.hget(uid1, 's_support')) <= 0:
                r.hset(uid1, 'support', 0)
        if int(r.hget(uid2, 'support')) == 1:
            hp(10, uid2, r)
            r.hincrby(uid2, 's_support', -1)
            if int(r.hget(uid2, 's_support')) <= 0:
                r.hset(uid2, 'support', 0)

        stats11 = r.hmget(uid1, 'strength', 'intellect', 'spirit', 'hp')
        stats22 = r.hmget(uid2, 'strength', 'intellect', 'spirit', 'hp')
        s1, s2 = int(stats11[0]), int(stats22[0])
        s11 = s1
        s22 = s2
        i1, i2 = int(stats11[1]), int(stats22[1])
        bd1, bd2 = int(stats11[2]), int(stats22[2])
        hp1, hp2 = int(stats11[3]), int(stats22[3])

        if hp1 >= 90:
            s1 = int(s1 * 1.1)
        if hp2 >= 90:
            s2 = int(s2 * 1.1)

        if int(r.hget(uid1, 'injure')) > 0:
            s1, bd1 = injure(uid1, s1, bd1, True, r)
            s11 = s1
            inj1 = '\U0001fa78 '
        if int(r.hget(uid2, 'injure')) > 0:
            s2, bd2 = injure(uid2, s2, bd2, True, r)
            s22 = s2
            inj2 = '\U0001fa78 '
        if int(r.hget(uid1, 'sch')) > 0:
            i1, bd1 = schizophrenia(uid1, i1, bd1, True, r)
            inj1 += '\U0001F464 '
        if int(r.hget(uid2, 'sch')) > 0:
            i2, bd2 = schizophrenia(uid2, i2, bd2, True, r)
            inj2 += '\U0001F464 '

        if weapon2 == 11:
            s1 = int(s1 / 2)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' дістав травмат і прострелив ворогу коліно!'
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)
        elif weapon2 == 12:
            s2 = int(s2 * 1.1)
            i2 = int(i2 * 1.1)
            bd2 = int(bd2 * 1.1)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' прийшов на бій з діамантовим кайлом.'
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)
        elif weapon2 == 13:
            if c2 == 13 or c2 == 23:
                if i1 > i2:
                    it = i2
                    i2 = i1
                    i1 = it
                if s1 > s2:
                    st = s2
                    s2 = s1
                    s1 = st
                if bd1 > bd2:
                    bt = bd2
                    bd2 = bd1
                    bd1 = bt
            else:
                st = s2
                it = i2
                bt = bd2
                s2 = s1
                s1 = st
                i2 = i1
                i1 = it
                bd2 = bd1
                bd1 = bt
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' поміняв характеристики місцями!'
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)
        elif weapon2 == 15:
            s2 = int(s2 * 1.75)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' приніс на бій заряджений АК-47...'
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)
                r.hset(uid2, 'defense', 0)
            ran = choices([1, 2], weights=[98, 2])
            if ran == [2] and defense1 != 2:
                weapon = weapon + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе ' \
                                  'і отримав важкі поранення.'
                r.hset(uid2, 'spirit', 0)
                r.hset(uid2, 'weapon', 0)
                r.hset(uid2, 'defense', 0)
                r.hincrby(uid2, 'injure', 100)
                if c2 == 25 and int(r.hget(uid2, 'strength')) >= 300:
                    weapon = '\n\n\U0001F5E1 ' + names[name2] + ' приніс на бій заряджений АК-47...' \
                              + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе і отримав' \
                                ' важкі поранення, як і ' + names[name1] + '.'
                    r.hset(uid1, 'spirit', 0)
                    if c1 != 6 and c1 != 16 and c1 != 26:
                        r.hset(uid1, 'weapon', 0)
                    r.hset(uid1, 'defense', 0)
                    r.hincrby(uid1, 'injure', 100)
        elif defense2 == 16:
            s1 = int(s1 * 0.8)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' атакує, прикрившись поліцейським щитом.'
            r.hincrby(uid2, 's_defense', -1)
            if int(r.hget(uid2, 's_defense')) <= 0:
                r.hset(uid2, 'defense', 0)
        elif weapon2 == 17:
            bd2 = 10000
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' кинувся на ворога, тримаючи в руках прапор новоросії.'
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)
                r.hset(uid2, 'defense', 0)
        elif weapon2 == 19:
            if int(r.hget(uid1, 'injure')) == 0:
                r.hincrby(uid1, 'injure', 1)
                weapon = '\n\n\U0001F5E1 ' + names[name2] + ' порізав ворога медичною пилкою.\n\U0001fa78 +1'
            else:
                r.hincrby(uid1, 'injure', -10)
                if int(r.hget(uid1, 'injure')) < 0:
                    r.hset(uid1, 'injure', 0)
                hp(-10, uid1, r)
                weapon = '\n\n\U0001F5E1 ' + names[name2] + ' припинив ворогу кровотечу.\n\U0001fa78 -10 \U0001fac0 -10'
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)

        elif weapon2 == 2 and defense1 != 2:
            weapon = '\n\n\u2620\uFE0F ' + names[name2] + ': АЛЛАХ АКБАР!'
            r.hincrby(uid1, 'injure', 200)
            r.hset(uid1, 'spirit', 0)
            if c1 != 6 and c1 != 16 and c1 != 26:
                r.hset(uid1, 'weapon', 0)
            r.hset(uid1, 'defense', 0)
            r.hset(uid2, 'weapon', 0)
            r.hset(uid2, 's_weapon', 0)
        elif weapon2 == 3:
            weapon = '\n\n\U0001F381 ' + names[name2] + ' прийшов на бій з посохом Діда Мороза і вручив ворогу ' \
                                                        'подарунок!\n\U0001F54A +1000'
            r.hincrby(uid1, 'n_packs', 1)
            spirit(1000, uid2, c2, False, r)
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)

        if defense1 == 9:
            s1 = int(s1 * 1.3)
            defense = '\n\n\U0001F6E1 ' + names[name1] + ' прикривається від ударів уламком бронетехніки.'
            r.hincrby(uid1, 's_defense', -1)
            if int(r.hget(uid1, 's_defense')) <= 0:
                r.hset(uid1, 'defense', 0)
                r.hincrby(uid1, 'money', 4)
        elif defense1 == 10:
            if i2 > i1:
                if c2 != 3 and c2 != 13 and c2 != 23:
                    s1 = int(s1 * 0.5)
                    intellect(1, uid1, r)
                    defense = '\n\n\U0001F6E1 ' + names[name1] + ' прийшов на бій під мухоморами. Він був' \
                                                                 ' обезсилений, але запам`ятав тактику ворога.'
                    r.hset(uid1, 'defense', 0)
        elif weapon1 == 15:
            s1 = int(s1 * 1.75)
            defense = '\n\n\U0001F5E1 ' + names[name1] + ' приніс на бій заряджений АК-47...'
            r.hincrby(uid1, 's_weapon', -1)
            if int(r.hget(uid1, 's_weapon')) <= 0:
                r.hset(uid1, 'weapon', 0)
                r.hset(uid1, 'defense', 0)
            ran = choices([1, 2], weights=[98, 2])
            if ran == [2] and defense2 != 2:
                defense = defense + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе ' \
                                    'і отримав важкі поранення.'
                r.hset(uid1, 'spirit', 0)
                r.hset(uid1, 'weapon', 0)
                r.hset(uid1, 'defense', 0)
                r.hincrby(uid1, 'injure', 100)
                if c1 == 25 and int(r.hget(uid1, 'strength')) >= 300:
                    defense = '\n\n\U0001F5E1 ' + names[name1] + ' приніс на бій заряджений АК-47...' \
                              + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе і отримав' \
                                ' важкі поранення, як і ' + names[name2] + '.'
                    r.hset(uid2, 'spirit', 0)
                    if c2 != 6 and c2 != 16 and c2 != 26:
                        r.hset(uid2, 'weapon', 0)
                    r.hset(uid2, 'defense', 0)
                    r.hincrby(uid2, 'injure', 100)
        elif defense1 == 16:
            s2 = int(s2 * 0.8)
            defense = '\n\n\U0001F6E1 ' + names[name1] + ' захищається поліцейським щитом.'
            r.hincrby(uid1, 's_defense', -1)
            if int(r.hget(uid1, 's_defense')) <= 0:
                r.hset(uid1, 'defense', 0)
        elif weapon1 == 17:
            bd1 = 10000
            defense = '\n\n\U0001F6E1 ' + names[name1] + ' гордо стоїть, тримаючи в руках прапор новоросії.'
            r.hincrby(uid1, 's_weapon', -1)
            if int(r.hget(uid1, 's_weapon')) <= 0:
                r.hset(uid1, 'weapon', 0)
                r.hset(uid1, 'defense', 0)
        elif defense1 == 2:
            s2 = int(s2 * 0.25)
            defense = '\n\n\U0001F6E1 ' + names[name1] + ' б`ється в бронежилеті.'
            r.hincrby(uid1, 's_defense', -1)
            if int(r.hget(uid1, 's_defense')) <= 0:
                r.hset(uid1, 'defense', 0)

        if c1 == 6 or c2 == 6 or c1 == 16 or c2 == 16 or c1 == 26 or c2 == 26:
            if c1 == 6 or c1 == 16 or c1 == 26:
                if c2 == 6 or c2 == 16 or c2 == 26:
                    bd1, bd2 = 0, 0
                else:
                    if weapon1 == 16 and defense1 == 16:
                        bd2 = 0
                    elif weapon1 == 16:
                        bd1, bd2 = 0, 0
                    if c1 == 16 or c1 == 26:
                        if i2 >= i1:
                            i1, i2 = 0, 0
                        else:
                            diff = i1 - i2
                            s1 = int(s1 * (1 + 0.15 * diff))
                            i1, i2 = 0, 0
            else:
                if weapon2 == 16 and defense2 == 16:
                    bd1 = 0
                elif weapon2 == 16:
                    bd1, bd2 = 0, 0
                if c2 == 16 or c2 == 26:
                    if i1 >= i2:
                        i1, i2 = 0, 0
                    else:
                        diff = i2 - i1
                        s2 = int(s2 * (1 + 0.15 * diff))
                        i1, i2 = 0, 0

        if hach1 == 1:
            s1 = int(s1 * 1.1)
            spirit(30, uid1, c1, True, r)
        elif hach1 == 0:
            if c1 == 1 or c1 == 11 or c1 == 21:
                s1 = int(s1 * 0.9)
        if hach2 == 1:
            s2 = int(s2 * 1.1)
            spirit(30, uid2, c2, True, r)
        elif hach2 == 0:
            if c2 == 1 or c2 == 11 or c2 == 21:
                s2 = int(s2 * 0.9)

        if c1 == 23:
            magic = int(r.hget(uid1, 'deaths')) * 5
            if magic > 35:
                magic = 35
            i1 = int(i1 * (1 + magic / 100))
        if c2 == 23:
            magic = int(r.hget(uid1, 'deaths')) * 3
            if magic > 33:
                magic = 33
            s2 = int(s2 * (1 + magic / 100))

        if c1 == 14 or c1 == 24:
            if c2 == 1 or c2 == 11 or c2 == 21:
                bd1 = bd1 * 2
            if c1 == 24:
                if int(r.hget(uid1, 'trophy')) > int(r.hget(uid2, 'trophy')):
                    s1 = int(s1 * 1.2)
                white = int(r.hget(uid1, 'trophy'))
                if white > 50:
                    white = 50
                bd1 = int(bd1 * (1 + white / 100))

        if c2 == 14 or c2 == 24:
            if c1 == 1 or c1 == 11 or c1 == 21:
                bd2 = bd2 * 2
            if c2 == 24:
                if int(r.hget(uid2, 'trophy')) > int(r.hget(uid1, 'trophy')):
                    s2 = int(s2 * 1.2)
                white = int(r.hget(uid2, 'trophy'))
                if white > 50:
                    white = 50
                bd2 = int(bd2 * (1 + white / 100))

        if c1 == 15 or c1 == 25:
            ch = int(r.hget(uid1, 'childs'))
            if ch > 20:
                ch = 20
            s1 = int(s1 * (1 + 0.025 * ch))
            if c1 == 25 and int(r.hget(uid1, 'strength')) >= 300 and int(r.hget(uid2, 'strength')) >= 30:
                shot = choices([1, 0], weights=[10, 90])
                if shot == [1]:
                    ran = randint(5, 10)
                    meat += '\n\U0001fa96 ' + names[name1] + ' +1 \U0001fa78 | ' + names[name2] + ' +' + \
                            str(ran) + ' \U0001fa78\n'
                    r.hincrby(uid1, 'injure', 1)
                    r.hincrby(uid2, 'injure', ran)
        if c2 == 15 or c2 == 25:
            ch = int(r.hget(uid2, 'childs'))
            if ch > 20:
                ch = 20
            s2 = int(s2 * (1 + 0.025 * ch))
            if c2 == 25 and int(r.hget(uid2, 'strength')) >= 300 and int(r.hget(uid1, 'strength')) >= 30:
                shot = choices([1, 0], weights=[10, 90])
                if shot == [1]:
                    ran = randint(5, 10)
                    meat += '\n\U0001fa96 ' + names[name2] + ' +1 \U0001fa78 | ' + names[name1] + ' +' + \
                            str(ran) + ' \U0001fa78\n'
                    r.hincrby(uid2, 'injure', 1)
                    r.hincrby(uid1, 'injure', ran)

        if c1 == 9 or c1 == 19 or c1 == 29:
            if hp2 < 50:
                hp(5, uid2, r)
                m1 = '\n\u26D1 ' + names[name1] + ' підлатав ворога.'
                if c1 == 29:
                    money = 0
                    if int(r.hget(uid2, 'injure')) > 0:
                        money += 1
                        r.hincrby(uid2, 'injure', -1)
                    if int(r.hget(uid2, 'sch')) > 0:
                        money += 1
                        r.hincrby(uid2, 'sch', -1)
                    ran = choices([0, 1], weights=[75, 25])
                    if ran == [1]:
                        money += 2
                        m1 += '\n\U0001F4B5 +' + str(money)
                        r.hincrby(uid1, 'money', money)
            else:
                ran = choices([0, 1], weights=[80, 20])
                if ran == [1]:
                    m1 = '\n\u26D1 ' + names[name1] + ' побачив що ' + names[name2] + ' занадто здоровий і виправив це.'
                    if c1 == 9:
                        r.hincrby(uid2, 'injure', 2)
                        m1 += '\n\U0001fa78 +2'
                    else:
                        nar = r.hmget(uid2, 'mushrooms', 's1')
                        r.hincrby(uid2, 'injure', 2 + int(nar[0]))
                        hp(-int(nar[1]), uid2, r)
                        m1 += '\n\U0001fa78 +' + str(2 + int(nar[0])) + ' \U0001fac0 -' + nar[1].decode()
        if c2 == 9 or c2 == 19 or c2 == 29:
            if hp1 < 50:
                hp(5, uid1, r)
                m2 = '\n\u26D1 ' + names[name2] + ' підлатав ворога.'
                if c2 == 29:
                    money = 0
                    if int(r.hget(uid1, 'injure')) > 0:
                        money += 1
                        r.hincrby(uid1, 'injure', -1)
                    if int(r.hget(uid1, 'sch')) > 0:
                        money += 1
                        r.hincrby(uid1, 'sch', -1)
                    ran = choices([0, 1], weights=[75, 25])
                    if ran == [1]:
                        money += 2
                        m2 += '\n\U0001F4B5 +' + str(money)
                        r.hincrby(uid2, 'money', money)
            else:
                ran = choices([0, 1], weights=[80, 20])
                if ran == [1]:
                    m2 = '\n\u26D1 ' + names[name2] + ' побачив що ' + names[name1] + ' занадто здоровий і виправив це.'
                    if c2 == 9:
                        r.hincrby(uid1, 'injure', 2)
                        m2 += '\n\U0001fa78 +2'
                    else:
                        nar = r.hmget(uid1, 'mushrooms', 's1')
                        r.hincrby(uid1, 'injure', 2 + int(nar[0]))
                        hp(-int(nar[1]), uid1, r)
                        m2 += '\n\U0001fa78 +' + str(2 + int(nar[0])) + ' \U0001fac0 -' + nar[1].decode()

        chance1 = s1 * (1 + 0.1 * i1) * (1 + 0.01 * (bd1 * 0.01))
        chance2 = s2 * (1 + 0.1 * i2) * (1 + 0.01 * (bd2 * 0.01))

        chance11 = chance1 / ((chance1 + chance2) / 100)
        chance22 = chance2 / ((chance1 + chance2) / 100)

        if c2 != 7 and chance11 > 95:
            win = choices(['1', '2'], weights=[95, 5])
        elif c1 != 7 and chance22 > 95:
            win = choices(['1', '2'], weights=[5, 95])
        elif c2 == 7 and chance11 > 80:
            win = choices(['1', '2'], weights=[80, 20])
        elif c1 == 7 and chance22 > 80:
            win = choices(['1', '2'], weights=[20, 80])
        else:
            win = choices(['1', '2'], weights=[chance1, chance2])

        if t == 5:
            if len(defense) > 0:
                defense = ' \U0001F6E1'
            if len(weapon) > 0:
                weapon = ' \U0001F5E1'
            if loop == 0:
                info = str(un1 + ' vs ' + un2 + '\n\n\U0001F3F7 ' + inj1 + names[name1] + ' ' + icons[c1] +
                           ' | ' + inj2 + names[name2] + ' ' + icons[c2] +
                           '\n\U0001F4AA ' + stats11[0].decode() + ' | ' + stats22[0].decode() +
                           '\n\U0001F9E0 ' + stats11[1].decode() + ' | ' + stats22[1].decode() +
                           '\n\U0001F54A ' + stats11[2].decode() + ' | ' + stats22[2].decode() + '\n\n')

            if win == ['1']:
                info += str(loop + 1) + '. ' + '\U0001F3C6 ' + names[name1] + ' ' + weapon + ' | ' + \
                        names[name2] + ' ' + defense + '\n'
                if loop % 2 == 0:
                    wins1 += 1
                else:
                    wins2 += 1
            elif win == ['2']:
                info += str(loop + 1) + '. ' + names[name1] + ' ' + weapon + ' | ' + '\U0001F3C6 ' \
                        + names[name2] + ' ' + defense + '\n'
                if loop % 2 == 0:
                    wins2 += 1
                else:
                    wins1 += 1
            if loop == 4:
                if wins1 > wins2:
                    info += '\n\U0001F3C6 ' + str(un1) + ' перемагає ' + str(un2) + ' в турнірному бою!'
                else:
                    info += '\n\U0001F3C6 ' + str(un2) + ' перемагає ' + str(un1) + ' в турнірному бою!'
            bot.edit_message_text(text=info, inline_message_id=mid)
            sleep(3)
            continue

        info = str('\u2744\uFE0F ' + un1 + ' vs ' + un2 + '\n\n\U0001F3F7 ' + inj1 + names[name1] + ' ' +
                   icons[c1] + ' | ' + inj2 + names[name2] + ' ' + icons[c2] +
                   '\n\U0001F4AA ' + str(s1) + ' | ' + str(s2) +
                   '\n\U0001F9E0 ' + str(i1) + ' | ' + str(i2) +
                   '\n\U0001F54A ' + str(bd1) + ' | ' + str(bd2)) + weapon + defense

        if win == ['1']:
            if s11 / s22 > 2:
                bonus = randint(1, 20)
                grn = ''
            elif s11 / s22 < 0.5:
                bonus = randint(60, 120)
                grn = choices([1, 2, 3], weights=[50, 48, 2])
                if grn == [1]:
                    r.hincrby(uid1, 'money', 1)
                    grn = '\n\U0001F4B5 +1'
                elif grn == [2]:
                    r.hincrby(uid1, 'money', 2)
                    grn = '\n\U0001F4B5 +2'
                elif grn == [3]:
                    r.hincrby(uid1, 'money', 3)
                    grn = '\n\U0001F4B5 +3'
            else:
                bonus = randint(20, 60)
                grn = choices([0, 1, 2, 3], weights=[50, 44, 5, 1])
                if grn == [1]:
                    r.hincrby(uid1, 'money', 1)
                    grn = '\n\U0001F4B5 +1'
                elif grn == [2]:
                    r.hincrby(uid1, 'money', 2)
                    grn = '\n\U0001F4B5 +2'
                elif grn == [3]:
                    r.hincrby(uid1, 'money', 3)
                    grn = '\n\U0001F4B5 +3'
                else:
                    grn = ''

            if hach1 == 1:
                if c1 != 1:
                    hc = s2 / (s1 + s2)
                    trick = choices([1, 0], weights=[hc, 1 - hc])
                    if trick == [1]:
                        trick = choices([1, 2, 3], weights=[45, 45, 10])
                        if trick == [1]:
                            ran = randint(50, 100)
                            hach += '\n\U0001F919 ' + names[name1] + ' кинув суперника через стегно!\n\U0001F54A -' + \
                                    str(ran) + '\n'
                            spirit(-ran, uid2, c2, False, r)
                        elif trick == [2]:
                            ran = randint(50, 100)
                            hach += '\n\U0001F919 ' + names[name1] + ' кинув суперника млином!\n\U0001F54A +' + \
                                    str(ran) + '\n'
                            spirit(ran, uid1, c1, False, r)
                        elif trick == [3]:
                            hach += '\n\U0001F919 ' + names[name1] + ' кинув суперника прогином!\n\U0001F4B5 +2\n'
                            r.hincrby(uid1, 'money', 2)

            pag = ''
            if weapon2 == 14:
                r.hincrby(uid1, 'spirit', int(r.hget(uid2, 'spirit')))
                r.hincrby(uid2, 'spirit', -int(r.hget(uid2, 'spirit')))
                r.hincrby(uid2, 's_weapon', -1)
                if int(r.hget(uid2, 's_weapon')) == 0:
                    r.hset(uid2, 'weapon', 0)
                pag = '\n\U0001F5E1 ' + names[name2] + ' прийшов на бій з сокирою Перуна. Коли русак програв' \
                                                       ', його бойовий дух влився у ворога...'

            spirit(bonus, uid1, c1, True, r)
            spirit(-bonus, uid2, c2, True, r)
            r.hincrby(uid1, 'wins', 1)

            hack = ''
            if c2 == 8 or c2 == 18 or c2 == 28:
                hack1 = choices([0, 1], weights=[82, 18])
                if weapon2 == 18:
                    hack1 = choices([0, 1], weights=[1, 99])
                    hack = '\n\n\U0001F5E1 ' + names[name2] + ' використав експлойт...'
                    r.hincrby(uid2, 's_weapon', -1)
                    if int(r.hget(uid2, 's_weapon')) <= 0:
                        r.hset(uid2, 'weapon', 0)
                if hack1 == [1]:
                    spirit(bonus * 2, uid2, c2, False, r)
                    spirit(-bonus, uid1, c1, False, r)
                    money = 1
                    if c2 == 28:
                        money2 = int(r.hget(uid1, 'money'))
                        if money2 > 250:
                            money2 = 250
                        if money2 >= 50:
                            money = int(money2 / 50)
                        else:
                            money = 1
                    r.hincrby(uid2, 'money', money)
                    hack = hack + '\n\U0001F4DF ' + names[name2] + ' зламав бота, і переписав бонусний бойовий дух ' \
                                                                   'собі.\n\U0001F4B5 +' + str(money)

            if weapon1 == 15:
                meat += '\n' + names[name1] + ' бахнув горілочки. ' + '\U0001F54A ' + vodka(uid1, 5, r)
            hp(-1, uid2, r)
            bottle = ''
            if int(r.hget(uid1, 'support')) == 3:
                bottle = '\n\U0001F37E ' + names[name1] + ' випив шампанського, а ' + names[name2] + \
                         ' сів на пляшку.\n\u2622 +5'
                r.hincrby(uid1, 'vodka', 5)
                r.hincrby(uid1, 's_support', -1)
                if int(r.hget(uid1, 's_support')) <= 0:
                    r.hset(uid1, 'support', 0)
            elif int(r.hget(uid2, 'support')) == 3:
                bottle = '\n\U0001F37E ' + names[name1] + ' випив шампанського, а ' + names[name2] + \
                         ' сів на пляшку.\n\u2622 +5'
                r.hincrby(uid1, 'vodka', 5)
                r.hincrby(uid2, 's_support', -1)
                if int(r.hget(uid2, 's_support')) <= 0:
                    r.hset(uid2, 'support', 0)
            info += '\n\U0001fac0 ' + stats11[3].decode() + ' | ' + stats22[3].decode() + '(-1)' + m1 + m2
            win_info = str('\n\n\U0001F3C6 ' + str(un1) + ' перемагає ' + str(un2) + '! ' + str(grn) +
                           '\nЙого русак отримує +' + str(bonus) + ' бойового духу, а русак опонента'
                                                                   ' стільки ж втрачає.' +
                           hach + worker + meat + cop + pag + fsb + hack + bottle)
            return info + win_info
        elif win == ['2']:
            if s22 / s11 > 2:
                bonus = randint(1, 20)
                grn = ''
            elif s22 / s11 < 0.5:
                bonus = randint(60, 120)
                grn = choices([1, 2, 3], weights=[50, 48, 2])
                if grn == [1]:
                    r.hincrby(uid2, 'money', 1)
                    grn = '\n\U0001F4B5 +1'
                elif grn == [2]:
                    r.hincrby(uid2, 'money', 2)
                    grn = '\n\U0001F4B5 +2'
                elif grn == [3]:
                    r.hincrby(uid2, 'money', 3)
                    grn = '\n\U0001F4B5 +3'
            else:
                bonus = randint(20, 60)
                grn = choices([0, 1, 2, 3], weights=[50, 44, 5, 1])
                if grn == [1]:
                    r.hincrby(uid2, 'money', 1)
                    grn = '\n\U0001F4B5 +1'
                elif grn == [2]:
                    r.hincrby(uid2, 'money', 2)
                    grn = '\n\U0001F4B5 +2'
                elif grn == [3]:
                    r.hincrby(uid2, 'money', 3)
                    grn = '\n\U0001F4B5 +3'
                else:
                    grn = ''

            if hach2 == 1:
                if c2 != 1:
                    hc = s1 / (s1 + s2)
                    trick = choices([1, 0], weights=[hc, 1 - hc])
                    if trick == [1]:
                        trick = choices([1, 2, 3], weights=[45, 45, 10])
                        if trick == [1]:
                            ran = randint(50, 100)
                            hach += '\n\U0001F919 ' + names[name2] + ' кинув суперника через стегно!\n\U0001F54A -' + \
                                    str(ran) + '\n'
                            spirit(-ran, uid1, c1, False, r)
                        elif trick == [2]:
                            ran = randint(50, 100)
                            hach += '\n\U0001F919 ' + names[name2] + ' кинув суперника млином!\n\U0001F54A +' + \
                                    str(ran) + '\n'
                            spirit(ran, uid2, c2, False, r)
                        elif trick == [3]:
                            hach += '\n\U0001F919 ' + names[name2] + ' кинув суперника прогином!\n\U0001F4B5 +2\n'
                            r.hincrby(uid2, 'money', 2)

            pag = ''
            if weapon2 == 14:
                r.hincrby(uid2, 'spirit', int(r.hget(uid1, 'spirit')))
                r.hincrby(uid1, 'spirit', -int(r.hget(uid1, 'spirit')))
                r.hincrby(uid2, 's_weapon', -1)
                if int(r.hget(uid2, 's_weapon')) == 0:
                    r.hset(uid2, 'weapon', 0)
                pag = '\n\U0001F5E1 ' + names[name2] + ' прийшов на бій з сокирою Перуна. Коли ворог програв' \
                                                       ', його бойовий дух влився у русака...'

            spirit(bonus, uid2, c2, True, r)
            spirit(-bonus, uid1, c1, True, r)
            r.hincrby(uid2, 'wins', 1)

            hack = ''
            if c1 == 8 or c1 == 18 or c1 == 28:
                hack2 = choices([0, 1], weights=[82, 18])
                if weapon1 == 18:
                    hack2 = choices([0, 1], weights=[1, 99])
                    hack = '\n\n\U0001F5E1 ' + names[name1] + ' використав експлойт...'
                    r.hincrby(uid1, 's_weapon', -1)
                    if int(r.hget(uid1, 's_weapon')) <= 0:
                        r.hset(uid1, 'weapon', 0)
                if hack2 == [1]:
                    spirit(bonus * 2, uid1, c1, False, r)
                    spirit(-bonus, uid2, c2, False, r)
                    money = 1
                    if c1 == 28:
                        money2 = int(r.hget(uid2, 'money'))
                        if money2 > 250:
                            money2 = 250
                        if money2 >= 50:
                            money = int(money2 / 50)
                        else:
                            money = 1
                    r.hincrby(uid1, 'money', money)
                    hack = hack + '\n\U0001F4DF ' + names[name1] + ' зламав бота, і переписав бонусний бойовий дух ' \
                                                                   'собі.\n\U0001F4B5 +' + str(money)

            if weapon2 == 15:
                meat += '\n' + names[name2] + ' бахнув горілочки. ' + '\U0001F54A ' + vodka(uid2, 5, r)
            hp(-1, uid1, r)
            bottle = ''
            if int(r.hget(uid2, 'support')) == 3:
                bottle = '\n\U0001F37E ' + names[name2] + ' випив шампанського, а ' + names[name1] + \
                         ' сів на пляшку.\n\u2622 +5'
                r.hincrby(uid2, 'vodka', 5)
                r.hincrby(uid2, 's_support', -1)
                if int(r.hget(uid2, 's_support')) <= 0:
                    r.hset(uid2, 'support', 0)
            elif int(r.hget(uid1, 'support')) == 3:
                bottle = '\n\U0001F37E ' + names[name2] + ' випив шампанського, а ' + names[name1] + \
                         ' сів на пляшку.\n\u2622 +5'
                r.hincrby(uid2, 'vodka', 5)
                r.hincrby(uid1, 's_support', -1)
                if int(r.hget(uid1, 's_support')) <= 0:
                    r.hset(uid1, 'support', 0)
            info += '\n\U0001fac0 ' + stats11[3].decode() + '(-1) | ' + stats22[3].decode() + m1 + m2
            win_info = str('\n\n\U0001F3C6 ' + str(un2) + ' перемагає ' + str(un1) + '! ' + str(grn) +
                           '\nЙого русак отримує +' + str(bonus) + ' бойового духу, а русак опонента'
                                                                   ' стільки ж втрачає.' +
                           hach + worker + meat + cop + pag + fsb + hack + bottle)
            return info + win_info
