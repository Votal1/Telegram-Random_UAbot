from random import randint, choice, choices
from datetime import datetime
from asyncio import sleep

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import r, bot
from parameters import spirit, vodka, intellect, injure, schizophrenia, trance, hp, \
    damage_weapon, damage_defense, damage_support, damage_head, increase_trance
from methods import checkClan, wood, stone, cloth, brick, q_points, anti_clicker
from constants.classes import icons
from constants.names import names
from constants.photos import p7
from content.quests import quest
from content.inventory import check_set


async def fight(uid1, uid2, un1, un2, t, mid):
    info, wins1, wins2 = '', 0, 0
    can_earn1 = anti_clicker(uid1)
    can_earn2 = anti_clicker(uid2)
    for loop in range(t):
        if loop / 2 != 0 and t == 5:
            uid = uid1
            uid1 = uid2
            uid2 = uid

        weapon, defense, support = '', '', ''
        stats1 = r.hmget(uid1, 'name', 'class', 'weapon', 'defense', 'support', 'head')
        stats2 = r.hmget(uid2, 'name', 'class', 'weapon', 'defense', 'support', 'head')
        name1, name2 = int(stats1[0]), int(stats2[0])
        c1, c2 = int(stats1[1]), int(stats2[1])
        weapon1, weapon2 = int(stats1[2]), int(stats2[2])
        defense1, defense2 = int(stats1[3]), int(stats2[3])
        support1, support2 = int(stats1[4]), int(stats2[4])
        head1, head2 = int(stats1[5]), int(stats2[5])

        grn, hach, worker, meat, cop, fsb, m1, m2, inj1, inj2 = '', '', '', '', '', '', '', '', '', ''
        m_bonus, hach1, hach2 = [0], 0, 0

        if c1 == 1 or c1 == 11 or c1 == 21:
            quest(uid2, 3, -1, 2)
            if weapon2 == 0 or weapon1 == 33:
                hach1 = 1
        if weapon2 == 0:
            quest(uid1, 3, -1, 3)
        if weapon1 == 0:
            quest(uid2, 3, -1, 3)
        if c2 == 1 or c2 == 11 or c2 == 21:
            quest(uid1, 3, -1, 2)
            if weapon1 == 0 or weapon2 == 33:
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

        if weapon2 == 4:
            if weapon1 > 0 or defense1 > 0:
                weapon1, defense1 = 0, 0
                damage_weapon(uid2, c2)
                weapon = '\n\n\U0001F5E1\U0001F5FF ' + names[name2] + ' обеззброїв ворога битою!'

        if c1 == 26 and t == 1:
            quest(uid2, 3, -1, 1)
            if c2 not in (6, 16, 26) and defense1 in (16, 17):
                if weapon2 != 0:
                    cop1 = choices([1, 0], weights=[10, 90])
                    if cop1 == [1]:
                        if int(r.hget(uid2, 's_weapon')) > 300:
                            r.hincrby(uid2, 's_weapon', -300)
                        else:
                            r.hset(uid2, 'weapon', 0)
                            r.hset(uid2, 's_weapon', 0)
                        r.hincrby(uid1, 's_defense', 20)
                        cop += '\n\U0001F46E ' + names[name1] + \
                               ' вилучив у ворога зброю!\n\U0001F6E1 +20\n'
        if c2 == 26 and t == 1:
            quest(uid1, 3, -3, 1)
            if c1 not in (6, 16, 26) and defense2 in (16, 17):
                if weapon1 != 0:
                    cop2 = choices([1, 0], weights=[10, 90])
                    if cop2 == [1]:
                        if int(r.hget(uid1, 's_defense')) > 300:
                            r.hincrby(uid1, 's_defense', -300)
                        else:
                            r.hset(uid1, 'defense', 0)
                            r.hset(uid1, 's_defense', 0)
                        r.hincrby(uid2, 's_defense', 20)
                        cop += '\n\U0001F46E ' + names[name2] + \
                               ' вилучив у ворога захисне спорядження!\n\U0001F6E1 +20\n'

        if c1 == 27 and c2 == 0 and t == 1:
            fsb1 = choices([1, 0], weights=[5, 95])
            if fsb1 == [1] and can_earn1:
                r.hset(uid2, 'class', 7)
                r.sadd('class-7', uid2)
                r.hset(uid2, 'photo', choice(p7))
                r.hincrby(uid1, 'money', 50)
                r.hset(uid2, 'sch', 300)
                fsb += '\n\U0001F921 ' + names[name1] + ' завербував ворога!\n\U0001F4B5 +50 \U0001F464 +300\n'
        if c2 == 27 and c1 == 0 and t == 1:
            fsb2 = choices([1, 0], weights=[5, 95])
            if fsb2 == [1] and can_earn2:
                r.hset(uid1, 'class', 7)
                r.sadd('class-7', uid1)
                r.hset(uid1, 'photo', choice(p7))
                r.hincrby(uid2, 'money', 50)
                r.hset(uid1, 'sch', 300)
                fsb += '\n\U0001F921 ' + names[name2] + ' завербував ворога!\n\U0001F4B5 +50 \U0001F464 +300\n'

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
                quest(uid2, 3, -2, 3)

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

        if support1 == 1:
            hp(10, uid1)
            damage_support(uid1)
        if support2 == 1:
            hp(10, uid2)
            damage_support(uid2)

        stats11 = r.hmget(uid1, 'strength', 'intellect', 'spirit', 'hp', 'injure', 'sch')
        stats22 = r.hmget(uid2, 'strength', 'intellect', 'spirit', 'hp', 'injure', 'sch')
        s1, s2 = int(stats11[0]), int(stats22[0])
        s11 = s1
        s22 = s2
        i1, i2 = int(stats11[1]), int(stats22[1])
        bd1, bd2 = int(stats11[2]), int(stats22[2])
        hp1, hp2 = int(stats11[3]), int(stats22[3])
        in1, in2 = int(stats11[4]), int(stats22[4])
        sc1, sc2 = int(stats11[5]), int(stats22[5])

        if hp1 >= 90:
            if c1 in (34, 35, 36):
                s1 = int(s1 * 1.4)
            else:
                s1 = int(s1 * 1.1)
        if hp2 >= 90:
            if c2 in (34, 35, 36):
                s2 = int(s2 * 1.4)
            else:
                s2 = int(s2 * 1.1)

        if in1 > 0:
            s1, bd1 = injure(uid1, s1, bd1, True)
            s11 = s1
            inj1 = '\U0001fa78 '
        if in2 > 0:
            s2, bd2 = injure(uid2, s2, bd2, True)
            s22 = s2
            inj2 = '\U0001fa78 '
        if sc1 > 0:
            i1, bd1 = schizophrenia(uid1, i1, bd1, True)
            inj1 += '\U0001F464 '
        if sc2 > 0:
            i2, bd2 = schizophrenia(uid2, i2, bd2, True)
            inj2 += '\U0001F464 '
        if int(r.hget(uid1, 'buff')) > 0 or support1 == 13:
            s1, bd1 = trance(uid1, s1, bd1, True)
            s11 = s1
            inj1 += '\U0001F44A '
            if int(r.hget(uid1, 's5')) >= 3 and randint(1, 2) == 1:
                increase_trance(1, uid1)
        if int(r.hget(uid2, 'buff')) > 0 or support2 == 13:
            s2, bd2 = trance(uid2, s2, bd2, True)
            s22 = s2
            inj2 += '\U0001F44A '
            if int(r.hget(uid2, 's5')) >= 3 and randint(1, 2) == 1:
                increase_trance(1, uid2)

        if head1 == 2:
            s1 = int(s1 * 1.31)
            damage_head(uid1)
        if head2 == 2:
            s2 = int(s2 * 1.31)
            damage_head(uid2)

        if weapon2 in (11, 22, 33):
            s1 = int(s1 / 2)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' дістав травмат і прострелив ворогу коліно!'
            damage_weapon(uid2, c2)
            if weapon2 in (22, 33):
                i1 = int(i1 / 2)
                bd1 = int(bd1 / 2)
                if weapon2 == 22:
                    weapon = '\n\n\U0001F5E1 ' + names[name2] + ' дістав револьвер і прострелив ворогу коліно!'
                if weapon2 == 33:
                    weapon = '\n\n\U0001F5E1 ' + names[name2] + ' дістав пістолет-кулемет і прострелив ворогу коліно!'
        elif weapon2 in (12, 23):
            s2 = int(s2 * 1.2)
            i2 = int(i2 * 1.2)
            bd2 = int(bd2 * 1.2)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' прийшов на бій з діамантовим кайлом.'
            if weapon2 == 23:
                weapon = '\n\n\U0001F5E1 ' + names[name2] + ' прийшов на бій з незеритовим кайлом.'
            if weapon2 == 23 and choice([1, 2, 3]) != 1:
                pass
            else:
                damage_weapon(uid2, c2)
        elif weapon2 in (15, 26) and c2 in (5, 15, 25):
            s2 = int(s2 * 1.5)
            ak = 'АКМ' if weapon2 == 26 else 'АК-47'
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' приніс на бій заряджений ' + ak + '...'
            damage_weapon(uid2, c2)
            ran = choices([1, 2], weights=[99, 1])
            if ran == [2] and defense1 != 2 and t == 1:
                weapon = weapon + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе ' \
                                  'і отримав важкі поранення.'
                r.hset(uid2, 'spirit', 0, {'hp': 0})
                r.hincrby(uid2, 'injure', 150)
                if c2 == 25:
                    weapon = '\n\n\U0001F5E1 ' + names[name2] + ' приніс на бій заряджений ' + ak + '...' \
                              + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе і отримав' \
                                ' важкі поранення, як і ' + names[name1] + '.'
                    r.hset(uid1, 'spirit', 0, {'hp': 0})
                    r.hincrby(uid1, 'injure', 150)
        elif defense2 in (16, 17):
            s1 = int(s1 * 0.8)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' атакує, прикрившись поліцейським щитом.'
            damage_defense(uid2, 16)
        elif weapon2 in (19, 30):
            db = r.hmget(uid1, 'injure', 'sch')
            injure1, sch1 = int(db[0]), int(db[1])
            if injure1 == 0 and sch1 < 4:
                r.hincrby(uid1, 'injure', 1)
                weapon = '\n\n\U0001F5E1 ' + names[name2] + ' порізав ворога медичною пилкою.\n\U0001fa78 +1'
            elif injure1 >= 4 or sch1 >= 4:
                inj = 10
                if weapon2 == 30:
                    inj = 15
                if injure1 >= 4:
                    stat = 'injure'
                    weapon = f'\n\n\U0001F5E1 {names[name2]} припинив ворогу кровотечу.\n' \
                             f'\U0001fa78 -{inj} \U0001fac0 -10'
                else:
                    stat = 'sch'
                    weapon = f'\n\n\U0001F5E1 {names[name2]} заглушив ворогу голоси в голові.\n' \
                             f'\U0001F464 -{inj} \U0001fac0 -10'
                r.hincrby(uid1, stat, -inj)
                if int(r.hget(uid1, stat)) < 0:
                    r.hset(uid1, stat, 0)
                hp(-10, uid1)
                if int(r.hget(uid1, 'hp')) == 0:
                    quest(uid1, 3, -1, 4)
            damage_weapon(uid2, c2)
        elif weapon2 in (20, 31):
            i1 = i1 - 10
            if i1 < 0:
                i1 = 0
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' вдарив ворога пляшкою по голові!'
            if weapon2 == 31:
                r.hincrby(uid1, 'injure', 1)
                r.hincrby(uid1, 'sch', 1)
                weapon = '\n\n\U0001F5E1 ' + names[name2] + ' вдарив ворога кастетом по морді!'
            damage_weapon(uid2, c2)
        elif weapon2 in (21, 32):
            damage_weapon(uid2, c2)
            if not checkClan(uid1):
                s2 = int(s2 * 2)
            else:
                s2 = int(s2 * 1.25)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' марширує в бій, тримаючи в руці палаш!'
            if weapon2 == 32:
                if int(r.hget(uid1, 'strap')) == 0 and c1 != 36:
                    s2 = int(s2 * 1.5)
                else:
                    s2 = int(s2 * 1.25)
                weapon = '\n\n\U0001F5E1 ' + names[name2] + ' марширує в бій, тримаючи в руці золотий палаш!'
        if weapon2 == 27 and t == 1:
            damage_weapon(uid2, c2)
            r.hset(uid1, 'hp', 0)
            weapon = '\n\n🔫 ' + names[name2] + ' вистрелив у ворога електрошокером!\n\U0001fac0 -100'
            quest(uid1, 3, -1, 4)

        if weapon2 == 6:
            weapon = '\n\n\U0001F381 ' + names[name1] + ' отримав подарунок від свого суперника...'
            r.hincrby(uid1, 'packs_2023_2', 1)
            damage_weapon(uid2, c2)

        if weapon2 == 2 and t == 1:
            weapon = '\n\n\u2620\uFE0F ' + names[name2] + ': АЛЛАХ АКБАР!'
            damage_weapon(uid2, c2)
            if defense1 in (2, 17):
                damage = int(int(r.hget(uid1, 's_defense')) / 2 - 5)
                r.hset(uid1, 's_defense', damage)
                if damage <= 0:
                    r.hset(uid1, 'defense', 0)
                    r.hset(uid1, 's_defense', 0)
            else:
                r.hincrby(uid1, 'injure', 300)
                if c1 != 6 and c1 != 16 and c1 != 26:
                    r.hset(uid1, 'weapon', 0)
                r.hset(uid1, 'spirit', 0, {'hp': 0, 'defense': 0, 'support': 0})
                if head1 != 6:
                    r.hset(uid1, 'head', 0)
                quest(uid1, 3, -1, 4)

        if weapon1 in (15, 26) and c1 in (5, 15, 25):
            s1 = int(s1 * 1.5)
            ak = 'АКМ' if weapon1 == 26 else 'АК-47'
            defense = '\n\n\U0001F5E1 ' + names[name1] + ' приніс на бій заряджений ' + ak + '...'
            damage_weapon(uid1, c1)
            ran = choices([1, 2], weights=[99, 1])
            if ran == [2] and defense2 != 2 and t == 1:
                defense = defense + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе ' \
                                    'і отримав важкі поранення.'
                r.hset(uid1, 'spirit', 0, {'hp': 0})
                r.hincrby(uid1, 'injure', 150)
                if c1 == 25 and int(r.hget(uid1, 'strength')) >= 300:
                    defense = '\n\n\U0001F5E1 ' + names[name1] + ' приніс на бій заряджений ' + ak + '...' \
                              + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе і отримав' \
                                ' важкі поранення, як і ' + names[name2] + '.'
                    r.hset(uid2, 'spirit', 0, {'hp': 0})
                    r.hincrby(uid2, 'injure', 150)
        elif weapon1 == 33:
            s2 = int(s2 / 2)
            i2 = int(i2 / 2)
            bd2 = int(bd2 / 2)
            defense = '\n\n\U0001F5E1 ' + names[name2] + ' дістав пістолет-кулемет і прострелив ворогу коліно!'
            damage_weapon(uid1, c1)

        if support1 == 6 and t == 1:
            if i2 > i1:
                if c2 != 3 and c2 != 13 and c2 != 23:
                    s1 = int(s1 * 0.5)
                    intellect(1, uid1)
                    r.hincrby(uid1, 'mushrooms', 1)
                    support += '\n\n\U0001F6E1 ' + names[name1] + ' прийшов на бій під мухоморами. Він був' \
                                                                  ' обезсилений, але запам`ятав тактику ворога.'
                    damage_support(uid1)
        if support2 == 6 and t == 1:
            if i1 > i2:
                if c1 != 3 and c1 != 13 and c1 != 23:
                    s2 = int(s2 * 0.5)
                    intellect(1, uid2)
                    r.hincrby(uid2, 'mushrooms', 1)
                    support += '\n\n\U0001F6E1 ' + names[name2] + ' прийшов на бій під мухоморами. Він був' \
                                                                  ' обезсилений, але запам`ятав тактику ворога.'
                    damage_support(uid2)
        if defense1 == 3 and t == 1:
            damage_defense(uid1, 3)
            if choice([1, 2, 3]) == 1:
                defense = '\n\n\u2620\uFE0F ' + names[name2] + ' наступив на міну!'
                r.hincrby(uid2, 'injure', 5)
                if c2 not in (6, 16, 26):
                    r.hincrby(uid2, 's_weapon', -5)
                    if int(r.hget(uid2, 's_weapon')) <= 0:
                        r.hset(uid2, 's_weapon', 0, {'weapon', 0})
        elif defense1 == 9:
            s1 = int(s1 * 1.3)
            defense = '\n\n\U0001F6E1 ' + names[name1] + ' прикривається від ударів уламком бронетехніки.'
            damage_defense(uid1, 9)
        elif defense1 in (16, 17):
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
                    if weapon1 == 16 and defense1 in (16, 17):
                        bd2 = 0
                    elif weapon1 == 16:
                        bd1, bd2 = 0, 0
                    if c1 == 16 or c1 == 26:
                        if i2 >= i1:
                            i1, i2 = 0, 0
                            if defense1 in (16, 17) and s2 >= s1:
                                s1, s2 = 10, 10
            else:
                if weapon2 == 16 and defense2 in (16, 17):
                    bd1 = 0
                elif weapon2 == 16:
                    bd1, bd2 = 0, 0
                if c2 == 16 or c2 == 26:
                    if i1 >= i2:
                        i1, i2 = 0, 0
                        if defense2 in (16, 17) and s1 >= s2:
                            s1, s2 = 10, 10

        if hach1 == 1:
            s1 = int(s1 * 1.2)
            spirit(30, uid1, 0)
        if hach2 == 1:
            s2 = int(s2 * 1.2)
            spirit(30, uid2, 0)

        if c1 == 23:
            magic = int(r.hget(uid1, 'deaths')) * 5
            if magic > 45:
                magic = 45
            i1 = int(i1 * (1 + magic / 100))
        if c2 == 23:
            magic = int(r.hget(uid1, 'deaths')) * 3
            if magic > 45:
                magic = 45
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
                if c1 == 29 and can_earn1:
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
                        if int(r.hget(uid2, 'hp')) == 0:
                            quest(uid2, 3, -1, 4)
                        m1 += '\n\U0001fa78 +' + str(2 + int(nar[0])) + ' \U0001fac0 -' + nar[1].decode()
        if c2 == 9 or c2 == 19 or c2 == 29:
            if hp1 < 50:
                if weapon2 in (19, 30) and in1 < 4 and sc1 < 4:
                    pass
                else:
                    hp(5, uid1)
                    m2 = '\n\u26D1 ' + names[name2] + ' підлатав ворога.'
                    if c2 == 29 and can_earn2:
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
                if weapon2 in (19, 30) and in1 > 4:
                    pass
                else:
                    ran = choices([0, 1], weights=[80, 20])
                    if ran == [1]:
                        m2 = f'\n\u26D1 {names[name2]} побачив що {names[name1]} занадто здоровий і виправив це.'
                        if c2 == 9:
                            r.hincrby(uid1, 'injure', 2)
                            m2 += '\n\U0001fa78 +2'
                        else:
                            nar = r.hmget(uid1, 'mushrooms', 's1')
                            r.hincrby(uid1, 'injure', 2 + int(nar[0]))
                            hp(-int(nar[1]), uid1)
                            if int(r.hget(uid1, 'hp')) == 0:
                                quest(uid1, 3, -1, 4)
                            m2 += '\n\U0001fa78 +' + str(2 + int(nar[0])) + ' \U0001fac0 -' + nar[1].decode()

        if c1 in (20, 30):
            if c2 not in (6, 16, 26):
                if int(r.hget(uid1, 'wins')) > int(r.hget(uid2, 'wins')):
                    bd2 = int(bd2 * 0.6)
                else:
                    bd2 = int(bd2 * 0.8)
        if c2 in (20, 30):
            if c1 not in (6, 16, 26):
                if int(r.hget(uid2, 'wins')) > int(r.hget(uid1, 'wins')):
                    bd1 = int(bd1 * 0.6)
                else:
                    bd1 = int(bd1 * 0.8)

        if weapon2 in (13, 24):
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
            if weapon2 == 24:
                sh = int(r.hget(uid2, 'sch'))
                if sh > 5:
                    sh = 5
                r.hincrby(uid1, 'sch', sh)
                r.hincrby(uid2, 'sch', -sh)
                quest(uid1, 3, -2, 3)
            weapon = '\n\n\U0001F5E1 ' + names[name2] + ' поміняв характеристики місцями!'
            damage_weapon(uid2, c2)

        mal1, mal2 = False, False
        if c1 == 7 or c1 == 17 or c1 == 27:
            mal1 = True
        if c2 == 7 or c2 == 17 or c2 == 27:
            mal2 = True

        chance1 = s1 * (1 + 0.1 * i1) * (1 + 0.01 * (bd1 * 0.01))
        chance2 = s2 * (1 + 0.1 * i2) * (1 + 0.01 * (bd2 * 0.01))

        chance11 = chance1 / ((chance1 + chance2) / 100)
        chance22 = chance2 / ((chance1 + chance2) / 100)

        if not mal2 and chance11 > 95:
            win = choices(['1', '2'], weights=[95, 5])
        elif not mal1 and chance22 > 95:
            win = choices(['1', '2'], weights=[5, 95])
        elif mal2 and chance11 > 80:
            if int(r.hget(uid2, 'sch')) > 0:
                win = choices(['1', '2'], weights=[75, 25])
            else:
                win = choices(['1', '2'], weights=[80, 20])
        elif mal1 and chance22 > 80:
            if int(r.hget(uid1, 'sch')) > 0:
                win = choices(['1', '2'], weights=[25, 75])
            else:
                win = choices(['1', '2'], weights=[20, 80])
        else:
            win = choices(['1', '2'], weights=[chance1, chance2])

        if support1 == 11 and support2 != 11 and t == 1:
            if support2:
                win = ['1']
                damage_support(uid1)
                support += f'\n\n📝 {names[name2]} втік з поля бою!'
            else:
                r.hset(uid2, 'support', 11, {'s_support': r.hget(uid1, 's_support')})
                r.hset(uid1, 'support', 0, {'s_support': 0})
                support += f'\n\n📝 {names[name1]} вручив ворогу повістку!'
        if support2 == 11 and support1 != 11 and t == 1:
            if support1:
                win = ['2']
                damage_support(uid2)
                support += f'\n\n📝 {names[name1]} втік з поля бою!'
            else:
                r.hset(uid1, 'support', 11, {'s_support': r.hget(uid2, 's_support')})
                r.hset(uid2, 'support', 0, {'s_support': 0})
                support += f'\n\n📝 {names[name2]} вручив ворогу повістку!'

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
            await bot.edit_message_text(text=info, inline_message_id=mid, disable_web_page_preview=True)
            await sleep(3)
            continue

        info = str(un1 + ' vs ' + un2 + '\n\n\U0001F3F7 ' + inj1 + names[name1] + ' ' +
                   icons[c1] + ' | ' + inj2 + names[name2] + ' ' + icons[c2] +
                   '\n\U0001F4AA ' + str(s1) + ' | ' + str(s2) +
                   '\n\U0001F9E0 ' + str(i1) + ' | ' + str(i2) +
                   '\n\U0001F54A ' + str(bd1) + ' | ' + str(bd2)) + weapon + defense + support

        if win == ['1']:
            if s11 / s22 > 2:
                bonus = randint(1, 20)
            elif s11 / s22 < 0.5:
                bonus = randint(60, 120)
                m_bonus = choices([3, 5], weights=[90, 10])
            else:
                bonus = randint(20, 60)
                m_bonus = choices([0, 3, 5], weights=[50, 45, 5])
            if c2 in (3, 13, 23) and checkClan(uid2, building='build3', level=3) and can_earn2:
                steal = choices([0, 1], weights=[80, 20])[0]
            else:
                steal = 0
            if c1 == 10 or c1 == 20 or c1 == 30:
                if int(r.hget(uid1, 'money')) < 100:
                    m_bonus[0] += 2
                elif int(r.hget(uid1, 'money')) < 200 and checkClan(uid1, building='build3', level=1):
                    m_bonus[0] += 2
            if m_bonus[0] > 0 and can_earn1:
                if checkClan(uid1, base=4):
                    if choices([1, 0], weights=[s2 / (s1 + s2), 1 - s2 / (s1 + s2)]) == [1]:
                        m_bonus = [m_bonus[0] * 2]
                if steal == 0:
                    r.hincrby(uid1, 'money', m_bonus[0])
                    grn = '\n\U0001F4B5 +' + str(m_bonus[0])
                else:
                    r.hincrby(uid2, 'money', m_bonus[0])
                    grn = '\n\U0001F4B5 +' + str(m_bonus[0]) + ' (вкрадено фокусником!)'

            if hach1 == 1:
                if c1 != 1:
                    hc = s2 / (s1 + s2)
                    trick = choices([1, 0], weights=[hc, 1 - hc])
                    if trick == [1]:
                        ran1, ran2 = randint(50, 100), 2
                        if weapon1 == 33:
                            ran1 *= 2
                            ran2 *= 2
                        trick = choices([1, 2, 3], weights=[45, 45, 10])
                        if checkClan(uid1, building='build2', level=3):
                            trick = choices([1, 2, 3], weights=[35, 35, 30])
                        if trick == [1]:
                            hach += '\n\U0001F919 ' + names[name1] + ' кинув суперника через стегно!\n\U0001F54A -' + \
                                    str(ran1) + '\n'
                            spirit(-ran1, uid2, 0)
                        elif trick == [2]:
                            hach += '\n\U0001F919 ' + names[name1] + ' кинув суперника млином!\n\U0001F54A +' + \
                                    str(ran1) + '\n'
                            spirit(ran1, uid1, 0)
                        elif trick == [3] and can_earn1:
                            hach += f'\n\U0001F919 {names[name1]} кинув суперника прогином!\n\U0001F4B5 +{ran2}\n'
                            r.hincrby(uid1, 'money', ran2)

            pag = ''
            if weapon2 in (14, 25):
                r.hincrby(uid1, 'spirit', int(r.hget(uid2, 'spirit')))
                r.hincrby(uid2, 'spirit', -int(r.hget(uid2, 'spirit')))
                damage_weapon(uid2, c2)
                pag = '\n\U0001F5E1 ' + names[name2] + ' прийшов на бій з сокирою Перуна. Коли русак програв' \
                                                       ', його бойовий дух влився у ворога...'
                if c1 in (4, 14, 24) and c2 in (4, 14, 24) and checkClan(uid1, building='build2', level=2):
                    spirit(10000, uid1, 0)
                    spirit(10000, uid2, 0)
                if weapon2 == 25:
                    ran = randint(0, 5)
                    r.hincrby(uid1, 'injure', ran)
                    r.hincrby(uid1, 'sch', 5-ran)
                    pag = '\n\U0001F5E1 ' + names[name2] + ' прийшов на бій з рунічною сокирою Перуна. Коли русак' \
                                                           ' програв, ворога вдарило блискавкою...'

            spirit(bonus, uid1, c1)
            spirit(-bonus, uid2, 0)
            if can_earn1:
                r.hincrby(uid1, 'wins', 1)
            quest(uid1, 1, 1)
            quest(uid1, 1, -1)
            r.hincrby('win_rate', f'win-{c1}', 1)
            r.hincrby('win_rate', f'lose-{c2}', 1)
            r.hincrby('all_wins', 'wins', 1)

            if c1 == 36:
                quest(uid2, 3, -2, 2)
            if c2 in (7, 17, 27):
                quest(uid1, 3, -3, 3)

            if randint(1, 100) == 100:
                if checkClan(uid1) and int(r.hget('c' + r.hget(uid1, 'clan').decode(), 'buff_4')) == 21:
                    q_points(uid1, 12)

            hack = ''
            if c2 == 8 or c2 == 18 or c2 == 28:
                hack1 = choices([0, 1], weights=[82, 18])
                if weapon2 in (18, 29) and can_earn2:
                    hack1 = choices([0, 1], weights=[1, 99])
                    hack = '\n\n\U0001F5E1 ' + names[name2] + ' використав експлойт...'
                    if hack1 == [0]:
                        hack += '\n' + r.hget('promo_code', 'hacker_promo_code').decode()
                    damage_weapon(uid2, c2)
                if hack1 == [1] and can_earn2:
                    spirit(bonus * 2, uid2, 0)
                    spirit(-bonus, uid1, 0)
                    money = 1
                    if c2 == 28:
                        money2 = int(r.hget(uid1, 'money'))
                        if money2 > 250 and weapon2 != 29:
                            money2 = 250
                        elif money2 > 500 and weapon2 == 29:
                            money2 = 500
                        if money2 >= 50:
                            money = int(money2 / 50)
                        else:
                            money = 1
                        quest(uid1, 3, -3, 4)
                    if checkClan(uid2, building='build4', level=4):
                        r.hincrby('c' + r.hget(uid2, 'clan').decode(), 'money', money)
                    r.hincrby(uid2, 'money', money)
                    hack = hack + '\n\U0001F4DF ' + names[name2] + ' зламав бота, і переписав бонусний бойовий дух ' \
                                                                   'собі.\n\U0001F4B5 +' + str(money)

            if weapon1 in (15, 26):
                meat += '\n' + names[name1] + ' бахнув горілочки. ' + '\U0001F54A ' + vodka(uid1)
                if c1 not in (5, 15, 25):
                    damage_weapon(uid1, c1)
            hp(-1, uid2)
            if int(r.hget(uid2, 'hp')) == 0:
                quest(uid2, 3, -1, 4)
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
                m_bonus = choices([3, 5], weights=[90, 10])
            else:
                bonus = randint(20, 60)
                m_bonus = choices([0, 3, 5], weights=[50, 45, 5])
            if c1 in (3, 13, 23) and checkClan(uid1, building='build3', level=3) and can_earn1:
                steal = choices([0, 1], weights=[80, 20])[0]
            else:
                steal = 0
            if c2 == 10 or c2 == 20 or c2 == 30:
                if int(r.hget(uid2, 'money')) < 100:
                    m_bonus[0] += 2
                elif int(r.hget(uid2, 'money')) < 200 and checkClan(uid2, building='build3', level=1):
                    m_bonus[0] += 2
            if m_bonus[0] > 0 and can_earn2:
                if checkClan(uid2, base=4):
                    if choices([1, 0], weights=[s1 / (s1 + s2), 1 - s1 / (s1 + s2)]) == [1]:
                        m_bonus = [m_bonus[0] * 2]
                if steal == 0:
                    r.hincrby(uid2, 'money', m_bonus[0])
                    grn = '\n\U0001F4B5 +' + str(m_bonus[0])
                else:
                    r.hincrby(uid1, 'money', m_bonus[0])
                    grn = '\n\U0001F4B5 +' + str(m_bonus[0]) + ' (вкрадено фокусником!)'

            if hach2 == 1:
                if c2 != 1:
                    hc = s1 / (s1 + s2)
                    trick = choices([1, 0], weights=[hc, 1 - hc])
                    if trick == [1]:
                        ran1, ran2 = randint(50, 100), 2
                        if weapon2 == 33:
                            ran1 *= 2
                            ran2 *= 2
                        trick = choices([1, 2, 3], weights=[45, 45, 10])
                        if checkClan(uid2, building='build2', level=3):
                            trick = choices([1, 2, 3], weights=[35, 35, 30])
                        if trick == [1]:
                            hach += '\n\U0001F919 ' + names[name2] + ' кинув суперника через стегно!\n\U0001F54A -' + \
                                    str(ran1) + '\n'
                            spirit(-ran1, uid1, 0)
                        elif trick == [2]:
                            hach += '\n\U0001F919 ' + names[name2] + ' кинув суперника млином!\n\U0001F54A +' + \
                                    str(ran1) + '\n'
                            spirit(ran1, uid2, 0)
                        elif trick == [3] and can_earn2:
                            hach += f'\n\U0001F919 {names[name2]} кинув суперника прогином!\n\U0001F4B5 +{ran2}\n'
                            r.hincrby(uid2, 'money', ran2)

            pag = ''
            if weapon2 in (14, 25):
                r.hincrby(uid2, 'spirit', int(r.hget(uid1, 'spirit')))
                r.hincrby(uid1, 'spirit', -int(r.hget(uid1, 'spirit')))
                damage_weapon(uid2, c2)
                pag = '\n\U0001F5E1 ' + names[name2] + ' прийшов на бій з сокирою Перуна. Коли ворог програв' \
                                                       ', його бойовий дух влився у русака...'
                if c1 in (4, 14, 24) and c2 in (4, 14, 24) and checkClan(uid2, building='build2', level=2):
                    spirit(10000, uid1, 0)
                    spirit(10000, uid2, 0)
                if weapon2 == 25:
                    pag = '\n\U0001F5E1 ' + names[name2] + ' прийшов на бій з рунічною сокирою Перуна. Коли ворог ' \
                                                           'програв, його бойовий дух влився у русака...'

            elif weapon2 in (17, 28) and can_earn2:
                r.hincrby(uid2, 'wins', 1)
                if weapon2 == 17:
                    fsb += '\n\n\U0001F5E1 ' + names[name2] + ' гордо стоїть, тримаючи в руках прапор новоросії.' \
                                                              '\n\U0001F3C6 +1'
                damage_weapon(uid2, c2)
                if weapon2 == 28:
                    increase_trance(2, uid2)
                    fsb += '\n\n\U0001F5E1 ' + names[name2] + ' гордо стоїть, тримаючи в руках прапор совка.' \
                                                              '\n\U0001F3C6 +1'

            spirit(bonus, uid2, c2)
            spirit(-bonus, uid1, 0)
            if can_earn2:
                r.hincrby(uid2, 'wins', 1)
            quest(uid2, 1, 1)
            quest(uid2, 1, -1)
            r.hincrby('win_rate', f'win-{c2}', 1)
            r.hincrby('win_rate', f'lose-{c1}', 1)
            r.hincrby('all_wins', 'wins', 1)

            if c2 == 36:
                quest(uid1, 3, -2, 2)
            if c1 in (7, 17, 27):
                quest(uid2, 3, -3, 3)

            if randint(1, 100) == 100:
                if checkClan(uid2) and int(r.hget('c' + r.hget(uid2, 'clan').decode(), 'buff_4')) == 21:
                    q_points(uid2, 12)

            hack = ''
            if c1 == 8 or c1 == 18 or c1 == 28:
                hack2 = choices([0, 1], weights=[82, 18])
                if weapon1 in (18, 29) and can_earn1:
                    hack2 = choices([0, 1], weights=[1, 99])
                    hack = '\n\n\U0001F5E1 ' + names[name1] + ' використав експлойт...'
                    if hack2 == [0]:
                        hack += '\n' + r.hget('promo_code', 'hacker_promo_code').decode()
                    damage_weapon(uid1, c1)
                if hack2 == [1] and can_earn1:
                    spirit(bonus * 2, uid1, 0)
                    spirit(-bonus, uid2, 0)
                    money = 1
                    if c1 == 28:
                        money2 = int(r.hget(uid2, 'money'))
                        if money2 > 250 and weapon1 != 29:
                            money2 = 250
                        elif money2 > 500 and weapon1 == 29:
                            money2 = 500
                        if money2 >= 50:
                            money = int(money2 / 50)
                        else:
                            money = 1
                        quest(uid2, 3, -3, 4)
                    if checkClan(uid1, building='build4', level=4):
                        r.hincrby('c' + r.hget(uid1, 'clan').decode(), 'money', money)
                    r.hincrby(uid1, 'money', money)
                    hack = hack + '\n\U0001F4DF ' + names[name1] + ' зламав бота, і переписав бонусний бойовий дух ' \
                                                                   'собі.\n\U0001F4B5 +' + str(money)

            if weapon2 in (15, 26):
                meat += '\n' + names[name2] + ' бахнув горілочки. ' + '\U0001F54A ' + vodka(uid2)
                if c2 not in (5, 15, 25):
                    damage_weapon(uid2, c2)
            hp(-1, uid1)
            if int(r.hget(uid1, 'hp')) == 0:
                quest(uid1, 3, -1, 4)
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
    msg1 = '\u2694 Йде бій...'
    if randint(1, 10) == 10 and location == 'Штурм Горлівки':
        msg1 += f"\n{r.hget('promo_code', 'battle_promo_code').decode()}"
    m = await bot.send_message(cid, msg1)

    everyone = r.smembers('fighters' + str(cid))
    fighters = {}
    for member in everyone:
        try:
            stats = r.hmget(member, 'strength', 'intellect', 'spirit', 'weapon', 'defense', 'injure', 'sch', 'buff',
                            'support', 'head')
            s = int(stats[0])
            i = int(stats[1])
            bd = int(stats[2])
            if int(stats[5]) > 0:
                s, bd = injure(int(member), s, bd, True)
            if int(stats[6]) > 0:
                i, bd = schizophrenia(int(member), i, bd, True)
            if int(stats[7]) > 0 or int(stats[8]) == 13:
                s, bd = trance(int(member), s, bd, True)
            w = int(stats[3])
            if w > 0:
                if w == 5:
                    mas = int(r.hget(member, 's2'))
                    w = 0.25 + 0.5 * mas
                    if choices([1, 0], [100 - 18 * mas, 18 * mas]) == [1]:
                        damage_weapon(member, int(r.hget(member, 'class')))
                else:
                    w = 0.25
            else:
                w = 0
            d = int(stats[4])
            if d > 0:
                d = 0.25
            else:
                d = 0
            support = int(stats[8])
            if support > 0:
                if support in (2, 9):
                    support = 0.5
                    damage_support(member)
                else:
                    support = 0.25
            else:
                support = 0
            head = int(stats[9])
            if head > 0:
                head = 0.25
            else:
                head = 0
            chance = s * (1 + 0.1 * i) * (1 + 0.01 * (bd * 0.01)) * (1 + w + d + support + head)
            fighters.update({member: chance})

            quest(member, 1, 6)
        except:
            continue

    if location == 'Штурм Горлівки':
        for key in fighters:
            fighters.update({key: 1})

    if location == 'Штурм ДАП':
        for key in fighters:
            armor = r.hmget(key, 'weapon', 'defense', 'support')
            w = int(armor[0])
            if w > 0:
                w = 1/3
            else:
                w = 0
            d = int(armor[1])
            if d > 0:
                d = 1/3
            else:
                d = 0
            support = int(armor[2])
            if support > 0:
                support = 1/3
            else:
                support = 0
            chance = 1 + w + d + support
            fighters.update({key: chance})
    win = choices(list(fighters.keys()), weights=list(fighters.values()))
    win = int(str(win)[3:-2])
    quest(win, 1, -2)
    wc = int(r.hget(win, 'class'))
    user_name = r.hget(win, 'firstname').decode().replace('@', '')
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
            quest(member, 1, -6)
    else:
        money = 10
        if checkClan(win, building='build3', level=4) and wc in (31, 32, 33):
            money = 15
        reward = f'\n\n\U0001F3C5 +1 \U0001F3C6 +1 \U0001F4B5 +{money}'
        if randint(1, 4) == 4:
            if checkClan(win) and int(r.hget('c' + r.hget(win, 'clan').decode(), 'buff_4')) == 12:
                q_points(win, 3)
                reward += ' \U0001fa99 +3'
        r.hincrby(win, 'trophy', 1)
        r.hincrby('all_trophy', 'trophy', 1)
        r.hincrby(win, 'wins', 1)
        r.hincrby(win, 'money', 10)
    class_reward = ''

    if wc in (31, 32, 33) and location != 'Висадка в Чорнобаївці' and big_battle:
        class_reward = '\U0001F695: \U0001F4E6 +1'
        r.hincrby(win, 'packs', 1)

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
            r.hincrby('all_vodka', 'vodka', 10)
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
            r.hincrby('all_vodka', 'vodka', 15)
    elif location == 'Битва біля поліцейського відділку':
        if wc == 6 or wc == 16 or wc == 26:
            class_reward = '\U0001F46E: \U0001F4B5 +5'
            r.hincrby(win, 'money', 5)
            if int(r.hget(win, 'defense')) in (16, 17):
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
            r.hincrby('all_trophy', 'trophy', 1)
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
    elif location == 'Битва в темному провулку':
        if wc == 10 or wc == 20 or wc == 30:
            class_reward = '\U0001F6AC: \U0001F3C5 +1 \U0001F44A +1 \u2622 +1 \U0001F4B5 +8'
            r.hincrby(win, 'trophy', 1)
            r.hincrby('all_trophy', 'trophy', 1)
            increase_trance(1, win)
            r.hincrby(win, 'money', 8)
            r.hincrby(win, 'vodka', 1)
            r.hincrby('all_vodka', 'vodka', 1)
        for member in r.smembers('fighters' + str(cid)):
            quest(member, 3, -2, 1)
    elif location == 'Битва біля розбитої колони':
        if wc in (31, 32, 33):
            class_reward = '\U0001F695: \U0001F4E6 +2'
            r.hincrby(win, 'packs', 1)
    elif location == 'Розгром командного пункту':
        if wc in (34, 35, 36):
            class_reward = '\U0001F396: \U0001F4B5 +7'
            r.hincrby(win, 'money', 7)
            if checkClan(win):
                class_reward += ' \U0001F4FB +3'
                r.hincrby('c' + r.hget(win, 'clan').decode(), 'technics', 3)
    elif location == 'Битва біля новорічної ялинки':
        class_reward = '\U0001F381: Всі бійці отримали подарунок.'
        # winners = r.srandmember('fighters' + str(cid), 3)
        for member in r.smembers('fighters' + str(cid)):
            r.hincrby(member, 'packs_2023')

    elif location == 'Битва біля Києво-Печерської Лаври':
        class_reward = '🧺: Всі інші вкрали по кошику.'
        for member in r.smembers('fighters' + str(cid)):
            if int(member) != win:
                r.hincrby(member, 'packs_2023_2')
    elif location == 'Битва за великодній кошик':
        class_reward = '🧺 +1'
        r.hincrby(win, 'packs_2023_2')

    if class_reward:
        class_reward = '\n' + class_reward

    await sleep(10)
    r.hdel('battle' + str(cid), 'start')
    for member in r.smembers('fighters' + str(cid)):
        r.srem('fighters' + str(cid), member)
    end = ' завершена.'
    if location in ('Штурм Горлівки', 'Штурм ДАП', 'Розгром командного пункту'):
        end = ' завершено.'
    msg = location + end + winner + reward + class_reward
    if not r.hexists(f'c{cid}', 'hints') or int(r.hget(f'c{cid}', 'hints')) == 0:
        msg += '\n\n/battle'
    await bot.delete_message(m.chat.id, m.message_id)
    await bot.send_message(cid, msg, parse_mode='HTML', disable_web_page_preview=True)


