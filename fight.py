from random import randint, choice, choices
from datetime import datetime
from asyncio import sleep

from config import r, bot
from parameters import spirit, vodka, intellect, injure, schizophrenia, trance, hp, \
    damage_weapon, damage_defense, damage_support, increase_trance
from variables import names, icons, p7
from methods import checkClan


async def fight(uid1, uid2, un1, un2, t, mid):
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

        grn, hach, worker, meat, cop, fsb, m1, m2, inj1, inj2 = '', '', '', '', '', '', '', '', '', ''
        m_bonus, hach1, hach2 = [0], 0, 0

        if c1 == 1 or c1 == 11 or c1 == 21:
            if weapon2 == 0:
                hach1 = 1
        if c2 == 1 or c2 == 11 or c2 == 21:
            if weapon1 == 0:
                hach2 = 1
        if c1 == 21 and t == 1:
            if c2 == 1 or c2 == 11 or c2 == 21:
                if int(r.hget(uid1, 'hach_time2')) != datetime.now().day:
                    hach += '\n' + names[name1] + ': брат за брата! \U0001F919\n\U0001F4AA + 10 \U0001F54A +1000\n'
                    r.hset(uid1, 'hach_time2', datetime.now().day)
                    r.hincrby(uid1, 'strength', 10)
                    spirit(1000, uid1, 0)
        if c2 == 21 and t == 1:
            if c1 == 1 or c1 == 11 or c1 == 21:
                if int(r.hget(uid2, 'hach_time2')) != datetime.now().day:
                    hach += '\n' + names[name2] + ': брат за брата! \U0001F919\n\U0001F4AA + 10 \U0001F54A +1000\n'
                    r.hset(uid2, 'hach_time2', datetime.now().day)
                    r.hincrby(uid2, 'strength', 10)
                    spirit(1000, uid2, 0)
        if c1 == 22 and t == 1:
            if int(r.hget(uid1, 'worker')) != datetime.now().day and int(r.hget(uid1, 'time')) == datetime.now().day:
                alcohol = int(r.hget(uid1, 's1'))
                ran = choices([0, 1], weights=[100 - int(alcohol/2), int(alcohol/2)])
                if ran == [1]:
                    worker += '\n\U0001F9F0 ' + names[name1] + ' отримує від начальника талон на їжу.\n'
                    r.hset(uid1, 'worker', datetime.now().day)
                    r.hset(uid1, 'time', 0)
        if c2 == 22 and t == 1:
            if int(r.hget(uid2, 'worker')) != datetime.now().day and int(r.hget(uid2, 'time')) == datetime.now().day:
                alcohol = int(r.hget(uid2, 's1'))
                ran = choices([0, 1], weights=[100 - int(alcohol/2), int(alcohol/2)])
                if ran == [1]:
                    worker += '\n\U0001F9F0 ' + names[name2] + ' отримує від начальника талон на їжу.\n'
                    r.hset(uid2, 'worker', datetime.now().day)
                    r.hset(uid2, 'time', 0)
        if c1 == 26 and t == 1:
            if c2 != 6 and c2 != 16 and c2 != 26:
                if weapon2 != 0:
                    cop1 = choices([1, 0], weights=[20, 80])
                    if cop1 == [1]:
                        r.hset(uid2, 'weapon', 0)
                        r.hset(uid2, 's_weapon', 0)
                        if defense1 == 0:
                            r.hset(uid1, 'defense', 16)
                            r.hset(uid1, 's_defense', 10)
                        elif defense1 == 16:
                            r.hincrby(uid1, 's_defense', 10)
                        cop += '\n\U0001F46E ' + names[name1] + \
                               ' вилучив у ворога зброю! За це він отримав поліцейський щит.\n'
        if c2 == 26 and t == 1:
            if c1 != 6 and c1 != 16 and c1 != 26:
                if weapon1 != 0:
                    cop2 = choices([1, 0], weights=[20, 80])
                    if cop2 == [1]:
                        r.hset(uid1, 'defense', 0)
                        r.hset(uid1, 's_defense', 0)
                        if defense2 == 0:
                            r.hset(uid2, 'defense', 16)
                            r.hset(uid2, 's_defense', 10)
                        elif defense2 == 16:
                            r.hincrby(uid2, 's_defense', 10)
                        cop += '\n\U0001F46E ' + names[name2] + \
                               ' вилучив у ворога захисне спорядження! За це він отримав поліцейський щит.\n'

        if c1 == 27 and c2 == 0 and t == 1:
            fsb1 = choices([1, 0], weights=[5, 95])
            if fsb1 == [1]:
                r.hset(uid2, 'class', 7)
                r.sadd('class-7', uid2)
                r.hset(uid2, 'photo', choice(p7))
                r.hincrby(uid1, 'money', 20)
                fsb += '\n\U0001F921 ' + names[name1] + ' завербував ворога!\n\U0001F4B5 +20\n'
        if c2 == 27 and c1 == 0 and t == 1:
            fsb2 = choices([1, 0], weights=[5, 95])
            if fsb2 == [1]:
                r.hset(uid1, 'class', 7)
                r.sadd('class-7', uid1)
                r.hset(uid1, 'photo', choice(p7))
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
                damage_weapon(uid2, c2)
                weapon = '\n\n\U0001F5E1 ' + names[name2] + ' приніс на бій колючий дрин, опонента це' \
                                                            ' неабияк злякало!'
            else:
                weapon = '\n\n\U0001F52E ' + names[name1] + ' ухилився від дрина!\n\U0001F464 +5'
                r.hincrby(uid2, 'sch', 5)

        if weapon2 == 4 and int(r.hget(uid1, 'spirit')) >= 300:
            if int(r.hget(uid1, 'spirit')) <= 1000:
                r.hset(uid1, 'spirit', 0)
            elif 1000 < int(r.hget(uid1, 'spirit')) < 2500:
                r.hincrby(uid1, 'spirit', -1000)
            else:
                chance = choice([2.5, 3.333, 5])
                r.hincrby(uid1, 'spirit', -int(int(r.hget(uid1, 'spirit')) / chance))
            damage_weapon(uid2, c2)
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
            damage_defense(uid1, 1)
            defense = '\n\n\U0001F6E1 ' + names[name1] + ' захистився колючим щитом, опонент розгубився!'

        if int(r.hget(uid1, 'support')) == 1:
            hp(10, uid1)
            damage_support(uid1)
        if int(r.hget(uid2, 'support')) == 1:
            hp(10, uid2)
            damage_support(uid2)

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
            s1, bd1 = injure(uid1, s1, bd1, True)
            s11 = s1
            inj1 = '\U0001fa78 '
        if int(r.hget(uid2, 'injure')) > 0:
            s2, bd2 = injure(uid2, s2, bd2, True)
            s22 = s2
            inj2 = '\U0001fa78 '
        if int(r.hget(uid1, 'sch')) > 0:
            i1, bd1 = schizophrenia(uid1, i1, bd1, True)
            inj1 += '\U0001F464 '
        if int(r.hget(uid2, 'sch')) > 0:
            i2, bd2 = schizophrenia(uid2, i2, bd2, True)
            inj2 += '\U0001F464 '
        if int(r.hget(uid1, 'buff')) > 0:
            s1, bd1 = trance(uid1, s1, bd1, True)
            s11 = s1
            inj1 = '\U0001F44A '
        if int(r.hget(uid2, 'buff')) > 0:
            s2, bd2 = trance(uid2, s2, bd2, True)
            s22 = s2
            inj2 = '\U0001F44A '

        if weapon2 == 11:
            s1 = int(s1 / 2)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' дістав травмат і прострелив ворогу коліно!'
            damage_weapon(uid2, c2)
        elif weapon2 == 12:
            s2 = int(s2 * 1.2)
            i2 = int(i2 * 1.2)
            bd2 = int(bd2 * 1.2)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' прийшов на бій з діамантовим кайлом.'
            damage_weapon(uid2, c2)
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
            damage_weapon(uid2, c2)
        elif weapon2 == 15:
            s2 = int(s2 * 1.75)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' приніс на бій заряджений АК-47...'
            damage_weapon(uid2, c2)
            ran = choices([1, 2], weights=[99, 1])
            if ran == [2] and defense1 != 2:
                weapon = weapon + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе ' \
                                  'і отримав важкі поранення.'
                r.hset(uid2, 'spirit', 0)
                r.hset(uid2, 'hp', 0)
                r.hset(uid2, 'weapon', 0)
                r.hset(uid2, 'defense', 0)
                r.hset(uid2, 'support', 0)
                r.hincrby(uid2, 'injure', 150)
                if c2 == 25 and int(r.hget(uid2, 'strength')) >= 300:
                    weapon = '\n\n\U0001F5E1 ' + names[name2] + ' приніс на бій заряджений АК-47...' \
                              + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе і отримав' \
                                ' важкі поранення, як і ' + names[name1] + '.'
                    r.hset(uid1, 'spirit', 0)
                    r.hset(uid1, 'hp', 0)
                    if c1 != 6 and c1 != 16 and c1 != 26:
                        r.hset(uid1, 'weapon', 0)
                    r.hset(uid1, 'defense', 0)
                    r.hset(uid1, 'support', 0)
                    r.hincrby(uid1, 'injure', 150)
        elif defense2 == 16:
            s1 = int(s1 * 0.8)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' атакує, прикрившись поліцейським щитом.'
            damage_defense(uid2, 16)
        elif weapon2 == 19:
            if int(r.hget(uid1, 'injure')) == 0:
                r.hincrby(uid1, 'injure', 1)
                weapon = '\n\n\U0001F5E1 ' + names[name2] + ' порізав ворога медичною пилкою.\n\U0001fa78 +1'
            else:
                r.hincrby(uid1, 'injure', -10)
                if int(r.hget(uid1, 'injure')) < 0:
                    r.hset(uid1, 'injure', 0)
                hp(-10, uid1)
                weapon = '\n\n\U0001F5E1 ' + names[name2] + ' припинив ворогу кровотечу.\n\U0001fa78 -10 \U0001fac0 -10'
            damage_weapon(uid2, c2)

        if weapon2 == 2 and defense1 != 2 and t == 1:
            weapon = '\n\n\u2620\uFE0F ' + names[name2] + ': АЛЛАХ АКБАР!'
            r.hincrby(uid1, 'injure', 300)
            r.hset(uid1, 'spirit', 0)
            if c1 != 6 and c1 != 16 and c1 != 26:
                r.hset(uid1, 'weapon', 0)
            r.hset(uid1, 'hp', 0)
            r.hset(uid1, 'defense', 0)
            r.hset(uid1, 'support', 0)
            damage_weapon(uid2, c2)

        elif weapon1 == 15:
            s1 = int(s1 * 1.75)
            defense = '\n\n\U0001F5E1 ' + names[name1] + ' приніс на бій заряджений АК-47...'
            damage_weapon(uid1, c1)
            ran = choices([1, 2], weights=[99, 1])
            if ran == [2] and defense2 != 2:
                defense = defense + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе ' \
                                    'і отримав важкі поранення.'
                r.hset(uid1, 'spirit', 0)
                r.hset(uid1, 'hp', 0)
                r.hset(uid1, 'weapon', 0)
                r.hset(uid1, 'defense', 0)
                r.hset(uid1, 'support', 0)
                r.hincrby(uid1, 'injure', 150)
                if c1 == 25 and int(r.hget(uid1, 'strength')) >= 300:
                    defense = '\n\n\U0001F5E1 ' + names[name1] + ' приніс на бій заряджений АК-47...' \
                              + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе і отримав' \
                                ' важкі поранення, як і ' + names[name2] + '.'
                    r.hset(uid2, 'spirit', 0)
                    r.hset(uid2, 'hp', 0)
                    if c2 != 6 and c2 != 16 and c2 != 26:
                        r.hset(uid2, 'weapon', 0)
                    r.hset(uid2, 'defense', 0)
                    r.hset(uid2, 'support', 0)
                    r.hincrby(uid2, 'injure', 150)

        if defense1 == 9:
            s1 = int(s1 * 1.3)
            defense = '\n\n\U0001F6E1 ' + names[name1] + ' прикривається від ударів уламком бронетехніки.'
            damage_defense(uid1, 9)
        elif defense1 == 10 and t == 1:
            if i2 > i1:
                if c2 != 3 and c2 != 13 and c2 != 23:
                    s1 = int(s1 * 0.5)
                    intellect(1, uid1)
                    r.hincrby(uid1, 'mushrooms', 1)
                    defense = '\n\n\U0001F6E1 ' + names[name1] + ' прийшов на бій під мухоморами. Він був' \
                                                                 ' обезсилений, але запам`ятав тактику ворога.'
                    damage_defense(uid1, 10)
        elif defense1 == 16:
            s2 = int(s2 * 0.8)
            defense = '\n\n\U0001F6E1 ' + names[name1] + ' захищається поліцейським щитом.'
            damage_defense(uid1, 16)
        elif defense1 == 2:
            s2 = int(s2 * 0.25)
            defense += '\n\n\U0001F6E1 ' + names[name1] + ' б`ється в бронежилеті.'
            damage_defense(uid1, 2)

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
            s1 = int(s1 * 1.15)
            spirit(30, uid1, 0)
        elif hach1 == 0:
            if c1 == 1 or c1 == 11 or c1 == 21:
                s1 = int(s1 * 0.85)
        if hach2 == 1:
            s2 = int(s2 * 1.15)
            spirit(30, uid2, 0)
        elif hach2 == 0:
            if c2 == 1 or c2 == 11 or c2 == 21:
                s2 = int(s2 * 0.85)

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

        if c1 == 4 or c1 == 14 or c1 == 24:
            bd1 = bd1 * 2
        if c2 == 4 or c2 == 14 or c2 == 24:
            bd2 = bd2 * 2

        if c1 == 14 or c1 == 24:
            if c2 == 1 or c2 == 11 or c2 == 21:
                bd1 = bd1 * 2
            if int(r.hget(uid1, 'trophy')) > int(r.hget(uid2, 'trophy')):
                s1 = int(s1 * 1.2)
            if c1 == 24:
                white = int(r.hget(uid1, 'trophy'))
                if white > 50:
                    white = 50
                bd1 = int(bd1 * (1 + white / 100))

        if c2 == 14 or c2 == 24:
            if c1 == 1 or c1 == 11 or c1 == 21:
                bd2 = bd2 * 2
            if int(r.hget(uid2, 'trophy')) > int(r.hget(uid1, 'trophy')):
                s2 = int(s2 * 1.2)
            if c2 == 24:
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
                hp(5, uid2)
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
                        hp(-int(nar[1]), uid2)
                        m1 += '\n\U0001fa78 +' + str(2 + int(nar[0])) + ' \U0001fac0 -' + nar[1].decode()
        if c2 == 9 or c2 == 19 or c2 == 29:
            if hp1 < 50:
                hp(5, uid1)
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
                        hp(-int(nar[1]), uid1)
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
            await bot.edit_message_text(text=info, inline_message_id=mid)
            await sleep(3)
            continue

        info = str(un1 + ' vs ' + un2 + '\n\n\U0001F3F7 ' + inj1 + names[name1] + ' ' +
                   icons[c1] + ' | ' + inj2 + names[name2] + ' ' + icons[c2] +
                   '\n\U0001F4AA ' + str(s1) + ' | ' + str(s2) +
                   '\n\U0001F9E0 ' + str(i1) + ' | ' + str(i2) +
                   '\n\U0001F54A ' + str(bd1) + ' | ' + str(bd2)) + weapon + defense

        if win == ['1']:
            if s11 / s22 > 2:
                bonus = randint(1, 20)
            elif s11 / s22 < 0.5:
                bonus = randint(60, 120)
                m_bonus = choices([1, 2, 3], weights=[50, 48, 2])
            else:
                bonus = randint(20, 60)
                m_bonus = choices([0, 1, 2, 3], weights=[50, 44, 5, 1])
            if m_bonus[0] > 0:
                if checkClan(uid1, base=4):
                    if choices([1, 0], weights=[s2 / (s1 + s2), 1 - s2 / (s1 + s2)]) == [1]:
                        m_bonus = [m_bonus[0] * 2]
                r.hincrby(uid1, 'money', m_bonus[0])
                grn = '\n\U0001F4B5 +' + str(m_bonus[0])

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
                            spirit(-ran, uid2, 0)
                        elif trick == [2]:
                            ran = randint(50, 100)
                            hach += '\n\U0001F919 ' + names[name1] + ' кинув суперника млином!\n\U0001F54A +' + \
                                    str(ran) + '\n'
                            spirit(ran, uid1, 0)
                        elif trick == [3]:
                            hach += '\n\U0001F919 ' + names[name1] + ' кинув суперника прогином!\n\U0001F4B5 +2\n'
                            r.hincrby(uid1, 'money', 2)

            pag = ''
            if weapon2 == 14:
                r.hincrby(uid1, 'spirit', int(r.hget(uid2, 'spirit')))
                r.hincrby(uid2, 'spirit', -int(r.hget(uid2, 'spirit')))
                damage_weapon(uid2, c2)
                pag = '\n\U0001F5E1 ' + names[name2] + ' прийшов на бій з сокирою Перуна. Коли русак програв' \
                                                       ', його бойовий дух влився у ворога...'

            spirit(bonus, uid1, c1)
            spirit(-bonus, uid2, 0)
            r.hincrby(uid1, 'wins', 1)

            hack = ''
            if c2 == 8 or c2 == 18 or c2 == 28:
                hack1 = choices([0, 1], weights=[82, 18])
                if weapon2 == 18:
                    hack1 = choices([0, 1], weights=[1, 99])
                    hack = '\n\n\U0001F5E1 ' + names[name2] + ' використав експлойт...'
                    damage_weapon(uid2, c2)
                if hack1 == [1]:
                    spirit(bonus * 2, uid2, 0)
                    spirit(-bonus, uid1, 0)
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
                    ran = choices([1, 0], weights=[0.1, 99.9])
                    if ran == [1]:
                        hack += '\nGET_.../watch?v=dQw4w9WgXcQ'

            if weapon1 == 15:
                meat += '\n' + names[name1] + ' бахнув горілочки. ' + '\U0001F54A ' + vodka(uid1)
            hp(-1, uid2)
            info += '\n\U0001fac0 ' + stats11[3].decode() + ' | ' + stats22[3].decode() + '(-1)' + m1 + m2
            win_info = str('\n\n\U0001F3C6 ' + str(un1) + ' перемагає ' + str(un2) + '! ' + str(grn) +
                           '\nЙого русак отримує +' + str(bonus) + ' бойового духу, а русак опонента'
                                                                   ' стільки ж втрачає.' +
                           hach + worker + meat + cop + pag + fsb + hack)
            return info + win_info
        elif win == ['2']:
            if s22 / s11 > 2:
                bonus = randint(1, 20)
            elif s22 / s11 < 0.5:
                bonus = randint(60, 120)
                m_bonus = choices([1, 2, 3], weights=[50, 48, 2])
            else:
                bonus = randint(20, 60)
                m_bonus = choices([0, 1, 2, 3], weights=[50, 44, 5, 1])
            if m_bonus[0] > 0:
                if checkClan(uid2, base=4):
                    if choices([1, 0], weights=[s1 / (s1 + s2), 1 - s1 / (s1 + s2)]) == [1]:
                        m_bonus = [m_bonus[0] * 2]
                r.hincrby(uid2, 'money', m_bonus[0])
                grn = '\n\U0001F4B5 +' + str(m_bonus[0])

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
                            spirit(-ran, uid1, 0)
                        elif trick == [2]:
                            ran = randint(50, 100)
                            hach += '\n\U0001F919 ' + names[name2] + ' кинув суперника млином!\n\U0001F54A +' + \
                                    str(ran) + '\n'
                            spirit(ran, uid2, 0)
                        elif trick == [3]:
                            hach += '\n\U0001F919 ' + names[name2] + ' кинув суперника прогином!\n\U0001F4B5 +2\n'
                            r.hincrby(uid2, 'money', 2)

            pag = ''
            if weapon2 == 14:
                r.hincrby(uid2, 'spirit', int(r.hget(uid1, 'spirit')))
                r.hincrby(uid1, 'spirit', -int(r.hget(uid1, 'spirit')))
                damage_weapon(uid2, c2)
                pag = '\n\U0001F5E1 ' + names[name2] + ' прийшов на бій з сокирою Перуна. Коли ворог програв' \
                                                       ', його бойовий дух влився у русака...'
            elif weapon2 == 17:
                r.hincrby(uid2, 'wins', 1)
                fsb += '\n\n\U0001F5E1 ' + names[name2] + ' гордо стоїть, тримаючи в руках прапор новоросії.' \
                                                          '\n\U0001F3F7 +1'
                damage_weapon(uid2, c2)

            spirit(bonus, uid2, c2)
            spirit(-bonus, uid1, 0)
            r.hincrby(uid2, 'wins', 1)

            hack = ''
            if c1 == 8 or c1 == 18 or c1 == 28:
                hack2 = choices([0, 1], weights=[82, 18])
                if weapon1 == 18:
                    hack2 = choices([0, 1], weights=[1, 99])
                    hack = '\n\n\U0001F5E1 ' + names[name1] + ' використав експлойт...'
                    damage_weapon(uid1, c1)
                if hack2 == [1]:
                    spirit(bonus * 2, uid1, 0)
                    spirit(-bonus, uid2, 0)
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
                    ran = choices([1, 0], weights=[0.1, 99.9])
                    if ran == [1]:
                        hack += '\nGET_.../watch?v=dQw4w9WgXcQ'

            if weapon2 == 15:
                meat += '\n' + names[name2] + ' бахнув горілочки. ' + '\U0001F54A ' + vodka(uid2)
            hp(-1, uid1)
            info += '\n\U0001fac0 ' + stats11[3].decode() + '(-1) | ' + stats22[3].decode() + m1 + m2
            win_info = str('\n\n\U0001F3C6 ' + str(un2) + ' перемагає ' + str(un1) + '! ' + str(grn) +
                           '\nЙого русак отримує +' + str(bonus) + ' бойового духу, а русак опонента'
                                                                   ' стільки ж втрачає.' +
                           hach + worker + meat + cop + pag + fsb + hack)
            return info + win_info