async def war_power(sett, cid):
    chance = clan5 = m = pag = meat = mal = gen1 = gen2 = koj = 0
    for member in sett:
        try:
            cl = int(r.hget(member, 'class'))
            if cl in (5, 15, 25):
                meat += 1
            elif cl in (35, 36):
                gen1 += 1
                if cl == 36:
                    gen2 = 1
        except:
            pass
    for member in sett:
        try:
            stats = r.hmget(member, 'strength', 'intellect', 'spirit', 'weapon', 'defense', 'injure', 'sch', 'class',
                            'clan', 'buff', 'support', 'head')
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
                if checkClan(member, building='build6', level=2):
                    r.hincrby(member, 'sch', -1)
                    i += 5
                else:
                    i, bd = schizophrenia(int(member), i, bd, True)
            if int(stats[9]) > 0 or int(stats[10]) == 13:
                s, bd = trance(int(member), s, bd, True)

            w = int(stats[3])
            if w > 0:
                if w == 26:
                    w = 0.5
                    damage_weapon(member, 25)
                elif w == 7:
                    boost = int(r.hget(member, 's_weapon'))
                    if boost > 25:
                        boost = 25
                    w = 0.25 + boost / 100
                    damage_weapon(member, 7)
                else:
                    w = 0.25
            else:
                w = 0
            d = int(stats[4])
            if d > 0:
                if d == 4:
                    koj += 1
                    damage_defense(member, 4)
                d = 0.25
            else:
                d = 0
            support = int(stats[10])
            if support > 0:
                if support in (2, 9):
                    support = 0.5
                    damage_support(member)
                else:
                    support = 0.25
            else:
                support = 0
            head = int(stats[11])
            if head > 0:
                if head == 2:
                    head = 0.56
                    damage_head(member)
                else:
                    head = 0.25
            else:
                head = 0

            if int(stats[7]) == 24:
                pag = 1
            elif int(stats[7]) in (5, 15, 25) and checkClan(member, building='build4', level=2):
                s = int(s * 1.2)
            elif int(stats[7]) in (7, 17, 27) and checkClan(member, building='build3', level=3):
                mal += 1
            elif int(stats[7]) in (9, 19, 29):
                m = 1
            elif int(stats[7]) in (34, 35, 36):
                if choices([1, 0], [2, 98]) == [1]:
                    intellect(1, member)
                if gen1 == 1 and meat > 0:
                    s = int(s + s * meat * 0.5)
                if r.hget('c' + str(cid), 'side') and int(r.hget('c' + str(cid), 'side')) == 1:
                    codes = int(r.hget('c' + str(cid), 'codes'))
                    if codes > 50:
                        codes = 50
                    s = int(s + s * codes * 0.01)
            if meat > 0:
                quest(member, 3, -3, 2)
            chance += s * (1 + 0.1 * i) * (1 + 0.01 * (bd * 0.01)) * (1 + w + d + support + head)

            quest(member, 1, 3)
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
    return chance, clan5, mal, gen1, gen2, koj


def war_reward(cid1, cid2, msg, r_spirit, money, general, clan, members, koj):
    reward, packs = '4', 0
    if cid1 == -1001211933154:
        money = randint(4, 15)
        reward = str(money)
    money += koj
    msg += r.hget('war_battle' + str(cid1), 'title').decode()
    try:
        if int(r.hget('c' + str(cid1), 'side')) == 1:
            if general > 0:
                if randint(0, 1):
                    money += 2
                else:
                    r_spirit += 2
        elif int(r.hget('c' + str(cid1), 'side')) == 2:
            r_spirit += 2
            if general > 0:
                if choices([0, 1], weights=[85, 15])[0] == 1 and r.hget(222, cid1):
                    packs = int(r.hget(222, cid1)) // 1000
                    if packs >= 2:
                        packs = 3
                    elif packs == 1:
                        packs = 2
                    else:
                        packs = 1
                if int(r.hget('c' + str(cid1), 'build3')) == 2:
                    r_spirit += 1
        elif int(r.hget('c' + str(cid1), 'side')) == 4:
            if general > 0:
                millions = int(r.hget('c' + str(cid1), 'money')) // 1000000
                money += 4 + millions
    except:
        pass
    if clan == 5 and int(r.hget('c' + str(cid1), 'base')) > 1:
        money += 4
        reward = f'{money} \U0001F47E +{r_spirit}'
        if packs:
            reward += f' \U0001F4E6 +{packs}'
    for n in members:
        r.hincrby(n, 'trophy', 1)
        r.hincrby(n, 'wins', 1)
        r.hincrby(n, 'money', money)
        r.hincrby(n, 'packs', packs)
        quest(n, 3, 1, 2)
    r.hincrby('all_trophy', 'trophy', 5)
    r.hincrby(222, cid1, 1)
    if clan >= 5:
        for n in members:
            quest(n, 2, 2)
        if int(r.hget('c' + str(cid1), 'base')) > 1:
            r.hincrby('c' + str(cid1), 'r_spirit', r_spirit)
            if int(r.hget('c' + str(cid1), 'side')) == 4:
                r.hincrby('c' + str(cid1), 'money', money)
        if int(r.hget('c' + str(cid1), 'war')) == 1:
            if int(r.hget('c' + str(cid1), 'enemy')) == cid2 or randint(1, 10) == 1:
                ran = randint(1, 5)
                r.hincrby('c' + str(cid1), 'points', ran)
                reward += f' \U0001fa99 +{ran}'
    return msg, reward