async def war(cid, location, big_battle):
    await bot.send_message(cid, '\U0001F5FA Починається ' + location + '!',
                           reply_to_message_id=int(r.hget('battle' + str(cid), 'start')))
    await sleep(2)
    ran = choice(['\U0001F93E\u200D\u2642\uFE0F \U0001F93A', '\U0001F6A3 \U0001F3C7', '\U0001F93C\u200D\u2642\uFE0F'])
    await bot.send_message(cid, ran + ' Русаки несамовито молотять один одного...')
    await sleep(3)
    m = await bot.send_message(cid, '\u2694 Йде бій...')

    everyone = r.smembers('fighters' + str(cid))
    fighters = {}
    for member in everyone:
        try:
            stats = r.hmget(member, 'strength', 'intellect', 'spirit', 'weapon', 'defense', 'injure', 'sch', 'buff')
            s = int(stats[0])
            i = int(stats[1])
            bd = int(stats[2])
            if int(stats[5]) > 0:
                s, bd = injure(int(member), s, bd, True)
            if int(stats[6]) > 0:
                i, bd = schizophrenia(int(member), i, bd, True)
            if int(stats[7]) > 0:
                s, bd = trance(int(member), s, bd, True)
            w = int(stats[3])
            if w > 0:
                w = 1.5
            else:
                w = 1
            d = int(stats[4])
            if d > 0:
                d = 1.5
            else:
                d = 1
            chance = s * (1 + 0.1 * i) * (1 + 0.01 * (bd * 0.01)) * w * d
            fighters.update({member: chance})
        except:
            continue
    if location == 'Битва в Соледарі':
        for key in fighters:
            if int(r.hget(key, 'class')) == 0:
                c = fighters.get(key)
                fighters.update({key: c * 2})

    if location == 'Штурм Горлівки':
        for key in fighters:
            fighters.update({key: 1})

    if location == 'Штурм ДАП':
        for key in fighters:
            armor = r.hmget(key, 'weapon', 'defense')
            w = int(armor[0])
            if w > 0:
                w = 1.5
            else:
                w = 1
            d = int(armor[1])
            if d > 0:
                d = 1.5
            else:
                d = 1
            chance = w * d
            fighters.update({key: chance})
    win = choices(list(fighters.keys()), weights=list(fighters.values()))
    win = int(str(win)[3:-2])
    wc = int(r.hget(win, 'class'))
    user_name = r.hget(win, 'firstname').decode()
    winner = '\n\n\U0001F3C6 ' + ' ' + f'<a href="tg://user?id={win}">{user_name}</a>' + ' перемагає!'

    if not big_battle:
        reward = '\n\n\U0001F3C6 +1 \U0001F4B5 +5\n'
        r.hincrby(win, 'wins', 1)
        r.hincrby(win, 'money', 5)
    elif location == 'Висадка в Чорнобаївці':
        winner = ''
        n = randint(5, 10)
        reward = '\n\n\U0001F3C6 Переможців немає.\n\U0001fa78 +' + str(n)
        for member in r.smembers('fighters' + str(cid)):
            r.hincrby(member, 'injure', n)
    else:
        reward = '\n\n\U0001F3C5 +1 \U0001F3C6 +1 \U0001F4B5 +10\n'
        r.hincrby(win, 'trophy', 1)
        r.hincrby(win, 'wins', 1)
        r.hincrby(win, 'money', 10)
    class_reward = ''

    if location == 'Битва на овечій фермі':
        if wc == 1 or wc == 11 or wc == 21:
            spirit(3000, win, 0)
            increase_trance(5, win)
            class_reward = '\U0001F919: \U0001F44A +5 \U0001F54A +3000'
    elif location == 'Битва на покинутому заводі':
        if wc == 2 or wc == 12 or wc == 22:
            class_reward = '\U0001F9F0: \U0001F4B5 +5 \u2622 +10'
            r.hincrby(win, 'money', 5)
            r.hincrby(win, 'vodka', 10)
    elif location == 'Битва в темному лісі':
        if wc == 3 or wc == 13 or wc == 23:
            class_reward = '\U0001F52E: \U0001F54A +2000\n\U0001F54A -1000 всім іншим учасникам битви.'
            r.srem('fighters' + str(cid), win)
            for member in r.smembers('fighters' + str(cid)):
                spirit(-1000, member, 0)
            spirit(2000, win, 0)
    elif location == 'Битва біля старого дуба':
        if wc == 4 or wc == 14 or wc == 24:
            class_reward = '\U0001F5FF: \U0001F54A +10000'
            spirit(10000, win, 0)
    elif location == 'Битва в житловому районі':
        if wc == 5 or wc == 15 or wc == 25:
            class_reward = '\U0001fa96: \u2622 +15'
            r.hincrby(win, 'vodka', 15)
    elif location == 'Битва біля поліцейського відділку':
        if wc == 6 or wc == 16 or wc == 26:
            class_reward = '\U0001F46E: \U0001F4B5 +5'
            r.hincrby(win, 'money', 5)
            if int(r.hget(win, 'defense')) == 16:
                r.hincrby(win, 's_defense', 10)
                class_reward = '\U0001F46E: \U0001F4B5 +5 \U0001F6E1 +10'
            elif int(r.hget(win, 'defense')) == 0:
                r.hset(win, 'defense', 16)
                r.hincrby(win, 's_defense', 10)
                class_reward = '\U0001F46E: \U0001F4B5 +5 \U0001F6E1 +10'
    elif location == 'Битва в офісі ОПЗЖ':
        if wc == 7 or wc == 17 or wc == 27:
            class_reward = '\U0001F921: \U0001F3C5 +1 \U0001F3C6 +5'
            r.hincrby(win, 'wins', 5)
            r.hincrby(win, 'trophy', 1)
    elif location == 'Битва в серверній кімнаті':
        if wc == 8 or wc == 18 or wc == 28:
            class_reward = '\U0001F4DF: \U0001F4B5 +20'
            r.hincrby(win, 'money', 20)
    elif location == 'Битва в психлікарні':
        if wc == 9 or wc == 19 or wc == 29:
            class_reward = '\u26D1: \U0001fac0 +100\n\U0001F464 +10 всім іншим учасникам битви.'
            r.srem('fighters' + str(cid), win)
            for member in r.smembers('fighters' + str(cid)):
                r.hincrby(member, 'sch', 10)
            hp(100, win)
        else:
            class_reward = '\U0001F5FA: \U0001F464 +10'
            r.hincrby(win, 'sch', 10)

    await sleep(10)
    r.hdel('battle' + str(cid), 'start')
    for member in r.smembers('fighters' + str(cid)):
        r.srem('fighters' + str(cid), member)
    end = ' завершена.'
    if location == 'Штурм Горлівки' or location == 'Штурм ДАП':
        end = ' завершено.'
    await bot.delete_message(m.chat.id, m.message_id)
    await bot.send_message(cid, location + end + winner + reward + class_reward, parse_mode='HTML')