async def great_war(cid1, cid2, a, b):
    await sleep(2)
    ran = choice(['\U0001F93E\u200D\u2642\uFE0F \U0001F93A', '\U0001F6A3 \U0001F3C7', '\U0001F93C\u200D\u2642\uFE0F'])
    chance1, clan1, mal1, gen11, gen12, koj1 = await war_power(a, cid1)
    chance2, clan2, mal2, gen21, gen22, koj2 = await war_power(b, cid2)

    try:
        if gen11 == 1:
            for member in b:
                spirit(-int(int(r.hget(member, 'spirit')) / 20), member, 0)
        if gen21 == 1:
            for member in a:
                spirit(-int(int(r.hget(member, 'spirit')) / 20), member, 0)
        for i in range(mal1):
            r.hincrby(choice(b), 'sch', 3)
        for i in range(mal2):
            r.hincrby(choice(a), 'sch', 3)
    except:
        pass

    await bot.send_message(cid1, ran + ' Русаки несамовито молотять один одного...\n\n\U0001F4AA '
                           + str(int(chance1)) + ' | ' + str(int(chance2)))
    await bot.send_message(cid2, ran + ' Русаки несамовито молотять один одного...\n\n\U0001F4AA '
                           + str(int(chance1)) + ' | ' + str(int(chance2)))
    await sleep(3)

    win = choices(['a', 'b'], weights=[chance1, chance2])

    msg = 'Міжчатова битва русаків завершена!\n\n\U0001F3C6 Бійці з '
    reward, money, r_spirit = '', 4, 1
    if win == ['a']:
        msg, reward = war_reward(cid1, cid2, msg, r_spirit, money, gen12, clan1, a, koj1)
    elif win == ['b']:
        msg, reward = war_reward(cid2, cid1, msg, r_spirit, money, gen22, clan2, b, koj2)
    msg += ' перемагають!\n\U0001F3C5 +1 \U0001F3C6 +1 \U0001F4B5 +' + reward
    msg1 = msg2 = msg.replace('@', '')
    if not r.hexists(f'c{cid1}', 'hints') or int(r.hget(f'c{cid1}', 'hints')) == 0:
        msg1 += '\n\n/war'
    if not r.hexists(f'c{cid2}', 'hints') or int(r.hget(f'c{cid2}', 'hints')) == 0:
        msg2 += '\n\n/war'

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

    await bot.send_message(cid1, msg1, disable_web_page_preview=True)
    await bot.send_message(cid2, msg2, disable_web_page_preview=True)


async def guard_power(mid):
    stats = r.hmget(mid, 'strength', 'intellect', 'spirit', 'weapon', 'defense', 'injure', 'sch', 'class',
                    'buff', 'support', 'head')
    s = int(stats[0])
    i = int(stats[1])
    bd = int(stats[2])
    cl = int(stats[7])
    if checkClan(mid, base=4, building='morgue'):
        d = int(r.hget(mid, 'deaths'))
        if d > 100:
            d = 100
        if d >= 25:
            if r.hexists(mid, 'ac16') == 0:
                r.hset(mid, 'ac16', 1)
        s = int(s * (1 + 0.002 * d))
    if int(stats[5]) > 0:
        s, bd = injure(int(mid), s, bd, True)
    if int(stats[6]) > 0:
        if checkClan(mid, building='build6', level=2):
            r.hincrby(mid, 'sch', -1)
            i += 5
        else:
            i, bd = schizophrenia(int(mid), i, bd, True)
    if int(stats[8]) > 0 or int(stats[9]) == 13:
        s, bd = trance(int(mid), s, bd, True)

    if cl == 6 or cl == 16 or cl == 26:
        if int(r.hget('c' + r.hget(mid, 'clan').decode(), 'build4')) == 1:
            s = s * 2
        else:
            s = int(s * 1.3)

    w = int(stats[3])
    if w > 0:
        w = 0.25
    else:
        w = 0
    d = int(stats[4])
    if d > 0:
        if d == 3:
            r.hincrby('c' + r.hget(mid, 'clan').decode(), 'mines', 1)
            damage_defense(mid, 3)
        d = 0.25
    else:
        d = 0
    support = int(stats[9])
    if support > 0:
        support = 0.25
    else:
        support = 0
    head = int(stats[10])
    if head > 0:
        head = 0.25
    else:
        head = 0
    return int(s * (1 + 0.1 * i) * (1 + 0.01 * (bd * 0.01)) * (1 + w + d + support + head))