async def war_power(sett, cid):
    chance, clan5, m, pag = 0, 0, 0, 0
    for member in sett:
        try:
            stats = r.hmget(member, 'strength', 'intellect', 'spirit', 'weapon', 'defense', 'injure', 'sch', 'class',
                            'clan', 'buff')
            if checkClan(member):
                if int(stats[8]) == cid:
                    clan5 += 1
            s = int(stats[0])
            i = int(stats[1])
            bd = int(stats[2])
            if checkClan(member, base=4, building='morgue'):
                d = int(r.hget(member, 'deaths'))
                if d > 100:
                    d = 100
                if d >= 25:
                    if r.hexists(member, 'ac16') == 0:
                        r.hset(member, 'ac16', 1)
                s = int(s * (1 + 0.002 * d))
            if int(stats[5]) > 0:
                s, bd = injure(int(member), s, bd, True)
            if int(stats[6]) > 0:
                i, bd = schizophrenia(int(member), i, bd, True)
            if int(stats[9]) > 0:
                s, bd = trance(int(member), s, bd, True)

            w = int(stats[3])
            if w > 0:
                w = 1.5
            else:
                w = 1
            d = int(stats[4])
            if d > 0:
                d = 1.5
            else:
                d = 1
            if int(stats[7]) == 9 or int(stats[7]) == 19 or int(stats[7]) == 29:
                m = 1
            if int(stats[7]) == 24:
                pag = 1
            chance += s * (1 + 0.1 * i) * (1 + 0.01 * (bd * 0.01)) * w * d
        except:
            continue
    if m == 1:
        chance = chance * 2
    if pag == 1 and clan5 == 5:
        chance = chance * 1.25
        for member in sett:
            try:
                spirit(250, int(member), 0)
            except:
                pass
    return chance, clan5