def raid_init(cid, raiders, c):
    if int(r.hget('convoy', 'day')) != datetime.now().day:
        r.hset('convoy', 'power', 5000000, {'day': datetime.now().day, 'hour': randint(8, 12), 'first': 1})
    for mem in r.smembers(f'raid_loot{cid}'):
        r.srem(f'raid_loot{cid}', mem)
    for mem in r.smembers(f'raiders{cid}'):
        r.srem(f'raiders{cid}', mem)
    for mem in raiders:
        r.sadd(f'raiders{cid}', mem)
    r.hset(c, 'raid_loot', 'empty', {'raid_loot_n': 0, 'raid_loot_s': 0, 'raid_loot_c': 0,
                                     'raid_loot_ts': 0, 'raid_loot_mid': 0})


def raid_loot(t, n, s, cnt, ts, markup, c):
    r.hset(c, 'raid_loot', t, {
        'raid_loot_n': n,
        'raid_loot_s': s,
        'raid_loot_c': cnt,
        'raid_loot_ts': ts
    })
    return markup.add(InlineKeyboardButton(text=f'Взяти лут. Залишилось {cnt}', callback_data='clan_raid_loot'))


async def start_raid(cid):
    c = 'c' + str(cid)
    title = r.hget(c, 'title').decode()
    raiders = list(r.smembers('fighters_3' + str(cid)))[0:5]
    markup = InlineKeyboardMarkup()
    await sleep(3)
    await bot.send_message(cid, 'Ціль знайдено')
    await sleep(1)

    raid_init(cid, raiders, c)

    chance1 = hack = mar = rocket = fish = jew = did = again = 0
    raid1, raid2, raid3 = 50, 50, 0
    for member in raiders:
        try:
            stats = r.hmget(member, 'strength', 'intellect', 'spirit', 'weapon', 'defense', 'injure', 'sch', 'class',
                            'buff', 'support', 'head')
            s = int(stats[0])
            i = int(stats[1])
            bd = int(stats[2])
            cl = int(stats[7])
            if check_set(int(stats[3]), int(stats[4]), int(stats[9]), int(stats[10])) == 1:
                did += 1
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
                if checkClan(member, building='build6', level=2):
                    r.hincrby(member, 'sch', -1)
                    i += 5
                else:
                    i, bd = schizophrenia(int(member), i, bd, True)
            if int(stats[8]) > 0 or int(stats[9]) == 13:
                s, bd = trance(int(member), s, bd, True)

            if cl in (10, 20, 30):
                s = int(s * 1.5)
                if cl == 30:
                    mar += 1
            if cl in (8, 18, 28):
                hack += 1
            if cl == 33 and int(r.hget('convoy', 'power')) > 0 and datetime.now().hour >= int(r.hget('convoy', 'hour')):
                raid1 -= 10
                raid2 -= 10
                raid3 += 20

            w = int(stats[3])
            if w > 0:
                if w == 3:
                    w = 1 if r.hexists(member, 'woman') == 0 or int(r.hget(member, 'woman')) == 0 else 0.5
                    damage_weapon(member, cl)
                else:
                    w = 0.25
            else:
                w = 0
            d = int(stats[4])
            if d > 0:
                d = 0.25
            else:
                d = 0
            support = int(stats[9])
            if support > 0:
                if support == 10:
                    fish += 1
                if support in (2, 9):
                    if support == 9:
                        rocket += 1
                    support = 0.5
                    damage_support(member)
                else:
                    support = 0.25
            else:
                support = 0
            head = int(stats[10])
            if head > 0:
                if head == 6:
                    jew += 1
                head = 0.25
            else:
                head = 0
            chance1 += int(s * (1 + 0.1 * i) * (1 + 0.01 * (bd * 0.01)) * (1 + w + d + support + head))

            quest(member, 2, 1)
        except:
            continue
    if int(r.hget(c, 'base')) == 11 and raid3 == 0 and int(r.hget('convoy', 'power')) > 0 \
            and datetime.now().hour >= int(r.hget('convoy', 'hour')):
        raid1, raid2, raid3 = 40, 40, 20
    raid1 = raid1 - 10 * mar
    if raid1 < 0:
        raid1 = 0
    raid2 = raid2 + 10 * mar
    mode = choices([1, 2, 3], [raid1, raid2, raid3])

    if chance1 >= 100000:
        for member in r.smembers('fighters_3' + str(cid)):
            quest(member, 3, 2, 3)

    enemy = c2 = ''
    if mode == [1]:
        enemy = r.srandmember('groupings')

        while int(enemy) == cid:
            enemy = r.srandmember('groupings')

        c2 = 'c' + enemy.decode()
        res = r.hmget(c2, 'wood', 'stone', 'cloth', 'brick')
        if int(res[0]) < 1500 or int(res[1]) < 1000 or int(res[2]) < 500 or int(res[3]) < 300:
            mode = [2]

    if mode == [1]:
        title2 = r.hget(c2, 'title').decode()
        if int(r.hget(c2, 'day')) != datetime.now().day:
            r.hset(c2, 'day', datetime.now().day)
            r.hset(c2, 'power', 0)
            for m in r.smembers('guard' + enemy.decode()):
                r.srem('guard' + enemy.decode(), m)
        chance2 = int(r.hget(c2, 'power'))
        msg0 = f'{title} | {title2}\n\n\U0001F4AA {chance1} | {chance2}'.replace('@', '')
        try:
            await bot.send_message(cid, msg0, disable_web_page_preview=True)
            await bot.send_message(int(enemy), 'На нас напали!\n\n' + msg0, disable_web_page_preview=True)
        except:
            pass
        win = choices(['a', 'b'], weights=[chance1, chance2])
        reward = '\n\n'

        if win == ['a']:
            res = r.hmget(c2, 'wood', 'stone', 'cloth', 'brick', 'money', 'r_spirit')
            li = [1, 1, 1, 1, 1, 1]
            if int(r.hget(c, 'base')) == 11:
                if int(r.hget(c, 'wood')) < int(res[0]):
                    li[0] = 2
                if int(r.hget(c, 'stone')) < int(res[1]):
                    li[1] = 2
                if int(r.hget(c, 'cloth')) < int(res[2]):
                    li[2] = 2
                if int(r.hget(c, 'brick')) < int(res[3]):
                    li[3] = 2
                if int(r.hget(c, 'money')) < int(res[4]):
                    li[4] = 2
                if int(r.hget(c, 'r_spirit')) < int(res[5]):
                    li[5] = 2
            ter = int(r.hget(c2, 'build1'))
            mode = choices([1, 2, 3], [70, 20, 10])
            if int(res[4]) < 1000 or int(res[5]) < 10:
                mode = [1]
            base = int(r.hget(c2, 'base'))
            if mode == [1]:
                reward += 'Русаки потрапили на склад і винесли ресурси!\n'
                ran = randint(16, 50) * li[0] if ter == 2 else randint(25, 75) * li[0]
                reward += '\U0001F333 +' + str(ran)
                wood(c, ran)
                r.hincrby(c2, 'wood', -ran)
                if base >= 2:
                    ran = randint(6, 33) * li[1] if ter == 2 else randint(10, 50) * li[1]
                    reward += ' \U0001faa8 +' + str(ran)
                    stone(c, ran)
                    r.hincrby(c2, 'stone', -ran)
                if base >= 3:
                    ran = randint(6, 16) * li[2] if ter == 2 else randint(10, 25) * li[2]
                    reward += ' \U0001F9F6 +' + str(ran)
                    cloth(c, ran)
                    r.hincrby(c2, 'cloth', -ran)
                if base >= 4:
                    ran = randint(3, 10) * li[3] if ter == 2 else randint(5, 15) * li[3]
                    reward += ' \U0001F9F1 +' + str(ran)
                    brick(c, ran)
                    r.hincrby(c2, 'brick', -ran)
            elif mode == [2]:
                reward += 'Русаки пограбували місцеву крамницю!\n'
                ran = randint(50, 100) * li[4]
                reward += f'Кожен забрав по \U0001F4B5 {ran} гривень.'
                r.hincrby(c2, 'money', -ran * 5)
                for mem in r.smembers('fighters_3' + str(cid)):
                    r.hincrby(mem, 'money', ran)
            elif mode == [3]:
                reward += 'Русакам не вдалось знайти нічого цінного, тому вони насрали біля будинку лідера.\n'
                ran = 10 * li[5]
                reward += '\U0001F47E +' + str(ran)
                r.hincrby(c, 'r_spirit', ran)
                r.hincrby(c2, 'r_spirit', -ran)

            if int(r.hget(c, 'war')) == 1 and int(r.hget(c2, 'war')) == 1 and int(r.hget(c2, 'points')) >= 20:
                if int(r.hget(c, 'enemy')) == int(enemy) or int(r.hget(c, 'buff_3')) == 1:
                    ran = randint(5, 10)
                    if int(r.hget(c, 'buff_2')) == 1:
                        ran *= 2
                    r.hincrby(c, 'points', ran)
                    r.hincrby(c2, 'points', -ran)
                    reward += '\n\U0001fa99 +' + str(ran)

        elif win == ['b']:
            if int(r.hget(c2, 'mines')) > 0:
                ran = randint(1, 5)
                for mem in r.smembers('fighters_3' + str(cid)):
                    r.hincrby(mem, 'injure', ran)
                r.hincrby(c2, 'mines', -1)
                reward += f'Русаки підірвались на міні...\n\U0001fa78 +{ran} \U0001fac0 -100'
            else:
                reward += 'Русаків затримала охорона...\n\U0001fac0 -100'
            if mar >= 1 and chance2 > 0:
                lose = int(chance2 * (1 - 0.1 * mar))
                reward += f'\nОхорона втратила \U0001F4AA {chance2 - lose}'
                r.hset(c2, 'power', lose)

            for member in r.smembers('fighters_3' + str(cid)):
                hp(-100, member)

            if did > 0:
                chance = 15 * did
                again = choices([0, 1], weights=[100 - chance, chance])[0]

        await sleep(10)
        msg = 'Проведено рейд на клан ' + r.hget(c2, 'title').decode().replace('@', '') + '!' + reward
        msg2 = 'На нас напали рейдери з клану ' + r.hget(c, 'title').decode().replace('@', '') + '!'
        if win == ['a']:
            msg2 += reward.replace('+', '-')
        else:
            msg2 += reward
        if again:
            msg += '\nРусаки готові до реваншу!'

        if win == ['a'] and int(r.hget(c, 'buff_1')) == 1:
            side2 = int(r.hget(c2, 'side'))

            if side2 == 1:
                if randint(1, 5) == 5:
                    r.hincrby(c, 'codes')
                    msg += '\n\U0001F916 +1'
                else:
                    msg += '\n\U0001F6E1 Кожух [Захист, міцність=20]'
                    markup = raid_loot('defense', 4, 20, 5, int(datetime.now().timestamp()) + 10, markup, c)

            elif side2 == 2:
                if randint(1, 5) == 5:
                    msg += '\n\u2620\uFE0F +5'
                    for mem in r.smembers('fighters_3' + str(cid)):
                        r.hincrby(mem, 'deaths', 5)
                else:
                    msg += '\n\U0001F3A9 Тактичний шолом [Шапка, міцність=20]'
                    markup = raid_loot('head', 2, 20, 5, int(datetime.now().timestamp()) + 10, markup, c)

            elif side2 == 3:
                if randint(1, 5) == 5:
                    msg += '\n\U0001fac0 +100 \U0001F4B5 +100'
                    for mem in r.smembers('fighters_3' + str(cid)):
                        r.hset(mem, 'hp', 100)
                        r.hincrby(mem, 'money', 100)
                else:
                    msg += '\n\U0001F5E1 Батіг [Зброя, міцність=3]'
                    markup = raid_loot('weapon', 3, 3, 5, int(datetime.now().timestamp()) + 10, markup, c)

            elif side2 == 4:
                if randint(1, 5) == 5:
                    msg += '\n\U0001F476 +1'
                    for mem in r.smembers('fighters_3' + str(cid)):
                        r.hincrby(mem, 'childs', 1)
                else:
                    msg += '\n\U0001F9EA Цукор [Допомога, міцність=1]'
                    markup = raid_loot('support', 7, 1, 5, int(datetime.now().timestamp()) + 10, markup, c)
            else:
                if randint(1, 5) == 5:
                    msg += '\n\U0001F4E6 +3'
                    for mem in r.smembers('fighters_3' + str(cid)):
                        r.hincrby(mem, 'packs', 3)
                else:
                    msg += '\n\u2622 +5'
                    for mem in r.smembers('fighters_3' + str(cid)):
                        for i in range(5):
                            vodka(mem)

        if choices([1, 0], [5, 95]) == [1]:
            r.hincrby(c, 'codes', 1)
            msg += '\n\U0001F916 +1'
        try:
            a = await bot.send_message(cid, msg, disable_web_page_preview=True, reply_markup=markup)
            r.hset(c, 'raid_loot_mid', a.message_id)
            await bot.send_message(int(enemy), msg2, disable_web_page_preview=True)
        except:
            pass

    elif mode == [2]:
        locations = ['Відділення монобанку', 'Магазин алкоголю', 'АТБ', 'Сільпо', 'Епіцентр', 'Макіївський роднічок']
        chances = ['0', '0.1', '0.2', '0.3', '0.5', '0.75']
        s = int(r.hget(c, 'side'))
        if s == 3:
            chances = ['0', '0.05', '0.1', '0.15', '0.25', '0.375']
        if fish >= 5:
            location = 'Ставок швайнокарасів'
            chance2 = 0
        elif jew >= 5 and int(r.hget(c, 'war')) == 1 and int(r.hget(c, 'buff_5')) < 3:
            location = 'Синагога'
            chance2 = int(chance1 * choice([0.5, 1, 2, 3]))
            if s == 3:
                chance2 = int(chance2 / 2)
        else:
            location = choice(locations)
            chance2 = int(chance1 * float(chances[locations.index(location)]))
        msg0 = f'{title} | {location}\n\n\U0001F4AA {chance1} | {chance2}'
        try:
            await bot.send_message(cid, msg0, disable_web_page_preview=True)
        except:
            pass
        win = choices(['a', 'b'], weights=[chance1, chance2])
        reward = '\n\n'

        if win == ['a']:
            if location == 'Ставок швайнокарасів':
                reward += f"Русаки випустили швайнокарасів в ставок і знайшли камінь, на якому було написано...\n\n" \
                          f"{r.hget('promo_code', 'fish_promo_code').decode()}"
                r.sadd('fifth_code_allowed', cid)
                for mem in r.smembers('fighters_3' + str(cid)):
                    r.hset(mem, 'support', 0, {'s_support': 0})
            elif location == 'Синагога':
                r.hincrby(c, 'buff_5', 1)
                reward += f"Русаки повернулись з синагоги...\n\n" \
                          f"Отримано баф:\n\n\U0001f7e1 +1 очко за виконання кошерних квестів."
                if int(r.hget(c, 'buff_5')) > 1:
                    reward += ' +40 квестових очків за купівлю ресурсів за погони.'
                if int(r.hget(c, 'buff_5')) > 2:
                    reward += '\n\n\U0001fa99 +100'
                    r.hincrby(c, 'points', 100)
            elif locations.index(location) == 0:
                if hack >= 1:
                    ran = randint(30, 250)
                    if mar >= 1:
                        ran *= 2
                    reward += 'Хакер отримав доступ до рахунків монобанку!\n\U0001F4B5 +' + str(ran)
                    r.hincrby(c, 'money', ran)
                    for mem in r.smembers('fighters_3' + str(cid)):
                        r.hincrby(mem, 'money', ran)
                else:
                    reward += 'Русаки шукали відділення...\nНа цей раз нічого не вдалось знайти.'

            elif locations.index(location) == 1:
                reward += 'Русаки пограбували магазин алкоголю\n'
                ran = randint(5, 20)
                if mar >= 1:
                    ran *= 2
                reward += '\u2622 +' + str(ran) + ' \U0001fac0 +100 \U0001F54A +10000'
                for mem in r.smembers('fighters_3' + str(cid)):
                    r.hincrby(mem, 'vodka', ran)
                    r.hincrby('all_vodka', 'vodka', ran)
                    hp(100, mem)
                    spirit(10000, mem, 0)
                if did > 0:
                    chance = 15 * did
                    again = choices([0, 1], weights=[100 - chance, chance])[0]
                    if again:
                        reward += '\nРусаки готові йти в наступний рейд!'
            elif locations.index(location) == 2:
                reward += 'Русаки пограбували АТБ\n'
                mode = choice([1, 2, 3, 4])
                mode2 = choice([1, 2])
                items = randint(5, 10)
                if mode == 1:
                    s = 3
                    if mar >= 1:
                        s *= 2
                    reward += f'\U0001F37A Квас [Допомога, міцність={s}]'
                    markup = raid_loot('support', 8, s, items, int(datetime.now().timestamp()) + 10, markup, c)
                if mode == 2:
                    s = 2
                    if mar >= 1:
                        s *= 2
                    reward += f'\U0001F9EA Цукор [Допомога, міцність={s}]'
                    markup = raid_loot('support', 7, s, items, int(datetime.now().timestamp()) + 10, markup, c)
                if mode == 3:
                    reward += '\U0001F349 Кавун базований [Шапка, міцність=∞]'
                    markup = raid_loot('head', 3, 1, items, int(datetime.now().timestamp()) + 10, markup, c)
                if mode == 4:
                    emoji = choice(['\U0001F35C', '\U0001F35D', '\U0001F35B', '\U0001F957', '\U0001F32D'])
                    reward += emoji + ' +1'
                    markup = raid_loot('food', 0, 0, 5, int(datetime.now().timestamp()) + 10, markup, c)
                if mode2 == 1:
                    ran = randint(50, 100)
                    if mar >= 1:
                        ran *= 2
                    reward += '\n\U0001F4B5 +' + str(ran)
                    for mem in r.smembers('fighters_3' + str(cid)):
                        r.hincrby(mem, 'money', ran)
            elif locations.index(location) == 3:
                reward += 'Русаки пограбували Сільпо\n'
                mode = choice([1, 2, 3, 4])
                mode2 = choice([1, 2])
                if mode == 1:
                    s = 6
                    if mar >= 1:
                        s *= 2
                    reward += f'\U0001F37A Квас [Допомога, міцність={s}]'
                    markup = raid_loot('support', 8, s, 5, int(datetime.now().timestamp()) + 10, markup, c)
                if mode == 2:
                    s = 4
                    if mar >= 1:
                        s *= 2
                    reward += f'\U0001F9EA Цукор [Допомога, міцність={s}]'
                    markup = raid_loot('support', 7, s, 5, int(datetime.now().timestamp()) + 10, markup, c)
                if mode == 3:
                    reward += '\U0001F349 Кавун базований [Шапка, міцність=∞]'
                    markup = raid_loot('head', 3, 1, 5, int(datetime.now().timestamp()) + 10, markup, c)
                if mode == 4:
                    emoji = choice(['\U0001F35C', '\U0001F35D', '\U0001F35B', '\U0001F957', '\U0001F32D'])
                    reward += emoji + ' +1'
                    markup = raid_loot('food', 0, 0, 5, int(datetime.now().timestamp()) + 10, markup, c)
                if mode2 == 1:
                    ran = randint(100, 200)
                    if mar >= 1:
                        ran *= 2
                    reward += '\n\U0001F4B5 +' + str(ran)
                    for mem in r.smembers('fighters_3' + str(cid)):
                        r.hincrby(mem, 'money', ran)
            elif locations.index(location) == 4:
                reward += 'Русаки пограбували Епіцентр\n'
                base = int(r.hget(c, 'base'))
                mode = choice([1, 2])
                if base >= 1:
                    ran = randint(25, 75)
                    if mar >= 1:
                        ran *= 2
                    reward += '\U0001F333 +' + str(ran)
                    wood(c, ran)
                if base >= 2:
                    ran = randint(10, 50)
                    if mar >= 1:
                        ran *= 2
                    reward += ' \U0001faa8 +' + str(ran)
                    stone(c, ran)
                if base >= 3:
                    ran = randint(10, 25)
                    if mar >= 1:
                        ran *= 2
                    reward += ' \U0001F9F6 +' + str(ran)
                    cloth(c, ran)
                if base >= 4:
                    ran = randint(5, 15)
                    if mar >= 1:
                        ran *= 2
                    reward += ' \U0001F9F1 +' + str(ran)
                    brick(c, ran)
                if mode == 1:
                    ran = 1
                    if mar >= 1:
                        ran *= 2
                    reward += f'\n🌀 +{ran}'
                    markup = raid_loot('tape', 0, ran, 5, int(datetime.now().timestamp()) + 10, markup, c)
            elif locations.index(location) == 5:
                reward += 'Русаки вчинили жахливий теракт...\n'
                ran = randint(10, 20)
                if mar >= 1:
                    ran *= 2
                reward += ' \U0001F47E +' + str(ran)
                r.hincrby(c, 'r_spirit', ran)
        elif win == ['b']:
            if location == 'Макіївський роднічок':
                reward += 'Русаки вирішили напитись води...\n\U0001F44A +20 \U0001fac0 -100'
                for member in r.smembers('fighters_3' + str(cid)):
                    increase_trance(20, member)
            elif location == 'Синагога':
                reward += 'Жиди вигнали русаків з синагоги...\n\U0001fac0 -100'
            else:
                reward += 'Русаків затримала охорона...\n\U0001fac0 -100'
            for member in r.smembers('fighters_3' + str(cid)):
                hp(-100, member)
            if did > 0:
                chance = 15 * did
                again = choices([0, 1], weights=[100 - chance, chance])[0]
                if again:
                    reward += '\nРусаки готові до реваншу!'
        if choices([1, 0], [5, 95]) == [1]:
            r.hincrby(c, 'codes', 1)
            reward += '\n\U0001F916 +1'
        await sleep(10)
        msg = 'Проведено рейд на ' + location + '!' + reward
        a = await bot.send_message(cid, msg, disable_web_page_preview=True, reply_markup=markup)
        r.hset(c, 'raid_loot_mid', a.message_id)

    elif mode == [3]:

        s = int(r.hget(c, 'side'))
        chance1 = int(chance1 * (1 + rocket * 0.07))
        chance2 = int(r.hget('convoy', 'power'))
        msg0 = f'{title} | Перехоплення гумконвою\n\n\U0001F4AA {chance1} | {chance2}'
        try:
            await bot.send_message(cid, msg0)
        except:
            pass

        msg = 'Русаки приїхали грабувати гумконвой...\n\n'
        diff = chance2 - chance1
        packs = 0
        if diff < 0:
            diff = 0
        if diff == 0:
            r.hset('convoy', 'power', 0)
            msg += 'Від гумконвою більше нічого не залишилось!\n'
            packs += 5
        else:
            r.hincrby('convoy', 'power', -chance1)
        if s == 3:
            reward = int(chance2 / 20000 - (diff / 20000))
        else:
            reward = int(chance2 / 25000 - (diff / 25000))
        if reward > 0 or packs > 0:
            packs += reward
            msg += f'\U0001F4E6 +{packs}'
            for mem in r.smembers('fighters_3' + str(cid)):
                quest(mem, 3, 3, 3)

            packs_s = 5
            if int(r.hget(c, 'build6')) == 3:
                packs_s = randint(5, 10)
            markup = raid_loot('convoy', 0, packs, packs_s, int(datetime.now().timestamp()) + 10, markup, c)
            if int(r.hget(c, 'buff_4')) == 31:
                q_points(int(r.srandmember('fighters_3' + str(cid))), 10)
                msg += ' \U0001fa99 +10'
        elif reward <= 0 and diff != 0:
            msg += 'Але їхньої сили не вистачило, щоб залутати хоч щось'

        if choices([1, 0], [5, 95]) == [1]:
            r.hincrby(c, 'codes', 1)
            msg += '\n\U0001F916 +1'

        await sleep(10)
        a = await bot.send_message(cid, msg, disable_web_page_preview=True, reply_markup=markup)
        r.hset(c, 'raid_loot_mid', a.message_id)
        if diff == 0 or int(r.hget('convoy', 'first')) == 1:
            if diff == 0:
                msg = '\U0001F69B Гумконвой розграбовано.'
            if int(r.hget('convoy', 'first')) == 1:
                msg = '\U0001F69B Гумконвой прибув.'
                r.hset('convoy', 'first', 0)
            for mem in r.smembers('followers'):
                try:
                    c3 = 'c' + mem.decode()
                    if int(r.hget(c3, 'not_time')) != datetime.now().day:
                        if int(r.hget(c3, 'technics')) >= 3:
                            r.hset(c3, 'not_time', datetime.now().day)
                            r.hincrby(c3, 'technics', -3)
                        else:
                            r.hset(c3, 'notification', 0)
                            r.srem('followers', mem)
                            continue
                    await bot.send_message(int(mem), msg)
                except:
                    pass
    try:
        await bot.unpin_chat_message(chat_id=cid, message_id=int(r.hget(c, 'pin')))
    except:
        pass
    if not again:
        r.hset(c, 'raid_ts2', int(datetime.now().timestamp()))
    r.hdel(c, 'start')
    for member in r.smembers('fighters_3' + str(cid)):
        r.srem('fighters_3' + str(cid), member)