async def great_war(cid1, cid2, a, b):
    await sleep(2)
    ran = choice(['\U0001F93E\u200D\u2642\uFE0F \U0001F93A', '\U0001F6A3 \U0001F3C7', '\U0001F93C\u200D\u2642\uFE0F'])
    chance1, clan1 = await war_power(a, cid1)
    chance2, clan2 = await war_power(b, cid2)

    await bot.send_message(cid1, ran + ' Русаки несамовито молотять один одного...\n\n\U0001F4AA '
                           + str(int(chance1)) + ' | ' + str(int(chance2)))
    await bot.send_message(cid2, ran + ' Русаки несамовито молотять один одного...\n\n\U0001F4AA '
                           + str(int(chance1)) + ' | ' + str(int(chance2)))
    await sleep(3)

    win = choices(['a', 'b'], weights=[chance1, chance2])
    msg = 'Міжчатова битва русаків завершена!\n\n\U0001F3C6 Бійці з '
    reward = ''
    if win == ['a']:
        msg += r.hget('war_battle' + str(cid1), 'title').decode()
        for n in a:
            r.hincrby(n, 'trophy', 1)
            r.hincrby(n, 'wins', 1)
            if clan1 < 5 or int(r.hget('c' + str(cid1), 'base')) <= 1:
                r.hincrby(n, 'money', 3)
                reward = '3'
            else:
                r.hincrby(n, 'money', 6)
                reward = '6 \U0001F47E +1'
        r.hincrby(222, cid1, 1)
        if clan1 >= 5:
            if int(r.hget('c' + str(cid1), 'base')) > 1:
                r.hincrby('c' + str(cid1), 'r_spirit', 1)
    elif win == ['b']:
        msg += r.hget('war_battle' + str(cid2), 'title').decode()
        for n in b:
            r.hincrby(n, 'trophy', 1)
            r.hincrby(n, 'wins', 1)
            if clan2 < 5 or int(r.hget('c' + str(cid2), 'base')) <= 1:
                r.hincrby(n, 'money', 3)
                reward = '3'
            else:
                r.hincrby(n, 'money', 6)
                reward = '6 \U0001F47E +1'
        r.hincrby(222, cid2, 1)
        if clan2 >= 5:
            if int(r.hget('c' + str(cid2), 'base')) > 1:
                r.hincrby('c' + str(cid2), 'r_spirit', 1)
    msg += ' перемагають!\n\U0001F3C5 +1 \U0001F3C6 +1 \U0001F4B5 +' + reward
    await sleep(10)

    r.hdel('war_battle' + str(cid1), 'start')
    for member in r.smembers('fighters_2' + str(cid1)):
        r.hdel(member, 'in_war')
        r.srem('fighters_2' + str(cid1), member)
    r.hdel('war_battle' + str(cid2), 'start')
    for member in r.smembers('fighters_2' + str(cid2)):
        r.hdel(member, 'in_war')
        r.srem('fighters_2' + str(cid2), member)
    r.srem('started_battles', cid1)
    r.srem('started_battles', cid2)

    await bot.send_message(cid1, msg)
    await bot.send_message(cid2, msg)
