import random
import telebot
from telebot import types
import os
from flask import Flask, request
import redis
from datetime import date
from datetime import datetime
import time

r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=int(os.environ.get('REDIS_PORT')),
                password=os.environ.get('REDIS_PASSWORD'), db=0)

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

names = ['Ваня', 'Ваня', 'Ваня', 'Славік', 'Колян', 'Вован', 'Мага', 'Махмед', 'Олег', 'Стасян',
         'Петруха', 'Алєксандр', 'Сашка', 'Міхаіл', 'Мішка', 'Юрас', 'Гіві', 'Андрюха', 'Хабіб',
         'Саньок', 'Льоха', 'Даня', 'Русік', 'Альоша', 'Вітя', 'Владос', 'Женя', 'Ігор', 'Сірьога',
         'Едік', 'Віталя', 'Ашот', 'Моторола']

icons = ['', '\U0001F919', '\U0001F9F0', '\U0001F52E', '\U0001F5FF',
         '\U0001fa96', '\U0001F46E', '\U0001F921', '\U0001F4DF', '', '',
         '\U0001F919\U0001F919', '\U0001F9F0\U0001F9F0', '\U0001F52E\U0001F52E', '\U0001F5FF\U0001F5FF',
         '\U0001fa96\U0001fa96', '\U0001F46E\U0001F46E', '\U0001F921\U0001F921', '\U0001F4DF\U0001F4DF', '', '',

         '\U0001F919\U0001F919\U0001F919', '\U0001F9F0\U0001F9F0\U0001F9F0', '\U0001F52E\U0001F52E\U0001F52E',
         '\U0001F5FF\U0001F5FF\U0001F5FF', '\U0001fa96\U0001fa96\U0001fa96', '\U0001F46E\U0001F46E\U0001F46E',
         '\U0001F921\U0001F921\U0001F921', '\U0001F4DF\U0001F4DF\U0001F4DF']

class_name = ['', 'Хач', 'Роботяга', 'Фокусник', 'Язичник', 'Гарматне м`ясо', 'Мусор', 'Малорос', 'Хакер', '', '',
              'Борцуха', 'Почесний алкаш', 'Злий геній', 'Скінхед', 'Орк', 'Силовик', 'Кремлебот', 'Кіберзлочинець',
              '', '', 'Гроза Кавказу', 'П`яний майстер', 'Некромант', 'Білий вождь', 'Герой Донбасу', 'Товариш майор',
              'Агент ФСБ', 'Black Hat']

weapons = ['', 'Колючий дрин', 'РПГ-7', '', 'Бита', '', '', '', '', '', '',
           'Травмат', 'Діамантове кайло', 'Колода з кіоску', 'Сокира Перуна',
           'АК-47', 'Гумова палиця', 'Прапор новоросії', 'Експлойт']

defenses = ['', 'Колючий щит', 'Бронежилет вагнерівця', '', '', '', '', '', '', 'Уламок бронетехніки',
            'Мухомор королівський', '', '', '', '', 'АК-47', 'Поліцейський щит', 'Прапор новоросії', '']

photos = ['https://i.ibb.co/rGd7L5n/rusnya.jpg',

          'https://i.ibb.co/qmkDFTP/1.jpg', 'https://i.ibb.co/hDsXjZb/2.jpg', 'https://i.ibb.co/NNmfy50/3.jpg',
          'https://i.ibb.co/gZ96zHK/4.jpg', 'https://i.ibb.co/8b0BWyR/5.jpg',

          'https://i.ibb.co/wQhWFcW/1.jpg', 'https://i.ibb.co/5GHPw0Q/2.jpg', 'https://i.ibb.co/2MmzDx1/3.jpg',
          'https://i.ibb.co/rFwxSsw/4.jpg', 'https://i.ibb.co/6RcHkdw/5.jpg',

          'https://i.ibb.co/h2VBPTx/1.jpg', 'https://i.ibb.co/gDzX80W/2.jpg', 'https://i.ibb.co/xJLTvKV/3.jpg',
          'https://i.ibb.co/s2ZydPD/4.jpg', 'https://i.ibb.co/wrv51G0/5.png',

          'https://i.ibb.co/NKG6rNT/1.png', 'https://i.ibb.co/jr64ddS/2.png', 'https://i.ibb.co/qWdYP6f/3.png',
          'https://i.ibb.co/NYPtWsX/4.png', 'https://i.ibb.co/H7dS23v/5.png',

          'https://i.ibb.co/9vYrMRY/1.png', 'https://i.ibb.co/wM3B3Z8/2.png', 'https://i.ibb.co/gM8BpYL/3.png',
          'https://i.ibb.co/cwbpQZc/4.png', 'https://i.ibb.co/w0kdDkJ/5.png',

          'https://i.ibb.co/FJmyWGW/1.jpg', 'https://i.ibb.co/ZHNrWQ1/2.jpg', 'https://i.ibb.co/YPTDzmZ/3.jpg',
          'https://i.ibb.co/zQpXqvr/4.jpg', 'https://i.ibb.co/LPW1RzY/5.jpg',

          'https://i.ibb.co/xGD85gj/1.png', 'https://i.ibb.co/px1wrjH/2.png', 'https://i.ibb.co/DYpB1dW/3.png',
          'https://i.ibb.co/RDJHW38/4.png', 'https://i.ibb.co/kqxKG3f/5.png',

          'https://i.ibb.co/db2zQ5r/1.png', 'https://i.ibb.co/HD8QXLg/2.png', 'https://i.ibb.co/7N3Mycb/3.png',
          'https://i.ibb.co/D7jMyq1/4.png', 'https://i.ibb.co/FV8xVPk/5.png',

          'https://i.ibb.co/GFMKxrp/9.png', 'https://i.ibb.co/nRpTjWt/10.png',
          'https://i.ibb.co/8D5kNzV/1.png', 'https://i.ibb.co/31jXXxQ/2.png', 'https://i.ibb.co/zmYDNrn/3.png',
          'https://i.ibb.co/QDHLRPp/4.png', 'https://i.ibb.co/GntBLKG/5.png', 'https://i.ibb.co/b1jN3GC/6.png',
          'https://i.ibb.co/QmfJRPP/7.png', 'https://i.ibb.co/9H5Wxfj/8.png']

sudoers = [456514639, 634799543, 379620096]


def prepare_to_fight(uid, fn, q):
    if r.hexists(uid, 'name') == 0:
        return 'В тебе немає русака.\n\n@Random_UAbot <- отримати русака'
    else:
        stats = r.hmget(uid, 'name', 'class', 'strength', 'intellect', 'spirit')
        name = int(stats[0])
        c = int(stats[1])
        s = int(stats[2])
        s1 = s
        i = int(stats[3])
        bd = int(stats[4])

        if int(r.hget(uid, 'injure')) > 0:
            s, s1, i, bd = injure(uid, False)

        if c == 3:
            s = random.randint(10, 1000)
            i = random.randint(1, 10)
            bd = random.randint(0, 10000)
        elif c == 13 or c == 23:
            s = random.randint(200, 2000)
            i = random.randint(10, 20)
            bd = random.randint(0, 10000)
            if c == 23:
                c = random.randint(0, len(icons))

        query = ''
        try:
            q = q.split()
            if q[0].startswith('турнірний_режим_2021'):
                query = '\n\n\U0001F530 Турнірний режим \U0001F530'
                try:
                    if q[1].startswith('@'):
                        query += '\n\U0001F4E3 Викликаю на бій ' + q[1] + '!'
                except:
                    pass
            elif q[0].startswith('особисте_запрошення_2021'):
                try:
                    if q[1].startswith('@'):
                        query += '\n\U0001F4E3 Викликаю на бій ' + q[1] + '!'
                except:
                    pass
            elif int(q[1]) > 0:
                s2 = s1 - int(q[1])
                if s2 < 1:
                    s2 = 1
                query = '\n\n\U0001F4E2 Розшукується суперник з силою від ' + \
                        str(s2) + ' до ' + str(s1 + int(q[1])) + '.'
        except:
            pass

        stats = str("\n\n\U0001F3F7 " + names[name] + ' ' + icons[c] +
                    '\n\U0001F4AA ' + str(s) +
                    ' \U0001F9E0 ' + str(i) +
                    ' \U0001F54A ' + str(bd) +
                    '\n\n\u2744\uFE0F @Random_UAbot <- отримати русака')

        return '\u2744\uFE0F ' + fn + ' починає битву русаків!' + query + stats


def fight(uid1, uid2, un1, un2):
    weapon, defense = '', ''
    stats1 = r.hmget(uid1, 'name', 'class', 'weapon', 'defense')
    stats2 = r.hmget(uid2, 'name', 'class', 'weapon', 'defense')
    name1, name2 = int(stats1[0]), int(stats2[0])
    c1, c2 = int(stats1[1]), int(stats2[1])
    weapon1, weapon2 = int(stats1[2]), int(stats2[2])
    defense1, defense2 = int(stats1[3]), int(stats2[3])

    hach1, hach2, hach, worker, meat, cop, fsb, inj1, inj2 = 0, 0, '', '', '', '', '', '', ''
    if c1 == 1 or c1 == 11 or c1 == 21:
        if weapon2 == 0:
            hach1 = 1
    if c2 == 1 or c2 == 11 or c2 == 21:
        if weapon1 == 0:
            hach2 = 1
    if c1 == 21:
        if c2 == 1 or c2 == 11 or c2 == 21:
            if int(r.hget(uid1, 'hach_time2')) != date.today().day:
                hach += '\n' + names[name1] + ': брат за брата! \U0001F919\n\U0001F4AA + 10 \U0001F54A +1000\n'
                r.hset(uid1, 'hach_time2', date.today().day)
                r.hincrby(uid1, 'strength', 10)
                spirit(1000, uid1, 21, fi=False)
    if c2 == 21:
        if c1 == 1 or c1 == 11 or c1 == 21:
            if int(r.hget(uid2, 'hach_time2')) != date.today().day:
                hach += '\n' + names[name2] + ': брат за брата! \U0001F919\n\U0001F4AA + 10 \U0001F54A +1000\n'
                r.hset(uid2, 'hach_time2', date.today().day)
                r.hincrby(uid2, 'strength', 10)
                spirit(1000, uid2, 21, fi=False)
    if c1 == 22:
        if int(r.hget(uid1, 'worker')) != date.today().day and int(r.hget(uid1, 'time')) == date.today().day:
            alcohol = int(r.hget(uid1, 's1'))
            ran = random.choices([0, 1], weights=[100 - int(alcohol/2), int(alcohol/2)])
            if ran == [1]:
                worker += '\n\U0001F9F0 ' + names[name1] + ' отримує від начальника талон на їжу.\n'
                r.hset(uid1, 'worker', date.today().day)
                r.hset(uid1, 'time', 0)
    if c2 == 22:
        if int(r.hget(uid2, 'worker')) != date.today().day and int(r.hget(uid2, 'time')) == date.today().day:
            alcohol = int(r.hget(uid2, 's1'))
            ran = random.choices([0, 1], weights=[100 - int(alcohol/2), int(alcohol/2)])
            if ran == [1]:
                worker += '\n\U0001F9F0 ' + names[name2] + ' отримує від начальника талон на їжу.\n'
                r.hset(uid2, 'worker', date.today().day)
                r.hset(uid2, 'time', 0)
    if c1 == 26:
        if c2 != 6 and c2 != 16 and c2 != 26:
            if weapon2 != 0:
                cop1 = random.choices([1, 0], weights=[20, 80])
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
                cop2 = random.choices([1, 0], weights=[20, 80])
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
        fsb1 = random.choices([1, 0], weights=[5, 95])
        if fsb1 == [1]:
            r.hset(uid2, 'class', 7)
            r.hset(uid2, 'photo', random.randint(31, 35))
            r.hincrby(uid1, 'money', 20)
            fsb += '\n\U0001F921 ' + names[name1] + ' завербував ворога!\n\U0001F4B5 +20\n'
    if c2 == 27 and c1 == 0:
        fsb2 = random.choices([1, 0], weights=[5, 95])
        if fsb2 == [1]:
            r.hset(uid1, 'class', 7)
            r.hset(uid1, 'photo', random.randint(31, 35))
            r.hincrby(uid2, 'money', 20)
            fsb += '\n\U0001F921 ' + names[name2] + ' завербував ворога!\n\U0001F4B5 +20\n'

    if weapon2 == 1 and int(r.hget(uid1, 'spirit')) >= 300:
        foc = 1
        if c1 == 3 or c1 == 13 or c1 == 23:
            foc = random.choice([0, 0, 0, 0, 1])
        if foc == 1:
            if int(r.hget(uid1, 'spirit')) <= 1000:
                r.hset(uid1, 'spirit', 0)
            elif 1000 < int(r.hget(uid1, 'spirit')) < 2500:
                r.hincrby(uid1, 'spirit', -1000)
            else:
                chance = random.choice([2.5, 3.333, 5])
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
            chance = random.choice([2.5, 3.333, 5])
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
            chance = random.choice([2.5, 3.333, 5])
            r.hincrby(uid2, 'spirit', -int(int(r.hget(uid2, 'spirit')) / chance))
        r.hset(uid1, 'defense', 0)
        defense = '\n\n\U0001F6E1 ' + names[name1] + ' захистився колючим щитом, опонент розгубився!'

    stats11 = r.hmget(uid1, 'strength', 'intellect', 'spirit')
    stats22 = r.hmget(uid2, 'strength', 'intellect', 'spirit')
    s1, s2 = int(stats11[0]), int(stats22[0])
    s11 = s1
    s22 = s2
    i1, i2 = int(stats11[1]), int(stats22[1])
    bd1, bd2 = int(stats11[2]), int(stats22[2])

    if int(r.hget(uid1, 'injure')) > 0:
        s1, s11, i1, bd1 = injure(uid1, True)
        inj1 = '\U0001fa78 '
    if int(r.hget(uid2, 'injure')) > 0:
        s2, s22, i2, bd2 = injure(uid2, True)
        inj2 = '\U0001fa78 '

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
        ran = random.choices([1, 2], weights=[98, 2])
        if ran == [2] and defense1 != 2:
            weapon = weapon + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе і отримав ' \
                              'важкі поранення.'
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
    elif weapon2 == 2 and defense1 != 2:
        weapon = '\n\n\u2620\uFE0F ' + names[name2] + ': АЛЛАХ АКБАР!'
        r.hincrby(uid1, 'injure', 200)
        r.hset(uid1, 'spirit', 0)
        if c1 != 6 and c1 != 16 and c1 != 26:
            r.hset(uid1, 'weapon', 0)
        r.hset(uid1, 'defense', 0)
        r.hset(uid2, 'weapon', 0)
        r.hset(uid2, 's_weapon', 0)

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
                intellect(1, uid1)
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
        ran = random.choices([1, 2], weights=[98, 2])
        if ran == [2] and defense2 != 2:
            defense = defense + '\n\u2620\uFE0F Але він не врятував русака, який випадково вистрелив в себе і отримав' \
                                ' важкі поранення.'
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
        spirit(30, uid1, c1, fi=True)
    elif hach1 == 0:
        if c1 == 1 or c1 == 11 or c1 == 21:
            s1 = int(s1 * 0.9)
    if hach2 == 1:
        s2 = int(s2 * 1.1)
        spirit(30, uid2, c2, fi=True)
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
            shot = random.choices([1, 0], weights=[10, 90])
            if shot == [1]:
                ran = random.randint(5, 10)
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
            shot = random.choices([1, 0], weights=[10, 90])
            if shot == [1]:
                ran = random.randint(5, 10)
                meat += '\n\U0001fa96 ' + names[name2] + ' +1 \U0001fa78 | ' + names[name1] + ' +' + \
                        str(ran) + ' \U0001fa78\n'
                r.hincrby(uid2, 'injure', 1)
                r.hincrby(uid1, 'injure', ran)

    chance1 = s1 * (1 + 0.1 * i1) * (1 + 0.01 * (bd1 * 0.01))
    chance2 = s2 * (1 + 0.1 * i2) * (1 + 0.01 * (bd2 * 0.01))

    chance11 = chance1 / ((chance1 + chance2) / 100)
    chance22 = chance2 / ((chance1 + chance2) / 100)

    if c2 != 7 and chance11 > 95:
        win = random.choices(['1', '2'], weights=[95, 5])
    elif c1 != 7 and chance22 > 95:
        win = random.choices(['1', '2'], weights=[5, 95])
    elif c2 == 7 and chance11 > 80:
        win = random.choices(['1', '2'], weights=[80, 20])
    elif c1 == 7 and chance22 > 80:
        win = random.choices(['1', '2'], weights=[20, 80])
    else:
        win = random.choices(['1', '2'], weights=[chance1, chance2])

    info = str('\u2744\uFE0F ' + un1 + ' vs ' + un2 + '\n\n\U0001F3F7 ' + inj1 + names[name1] + ' ' +
               icons[c1] + ' | ' + inj2 + names[name2] + ' ' + icons[c2] +
               '\n\U0001F4AA ' + str(s1) + ' | ' + str(s2) +
               '\n\U0001F9E0 ' + str(i1) + ' | ' + str(i2) +
               '\n\U0001F54A ' + str(bd1) + ' | ' + str(bd2)) + weapon + defense

    if win == ['1']:
        if s11 / s22 > 2:
            bonus = random.randint(1, 20)
            grn = ''
        elif s11 / s22 < 0.5:
            bonus = random.randint(60, 120)
            grn = random.choices([1, 2, 3], weights=[50, 48, 2])
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
            bonus = random.randint(20, 60)
            grn = random.choices([0, 1, 2, 3], weights=[50, 44, 5, 1])
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
                trick = random.choices([1, 0], weights=[hc, 1 - hc])
                if trick == [1]:
                    trick = random.choices([1, 2, 3], weights=[45, 45, 10])
                    if trick == [1]:
                        ran = random.randint(50, 100)
                        hach += '\n\U0001F919 ' + names[name1] + ' кинув суперника через стегно!\n\U0001F54A -' + \
                                str(ran) + '\n'
                        spirit(-ran, uid2, c2, fi=False)
                    elif trick == [2]:
                        ran = random.randint(50, 100)
                        hach += '\n\U0001F919 ' + names[name1] + ' кинув суперника млином!\n\U0001F54A +' + \
                                str(ran) + '\n'
                        spirit(ran, uid1, c1, fi=False)
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

        spirit(bonus, uid1, c1, fi=True)
        spirit(-bonus, uid2, c2, fi=True)
        r.hincrby(uid1, 'wins', 1)

        hack = ''
        if c2 == 8 or c2 == 18 or c2 == 28:
            hack1 = random.choices([0, 1], weights=[82, 18])
            if weapon2 == 18:
                hack1 = random.choices([0, 1], weights=[1, 99])
                hack = '\n\n\U0001F5E1 ' + names[name2] + ' використав експлойт...'
                r.hincrby(uid2, 's_weapon', -1)
                if int(r.hget(uid2, 's_weapon')) <= 0:
                    r.hset(uid2, 'weapon', 0)
            if hack1 == [1]:
                spirit(bonus * 2, uid2, c2, fi=False)
                spirit(-bonus, uid1, c1, fi=False)
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
            meat += '\n' + names[name1] + ' бахнув горілочки. ' + '\U0001F54A ' + vodka(uid1, 5)

        win_info = str('\n\n\U0001F3C6 ' + str(un1) + ' перемагає ' + str(un2) + '! ' + str(grn) +
                       '\nЙого русак отримує +' + str(bonus) + ' бойового духу, а русак опонента стільки ж втрачає.' +
                       hach + worker + meat + cop + pag + fsb + hack)
        return info + win_info
    elif win == ['2']:
        if s22 / s11 > 2:
            bonus = random.randint(1, 20)
            grn = ''
        elif s22 / s11 < 0.5:
            bonus = random.randint(60, 120)
            grn = random.choices([1, 2, 3], weights=[50, 48, 2])
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
            bonus = random.randint(20, 60)
            grn = random.choices([0, 1, 2, 3], weights=[50, 44, 5, 1])
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
                trick = random.choices([1, 0], weights=[hc, 1 - hc])
                if trick == [1]:
                    trick = random.choices([1, 2, 3], weights=[45, 45, 10])
                    if trick == [1]:
                        ran = random.randint(50, 100)
                        hach += '\n\U0001F919 ' + names[name2] + ' кинув суперника через стегно!\n\U0001F54A -' + \
                                str(ran) + '\n'
                        spirit(-ran, uid1, c1, fi=False)
                    elif trick == [2]:
                        ran = random.randint(50, 100)
                        hach += '\n\U0001F919 ' + names[name2] + ' кинув суперника млином!\n\U0001F54A +' + \
                                str(ran) + '\n'
                        spirit(ran, uid2, c2, fi=False)
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

        spirit(bonus, uid2, c2, fi=True)
        spirit(-bonus, uid1, c1, fi=True)
        r.hincrby(uid2, 'wins', 1)

        hack = ''
        if c1 == 8 or c1 == 18 or c1 == 28:
            hack2 = random.choices([0, 1], weights=[82, 18])
            if weapon1 == 18:
                hack2 = random.choices([0, 1], weights=[1, 99])
                hack = '\n\n\U0001F5E1 ' + names[name1] + ' використав експлойт...'
                r.hincrby(uid1, 's_weapon', -1)
                if int(r.hget(uid1, 's_weapon')) <= 0:
                    r.hset(uid1, 'weapon', 0)
            if hack2 == [1]:
                spirit(bonus * 2, uid1, c1, fi=False)
                spirit(-bonus, uid2, c2, fi=False)
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
            meat += '\n' + names[name2] + ' бахнув горілочки. ' + '\U0001F54A ' + vodka(uid2, 5)
        win_info = str('\n\n\U0001F3C6 ' + str(un2) + ' перемагає ' + str(un1) + '! ' + str(grn) +
                       '\nЙого русак отримує +' + str(bonus) + ' бойового духу, а русак опонента стільки ж втрачає.' +
                       hach + worker + meat + cop + pag + fsb + hack)
        return info + win_info


def tournament(uid1, uid2, un1, un2, mid):
    info, line, wins1, wins2 = '', '', 0, 0
    for loop in range(5):
        weapon, defense = '', ''
        if loop / 2 != 0:
            uid = uid1
            uid1 = uid2
            uid2 = uid
        stats1 = r.hmget(uid1, 'name', 'class', 'weapon', 'defense')
        stats2 = r.hmget(uid2, 'name', 'class', 'weapon', 'defense')
        name1, name2 = int(stats1[0]), int(stats2[0])
        c1, c2 = int(stats1[1]), int(stats2[1])
        weapon1, weapon2 = int(stats1[2]), int(stats2[2])
        defense1, defense2 = int(stats1[3]), int(stats2[3])

        hach1, hach2, meat, inj1, inj2 = 0, 0, '', '', ''
        if c1 == 1 or c1 == 11 or c1 == 21:
            if weapon2 == 0:
                hach1 = 1
        if c2 == 1 or c2 == 11 or c2 == 21:
            if weapon1 == 0:
                hach2 = 1

        if c1 == 26:
            if c2 != 6 and c2 != 16 and c2 != 26:
                if weapon2 != 0:
                    cop1 = random.choices([1, 0], weights=[20, 80])
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
        if c2 == 26:
            if c1 != 6 and c1 != 16 and c1 != 26:
                if weapon1 != 0:
                    cop2 = random.choices([1, 0], weights=[20, 80])
                    if cop2 == [1]:
                        if defense1 == 15 or defense1 == 17:
                            r.hset(uid1, 'weapon', 0)
                            r.hset(uid1, 'defense', 0)
                            r.hset(uid1, 's_weapon', 0)
                            r.hset(uid1, 's_defense', 0)
                        else:
                            r.hset(uid1, 'defense', 0)
                            r.hset(uid1, 's_defense', 0)
                        if defense1 == 0:
                            r.hset(uid2, 'defense', 16)
                            r.hset(uid2, 's_defense', 10)
                        elif defense1 == 16:
                            r.hincrby(uid2, 's_defense', 10)

        if weapon2 == 1 and int(r.hget(uid1, 'spirit')) >= 300:
            foc = 1
            if c1 == 3 or c1 == 13 or c1 == 23:
                foc = random.choice([0, 0, 0, 0, 1])
            if foc == 1:
                if int(r.hget(uid1, 'spirit')) <= 1000:
                    r.hset(uid1, 'spirit', 0)
                elif 1000 < int(r.hget(uid1, 'spirit')) < 2500:
                    r.hincrby(uid1, 'spirit', -1000)
                else:
                    chance = random.choice([2.5, 3.333, 5])
                    r.hincrby(uid1, 'spirit', -int(int(r.hget(uid1, 'spirit')) / chance))
                r.hset(uid2, 'weapon', 0)
                weapon = ' \U0001F5E1'
            else:
                weapon = ' \U0001F52E'

        if weapon2 == 4 and int(r.hget(uid1, 'spirit')) >= 300:
            if int(r.hget(uid1, 'spirit')) <= 1000:
                r.hset(uid1, 'spirit', 0)
            elif 1000 < int(r.hget(uid1, 'spirit')) < 2500:
                r.hincrby(uid1, 'spirit', -1000)
            else:
                chance = random.choice([2.5, 3.333, 5])
                r.hincrby(uid1, 'spirit', -int(int(r.hget(uid1, 'spirit')) / chance))
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)
            weapon = ' \U0001F5E1\U0001F5FF'

        if defense1 == 1 and int(r.hget(uid2, 'spirit')) >= 300:
            if int(r.hget(uid2, 'spirit')) <= 1000:
                r.hset(uid2, 'spirit', 0)
            elif 1000 < int(r.hget(uid2, 'spirit')) < 2500:
                r.hincrby(uid2, 'spirit', -1000)
            else:
                chance = random.choice([2.5, 3.333, 5])
                r.hincrby(uid2, 'spirit', -int(int(r.hget(uid2, 'spirit')) / chance))
            r.hset(uid1, 'defense', 0)
            defense = ' \U0001F6E1'

        stats11 = r.hmget(uid1, 'strength', 'intellect', 'spirit')
        stats22 = r.hmget(uid2, 'strength', 'intellect', 'spirit')
        s1 = int(stats11[0])
        s2 = int(stats22[0])
        i1 = int(stats11[1])
        i2 = int(stats22[1])
        bd1 = int(stats11[2])
        bd2 = int(stats22[2])

        if int(r.hget(uid1, 'injure')) > 0:
            s1, s11, i1, bd1 = injure(uid1, False)
            inj1 = '\U0001fa78 '
        if int(r.hget(uid2, 'injure')) > 0:
            s2, s22, i2, bd2 = injure(uid2, False)
            inj2 = '\U0001fa78 '

        if weapon2 == 11:
            s1 = int(s1 / 2)
            weapon = ' \U0001F5E1'
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)
        elif weapon2 == 12:
            s2 = int(s2 * 1.1)
            i2 = int(i2 * 1.1)
            bd2 = int(bd2 * 1.1)
            weapon = ' \U0001F5E1'
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
            weapon = ' \U0001F5E1'
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)
        elif weapon2 == 15:
            s2 = int(s2 * 1.75)
            weapon = ' \U0001F5E1'
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)
                r.hset(uid2, 'defense', 0)
            ran = random.choices([1, 2], weights=[98, 2])
            if ran == [2]:
                weapon = weapon + ' \u2620\uFE0F'
                r.hset(uid2, 'spirit', 0)
                r.hset(uid2, 'weapon', 0)
                r.hset(uid2, 'defense', 0)
                r.hincrby(uid2, 'injure', 100)
                if c2 == 25 and int(r.hget(uid2, 'strength')) >= 300:
                    meat = ' \u2620\uFE0F'
                    r.hset(uid1, 'spirit', 0)
                    if c1 != 6 and c1 != 16 and c1 != 26:
                        r.hset(uid1, 'weapon', 0)
                    r.hset(uid1, 'defense', 0)
                    r.hincrby(uid1, 'injure', 100)
        elif defense2 == 16:
            s1 = int(s1 * 0.8)
            weapon = ' \U0001F5E1'
            r.hincrby(uid2, 's_defense', -1)
            if int(r.hget(uid2, 's_defense')) <= 0:
                r.hset(uid2, 'defense', 0)
        elif weapon2 == 17:
            bd2 = 10000
            weapon = ' \U0001F5E1'
            r.hincrby(uid2, 's_weapon', -1)
            if int(r.hget(uid2, 's_weapon')) <= 0:
                r.hset(uid2, 'weapon', 0)
                r.hset(uid2, 'defense', 0)

        if defense1 == 9:
            s1 = int(s1 * 1.3)
            defense = ' \U0001F6E1'
            r.hincrby(uid1, 's_defense', -1)
            if int(r.hget(uid1, 's_defense')) <= 0:
                r.hset(uid1, 'defense', 0)
                r.hincrby(uid1, 'money', 4)
        elif weapon1 == 15:
            s1 = int(s1 * 1.75)
            defense = ' \U0001F5E1'
            r.hincrby(uid1, 's_weapon', -1)
            if int(r.hget(uid1, 's_weapon')) <= 0:
                r.hset(uid1, 'weapon', 0)
                r.hset(uid1, 'defense', 0)
            ran = random.choices([1, 2], weights=[98, 2])
            if ran == [2]:
                defense = defense + ' \u2620\uFE0F'
                r.hset(uid1, 'spirit', 0)
                r.hset(uid1, 'weapon', 0)
                r.hset(uid1, 'defense', 0)
                r.hincrby(uid1, 'injure', 100)
                if c1 == 25 and int(r.hget(uid1, 'strength')) >= 300:
                    meat = ' \u2620\uFE0F'
                    r.hset(uid2, 'spirit', 0)
                    if c2 != 6 and c2 != 16 and c2 != 26:
                        r.hset(uid2, 'weapon', 0)
                    r.hset(uid2, 'defense', 0)
                    r.hincrby(uid2, 'injure', 100)
        elif defense1 == 16:
            s2 = int(s2 * 0.8)
            defense = ' \U0001F6E1'
            r.hincrby(uid1, 's_defense', -1)
            if int(r.hget(uid1, 's_defense')) <= 0:
                r.hset(uid1, 'defense', 0)
        elif weapon1 == 17:
            bd1 = 10000
            defense = ' \U0001F6E1'
            r.hincrby(uid1, 's_weapon', -1)
            if int(r.hget(uid1, 's_weapon')) <= 0:
                r.hset(uid1, 'weapon', 0)
                r.hset(uid1, 'defense', 0)
        elif defense1 == 2:
            s2 = int(s2 * 0.25)
            defense = ' \U0001F6E1'
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
            spirit(30, uid1, c1, fi=True)
        elif hach1 == 0:
            if c1 == 1 or c1 == 11 or c1 == 21:
                s1 = int(s1 * 0.9)
        if hach2 == 1:
            s2 = int(s2 * 1.1)
            spirit(30, uid2, c2, fi=True)
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
                shot = random.choices([1, 0], weights=[10, 90])
                if shot == [1]:
                    ran = random.randint(5, 10)
                    meat += '\U0001fa96'
                    r.hincrby(uid1, 'injure', 1)
                    r.hincrby(uid2, 'injure', ran)
        if c2 == 15 or c2 == 25:
            ch = int(r.hget(uid2, 'childs'))
            if ch > 20:
                ch = 20
            s2 = int(s2 * (1 + 0.025 * ch))
            if c2 == 25 and int(r.hget(uid2, 'strength')) >= 300 and int(r.hget(uid1, 'strength')) >= 30:
                shot = random.choices([1, 0], weights=[10, 90])
                if shot == [1]:
                    ran = random.randint(5, 10)
                    meat += ' \U0001fa96'
                    r.hincrby(uid2, 'injure', 1)
                    r.hincrby(uid1, 'injure', ran)

        chance1 = s1 * (1 + 0.1 * i1) * (1 + 0.01 * (bd1 * 0.01))
        chance2 = s2 * (1 + 0.1 * i2) * (1 + 0.01 * (bd2 * 0.01))

        chance11 = chance1 / ((chance1 + chance2) / 100)
        chance22 = chance2 / ((chance1 + chance2) / 100)

        if chance11 > 95:
            win = random.choices(['1', '2'], weights=[95, 5])
        elif chance22 > 95:
            win = random.choices(['1', '2'], weights=[5, 95])
        elif c2 == 7 and chance1 > 80:
            win = random.choices(['1', '2'], weights=[80, 20])
        elif c1 == 7 and chance2 > 80:
            win = random.choices(['1', '2'], weights=[20, 80])
        else:
            win = random.choices(['1', '2'], weights=[chance1, chance2])

        if loop == 0:
            if int(r.hget(uid1, 'injure')) > 0:
                injure(uid1, True)
            if int(r.hget(uid2, 'injure')) > 0:
                injure(uid2, True)
            info = str(un1 + ' vs ' + un2 + '\n\n\U0001F3F7 ' + inj1 + names[name1] + ' ' + icons[c1] +
                       ' | ' + inj2 + names[name2] + ' ' + icons[c2] +
                       '\n\U0001F4AA ' + stats11[0].decode() + ' | ' + stats22[0].decode() +
                       '\n\U0001F9E0 ' + stats11[1].decode() + ' | ' + stats22[1].decode() +
                       '\n\U0001F54A ' + stats11[2].decode() + ' | ' + stats22[2].decode() + '\n\n')
        if win == ['1']:
            line = str(line + str(loop + 1) + '. ' + '\U0001F3C6 ' + names[name1] + ' ' + weapon +
                       meat + ' | ' + names[name2] + ' ' + defense + meat + '\n')
            if loop % 2 == 0:
                wins1 += 1
            else:
                wins2 += 1
        if win == ['2']:
            line = str(line + str(loop + 1) + '. ' + names[name1] + ' ' + weapon + meat + ' | ' +
                       '\U0001F3C6 ' + names[name2] + ' ' + defense + meat + '\n')
            if loop % 2 == 0:
                wins2 += 1
            else:
                wins1 += 1

        bot.edit_message_text(text=info + line, inline_message_id=mid)
        time.sleep(3)
        if loop == 4:
            if wins1 > wins2:
                win_info = '\n\U0001F3C6 ' + str(un1) + ' перемагає ' + str(un2) + ' в турнірному бою!'
            else:
                win_info = '\n\U0001F3C6 ' + str(un2) + ' перемагає ' + str(un1) + ' в турнірному бою!'
            bot.edit_message_text(text=info + line + win_info, inline_message_id=mid)


def get_rusak():
    name = random.randrange(0, len(names))
    strength = random.randint(10, 50)
    mind = int(random.choice(['1', '1', '1', '1', '2']))
    return name, strength, mind


def feed_rusak(uid):
    success = int(random.choice(['1', '1', '1', '1', '0']))
    strength = random.randint(1, 30)
    mind = 0
    if int(r.hget(uid, 'intellect')) < 20:
        mind = int(random.choice(['1', '0', '0', '0', '0']))
    bd = int(random.choice(['1', '0', '0']))
    return success, strength, mind, bd


def mine_salt(s2):
    success = int(random.choice(['1', '1', '1', '1', '0']))
    money = 5
    if s2 == 1:
        money = random.randint(3, 8)
    elif s2 == 2:
        money = random.randint(4, 9)
    elif s2 >= 3:
        money = random.randint(5, 10)
    mind = int(random.choice(['1', '0', '0', '0', '0', '0', '0', '0', '0', '0']))
    if s2 >= 4:
        mind = int(random.choice(['1', '0', '0', '0', '0']))
    return success, money, mind


def top(sett):
    try:
        everyone = r.smembers(sett)
        rating = {}
        for member in everyone:
            if sett != 111:
                try:
                    if bot.get_chat_member(sett, int(member)).status == 'left':
                        r.srem(sett, int(member))
                        continue
                except:
                    r.srem(sett, int(member))
            try:
                stats = r.hmget(member, 'strength', 'intellect', 'wins', 'deaths', 'childs', 'trophy',
                                'class', 'username')
                s = int(stats[0])
                i = int(stats[1])
                w = int(stats[2])
                d = int(stats[3])
                c = int(stats[4])
                t = int(stats[5])
                cl = int(stats[6])
                line = stats[7].decode() + ' ' + icons[cl] + '\n\U0001F4AA ' + str(s) + \
                                           ' \U0001F9E0 ' + str(i) + ' \u2620\uFE0F ' + str(d) + \
                                           ' \U0001F476 ' + str(c) + '\n\U0001F3C6 ' + str(w) + \
                                           ' \U0001F3C5 ' + str(t) + '\n'
                rate = s + i * 10 + w + t * 20 + d * 30 + c * 88
                rating.update({line: rate})
            except:
                continue
        s_rating = sorted(rating, key=rating.get, reverse=True)
        result = ''
        place = 1
        for n in s_rating:
            place1 = str(place) + '. '
            result += place1 + n
            place += 1
            if place == 11:
                break
        if sett == 111:
            return 'Глобальний рейтинг власників русаків \n\n' + result
        else:
            return 'Чатовий рейтинг власників русаків \n\n' + result

    except:
        return 'Недостатньо інформації для створення рейтингу.'


def itop(uid, cid, chat):
    try:
        result = ''
        if chat == 'supergroup':
            everyone = r.smembers(cid)
            rating = {}
            for member in everyone:
                try:
                    stats = r.hmget(member, 'strength', 'intellect', 'wins', 'deaths', 'childs', 'trophy',  'username')
                    s = int(stats[0])
                    i = int(stats[1])
                    w = int(stats[2])
                    d = int(stats[3])
                    c = int(stats[4])
                    t = int(stats[5])
                    line = stats[6].decode()
                    rate = s + i * 10 + w + t * 20 + d * 30 + c * 88
                    rating.update({line: rate})
                except:
                    continue
            s_rating = sorted(rating, key=rating.get, reverse=True)
            place = 1
            for n in s_rating:
                place1 = str(place) + '. '
                place += 1
                if r.hget(uid, 'username').decode() == n:
                    result = '\U0001F3C6 Твоє місце в чатовому рейтингу: \n' + place1 + n + '\n'
                    break
        everyone = r.smembers(111)
        rating = {}
        for member in everyone:
            try:
                stats = r.hmget(member, 'strength', 'intellect', 'wins', 'deaths', 'childs', 'trophy', 'username')
                s = int(stats[0])
                i = int(stats[1])
                w = int(stats[2])
                d = int(stats[3])
                c = int(stats[4])
                t = int(stats[5])
                line = stats[6].decode()
                rate = s + i * 10 + w + t * 20 + d * 30 + c * 88
                rating.update({line: rate})
            except:
                continue
        s_rating = sorted(rating, key=rating.get, reverse=True)
        place = 1
        for n in s_rating:
            place1 = str(place) + '. '
            place += 1
            if r.hget(uid, 'username').decode() == n:
                result += '\U0001F3C6 Твоє місце в глобальному рейтингу: \n' + place1 + n
                break
        return result
    except:
        return 'Недостатньо інформації для створення рейтингу.'


def ctop(sett):
    try:
        everyone = r.hkeys(sett)
        rating = {}
        for member in everyone:
            try:
                title = r.hget('war_battle' + member.decode(), 'title').decode()
                if '@' in title:
                    continue
                stats = int(r.hget(222, member))
                line = title + '\n\U0001F3C5 ' + str(stats) + '\n'
                rating.update({line: stats})
            except:
                continue
        s_rating = sorted(rating, key=rating.get, reverse=True)
        result = ''
        place = 1
        for n in s_rating:
            place1 = str(place) + '. '
            result += place1 + n
            place += 1
            if place == 11:
                break
        return 'Рейтинг найсильніших банд русаків\n\n' + result

    except:
        return 'Недостатньо інформації для створення рейтингу.'


def goods():
    markup = types.InlineKeyboardMarkup()
    items = {'Горілка "Козаки" - 2 грн': 'vodka', 'Колючий дрин - 7 грн': 'weapon', 'Колючий щит - 8 грн': 'defense',
             'Трофейний паспорт - 10 грн': 'passport', 'Утеплена будка - 30 грн': 'cabin',
             'Жінка - 150 грн': 'woman', 'Тютюн та люлька - 1 жінка': 'pipe'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def donate_goods():
    markup = types.InlineKeyboardMarkup()
    items = {'TF2_heavy - 1 погон': 'tf2', 'Слов`янин Рікардо - 1 погон': 'ricardo',
             'Преміум-фото класу - 1 погон': 'premium', '40 пакунків - 1 погон': '40_packs',
             'Настоянка глоду - 1 погон': 'glid', 'Курс перекваліфікації - 2 погони': 'course',
             'Велике будівництво - 3 погони': 'fast_cellar'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def merchant_goods():
    markup = types.InlineKeyboardMarkup()
    items = {'Купити уламок бронетехніки': 'fragment', 'Купити мухомор': 'mushroom',
             'Купити спорядження свого класу': 'equipment'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def skill_set():
    markup = types.InlineKeyboardMarkup()
    items = {'Прокачати алкоголізм': 'alcohol', 'Прокачати майстерність': 'master',
             'Продовжити будівництво': 'cellar'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def battle_button():
    markup = types.InlineKeyboardMarkup()
    items = {'Відправити русака на бій': 'join'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def battle_button_2():
    markup = types.InlineKeyboardMarkup()
    items = {'Відправити русака на бій': 'join', 'Почати битву': 'start_battle'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def battle_button_3():
    markup = types.InlineKeyboardMarkup()
    items = {'Відправити русака на міжчатовий бій': 'war_join'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def invent():
    markup = types.InlineKeyboardMarkup()
    items = {'Викинути зброю': 'drop_w', 'Викинути захист': 'drop_d'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def unpack():
    markup = types.InlineKeyboardMarkup()
    items = {'Так': 'unpack'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def boost():
    markup = types.InlineKeyboardMarkup()
    items = {'Отримати подарунок': 'boost'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def spirit(value, uid, c, fi):
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


def vodka(uid, cl):
    ran = random.randint(10, 70)
    increase = ran * int(r.hget(uid, 's1'))
    spirit(increase, uid, cl, fi=False)
    r.hincrby(uid, 'vodka', 1)
    return str(increase)


def intellect(value, uid):
    if value > 0:
        r.hincrby(uid, 'intellect', value)
        if int(r.hget(uid, 'intellect')) >= 21:
            r.hset(uid, 'intellect', 20)
    if value < 0:
        r.hincrby(uid, 'intellect', value)
        if int(r.hget(uid, 'intellect')) <= 0:
            r.hset(uid, 'intellect', 1)


def injure(uid, fi):
    stats = r.hmget(uid, 'strength', 'intellect', 'spirit')
    if fi:
        r.hincrby(uid, 'injure', -1)
    return int(int(stats[0])*(1/3)), int(int(stats[0])*(1/3)), int(int(stats[1])*(1/3)), int(int(stats[2])*(1/3))


def pastLife():
    life = ['Звичайний совковий роботяга', 'Видатний письменник', 'Лауреат Нобелівської премії',
            'Кріпак з Черкащини', 'Англійський аристократ', 'Хитрий жид', 'Запорізький козак',
            'Житель Зеленого Клину', 'Кубанський козак', 'А ніким і не був, це твоє перше життя',
            'Мер Харкова', 'Польська курва', 'Раб з Африки', 'Boss of gym', 'Dungeon master',
            'Динозавр', 'Штурмбанфюрер', 'Донощик', 'Грязний циган', 'Депутат', 'Кримський хан',
            'Московський холоп', 'НКВСник', 'Партизан з УПА', "Слов`янський ремісник", 'Дівчина чорноброва',
            'Карпатський гуцул', 'Монгольський кінний лучник', 'Інквізитор', 'Викладач політеху',
            'Дитя Донбасу', 'Руський боярин', 'Собака', 'Кіт', 'Козак-характерник', 'Німецький єврей',
            'Робот з Boston Dynamics', 'Канадський українець', "Дощовий черв`як звичайний", 'Космонавт',
            'Пірат', 'Французька дворянка', 'Повія з Санкт-Петербурга', 'Американський агент',
            'Розбійник', 'Серійний вбивця', 'Безхатько', 'Сольовий торчок']
    ran = random.choice(life)
    return ran


def earnings():
    country = ['\ud83c\uddfa\ud83c\udde6 Україна', '\ud83c\uddf5\ud83c\uddf1 Польща',
               '\ud83c\uddf7\ud83c\uddfa Росія (ганьба)', '\ud83c\udde8\ud83c\uddff Чехія',
               '\ud83c\udded\ud83c\uddfa Угорщина', '\ud83c\udde9\ud83c\uddea Німеччина',
               '\ud83c\uddf3\ud83c\uddf4 Норвегія', '\ud83c\udde9\ud83c\uddf0 Данія',
               '\ud83c\uddfa\ud83c\uddf8 США', '\ud83c\udde8\ud83c\udde6 Канада',
               '\ud83c\uddf2\ud83c\uddfd Мексика', '\ud83c\uddeb\ud83c\uddf7 Франція',
               '\ud83c\udde7\ud83c\uddea Бельгія', '\ud83c\uddf3\ud83c\uddf1 Нідерланди',
               '\ud83c\uddef\ud83c\uddf5 Японія', '\ud83c\uddf9\ud83c\udded Таїланд',
               '\ud83c\uddf2\ud83c\udde9 Молдова', '\ud83c\udde8\ud83c\udded Швейцарія',
               '\ud83c\uddee\ud83c\uddf9 Італія', '\ud83c\uddf3\ud83c\uddec Нігерія',
               '\ud83c\uddf9\ud83c\uddf7 Туреччина', '\ud83c\uddec\ud83c\uddea Грузія',
               '\ud83c\uddee\ud83c\uddea Ірландія', '\ud83c\uddea\ud83c\uddf8 Іспанія',
               '\ud83c\udde8\ud83c\uddf3 Китай', '\ud83c\uddee\ud83c\uddf3 Індія',
               '\ud83c\udde7\ud83c\uddf7 Бразилія', '\ud83c\udde6\ud83c\uddfa Австралія',
               '\ud83c\uddec\ud83c\udde7 Великобританія', '\ud83c\udde6\ud83c\uddf7 Аргентина',
               '\ud83c\udde6\ud83c\uddea ОАЕ', '\ud83c\uddf3\ud83c\uddff Нова Зеландія']
    ran = random.choice(country)
    return ran


def political():
    a1 = random.choice(['Економічно праві - ', 'Економічно ліві - '])
    a2 = random.choice(['Авторитаризм - ', 'Лібертаріанство - '])
    ran = a1 + str(random.randint(0, 100)) + '%\n' + a2 + str(random.randint(0, 100)) + '%'
    return ran


def question():
    q = (['\ud83d\udfe9 Так \ud83d\udfe9', '\ud83d\udfe5 Ні \ud83d\udfe5', '\ud83d\udfeb Не скажу \ud83d\udfeb',
          '\u2b1b\ufe0f Неможливо передбачити \u2b1b\ufe0f', '\ud83d\udfe6 100% \ud83d\udfe6',
          '\u2b1c\ufe0f Ніколи \u2b1c\ufe0f', '\ud83d\udfea Скорше так, ніж ні \ud83d\udfea',
          '\ud83d\udfe7 Скорше ні, ніж так \ud83d\udfe7', '\ud83d\udfe8 Слава Україні! \ud83d\udfe6'
          ])
    ran = '-----|' + random.choice(q) + '|-----'
    return ran


def love():
    i = random.randint(0, 100)
    s = random.choice(['\ud83c\udff3\u200d\ud83c\udf08', '\ud83d\udc9a', '\ud83d\udc9c', '\u2764\ufe0f',
                       '\ud83d\udc9e', '\ud83d\udc96', '\ud83d\udc98', '\ud83d\udc85'])
    ran = str(s) + ' ' + str(i) + '% ' + str(s)
    return ran


def zradoMoga():
    ran = random.choice(['\ud83c\uddfa\ud83c\udde6 Перемога \ud83c\uddfa\ud83c\udde6',
                         '\u2721 Зрада \ud83c\uddf7\ud83c\uddfa', '\u23f3 Боротьба триває',
                         '\ud83c\uddfa\ud83c\udde6 Перемога \ud83c\uddfa\ud83c\udde6',
                         '\u2721 Зрада \ud83c\uddf7\ud83c\uddfa'])
    return ran


def penis():
    normal = f'Твій пісюн - {random.uniform(5.0, 16.0):.2f} см'
    small = f'Твій мініган - {random.uniform(0.0, 5.0):.2f} см'
    big = f'Твій моцний гилун - {random.uniform(16.0, 40):.2f} см'
    rare = random.choice(['Найбільший член в чаті', 'Найменший член в чаті'])
    vg = 'В тебе немає пісюна \ud83c\udf1a'
    decor = random.choice(['\ud83c\udf46 ', '\ud83e\udd55 ', '\ud83d\udc46 ',
                           '\ud83d\udc4c ', '\ud83c\udf36 ', '\u2642\ufe0f '])
    ran = decor + random.choice([normal, normal, normal, normal, small, small, big, big, rare, vg])
    return ran


def choose(q):
    s = random.choice(['\ud83c\udfb0 ', '\ud83d\udc49 ', '\u270d ', '\ud83c\udf9b ',
                       '\ud83d\udcdf ', '\u2696 ', '\ud83d\udcca ', '\u21aa\ufe0f '])
    q = q.replace(' чи ', '2a2b').replace(' або ', '2a2b').replace('?', '')
    q = q.replace(' ', '1a2b')
    q = q.replace('2a2b', ' ').split()
    end = []
    for i in q:
        i = i.replace('1a2b', ' ').strip()
        end.append(i)
    ran = s + random.choice(end)
    return ran


def beer():
    beer1 = '\ud83c\udf7a ' + random.choice(['Львівське різдвяне', 'Bud', 'Львівське 1715', 'Carlsberg',
                                             'Kronenbourg Blanc', 'Staropramen', 'Чернігівське', 'Оболонь',
                                             'Stella Artois', 'Tuborg', 'Corona Extra', 'Krušovice',
                                             'Старий Мельник', 'Velkopopovicky Kozel', 'Heineken', 'Faxe',
                                             'Опілля Корифей', 'Опілля Княже', 'Закарпатське', 'Арсенал',
                                             'Kalusher', 'Kaluskie Exportove', 'Правда', 'Балтика', 'Zeman',
                                             'Проскурівське', 'Zibert',
                                             'Тетерів', 'Вишневий Тетерів'])
    not_beer = random.choice(['\ud83d\udeab Сьогодні не пити', '\ud83c\udf7b Сходити в паб',
                              '\ud83e\udd5b Випити молока', '\ud83d\udcaf Бахнути горілочки',
                              '\ud83c\udf77 Випити холодного вина', '\ud83d\udc92 Піти на пивзавод',
                              '\u2620 Годі бухати, заїбав, здохнеш так скоро к хуям собачим'
                              ])
    ran = random.choice([beer1, beer1, beer1, beer1, not_beer])
    return ran


def generator(q):
    error = 'Неправильний запит\n[x] - число від 0 до x\n[x] [y] - число від x до y' \
            '\n[x] [y] [n<=10] - n випадкових чисел від x до y'
    try:
        numbers = q.split()
        if len(numbers) == 0:
            ran = '\ud83c\udfb2 Випадкове число від 1 до 100' + '\n\n' + str(random.randrange(1, 101))
            return ran
        elif len(numbers) == 1:
            number = int(q) + 1
            ran = '\ud83c\udfb2 Випадкове число від 1 до ' + str(q) + '\n\n' + str(random.randrange(1, number))
            return ran
        elif len(numbers) == 2:
            first = int(numbers[0])
            second = int(numbers[1]) + 1
            if first < second - 1:
                ran = '\ud83c\udfb3 Випадкове число від ' + str(first) + ' до ' + str(second - 1) \
                      + '\n\n' + str(random.randrange(first, second))
                return ran
            else:
                return error
        elif len(numbers) == 3:
            first = int(numbers[0])
            second = int(numbers[1]) + 1
            third = int(numbers[2])
            if first < second - 1 and third <= 10:
                ran = '\ud83c\udfb0 Випадкові числа від ' + str(first) + ' до ' + str(second - 1) + '\n\n'
                for i in range(third):
                    a = random.randrange(first, second)
                    ran += str(a) + '\n'
                return ran
            else:
                return error
        else:
            return error
    except:
        return error


def race():
    races = ["Східний слов'янин", "Західний слов'янин", "Південний слов'янин", "Балтієць",
             'Кельт', 'Германець', 'Скандинав', 'Британець', 'Вірмен',
             'Циган', 'Італієць', 'Іспанець', 'Француз', 'Грек',
             'Албанець', 'Фіно-угорець', 'Мокша', 'Тюрк', 'Татар',
             'Кавказець', 'Індієць', 'Іранець', 'Монгол', 'Кореєць',
             'Японець', 'Китаєць', 'Сибіряк', 'Індонезієць', 'Семіт',
             'Негроїд', 'Австралоїд', 'Корінний американець']
    choice1 = ['Арієць', 'Українець', 'Єврей', 'Циган', 'Кельт', 'Германець', 'Негроїд',
               'Скандинав', 'Британець', 'Італієць', 'Іспанець', 'Француз', 'Грек']
    variant = random.choice([1, 2, 2, 3, 3, 3, 3, 4, 5])
    ran = ''

    if variant == 1:
        ran = '100% - ' + random.choice(choice1)
    elif variant > 1:
        try:
            n = 90
            percents = []
            for i in range(variant):
                if i == variant - 1:
                    percent = 100 - sum(percents)
                    percents.append(percent)
                else:
                    percent = random.randrange(1, n)
                    percents.append(percent)
                    n = n - percent
            percents.sort(reverse=True)
            random_values = random.sample(races, k=variant)
            for i in range(variant):
                ran = ran + str(percents[i]) + '% - ' + random_values[i] + '\n'
        except:
            ran = '100% - ' + random.choice(choice1)

    return ran


def gender():
    emoji = ['\ud83d\uddff', '\u267f\ufe0f', '\ud83e\udd78', '\ud83d\udc68\u200d\ud83c\udfa4', '\ud83e\udddc',
             '\ud83e\uddd1\u200d\ud83c\udfa4', '\ud83d\udc69\u200d\ud83c\udfa4', '\ud83e\udd77', '\ud83e\udd9e',
             '\ud83e\uddd9\u200d\u2640', '\ud83e\uddda', '\ud83e\udeb5', '\u26c4\ufe0f', '\u2708\ufe0f', '\ud83d\udef0',
             '\ud83d\ude81', '\ud83d\udef8', '\u26a7']
    genders = ['Протитанковий ракетний комплекс FGM-148 Javelin', 'ПТКР BGM-71 TOW', 'Самозарядний пістолет Форт-14',
               'Пістолет Desert Eagle', 'Пістолет-кулемет STEN', 'Автомат Калашникова модернізований', 'Кулемет M240',
               'Пістолетний унітарний патрон 9×19 мм Парабелум', 'Кулемет КМ-7,62', 'Самозарядна гвинтівка Gewehr 41',
               'Багатоцільовий вертольіт PZL W-3 Sokół', 'Багатоцільовий гелікоптер ВМ-4 «Джміль»', 'Кулемет MG-42',
               'Пістолет-кулемет Heckler & Koch MP5', 'Пістолет Walther P38', 'Болтова гвинтівка Vz.24/G24(t)',
               'Пістолет-кулемет MP-40', 'Гвинтівка Mauser 98k', 'Автомат Вулкан-М', 'ПТРК Скіф', 'Пістолет Mauser C96',
               '40-мм ручний протитанковий гранатомет РПГ-7', 'Автомат Ґаліль', 'Карабін мисливський Зброяр Z-10 ',
               'Снайперська гвинтівка Stealth Recon Scout', 'Автоматичний гранатомет УАГ-40', 'Гвинтівка FG-42',
               'Великокаліберна снайперська гвинтівка  Barrett M82', 'Багатоцільовий вертольіт NHI NH90',
               'Підствольний гранатомет ГП-25 «Костьор»', 'Атомний підводний човен з балістичними ракетами',
               'Ударний вертоліт Мі-24ПУ1', 'Протитанкова рушниця Panzerbüchse 35(p)', 'Вогнемет Flammenwerfer 35',
               'Переносна протитанкова безвідкатна гармата Panzerfaust', 'Реактивний піхотний вогнемет РПВ «Джміль»',
               'Переносний зенітно-ракетний комплекс FIM-92 Stinger', 'Автомат FN SCAR', 'Автоматична гвинтівка M4',
               'Розвідувально-ударний вертоліт Boeing–Sikorsky RAH-66 Comanche', 'Автоматична гвинтівка M16',
               'Проміжний патрон для сучасних автоматичних гвинтівок 5,56×45 мм', 'Пістолет-кулемет Thompson M1',
               'Основний бойовий танк БМ Оплот', 'Основний бойовий танк Т-84', 'Бронетранспортер БТР-7',
               'Авіадесантний бронетранспортер БТР-Д', 'Бронеавтомобіль KrAZ-MPV Shrek One',
               'Безпілотний літальний апарат Bayraktar TB2', 'Патрульний катер типу «Айленд»',
               'Береговий ракетний комплекс РК-360МЦ «Нептун»', '152-мм самохідна гармата-гаубиця vz.77 «Дана»',
               'Легкий тактичний позадорожній бронеавтомобіль HMMWV', 'Багатоцільовий гелікоптер МСБ-2']
    ran = random.choice(emoji) + ' Я по гендеру... \n\n' + random.choice(genders)
    return ran


@bot.message_handler(commands=['start'])
def handle_start(message):
    if message.chat.type == 'private':
        bot.reply_to(message, "Почнемо.\n\nЗайди в який-небудь чат (наприклад цей), напиши @Random_UAbot, а далі думаю "
                              "все зрозумієш.\nДля деяких команд потрібно додати текст, бажано зі сенсом (логічно, так?"
                              ").\n\nЩоб взяти русака напиши команду \n/donbass\nДетальна інформація про русаків -"
                              "\nhttps://t.me/randomuanews/4.")


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "Зайди в який-небудь чат (наприклад цей), напиши @Random_UAbot, а далі думаю все зрозумієш.\n"
                          "Для деяких команд потрібно додати текст, бажано зі сенсом (логічно, так?).\n\n"
                          "Щоб взяти русака напиши команду \n/donbass\nВсі команди - /commands\nДетальна інформація про"
                          " русаків -\nhttps://t.me/randomuanews/4")


@bot.message_handler(commands=['links'])
def handle_links(message):
    bot.reply_to(message, "@soledar1 - місце, де збираються люди з усіх куточків України, "
                          "щоб похизуватись своїми бойовими русаками!\n"
                          "@randomuanews - новини, патчноути, опитування\n\n"
                          "@borykva - осередок цебулізму\n"
                          "@ukrnastup - осередок сучасного українського націоналізму\n"
                          "@golovkaothuya - крінж і шітпост, рекомендую\n@digital_anon - подкасти\n"
                          "@archive_st - брендові стікери\n"
                          "@vota_l - завдяки ньому ти натиснув цю кнопку")


@bot.message_handler(commands=['toggle_admin'])
def toggle_admin(message):
    if bot.get_chat_member(message.chat.id, message.from_user.id).status == 'creator' or \
            bot.get_chat_member(message.chat.id, message.from_user.id).can_change_info is True:
        if r.hexists('f' + str(message.chat.id), 'admin') == 0:
            r.hset('f' + str(message.chat.id), 'admin', 0)
        if int(r.hget('f' + str(message.chat.id), 'admin')) == 0:
            r.hset('f' + str(message.chat.id), 'admin', 1)
            bot.reply_to(message, 'Адмінські команди УВІМКНЕНО')
        else:
            r.hset('f' + str(message.chat.id), 'admin', 0)
            bot.reply_to(message, 'Адмінські команди ВИМКНЕНО')


@bot.message_handler(commands=['ban'])
def ban(message):
    try:
        if int(r.hget('f' + str(message.chat.id), 'admin')) == 1:
            if bot.get_chat_member(message.chat.id, message.from_user.id).status == 'creator' or \
                    bot.get_chat_member(message.chat.id, message.from_user.id).can_restrict_members is True:
                bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                bot.send_message(message.chat.id, message.reply_to_message.from_user.first_name + ' вигнаний з чату.')
    except:
        pass


@bot.message_handler(commands=['moxir'])
def moxir(message):
    try:
        if int(r.hget('f' + str(message.chat.id), 'admin')) == 1:
            if bot.get_chat_member(message.chat.id, message.from_user.id).status == 'creator' or \
                    bot.get_chat_member(message.chat.id, message.from_user.id).can_restrict_members is True:
                bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=True,
                                         can_send_media_messages=False, can_send_polls=False,
                                         can_send_other_messages=False)
                bot.send_message(message.chat.id, 'У ' + message.reply_to_message.from_user.first_name +
                                 ' забрали стікери і медіа.')
    except:
        pass


@bot.message_handler(commands=['donbass'])
def donbass(message):
    markup = types.InlineKeyboardMarkup()
    bot.reply_to(message, text='\U0001F3DA Ти приходиш на Донбас - чудове місце для полювання на русаків',
                 reply_markup=markup.add(types.InlineKeyboardButton(text='Знайти русака', callback_data='getrusak')))


@bot.message_handler(commands=['rusak'])
def my_rusak(message):
    try:
        cl, inj, ms = '', '', ''
        name = int(r.hget(message.from_user.id, 'name'))
        name = names[name]
        c = int(r.hget(message.from_user.id, 'class'))
        if c != 0:
            cl = '\n' + icons[c] + ' Клас: ' + class_name[c]
        try:
            r_photo = photos[int(r.hget(message.from_user.id, 'photo'))]
        except:
            r_photo = photos[0]
        stats = r.hmget(message.from_user.id, 'strength', 'intellect', 'spirit', 'injure', 'mushrooms')
        if int(stats[3]) > 0:
            inj = '\n\U0001fa78 Поранення: ' + stats[3].decode()
        if int(stats[4]) > 0:
            ms = '\n\U0001F344 Куплені мухомори: ' + stats[4].decode() + '/3'
        photo_text = '\U0001F412 Твій русак:\n\n\U0001F3F7 Ім`я: ' + name + \
                     '\n\U0001F4AA Сила: ' + stats[0].decode() + '\n\U0001F9E0 Інтелект: ' + stats[1].decode() + \
                     '\n\U0001F54A Бойовий дух: ' + stats[2].decode() + cl + ms + inj
        bot.send_photo(message.chat.id, photo=r_photo, caption=photo_text)
    except:
        bot.reply_to(message, '\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на /donbass')


@bot.message_handler(commands=['feed'])
def feed(message):
    try:
        try:
            r.hset(message.from_user.id, 'username', message.from_user.username)
            if message.chat.type != 'private':
                r.sadd(message.chat.id, message.from_user.id)
                r.sadd(111, message.from_user.id)
            if message.chat.type == 'supergroup':
                r.hset('f' + str(message.chat.id), 'title', message.chat.title)
        except:
            pass
        if not date.today().day == int(r.hget(message.from_user.id, 'time')):
            r.hset(message.from_user.id, 'time', date.today().day)
            fr = feed_rusak(message.from_user.id)
            r.hincrby(message.from_user.id, 'eat', 1)
            success = fr[0]
            cl = int(r.hget(message.from_user.id, 'class'))
            if cl == 2 or cl == 12 or cl == 22:
                success = 1
            if success == 1:
                try:
                    if int(r.hget(message.from_user.id, 'cabin')) == 1:
                        r.hincrby(message.from_user.id, 'strength', fr[1] + 15)
                        ran = fr[1] + 15
                    else:
                        r.hincrby(message.from_user.id, 'strength', fr[1])
                        ran = fr[1]
                except:
                    r.hincrby(message.from_user.id, 'strength', fr[1])
                    ran = fr[1]
                emoji = random.choice(['\U0001F35C', '\U0001F35D', '\U0001F35B', '\U0001F957', '\U0001F32D'])
                msg = emoji + ' Твій ' + names[int(r.hget(message.from_user.id, 'name'))] + \
                              ' смачно поїв.\n\nСила зросла на ' + str(ran) + '.\n'
                if fr[2] == 1:
                    msg += 'Інтелект збільшився на 1.\n'
                    intellect(1, message.from_user.id)
                if fr[3] == 1:
                    msg += 'Русак сьогодні в гарному настрої. Бойовий дух збільшився на 1000.'
                    spirit(1000, message.from_user.id, int(r.hget(message.from_user.id, 'class')), fi=False)
                    bot.send_photo(message.chat.id, photo='https://i.ibb.co/bK2LrSD/feed.jpg',
                                   caption=msg, reply_to_message_id=message.id)
                else:
                    bot.reply_to(message, msg)
            else:
                bot.reply_to(message, '\U0001F9A0 Твій русак сьогодні захворів. Сили від їжі не прибавилось.')
        elif date.today().day == int(r.hget(message.from_user.id, 'time')):
            bot.reply_to(message, 'Твій русак сьогодні їв, хватить з нього')
    except:
        bot.reply_to(message, '\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на /donbass')


@bot.message_handler(commands=['mine', 'minecraft'])
def mine(message):
    if message.chat.id == -1001211933154:
        try:
            if r.hexists(message.from_user.id, 'time1') == 0:
                r.hset(message.from_user.id, 'time1', 0)
            if not date.today().day == int(r.hget(message.from_user.id, 'time1')):
                ms = mine_salt(int(r.hget(message.from_user.id, 's2')))
                r.hset(message.from_user.id, 'time1', date.today().day)
                if message.text.startswith('/minecraft'):
                    if r.hexists(message.from_user.id, 'ac1') == 0:
                        r.hset(message.from_user.id, 'ac1', 1)
                success = ms[0]
                cl = int(r.hget(message.from_user.id, 'class'))
                if cl == 2 or cl == 12 or cl == 22:
                    success = random.choice([0, 0, 1, 1, 1])
                if success == 1:
                    money = ms[1]
                    if cl == 2 or cl == 12 or cl == 22:
                        money = money * 3
                    r.hincrby(message.from_user.id, 'money', money)
                    msg = '\u26CF Твій ' + names[int(r.hget(message.from_user.id, 'name'))] + \
                          ' успішно відпрацював зміну на соляній шахті.\n\n\U0001F4B5 ' \
                          'Зароблено гривень: ' + str(money) + '.'
                    if ms[2] == 1:
                        msg += '\nРусак сьогодні працював з новітніми технологіями.\n'
                        if int(r.hget(message.from_user.id, 'intellect')) < 20:
                            msg += '\U0001F9E0 +1'
                            intellect(1, message.from_user.id)
                        else:
                            msg += '\U0001F4B5 +20'
                            r.hincrby(message.from_user.id, 'money', 20)
                    bot.reply_to(message, msg)
                else:
                    if cl == 2 or cl == 12 or cl == 22:
                        msg = '\U0001F37A Твій роботяга втік з-під нагляду. Його знайшли п`яним біля шахти.\n\u2622 +5'
                        if cl == 12 or cl == 22:
                            msg = msg + ' \U0001F4B5 + 8'
                            r.hincrby(message.from_user.id, 'money', 8)
                        r.hincrby(message.from_user.id, 'vodka', 5)
                        bot.reply_to(message, msg)
                    else:
                        bot.reply_to(message, '\U0001F37A Твій русак втік з-під нагляду. Його знайшли п`яним біля шахти'
                                              '.\n\u2622 +1')
                        r.hincrby(message.from_user.id, 'vodka', 1)
                        if int(r.hget(message.from_user.id, 'class')) == 18 or \
                                int(r.hget(message.from_user.id, 'class')) == 28:
                            r.hset(message.from_user.id, 'time1', 0)
            elif date.today().day == int(r.hget(message.from_user.id, 'time1')):
                bot.reply_to(message, 'Твій русак сьогодні відпрацював зміну.')
        except:
            bot.reply_to(message, '\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на /donbass')


@bot.message_handler(commands=['sacrifice'])
def sacrifice(message):
    if r.hexists(message.from_user.id, 'time2') == 0:
        r.hset(message.from_user.id, 'time2', 0)

    if date.today().day != int(r.hget(message.from_user.id, 'time2')) \
            and r.hexists(message.from_user.id, 'strength') == 1 \
            and int(r.hget(message.from_user.id, 'strength')) != 0:
        markup = types.InlineKeyboardMarkup()
        bot.reply_to(message, text='Після смерті русака, у всіх русаків в цьому чаті (що можуть увійти в топ) впаде '
                                   'бойовий дух на 100. У нового русака буде стартове значення бойового духу рівним '
                                   'теперішній силі * 5.',
                     reply_markup=markup.add(types.InlineKeyboardButton(text='Принести в жертву русака',
                                                                        callback_data='sacrifice')))
    else:
        bot.reply_to(message, 'Робити пожертвування русаків можна раз в день, і якщо є живий русак.')


@bot.message_handler(commands=['fascist'])
def fascist(message):
    try:
        if message.chat.type != 'private' and len(r.smembers(message.chat.id)) >= 14:
            if r.hexists('f' + str(message.chat.id), 'time3') == 0:
                r.hset('f' + str(message.chat.id), 'time3', 0)
            if int(r.hget('f' + str(message.chat.id), 'time3')) != int(date.today().day):
                r.hset('f' + str(message.chat.id), 'time3', date.today().day)
                ran = []
                for member in r.smembers(message.chat.id):
                    mem = int(member)
                    try:
                        if bot.get_chat_member(message.chat.id, mem).status == 'left':
                            r.srem(message.chat.id, mem)
                        else:
                            ran.append(member)
                    except:
                        r.srem(message.chat.id, mem)
                ran = random.choice(ran)
                ran = int(ran)
                r.hset('f' + str(message.chat.id), 'username', r.hget(ran, 'username').decode())
                r.hincrby(ran, 'childs', 1)
                pin = bot.reply_to(message, '\U0001F468\U0001F3FB\u200D\u2708\uFE0F @' +
                                   r.hget('f' + str(message.chat.id), 'username').decode() +
                                   ' сьогодні займає посаду Фашист дня! Йому видано одне \U0001F476 російське немовля!')
                try:
                    try:
                        bot.unpin_chat_message(chat_id=pin.chat.id,
                                               message_id=int(r.hget('f' + str(message.chat.id), 'pin')))
                    except:
                        pass
                    bot.pin_chat_message(chat_id=pin.chat.id, message_id=pin.message_id, disable_notification=True)
                    r.hset('f' + str(message.chat.id), 'pin', pin.message_id)
                except:
                    pass

            else:
                bot.reply_to(message, '\U0001F468\U0001F3FB\u200D\u2708\uFE0F Сьогодні вже вибраний фашист дня - ' +
                             r.hget('f' + str(message.chat.id), 'username').decode())
        else:
            print(1 / 0)
    except:
        bot.reply_to(message, 'Фашиста дня можна обирати раз в добу і в чатах,'
                              ' де є від 14 власників русаків (з юзернеймами).')


@bot.message_handler(commands=['shop'])
def shop(message):
    if message.chat.type == 'private':
        if r.hexists(message.from_user.id, 'money') == 0:
            r.hset(message.from_user.id, 'money', 20)
        else:
            pass

        if r.hexists(message.from_user.id, 'childs') == 0:
            bot.reply_to(message, 'У тебе ще не було русаків.\n\nРусака можна отримати, сходивши на /donbass')
        else:
            bot.reply_to(message, text='\U0001F4B5 Гривні: ' + r.hget(message.from_user.id, 'money').decode() +
                                       '\n\nОсь опис товарів, які можна придбати:\n\n\u2622 '
                                       'Горілка "Козаки" - збільшує русаку бойовий дух на 10-70.\n\U0001F5E1 '
                                       'Колючий дрин [Атака]- зменшує перед боєм бойовий дух ворогу, якщо атакувати'
                                       ' його (не використовується, '
                                       'якщо бойовий дух ворога менший за 300, обнуляє, якщо від 300 до 1000, '
                                       'зменшує на 1000, якщо'
                                       ' від 1000 до 2500 і зменшує на 20/30/40%, якщо бойовий дух більше 2500).'
                                       '\n\U0001F6E1 Колючий '
                                       'щит [Захист] - працює так само як дрин, тільки знижує бойовий дух тому, '
                                       'хто атакує.'
                                       '\n\U0001F4B3 Трофейний паспорт - поміняє ім`я русака на інше, випадкове.'
                                       '\n\U0001F3DA '
                                       'Утеплена будка - 15 додаткової сили при кожному годуванні русака '
                                       '\n\U0001F469\U0001F3FB Жінка - раз в 9 днів народжуватиме смачне російське '
                                       'немовля. Жінку треба провідувати кожен день командою /woman\n\U0001F6AC Тютюн '
                                       'та люлька - '
                                       'на це можна проміняти жінку і піти в козацький похід (бойовий дух русака '
                                       'стане 1713, '
                                       'а кількість жертв збільшиться на 5)', reply_markup=goods())
    else:
        bot.reply_to(message, 'Цю команду необхідно писати в пп боту.')


@bot.message_handler(commands=['passport'])
def passport(message):
    if r.hexists(message.from_user.id, 'wins') == 1:
        stats = r.hmget(message.from_user.id, 'wins', 'trophy', 'deaths', 'childs', 'vodka', 'opened')
        sk = r.hmget(message.from_user.id, 's1', 's2', 's3')
        skill = int((int(sk[0]) + int(sk[1]) + int(sk[2])) * 100 / 20)
        ac = 0
        acs = r.hmget(message.from_user.id, 'ac1', 'ac2', 'ac3', 'ac4', 'ac5',
                      'ac6', 'ac7', 'ac8', 'ac9', 'ac10', 'ac11', 'ac12', 'ac13')
        for a in acs:
            try:
                ac += int(a)
            except:
                pass
        bot.reply_to(message, '\U0001F4DC ' + message.from_user.first_name +
                              '\n\n\U0001F3C6 Кількість перемог: ' + stats[0].decode() +
                              '\n\U0001F3C5 Кількість трофеїв: ' + stats[1].decode() +
                              '\n\u2620\uFE0F Вбито русаків: ' + stats[2].decode() +
                              '\n\U0001F476 З`їдено немовлят: ' + stats[3].decode() +
                              '\n\u2622 Випито горілки: ' + stats[4].decode() +
                              '\n\U0001F4E6 Відкрито пакунків: ' + stats[5].decode() +
                              '\n\u26CF Скіли: ' + str(skill) + '%' +
                              '\n\u2B50 Досягнення: ' + str(int(ac * 100 / 26)) + '%')


@bot.message_handler(commands=['woman'])
def woman(message):
    try:
        if r.hexists(message.from_user.id, 'nnn') == 0:
            if r.hexists(message.from_user.id, 'time4') == 0:
                r.hset(message.from_user.id, 'time4', 0)
            if int(r.hget(message.from_user.id, 'woman')) == 1:
                if int(r.hget(message.from_user.id, 'time4')) != date.today().day:
                    if r.hexists(message.from_user.id, 'time5') == 0:
                        r.hset(message.from_user.id, 'time5', 0)
                    r.hset(message.from_user.id, 'time4', date.today().day)
                    r.hincrby(message.from_user.id, 'time5', 1)
                    if int(r.hget(message.from_user.id, 'time5')) == 9:
                        bot.reply_to(message, '\U0001F469\U0001F3FB Ти провідав жінку. Вона народила \U0001F476 '
                                              'немовля. В тебе буде смачний сніданок!')
                        r.hincrby(message.from_user.id, 'childs', 1)
                        r.hset(message.from_user.id, 'time5', 0)
                    else:
                        bot.reply_to(message, '\U0001F469\U0001F3FB Ти провідав жінку. Вона на ' +
                                     r.hget(message.from_user.id, 'time5').decode() + ' місяці.')
                else:
                    bot.reply_to(message, '\U0001F469\U0001F3FB Ти знову провідав жінку. Вона на ' +
                                 r.hget(message.from_user.id, 'time5').decode() + ' місяці.')
            else:
                print(1 / 0)
        else:
            if int(r.hget(message.from_user.id, 'woman')) == 1:
                bot.reply_to(message, '\U0001F469\U0001F3FB Жінки під час No Nut November заборонені!')
    except:
        pass


@bot.message_handler(commands=['ltop'])
def l_top(message):
    bot.reply_to(message, top(message.chat.id))


@bot.message_handler(commands=['gtop'])
def g_top(message):
    bot.reply_to(message, top(111))


@bot.message_handler(commands=['itop'])
def i_top(message):
    bot.reply_to(message, itop(message.from_user.id, message.chat.id, message.chat.type))


@bot.message_handler(commands=['ctop'])
def c_top(message):
    bot.reply_to(message, ctop(222))


@bot.message_handler(commands=['class'])
def classes(message):
    if message.chat.type == 'private':
        bot.reply_to(message, 'Класи русаків:\n\n\n'
                              'Хач \U0001F919 - моментально додає +100 сили. Якщо у ворога нема зброї'
                              ', додає 30 бойового духу та збільшує свою силу на 13%, а якщо є зброя - зменшує'
                              ' силу на 13%.\n\n'
                              'Роботяга \U0001F9F0 - йому заборонено хворіти. В шахті заробляє втричі більше грошей,'
                              ' але вдвічі більший шанс забухати (п`є в 5 раз більше). \n\n'
                              'Фокусник \U0001F52E - моментально додає 1 інтелекту. 80% шанс ігнорувати дрин ворога, '
                              'перед початком бою показує випадкові характеристики.\n\n'
                              'Язичник \U0001F5FF - вдвічі збільшує максимальний бойовий дух. При перемозі отримує'
                              ' втричі більше бойового духу, але при поразці вдвічі більше втрачає.\n\n'
                              'Гарматне м`ясо \U0001fa96 - +50% сили в бою, якщо є АК-47 (зброя, яку можна придбати в '
                              'мандрівного торговця). 2% шанс отримати поранення в бою від АК-47 (втрачає весь бойовий'
                              ' дух, зброю, захист, на 100 боїв втричі зменшує силу, інтелект та бойовий дух).\n\n'
                              'Мусор \U0001F46E - має постійну зброю, яка перед боєм ігнорує бойовий дух двох сторін.'
                              ' Якщо є захист, ігнорує лише бойовий дух ворога.\n\n'
                              'Малорос \U0001F921 - моментально віднімає 2 інтелекту. При жертві віднімає у всіх'
                              ' русаків чату інтелект, який вони здобули від мухоморів (їх можна буде знову купити). '
                              'Якщо інтелект не зняло, віднімає 90% бойового духу. Мінімальний шанс перемоги збільшено '
                              'до 20%.\n\nХакер \U0001F4DF - при поразці є 18% підняти собі бойовий дух, знизити ворогу'
                              ' і заробити гривню.\n\n\n'
                              'Щоб подивитись другий рівень класів натисни /class_2\n'
                              'Якщо твій русак вже набрав 5 інтелекту, можеш вибрати один з цих класів (один раз на '
                              'одного русака), написавши сюди "Обираю клас " і назву класу.')
    else:
        bot.reply_to(message, 'Цю команду необхідно писати в пп боту.')


@bot.message_handler(commands=['class_2'])
def classes_2(message):
    if message.chat.type == 'private':
        bot.reply_to(message, 'Класи русаків:\n\n\n'
                              'Борцуха \U0001F919\U0001F919 - моментально додає ще +100 сили. Якщо у ворога нема зброї'
                              ', є шанс активувати один з прийомів при перемозі. Чим більша сила ворога, тим більший '
                              'цей шанс. Кидок через стегно: -50-100 бойового духу ворогу. Млин: +50-100 бойового духу.'
                              ' Кидок прогином: +2 гривні (10% шанс).\n\n'
                              'Почесний алкаш \U0001F9F0\U0001F9F0 - наполовину зменшує кількість потрібних перемог та'
                              ' горілки для прокачки майстерності та алкоголізму. Навіть якщо в шахті нап`ється, йому '
                              'буде видано 8 гривень.\n\n'
                              'Злий геній \U0001F52E\U0001F52E - +2 інтелекту, колода з кіоску мінятиме лише ті '
                              'характеристики, які у ворога більші.\n\n'
                              'Скінхед \U0001F5FF\U0001F5FF - подвоєний бойовий дух в боях з хачами. При поразці не'
                              ' втрачає вдвічі більше бойового духу. Тепер замість купівлі дрина буде видана зброя з '
                              'аналогічним ефектом - Бита [Атака, міцність=3].\n\n'
                              'Орк \U0001fa96\U0001fa96 - додає +2.5% сили на бій за кожне з`їдене немовля '
                              '(максимум 50%).\n\n'
                              'Силовик \U0001F46E\U0001F46E - ігнорує інтелект. Додає +15% сили за кожне марно'
                              ' втрачене очко інтелекту. Здібність не діє проти інших мусорів.\n\n'
                              'Кремлебот \U0001F921\U0001F921 - +60 гривень і онуляє рахунок мухоморів. При жертві'
                              ' отримує по 2 гривні за кожного, хто втратив бойовий дух (максимум 200 гривень).\n\n'
                              'Кіберзлочинець \U0001F4DF\U0001F4DF - отримує доступ до баз даних - якщо напився на '
                              'роботі, то може працювати ще раз; можливість купляти мухомори без обмежень.\n\n\n'
                              'Щоб подивитись третій рівень класів натисни /class_3\n'
                              'Якщо твій русак вже набрав 12 інтелекту і вибрав клас, можеш '
                              'покращити клас, написавши сюди "Покращити русака".')
    else:
        bot.reply_to(message, 'Цю команду необхідно писати в пп боту.')


@bot.message_handler(commands=['class_3'])
def classes_3(message):
    if message.chat.type == 'private':
        bot.reply_to(message, 'Класи русаків:\n\n\n'
                              'Гроза Кавказу \U0001F919\U0001F919\U0001F919 - Збільшує силу на 100. +10 сили і +1000 '
                              'бойового духу якщо вперше за день в бою зустрів хача.\n\n'
                              'П`яний майстер \U0001F9F0\U0001F9F0\U0001F9F0 - якщо русак вже їв, 0% шанс в бою '
                              'отримати талон на їжу (додаткове годування). Шанс збільшується на 1% за кожні два рівня '
                              'алкоголізму.\n\n'
                              'Некромант \U0001F52E\U0001F52E\U0001F52E - при захисті збільшує інтелект на 5% за кожну'
                              ' смерть (максимум 35%). При атаці збільшує силу на 3% за кожну смерть ворога '
                              '(максимум 33%).\n\n'
                              'Білий вождь \U0001F5FF\U0001F5FF\U0001F5FF - в боях втрачає вдвічі менше бойового духу. '
                              'Збільшує силу на 20% якщо у ворога менше трофеїв. Збільшує бойовий дух на 1% за '
                              'кожен трофей (максимум 50%).\n\n'
                              'Герой Новоросії \U0001fa96\U0001fa96\U0001fa96 - якщо більше ніж 300 сили: '
                              'обидва русаки можуть отримати поранення на 100 боїв (якщо в героя є АК-47), з шансом 10%'
                              ' в бою герой і ворог отримають невелике поранення (герой: +1 \U0001fa78, ворог +5-10'
                              '\U0001fa78).\n\n'
                              'Товариш майор \U0001F46E\U0001F46E\U0001F46E - 20% шанс вилучити в ворога зброю при '
                              'захисті і захист при атаці і отримати щит або підняти його міцність на 10 (не діє проти'
                              ' інших мусорів).\n\n'
                              'Агент ФСБ \U0001F921\U0001F921\U0001F921 - одноразова премія - 100 гривень. В бою проти '
                              'русака без класу є 5% шанс перетворити його в малороса. За це агент отримує 20 гривень.'
                              '\n\n'
                              'Black Hat \U0001F4DF\U0001F4DF\U0001F4DF - здібність хакера тепер додає по гривні за '
                              'кожні 50 гривень на рахунку ворога (1-5 гривень).\n\n\n'
                              'Якщо твій русак вже набрав 20 інтелекту і покращив клас, можеш ще раз'
                              'покращити клас, написавши сюди "Вдосконалити русака".')
    else:
        bot.reply_to(message, 'Цю команду необхідно писати в пп боту.')


@bot.message_handler(commands=['merchant'])
def merchant(message):
    if message.chat.id == -1001211933154:
        if r.hexists('soledar', 'merchant_day') == 0:
            r.hset('soledar', 'merchant_day', 0)
            r.hset('soledar', 'merchant_hour', random.randint(16, 20))

        if int(r.hget('soledar', 'merchant_day')) != date.today().day and \
                int(r.hget('soledar', 'merchant_hour')) == datetime.now().hour:
            pin = bot.reply_to(message, 'Прийшов мандрівний торговець, приніс різноманітні товари.\n\n'
                                        '\U0001F6E1 Уламок бронетехніки [Захист, міцність=7, ціна=10] - збільшує силу '
                                        'на бій на 30%. Після зношення повертаються 4 гривні.\n\U0001F344 '
                                        'Мухомор королівський [Захист, міцність=1, ціна=60] - якщо у ворога більший '
                                        'інтелект, додає +1 інтелекту (не діє проти фокусників). На бій зменшує свою '
                                        'силу на 50%. Максимальна кількість покупок на русака - 3.\n\n'
                                        '\U0001F919 Травмат [Атака, міцність=5, ціна=6] - зменшує силу ворога на бій '
                                        'на 50%.\n\U0001F9F0 Діамантове кайло [Атака, міцність=25, ціна=12] - збільшує '
                                        'силу, інтелект і бойовий дух на 10%.\n\U0001F52E Колода з кіоску [Атака, міцні'
                                        'сть=3, ціна=5] - міняє твої характеристики з ворогом на бій.\n\U0001F5FF Сокир'
                                        'а Перуна [Атака, міцність=1, ціна=7] - при перемозі забирає весь бойовий дух в'
                                        'орога, при поразці ворог забирає твій.\n\U0001fa96 АК-47 [Атака&Захист, міцніс'
                                        'ть=30, ціна=20] - після перемоги активує ефект горілки.\n\U0001F46E Поліцейськ'
                                        'ий щит [Захист, міцність=10, ціна=10] - зменшує силу ворога на 20%.\n'
                                        '\U0001F921 Прапор новоросії [Атака&Захист, міцність=8, ціна=11] - піднімає '
                                        'бойовий дух до максимуму на бій.\n\U0001F4DF Експлойт [Атака, міцність=2, '
                                        'ціна=9] - шанс активувати здібність хакера - 99%.',
                               reply_markup=merchant_goods())
            r.hset('soledar', 'merchant_day', date.today().day)
            r.hset('soledar', 'merchant_hour_now', datetime.now().hour)
            r.hset('soledar', 'merchant_hour', random.randint(16, 20))
            try:
                bot.unpin_chat_message(chat_id=pin.chat.id,
                                       message_id=int(r.hget('soledar', 'pin')))
            except:
                pass
            bot.pin_chat_message(chat_id=pin.chat.id, message_id=pin.message_id, disable_notification=True)
            r.hset('soledar', 'pin', pin.message_id)

        else:
            msg = 'Мандрівний торговець приходить раз в день у випадкову годину (від 18 до 22).\n' \
                  'Продає універсальний захист, рідкісні гриби та спорядження для всіх класів.'
            if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                    int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
                msg = msg + '\n\nТорговець прийшов:\nt.me/soledar1/' + r.hget('soledar', 'pin').decode()
            bot.send_message(message.chat.id, msg, disable_web_page_preview=True)
    else:
        msg = 'Мандрівний торговець приходить увечері в @soledar1.'
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            msg = msg + '\n\nТорговець прийшов:\nt.me/soledar1/' + r.hget('soledar', 'pin').decode()
        bot.send_message(message.chat.id, msg, disable_web_page_preview=True)


@bot.message_handler(commands=['donate'])
def donate(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, 'Якщо хтось хоче підтримати автора, то можне задонатити і отримати\n'
                                      '\U0001F31F погон російського генерала, який можна потратити в \n/donate_shop:'
                                      '\n\n<code>5375414105409873</code>',
                     reply_markup=markup.add(types.InlineKeyboardButton(text='Як отримати погони?',
                                                                        callback_data='donate')), parse_mode='HTML')


@bot.message_handler(commands=['donated'])
def donated(message):
    if message.chat.type == 'private':
        full_text = '<code>' + str(message.from_user.id) + '</code>\n' + str(message.from_user.first_name) + ' ' + \
                    str(message.from_user.last_name) + '\n@' + str(message.from_user.username) + '\n\n' + message.text
        bot.send_message(456514639, full_text, parse_mode='HTML')
        bot.send_message(message.chat.id, '\u2705', reply_to_message_id=message.id)
        if message.from_user.id == 456514639:
            try:
                code = message.text.split(' ')
                r.hincrby(int(code[1]), 'strap', int(code[2]))
                bot.send_message(message.chat.id, '\u2705', reply_to_message_id=message.id)
                bot.send_message(int(code[1]), 'Нараховано:\n\n\U0001F31F Погон російського генерала: ' + code[2])
            except Exception as e:
                print(e)
                bot.send_message(message.chat.id, '\u274E', reply_to_message_id=message.id)


@bot.message_handler(commands=['donate_shop'])
def donate_shop(message):
    if message.chat.type == 'private':
        if r.hexists(message.from_user.id, 'strap') == 0:
            r.hset(message.from_user.id, 'strap', 0)
        bot.send_message(message.chat.id, '\U0001F31F Погони російських генералів: ' +
                         r.hget(message.from_user.id, 'strap').decode() +
                         '\n\nОсь опис товарів, які можна придбати:\n\n\U0001F304 Зміна звичайної фотки русака на фото '
                         'Хеві з ТФ2, слов`янина Рікардо (Увага! Ці фото зникнуть в момент вибору класу), або на преміу'
                         'м фото свого класу(Кадиров, Обеме, Горшок, Тесак, Захарченко, Дерек, Янукович, Petya).\n'
                         '\U0001F943 Настоянка глоду - буст для новачків. Якщо в русака менше 400 сили і 5 інтелекту, '
                         'то настоянка моментально додасть 400 сили і 4 інтелекту.\n'
                         '\U0001F4E6 40 Донбаських пакунків\n'
                         '\U0001F393 Курс перекваліфікації - '
                         'дозволяє русаку наново вибрати клас.\n\U0001F3E0 Велике будівництво - додатковий підвал найви'
                         'щого рівня (покупка доступна до етапу 2. Купівля будівельних матеріалів).',
                         reply_markup=donate_goods())
    else:
        bot.reply_to(message, 'Цю команду необхідно писати в пп боту.')


def war(cid, location, big_battle):
    bot.send_message(cid, '\U0001F5FA Починається ' + location + '!',
                     reply_to_message_id=int(r.hget('battle' + str(cid), 'start')))
    time.sleep(2)
    ran = random.choice(['\U0001F93E\u200D\u2642\uFE0F \U0001F93A', '\U0001F6A3 \U0001F3C7',
                         '\U0001F93C\u200D\u2642\uFE0F'])
    bot.send_message(cid, ran + ' Русаки несамовито молотять один одного...')
    time.sleep(3)
    m = bot.send_message(cid, '\u2694 Йде бій...')

    everyone = r.smembers('fighters' + str(cid))
    fighters = {}
    for member in everyone:
        try:
            stats = r.hmget(member, 'strength', 'intellect', 'spirit', 'weapon', 'defense', 'injure')
            s = int(stats[0])
            i = int(stats[1])
            bd = int(stats[2])
            if int(stats[5]) > 0:
                s, s1, i, bd = injure(int(member), True)
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
    win = random.choices(list(fighters.keys()), weights=list(fighters.values()))
    win = int(str(win)[3:-2])
    wc = int(r.hget(win, 'class'))
    if not big_battle:
        reward = '\n\n\U0001F3C6 +1 \U0001F4B5 +5\n'
        r.hincrby(win, 'wins', 1)
        r.hincrby(win, 'money', 5)
    else:
        reward = '\n\n\U0001F3C5 +1 \U0001F3C6 +3 \U0001F4B5 +10\n'
        r.hincrby(win, 'trophy', 1)
        r.hincrby(win, 'wins', 3)
        r.hincrby(win, 'money', 10)
    class_reward = ''

    if location == 'Битва на овечій фермі':
        if wc == 1 or wc == 11 or wc == 21:
            if int(r.hget(win, 'hach_time')) == date.today().day:
                spirit(1000, win, wc, fi=False)
                class_reward = '\U0001F919: \U0001F54A +1000'
            else:
                r.hincrby(win, 'strength', 10)
                class_reward = '\U0001F919: \U0001F4AA +10'
                r.hset(win, 'hach_time', date.today().day)
    if location == 'Битва на покинутому заводі':
        if wc == 2 or wc == 12 or wc == 22:
            class_reward = '\U0001F9F0: \U0001F4B5 +5 \u2622 +10'
            r.hincrby(win, 'money', 5)
            r.hincrby(win, 'vodka', 10)
    if location == 'Битва в темному лісі':
        if wc == 3 or wc == 13 or wc == 23:
            class_reward = '\U0001F52E: \U0001F54A +2000\nВсі інші учасники битви втратили по 1000 бойового духу.'
            r.srem('fighters' + str(cid), win)
            for member in r.smembers('fighters' + str(cid)):
                spirit(-1000, member, int(r.hget(member, 'class')), fi=False)
            spirit(2000, win, wc, fi=False)
    if location == 'Битва біля старого дуба':
        if wc == 4 or wc == 14 or wc == 24:
            class_reward = '\U0001F5FF: \U0001F54A +10000'
            spirit(10000, win, wc, fi=False)
    if location == 'Битва в житловому районі':
        if wc == 5 or wc == 15 or wc == 25:
            class_reward = '\U0001fa96: \u2622 +15'
            r.hincrby(win, 'vodka', 15)
    if location == 'Битва біля поліцейського відділку':
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
    if location == 'Битва в офісі ОПЗЖ':
        if wc == 7 or wc == 17 or wc == 27:
            class_reward = '\U0001F921: \U0001F3C5 +1 \U0001F3C6 +5'
            r.hincrby(win, 'wins', 5)
            r.hincrby(win, 'trophy', 1)
    if location == 'Битва в серверній кімнаті':
        if wc == 8 or wc == 18 or wc == 28:
            class_reward = '\U0001F4DF: \U0001F4B5 +20'
            r.hincrby(win, 'money', 20)

    time.sleep(10)
    r.hdel('battle' + str(cid), 'start')
    for member in r.smembers('fighters' + str(cid)):
        r.srem('fighters' + str(cid), member)
    end = ' завершена.'
    if location == 'Штурм Горлівки' or location == 'Штурм ДАП':
        end = ' завершено.'
    user_name = r.hget(win, 'firstname').decode()
    bot.delete_message(m.chat.id, m.message_id)
    bot.send_message(cid, location + end + '\n\n\U0001F3C6 ' + ' ' + f'<a href="tg://user?id={win}">{user_name}</a>'
                     + ' перемагає!' + reward + class_reward, parse_mode='HTML')


def great_war(cid1, cid2, a, b):
    time.sleep(2)
    ran = random.choice(['\U0001F93E\u200D\u2642\uFE0F \U0001F93A', '\U0001F6A3 \U0001F3C7',
                         '\U0001F93C\u200D\u2642\uFE0F'])
    bot.send_message(cid1, ran + ' Русаки несамовито молотять один одного...')
    bot.send_message(cid2, ran + ' Русаки несамовито молотять один одного...')
    time.sleep(3)
    chance1 = 0
    chance2 = 0
    for member in a:
        try:
            stats = r.hmget(member, 'strength', 'intellect', 'spirit', 'weapon', 'defense', 'injure')
            s = int(stats[0])
            i = int(stats[1])
            bd = int(stats[2])
            if int(stats[5]) > 0:
                s, s1, i, bd = injure(int(member), True)
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
            chance1 += chance
        except:
            continue
    for member in b:
        try:
            stats = r.hmget(member, 'strength', 'intellect', 'spirit', 'weapon', 'defense', 'injure')
            s = int(stats[0])
            i = int(stats[1])
            bd = int(stats[2])
            if int(stats[5]) > 0:
                s, s1, i, bd = injure(int(member), True)
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
            chance2 += chance
        except:
            continue

    win = random.choices(['a', 'b'], weights=[chance1, chance2])
    msg = 'Міжчатова битва русаків завершена!\n\n\U0001F3C6 Бійці з '
    if win == ['a']:
        msg += r.hget('war_battle' + str(cid1), 'title').decode()
        for n in a:
            r.hincrby(n, 'trophy', 1)
            r.hincrby(n, 'wins', 2)
            r.hincrby(n, 'money', 3)
        r.hincrby(222, cid1, 1)
    elif win == ['b']:
        msg += r.hget('war_battle' + str(cid2), 'title').decode()
        for n in b:
            r.hincrby(n, 'trophy', 1)
            r.hincrby(n, 'wins', 2)
            r.hincrby(n, 'money', 3)
        r.hincrby(222, cid2, 1)
    msg += ' перемагають!\n\U0001F3C5 +1 \U0001F3C6 +2 \U0001F4B5 +3'
    time.sleep(10)

    r.hdel('war_battle' + str(cid1), 'start')
    r.hdel('war_battle' + str(cid1), 'enemy')
    r.hdel('battles', cid1)
    for member in r.smembers('fighters_2' + str(cid1)):
        r.srem('fighters_2' + str(cid1), member)
    r.hdel('war_battle' + str(cid2), 'start')
    r.hdel('war_battle' + str(cid2), 'enemy')
    r.hdel('battles', cid2)
    for member in r.smembers('fighters_2' + str(cid2)):
        r.srem('fighters_2' + str(cid2), member)

    bot.send_message(cid1, msg)
    bot.send_message(cid2, msg)


@bot.message_handler(commands=['battle'])
def battle(message):
    if message.chat.type != 'private':
        if r.hexists('battle' + str(message.chat.id), 'start') == 0:
            bot.delete_message(message.chat.id, message.id)
            a = bot.send_message(message.chat.id, '\u2694 Починається битва...\n\n', reply_markup=battle_button())
            r.hset('battle' + str(message.chat.id), 'start', a.message_id)
            r.hset('battle' + str(message.chat.id), 'starter', message.from_user.id)
            try:
                bot.pin_chat_message(a.chat.id, a.message_id, disable_notification=True)
                r.hset('battle' + str(message.chat.id), 'pin', a.message_id)
            except:
                pass
        else:
            try:
                bot.send_message(message.chat.id, '\U0001F5E1 Підготовка до битви тут\n\nКількість бійців: ' +
                                 str(r.scard('fighters' + str(message.chat.id))),
                                 reply_to_message_id=int(r.hget('battle' + str(message.chat.id), 'start')))
                bot.delete_message(message.chat.id, message.id)
            except:
                try:
                    bot.delete_message(message.chat.id, int(r.hget('battle' + str(message.chat.id), 'start')))
                except:
                    pass
                r.hdel('battle' + str(message.chat.id), 'start')
                for mem in r.smembers('fighters' + str(message.chat.id)):
                    r.srem('fighters' + str(message.chat.id), mem)
                bot.delete_message(message.chat.id, message.id)


@bot.message_handler(commands=['war'])
def war_battle(message):
    banned = [-1001646765307, -1001475102262, -714355096, 557298328, 530769095, 470411500, 1767253195]
    if message.chat.type != 'private' and bot.get_chat_members_count(message.chat.id) >= 10 \
            and '@' not in message.chat.title \
            and str(bot.get_chat_member(message.chat.id, bot.get_me().id).can_send_messages) != 'False'\
            and message.chat.id not in banned and message.from_user.id not in banned:
        if r.hexists('war_battle' + str(message.chat.id), 'start') == 0:
            try:
                bot.delete_message(message.chat.id, message.id)
            except:
                pass
            r.hset('war_battle' + str(message.chat.id), 'title', message.chat.title)
            if len(r.hgetall('battles')) == 0:
                a = bot.send_message(message.chat.id, '\u2694 Пошук ворогів...\n\n')
                r.hset('battles', a.chat.id, 0)
                r.hset('war_battle' + str(message.chat.id), 'start', a.message_id)
            else:
                i = len(r.hkeys('battles'))
                for k in r.hkeys('battles'):
                    if int(k) != message.chat.id:
                        if int(r.hget('battles', int(k))) == 0:
                            r.hset('battles', int(k), message.chat.id)
                            r.hset('war_battle' + str(message.chat.id), 'enemy', int(k))
                            r.hset('war_battle' + k.decode(), 'enemy', message.chat.id)
                            a = bot.send_message(message.chat.id, '\u2694 Починається міжчатова битва проти ' +
                                                 r.hget('war_battle' + k.decode(), 'title').decode() + '...\n\n',
                                                 reply_markup=battle_button_3())
                            b = bot.send_message(int(k), '\u2694 Починається міжчатова битва проти ' +
                                                 r.hget('war_battle' + str(message.chat.id), 'title').decode() +
                                                 '...\n\n', reply_markup=battle_button_3())
                            try:
                                bot.pin_chat_message(a.chat.id, a.message_id, disable_notification=True)
                                r.hset('war_battle' + str(message.chat.id), 'pin', a.message_id)
                            except:
                                pass
                            try:
                                bot.pin_chat_message(b.chat.id, b.message_id, disable_notification=True)
                                r.hset('war_battle' + k.decode(), 'pin', b.message_id)
                            except:
                                pass
                            r.hset('war_battle' + str(message.chat.id), 'start', a.message_id)
                            r.hset('war_battle' + k.decode(), 'start', b.message_id)
                            break
                    i -= 1
                    if i == 0:
                        a = bot.send_message(message.chat.id, '\u2694 Пошук ворогів...\n\n')
                        r.hset('battles', a.chat.id, 0)
                        r.hset('war_battle' + str(message.chat.id), 'start', a.message_id)
        elif '@' not in message.chat.title:
            try:
                msg = '\U0001F5E1 Підготовка до міжчатової битви тут.\n\nКількість наших бійців: ' \
                      + str(r.scard('fighters_2' + str(message.chat.id)))
                try:
                    msg += '\nКількість ворожих бійців: ' + \
                           str(r.scard('fighters_2' + r.hget('war_battle' + str(message.chat.id), 'enemy').decode()))
                except:
                    pass
                bot.send_message(message.chat.id, msg,
                                 reply_to_message_id=int(r.hget('war_battle' + str(message.chat.id), 'start')))
                try:
                    bot.delete_message(message.chat.id, message.id)
                except:
                    pass
            except:
                try:
                    bot.delete_message(message.chat.id, message.id)
                    bot.delete_message(message.chat.id, int(r.hget('war_battle' + str(message.chat.id), 'start')))
                except:
                    pass
                r.hdel('war_battle' + str(message.chat.id), 'start')
                r.hdel('battles', message.chat.id)
                for member in r.smembers('fighters_2' + str(message.chat.id)):
                    r.srem('fighters_2' + str(message.chat.id), member)


@bot.message_handler(commands=['crash'])
def crash(message):
    if bot.get_chat_member(message.chat.id, message.from_user.id).status == 'creator' \
            or bot.get_chat_member(message.chat.id, message.from_user.id).can_restrict_members is True \
            or message.from_user.id in sudoers:
        r.hdel('war_battle' + str(message.chat.id), 'start')
        r.hdel('battles', message.chat.id)
        for member in r.smembers('fighters_2' + str(message.chat.id)):
            r.srem('fighters_2' + str(message.chat.id), member)
        if r.hexists('war_battle' + str(message.chat.id), 'enemy') == 1:
            enemy = int(r.hget('war_battle' + str(message.chat.id), 'enemy'))
            r.hdel('war_battle' + str(enemy), 'start')
            r.hdel('battles', enemy)
            for member in r.smembers('fighters_2' + str(enemy)):
                r.srem('fighters_2' + str(enemy), member)
            bot.send_message(enemy, 'Ворожий чат вирішив здатись.')
        try:
            bot.unpin_chat_message(message.chat.id, int(r.hget('war_battle' + str(message.chat.id), 'pin')))
        except:
            pass
        try:
            enemy = int(r.hget('war_battle' + str(message.chat.id), 'enemy'))
            r.hdel('war_battle' + str(enemy), 'enemy')
            bot.unpin_chat_message(enemy, int(r.hget('war_battle' + str(enemy), 'pin')))
        except:
            pass
        r.hdel('war_battle' + str(message.chat.id), 'enemy')
        bot.reply_to(message, '\u2705')


@bot.message_handler(commands=['achieve'])
def achievements(message):
    try:
        full_list = ['', '\u26AA Хто не з нами, той нехай йде собі до сраки', '\u26AA І москаля нема, немає москаля',
                     '\u26AA Моя фамілія Залупа', '\u26AA Наливай, куме, горілки стаканчик',
                     '\u26AA Бігає по полю весело кабанчик', '\U0001f535 Геніальний розум, великий чоловік',
                     '\U0001f535 Гордо і достойно ти живеш свій вік',
                     '\U0001f535 Зараз розберемося, кому належить вулиця',
                     '\U0001f535 Ах лента за лентою набої подавай', '\U0001f7e3 Ніколи не плач на радість орді',
                     '\U0001f7e3 Ворога знищено, як був наказ', '\U0001f7e3 Я заводжу хімікат, розпочинаю атентат',
                     '\U0001f534 Кривавий пастор']

        acs = r.hmget(message.from_user.id, 'ac1', 'ac2', 'ac3', 'ac4', 'ac5',
                      'ac6', 'ac7', 'ac8', 'ac9', 'ac10', 'ac11', 'ac12', 'ac13')

        if isinstance(acs[1], type(None)):
            if int(r.hget(message.from_user.id, 'deaths')) >= 1:
                r.hset(message.from_user.id, 'ac2', 1)
        if isinstance(acs[3], type(None)):
            if int(r.hget(message.from_user.id, 'vodka')) >= 150:
                r.hset(message.from_user.id, 'ac4', 1)
        if isinstance(acs[4], type(None)):
            if int(r.hget(message.from_user.id, 'eat')) >= 15:
                r.hset(message.from_user.id, 'ac5', 1)
        if isinstance(acs[5], type(None)):
            if int(r.hget(message.from_user.id, 'intellect')) >= 20:
                r.hset(message.from_user.id, 'ac6', 1)
        if isinstance(acs[6], type(None)):
            if int(r.hget(message.from_user.id, 'strength')) >= 1000:
                r.hset(message.from_user.id, 'ac7', 1)
        if isinstance(acs[7], type(None)):
            if int(r.hget(message.from_user.id, 'spirit')) >= 10000:
                r.hset(message.from_user.id, 'ac8', 1)
        if isinstance(acs[8], type(None)):
            if int(r.hget(message.from_user.id, 'wins')) >= 1000:
                r.hset(message.from_user.id, 'ac9', 1)
        if isinstance(acs[9], type(None)):
            if str(message.from_user.id).encode() in r.smembers('fighters' + str(message.chat.id)):
                r.hset(message.from_user.id, 'ac10', 1)
        if isinstance(acs[10], type(None)):
            if int(r.hget(message.from_user.id, 'weapon')) >= 11 or int(r.hget(message.from_user.id, 'defense')) >= 11:
                r.hset(message.from_user.id, 'ac11', 1)
        if isinstance(acs[11], type(None)):
            if int(r.hget(message.from_user.id, 'deaths')) >= 15 and int(r.hget(message.from_user.id, 'childs')) >= 15:
                r.hset(message.from_user.id, 'ac12', 1)

        acl = ['', 'ac1', 'ac2', 'ac3', 'ac4', 'ac5', 'ac6', 'ac7', 'ac10', 'ac11', 'ac8', 'ac9', 'ac13', 'ac12']
        acs = r.hmget(message.from_user.id, 'ac1', 'ac2', 'ac3', 'ac4', 'ac5',
                      'ac6', 'ac7', 'ac10', 'ac11', 'ac8', 'ac9', 'ac13', 'ac12')

        reply = '\u2B50 Досягнення ' + message.from_user.first_name + ':\n\n'
        new, new_a, number = '', 0, 1
        for ac in acs:
            if str(ac) == 'None':
                number = number + 1
                continue
            elif ac.decode() == '1':
                new_a = new_a + 1
                new = 'Отримано нові досягнення!\n\U0001F476 + ' + str(new_a) + '\n'
                r.hincrby(message.from_user.id, 'childs', 1)
                r.hset(message.from_user.id, acl[number], 2)
                reply += full_list[number] + '\n'
            elif ac.decode() == '2':
                reply += full_list[number] + '\n'

            number = number + 1
        bot.reply_to(message, text=new + reply)
    except Exception as e:
        print(e)


@bot.message_handler(commands=['i'])
def inventory(message):
    try:
        inv = r.hmget(message.from_user.id, 'weapon', 'defense', 'support', 's_weapon', 's_defense')
        if int(inv[0]) != 0 or int(inv[1]) != 0:
            rep = invent()
        else:
            rep = None
        if int(inv[0]) == 1 or int(inv[0]) == 14 or int(inv[0]) == 2:
            m1 = '\nМіцність: 1'
        elif int(inv[0]) == 16:
            m1 = '\nМіцність: ∞'
        elif int(inv[0]) == 0:
            m1 = '[Порожньо]'
        else:
            m1 = '\nМіцність: ' + inv[3].decode()

        if int(inv[1]) == 1 or int(inv[1]) == 10:
            m2 = '\nМіцність: 1'
        elif int(inv[1]) == 15 or int(inv[1]) == 17:
            m2 = '\nМіцність: ' + inv[3].decode()
        elif int(inv[1]) == 0:
            m2 = '[Порожньо]'
        else:
            m2 = '\nМіцність: ' + inv[4].decode()
        bot.reply_to(message, '\U0001F5E1 Зброя: ' + weapons[int(inv[0])] + m1 +
                     '\n\U0001F6E1 Захист: ' + defenses[int(inv[1])] + m2 + '\n\U0001F9EA Допомога: [Порожньо]',
                     reply_markup=rep)
    except:
        bot.reply_to(message, '\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на /donbass')


@bot.message_handler(commands=['pack'])
def pack(message):
    if r.hexists(message.from_user.id, 'name') == 1:
        packs = int(r.hget(message.from_user.id, 'packs'))
        if packs != 0:
            bot.reply_to(message, '\U0001F4E6 Донбаські пакунки: ' + str(packs) + '\n\nВідкрити?',
                         reply_markup=unpack())
        else:
            bot.reply_to(message, '\U0001F4E6 Донбаський пакунок коштує \U0001F4B5 20 гривень.'
                                  '\n\nКупити один і відкрити?', reply_markup=unpack())
    else:
        bot.reply_to(message, '\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на /donbass')


@bot.message_handler(commands=['skills'])
def skills(message):
    try:
        if message.chat.type == 'private':
            s = r.hmget(message.from_user.id, 's1', 's2', 's3')
            s1, s2, s3 = int(s[0]), int(s[1]), int(s[2])
            s11, s22, s221, s222 = s1, s2, 0, 0
            intel = ' гривень, а шанс підняти інтелект - 10%. '
            if s2 == 1:
                s221, s222 = 3, 8
            elif s2 == 2:
                s221, s222 = 4, 9
            elif s2 == 3:
                s221, s222 = 5, 10
            else:
                s221, s222 = 5, 10
                intel = ' гривень, а шанс підняти інтелект - 20%. '
            cl = int(r.hget(message.from_user.id, 'class'))
            if cl == 2 or cl == 12 or cl == 22:
                s221 = s221 * 3
                s222 = s222 * 3
                if cl == 12 or cl == 22:
                    s11 = s11 / 2
                    s22 = s22 / 2

            up1 = ' Для покращення цієї здібності треба випити \u2622 ' + str(int(s11 * 100)) + ' горілки.'
            up2 = 'Покращення цієї здібності збільшить матеріальну та моральну користь від шахт та коштує 100 грн. ' \
                  'Також необхідно набрати \n\U0001F3C6 ' + str(int(s22 * 250)) + ' перемог.'
            up3 = 'Етапи будівництва:\n' \
                  '1. Купівля другої утепленої будки (30 грн)\n' \
                  '2. Купівля будівельних матеріалів (750 грн)\n' \
                  '3. Будівництво (твій русак втратить 25% сили). ' \
                  'На цьому етапі можна отримати додаткового русака (годувати одного в день)\n' \
                  '4. Купівля припасів (1500 грн). Можна годувати і відправляти в шахти обох русаків.\n'
            if s1 >= 10:
                up1 = ''
            if s2 >= 5:
                up2 = ''
            if s3 >= 5:
                up3 = ''
            msg = '\u2622 Алкоголізм:\n\nГорілка додає від ' + str(10 * s1) + ' до ' + str(70 * s1) + \
                  ' бойового духу.' + up1 + '\n'
            for a in range(10):
                if s1 <= 0:
                    msg = msg + '\u2B1C'
                else:
                    msg = msg + '\U0001f7e7'
                    s1 = s1 - 1

            msg = msg + '\n\n\u26CF Майстерність:\n\nЗараз русак в шахті може заробити від ' + str(s221) + ' до ' + \
                        str(s222) + intel + up2 + '\n'

            for a in range(5):
                if s2 <= 0:
                    msg = msg + '\u2B1C'
                else:
                    msg = msg + '\U0001f7e5'
                    s2 = s2 - 1

            msg = msg + '\n\n\U0001F3DA Велике будівництво\n\nПідвал для додаткового русака. \n' + up3
            for a in range(5):
                if s3 <= 0:
                    msg = msg + '\u2B1C'
                else:
                    msg = msg + '\U0001f7eb'
                    s3 = s3 - 1

            bot.send_message(message.chat.id, msg, reply_markup=skill_set())
        else:
            bot.reply_to(message, 'Цю команду необхідно писати в пп боту.')
    except:
        pass


@bot.message_handler(commands=['swap'])
def swap(message):
    try:
        if int(r.hget(message.from_user.id, 's3')) >= 4 and r.hexists(message.from_user.id, 'name') == 1:
            a = r.hmget(message.from_user.id, 'name', 'strength', 'intellect', 'spirit',
                        'weapon', 's_weapon', 'defense', 's_defense', 'mushrooms', 'class', 'photo', 'injure', 'hp')
            b = r.hmget(message.from_user.id, 'name2', 'strength2', 'intellect2', 'spirit2', 'weapon2', 's_weapon2',
                        'defense2', 's_defense2', 'mushrooms2', 'class2', 'photo2', 'injure2', 'hp2')
            r.hset(message.from_user.id, 'name2', a[0], {'strength2': a[1], 'intellect2': a[2], 'spirit2': a[3],
                                                         'weapon2': a[4], 's_weapon2': a[5], 'defense2': a[6],
                                                         's_defense2': a[7], 'mushrooms2': a[8], 'class2': a[9],
                                                         'photo2': a[10], 'injure2': a[11], 'hp2': a[12]})
            r.hset(message.from_user.id, 'name', b[0], {'strength': b[1], 'intellect': b[2], 'spirit': b[3],
                                                        'weapon': b[4], 's_weapon': b[5], 'defense': b[6],
                                                        's_defense': b[7], 'mushrooms': b[8], 'class': b[9],
                                                        'photo': b[10], 'injure': b[11], 'hp': b[12]})
            if r.hexists(message.from_user.id, 'time22') == 1:
                a1 = r.hget(message.from_user.id, 'time')
                b1 = r.hget(message.from_user.id, 'time22')
                a2 = r.hget(message.from_user.id, 'time1')
                b2 = r.hget(message.from_user.id, 'time23')
                r.hset(message.from_user.id, 'time', b1)
                r.hset(message.from_user.id, 'time22', a1)
                r.hset(message.from_user.id, 'time1', b2)
                r.hset(message.from_user.id, 'time23', a2)
            bot.reply_to(message, 'Бойового русака змінено.')
    except:
        pass


@bot.message_handler(commands=['commands'])
def commands(message):
    markup = types.InlineKeyboardMarkup()
    bot.reply_to(message, '/links - реклама, головний чат, творець\n'
                          '/feed - погодувати русака\n'
                          '/mine - відправити русака заробляти гроші (доступно тільки в @soledar1)\n'
                          '/woman - провідати жінку\n'
                          '/fascist - вибрати фашиста дня\n'
                          '/achieve - досягнення\n'
                          '/skills - вміння\n'
                          '/i - інвентар\n'
                          '/battle - чатова битва (5-10 русаків)\n'
                          '/war - міжчатова битва 5х5\n'
                          '...', reply_markup=markup.add(types.InlineKeyboardButton(text='Розгорнути',
                                                                                    callback_data='full_list')))


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data.startswith('getrusak') and call.from_user.id == call.message.reply_to_message.from_user.id:
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True)
        try:
            if r.hexists(call.from_user.id, 'name') == 1:
                bot.edit_message_text(text='\U0001F98D У тебе вже є русак!',
                                      chat_id=call.message.chat.id, message_id=call.message.id)
            else:
                print(1 / 0)
        except:
            r.hset(call.from_user.id, 'name', get_rusak()[0])
            r.hset(call.from_user.id, 'strength', get_rusak()[1])
            r.hset(call.from_user.id, 'intellect', get_rusak()[2])
            if r.hexists(call.from_user.id, 'spirit') == 0:
                r.hset(call.from_user.id, 'spirit', 0)
            if r.hexists(call.from_user.id, 'time') == 0:
                r.hset(call.from_user.id, 'time', 0)
            r.hset(call.from_user.id, 'class', 0)
            r.hset(call.from_user.id, 'weapon', 0)
            r.hset(call.from_user.id, 'defense', 0)
            r.hset(call.from_user.id, 'support', 0)
            r.hset(call.from_user.id, 's_weapon', 0)
            r.hset(call.from_user.id, 's_defense', 0)
            r.hset(call.from_user.id, 'photo', 0)
            r.hset(call.from_user.id, 'mushrooms', 0)
            r.hset(call.from_user.id, 'packs', 0)
            r.hset(call.from_user.id, 'opened', 0)
            r.hset(call.from_user.id, 'injure', 0)
            r.hset(call.from_user.id, 'hp', 0)
            try:
                r.hset(call.from_user.id, 'username', call.from_user.username)
                if call.message.chat.type != 'private':
                    r.sadd(call.message.chat.id, call.from_user.id)
                    r.sadd(111, call.from_user.id)
            except:
                pass
            if r.hexists(call.from_user.id, 'childs') == 0:
                r.hset(call.from_user.id, 'childs', 0)
            if r.hexists(call.from_user.id, 'deaths') == 0:
                r.hset(call.from_user.id, 'deaths', 0)
            if r.hexists(call.from_user.id, 'wins') == 0:
                r.hset(call.from_user.id, 'wins', 0)
            if r.hexists(call.from_user.id, 'trophy') == 0:
                r.hset(call.from_user.id, 'trophy', 0)
            if r.hexists(call.from_user.id, 'vodka') == 0:
                r.hset(call.from_user.id, 'vodka', 0)
            if r.hexists(call.from_user.id, 'eat') == 0:
                r.hset(call.from_user.id, 'eat', 0)
            if r.hexists(call.from_user.id, 's1') == 0:
                r.hset(call.from_user.id, 's1', 1)
            if r.hexists(call.from_user.id, 's2') == 0:
                r.hset(call.from_user.id, 's2', 1)
            if r.hexists(call.from_user.id, 's3') == 0:
                r.hset(call.from_user.id, 's3', 1)
            bot.edit_message_text(text='\U0001F3DA Ти приходиш на Донбас - чудове місце для полювання на'
                                       ' русаків\n\n\U0001F412 Русака взято в полон... ',
                                  chat_id=call.message.chat.id, message_id=call.message.id)

    elif call.data.startswith('fight') and r.hexists(call.from_user.id, 'name') != 0:
        cdata = call.data[5:].split(',', 3)
        uid1 = cdata[1]
        un1 = cdata[0]
        if call.from_user.id != int(uid1):
            try:
                q = cdata[2].split()
                diff = int(q[1])
                uid2 = call.from_user.id
                if int(r.hget(uid1, 'strength')) - diff <= int(r.hget(uid2, 'strength')) <= \
                        int(r.hget(uid1, 'strength')) + diff:
                    un2 = call.from_user.first_name
                    bot.edit_message_text(text=fight(uid1, uid2, un1, un2), inline_message_id=call.inline_message_id)
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='Твій русак не підходить по силі для цього бою.')
            except:
                try:
                    uid2 = call.from_user.id
                    un2 = call.from_user.first_name
                    if cdata[2] == 'tournament':
                        try:
                            q = cdata[3].split()
                            if q[1][1:] == call.from_user.username:
                                tournament(uid1, uid2, un1, un2, call.inline_message_id)
                            else:
                                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                          text='Цей бій не для тебе.')
                        except:
                            tournament(uid1, uid2, un1, un2, call.inline_message_id)
                    elif cdata[2] == 'private':
                        try:
                            q = cdata[3].split()
                            if q[1][1:] == call.from_user.username:
                                bot.edit_message_text(text=fight(uid1, uid2, un1, un2),
                                                      inline_message_id=call.inline_message_id)
                            else:
                                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                          text='Цей бій не для тебе.')
                        except:
                            print(1/0)
                    else:
                        print(1/0)
                except:
                    uid2 = call.from_user.id
                    un2 = call.from_user.first_name
                    bot.edit_message_text(text=fight(uid1, uid2, un1, un2), inline_message_id=call.inline_message_id)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Ти хочеш атакувати свого русака'
                                                                                       ', але розумієш, що він зараз ма'
                                                                                       'є битись з іншими русаками.')

    elif call.data.startswith('join'):
        if str(call.from_user.id).encode() not in r.smembers('fighters' + str(call.message.chat.id)) and \
                r.hexists(call.from_user.id, 'name') == 1 and \
                call.message.id == int(r.hget('battle' + str(call.message.chat.id), 'start')):
            r.sadd('fighters' + str(call.message.chat.id), call.from_user.id)
            r.hset(call.from_user.id, 'firstname', call.from_user.first_name)
            fighters = r.scard('fighters' + str(call.message.chat.id))
            if fighters == 1:
                bot.edit_message_text(
                    text=call.message.text + '\n\nБійці: ' + call.from_user.first_name, chat_id=call.message.chat.id,
                    message_id=call.message.id, reply_markup=battle_button())
            elif 5 <= fighters <= 9:
                bot.edit_message_text(
                    text=call.message.text + ', ' + call.from_user.first_name, chat_id=call.message.chat.id,
                    message_id=call.message.id, reply_markup=battle_button_2())
            elif fighters >= 10:
                bot.edit_message_text(
                    text=call.message.text + ', ' + call.from_user.first_name + '\n\nБій почався...',
                    chat_id=call.message.chat.id, message_id=call.message.id)
                ran = random.choice(['Битва в Соледарі', 'Битва на овечій фермі', 'Битва на покинутому заводі',
                                     'Битва в темному лісі', 'Битва біля старого дуба', 'Битва в житловому районі',
                                     'Битва біля поліцейського відділку', 'Битва в офісі ОПЗЖ',
                                     'Битва в серверній кімнаті', 'Штурм Горлівки', 'Штурм ДАП'])
                big_battle = True
                try:
                    bot.unpin_chat_message(chat_id=call.message.chat.id,
                                           message_id=int(r.hget('battle' + str(call.message.chat.id), 'pin')))
                except:
                    pass
                war(call.message.chat.id, ran, big_battle)
            else:
                bot.edit_message_text(
                    text=call.message.text + ', ' + call.from_user.first_name, chat_id=call.message.chat.id,
                    message_id=call.message.id, reply_markup=battle_button())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Ти або вже в битві, або в тебе'
                                                                                       ' нема русака')

    elif call.data.startswith('start_battle'):
        if call.from_user.id == int(r.hget('battle' + str(call.message.chat.id), 'starter')):
            bot.edit_message_text(text=call.message.text + '\n\nБій почався...',
                                  chat_id=call.message.chat.id, message_id=call.message.id)
            ran = random.choice(['Битва в Соледарі', 'Штурм Горлівки', 'Штурм ДАП'])
            big_battle = False
            try:
                bot.unpin_chat_message(chat_id=call.message.chat.id,
                                       message_id=int(r.hget('battle' + str(call.message.chat.id), 'pin')))
            except:
                pass
            war(call.message.chat.id, ran, big_battle)
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Почати битву може тільки той,'
                                                                                       ' хто почав набір.')

    elif call.data.startswith('war_join'):
        enemy = r.hget('war_battle' + str(call.message.chat.id), 'enemy')
        if str(call.from_user.id).encode() not in r.smembers('fighters_2' + str(call.message.chat.id)) and \
                str(call.from_user.id).encode() not in r.smembers('fighters_2' + enemy.decode()) and \
                r.hexists(call.from_user.id, 'name') == 1 and \
                call.message.id == int(r.hget('war_battle' + str(call.message.chat.id), 'start')):
            r.sadd('fighters_2' + str(call.message.chat.id), call.from_user.id)
            r.hset(call.from_user.id, 'firstname', call.from_user.first_name)
            fighters = r.scard('fighters_2' + str(call.message.chat.id))
            fighters2 = r.scard('fighters_2' + enemy.decode())
            if fighters == 1:
                bot.edit_message_text(
                    text=call.message.text + '\n\nБійці: ' + call.from_user.first_name, chat_id=call.message.chat.id,
                    message_id=call.message.id, reply_markup=battle_button_3())
            elif fighters >= 5 and fighters2 < 5:
                bot.edit_message_text(
                    text=call.message.text + ', ' + call.from_user.first_name + '\n\nЧекаємо поки інший чат набере'
                                                                                ' 5 бійців...',
                    chat_id=call.message.chat.id, message_id=call.message.id)
            elif fighters >= 5 and fighters2 >= 5:
                bot.edit_message_text(
                    text=call.message.text + '\n\nБій почався...',
                    chat_id=call.message.chat.id, message_id=call.message.id)
                a = list(r.smembers('fighters_2' + str(call.message.chat.id)))
                b = list(r.smembers('fighters_2' + enemy.decode()))
                msg = 'Починається сутичка між двома бандами русаків!\n\n' + \
                      r.hget('war_battle' + str(call.message.chat.id), 'title').decode() + ' | ' + \
                      r.hget('war_battle' + enemy.decode(), 'title').decode() + \
                      '\n1. ' + r.hget(a[0], 'firstname').decode() + ' | ' + r.hget(b[0], 'firstname').decode() + \
                      '\n2. ' + r.hget(a[1], 'firstname').decode() + ' | ' + r.hget(b[1], 'firstname').decode() + \
                      '\n3. ' + r.hget(a[2], 'firstname').decode() + ' | ' + r.hget(b[2], 'firstname').decode() + \
                      '\n4. ' + r.hget(a[3], 'firstname').decode() + ' | ' + r.hget(b[3], 'firstname').decode() + \
                      '\n5. ' + r.hget(a[4], 'firstname').decode() + ' | ' + r.hget(b[4], 'firstname').decode()
                bot.send_message(int(call.message.chat.id), msg)
                bot.send_message(int(enemy), msg)
                great_war(call.message.chat.id, int(enemy), a, b)
                try:
                    bot.unpin_chat_message(chat_id=call.message.chat.id,
                                           message_id=int(r.hget('war_battle' + str(call.message.chat.id), 'pin')))
                except:
                    pass
                try:
                    bot.unpin_chat_message(chat_id=int(enemy),
                                           message_id=int(r.hget('war_battle' + enemy.decode(), 'pin')))
                except:
                    pass
            else:
                bot.edit_message_text(
                    text=call.message.text + ', ' + call.from_user.first_name, chat_id=call.message.chat.id,
                    message_id=call.message.id, reply_markup=battle_button_3())
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Ти або вже в битві, або в тебе'
                                                                                       ' нема русака')

    elif call.data.startswith('sacrifice') and call.from_user.id == call.message.reply_to_message.from_user.id and \
            int(r.hget(call.from_user.id, 'time2')) != date.today().day:
        try:
            for member in r.smembers(call.message.chat.id):
                mem = int(member)
                try:
                    if bot.get_chat_member(call.message.chat.id, mem).status == 'left':
                        r.srem(call.message.chat.id, mem)
                        continue
                except:
                    r.srem(call.message.chat.id, mem)
                i = int(r.hget(mem, 'spirit')) / 10
                r.hincrby(mem, 'spirit', -int(i))
                cl = int(r.hget(call.from_user.id, 'class'))
                if cl == 7 or cl == 17 or cl == 27:
                    try:
                        mush = int(r.hget(mem, 'mushrooms'))
                        if mush > 0:
                            r.hset(mem, 'mushrooms', 0)
                            intellect(-mush, mem)
                        else:
                            r.hset(mem, 'spirit', int(i))
                    except:
                        r.hset(mem, 'spirit', int(i))
        except:
            pass
        name = int(r.hget(call.from_user.id, 'name'))
        clm = int(r.hget(call.from_user.id, 'class'))
        r.hdel(call.from_user.id, 'name')
        r.hset(call.from_user.id, 'photo', 0)
        r.hset(call.from_user.id, 'mushrooms', 0)
        r.hset(call.from_user.id, 'spirit', 0)
        spirit(5 * int(r.hget(call.from_user.id, 'strength')), call.from_user.id, 0, False)
        r.hset(call.from_user.id, 'strength', 0)
        r.hset(call.from_user.id, 'class', 0)
        r.hset(call.from_user.id, 'intellect', 0)
        r.hset(call.from_user.id, 'time2', date.today().day)
        r.hincrby(call.from_user.id, 'deaths', 1)
        if call.message.chat.type == 'private':
            bot.edit_message_text(text='\u2620\uFE0F ' + names[name] + ' був убитий. \nОдним кацапом менше, '
                                                                       'а вторий насрав в штани.',
                                  chat_id=call.message.chat.id, message_id=call.message.id)
        else:
            money = ''
            if clm == 17 or clm == 27:
                money = 2 * (len(r.smembers(call.message.chat.id)) - 1)
                if money > 200:
                    money = 200
                r.hincrby(call.from_user.id, 'money', money)
                money = '\n\U0001F4B5 +' + str(money)

            bot.edit_message_text(text='\u2620\uFE0F ' + names[name] + ' був убитий.\nОдним кацапом менше, '
                                                                       'а вторий насрав в штани.\n' +
                                       str(len(
                                           r.smembers(call.message.chat.id)) - 1) + ' русаків втратили бойовий дух.' +
                                       money, chat_id=call.message.chat.id, message_id=call.message.id)

    elif call.data.startswith('full_list'):
        bot.edit_message_text(text='Загальні:\n'
                                   '/links - реклама, головний чат, творець\n'
                                   '/help - як користуватись\n'
                                   '@Random_UAbot - вибрати одну з функцій рандому\n'
                                   '/donate - сподобався бот?\n\n'
                                   'Топ:\n'
                                   '/ltop - топ цього чату\n'
                                   '/gtop - глобальний топ\n'
                                   '/itop - яке я місце в топі?\n'
                                   '/ctop - топ чатів\n'
                                   '/passport - твої характеристикиn\n\n'
                                   'Русаки:\n'
                                   '/donbass - взяти русака\n'
                                   '/rusak - характеристики твого русака\n'
                                   '@Random_UAbot - почати битву\n'
                                   '@Random_UAbot [число] - почати битву з суперником з певною силою\n'
                                   '/feed - погодувати русака\n'
                                   '/shop - магазин\n'
                                   '/pack - Донбаський пакунок\n'
                                   '/woman - провідати жінку\n'
                                   '/sacrifice - вбити свого русака\n'
                                   '/fascist - вибрати фашиста дня\n'
                                   '/class - вибрати русаку клас\n'
                                   '/achieve - досягнення\n'
                                   '/skills - вміння\n'
                                   '/i - інвентар\n'
                                   '/swap - змінити бойового русака (якщо є підвал)\n'
                                   '/battle - почати масову битву\n'
                                   '/war - почати міжчатову битву\n'
                                   '/crash - зупинити міжчатову битву\n\n'

                                   'Команди, доступні тільки в @soledar1 та тимчасові івенти:\n'
                                   '/mine - відправити русака заробляти гроші\n'
                                   '/merchant - мандрівний торговець, який продає топову снарягу\n\n'

                                   'Адміністраторські команди:\n'
                                   '/toggle_admin - ввімкнути/вимкнути (для адмінів з правом редагування групи)\n'
                                   '/ban - перманентий бан (для адмінів з правом банити)\n'
                                   '/moxir - забрати стікери і медіа (також боту необхідні права банити)\n',
                              chat_id=call.message.chat.id, message_id=call.message.id)

    elif call.data.startswith('alcohol'):
        s1 = int(r.hget(call.from_user.id, 's1'))
        if s1 < 10:
            cl = int(r.hget(call.from_user.id, 'class'))
            s11 = s1
            if cl == 12 or cl == 22:
                s11 = s1 / 2
            if int(r.hget(call.from_user.id, 'vodka')) >= s11 * 100:
                r.hincrby(call.from_user.id, 's1', 1)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='\u2622 Ви підняли рівень алкоголізму до ' + str(s1 + 1) + '.')
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Ще рано переходити на наступний етап алкоголізму.')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Немає сенсу ставати ще більшим алкоголіком.')

    elif call.data.startswith('master'):
        s2 = int(r.hget(call.from_user.id, 's2'))
        if s2 < 5:
            cl = int(r.hget(call.from_user.id, 'class'))
            s22 = s2
            if cl == 12 or cl == 22:
                s22 = s2 / 2
            if int(r.hget(call.from_user.id, 'wins')) >= s22 * 250:
                if int(r.hget(call.from_user.id, 'money')) >= 100:
                    r.hincrby(call.from_user.id, 'money', -100)
                    r.hincrby(call.from_user.id, 's2', 1)
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='\u26CF Ви підняли рівень майстерності до ' + str(s2 + 1) + '.')
                    if s2 + 1 == 5:
                        intellect(2, call.from_user.id)
                        bot.send_message(call.message.chat.id, 'За досягнення найвищого рівня майстерності твій'
                                                               ' русак отримує \U0001F9E0 +2 інтелекту.')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='Недостатньо коштів на рахунку.')
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Ще рано переходити на наступний етап майтерності.')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Немає сенсу ставати ще кращим майстром.')

    elif call.data.startswith('cellar'):
        s3 = int(r.hget(call.from_user.id, 's3'))
        if s3 == 1:
            if int(r.hget(call.from_user.id, 'money')) >= 30:
                r.hincrby(call.from_user.id, 'money', -30)
                r.hincrby(call.from_user.id, 's3', 1)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Ви купили другу утеплену будку.')
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Недостатньо коштів на рахунку.')
        elif s3 == 2:
            if int(r.hget(call.from_user.id, 'money')) >= 750:
                r.hincrby(call.from_user.id, 'money', -750)
                r.hincrby(call.from_user.id, 's3', 1)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Ви купили будівельні матеріали.')
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Недостатньо коштів на рахунку.')
        elif s3 == 3:
            if r.hexists(call.from_user.id, 'name') == 1:
                st = int(int(r.hget(call.from_user.id, 'strength')) * 0.75)
                r.hset(call.from_user.id, 'strength', st)
                r.hincrby(call.from_user.id, 's3', 1)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Ви розширили місце в підвалі для додаткового русака.')
                bot.send_message(call.message.chat.id, '\U0001F412 У вас з`явився другий русак.\n'
                                                       'Змінити бойового русака можна командою /swap.')
                r.hset(call.from_user.id, 'name2', random.randrange(0, len(names)),
                       {'strength2': random.randint(10, 50),
                        'intellect2': int(random.choice(['1', '1', '1', '1', '2'])),
                        'spirit2': 0, 'weapon2': 0, 's_weapon2': 0, 'defense2': 0, 's_defense2': 0,
                        'mushrooms2': 0, 'class2': 0, 'photo2': 0, 'injure2': 0, 'hp2': 0})
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='У вас немає русака.')
        elif s3 == 4:
            if int(r.hget(call.from_user.id, 'money')) >= 1500:
                r.hincrby(call.from_user.id, 'money', -1500)
                r.hincrby(call.from_user.id, 's3', 1)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Ви купили припаси.')
                bot.send_message(call.message.chat.id, 'Тепер можна по одному годувати двох русаків. Змінити бойового'
                                                       ' русака можна командою /swap.')
                r.hset(call.from_user.id, 'time22', 0)
                r.hset(call.from_user.id, 'time23', 0)
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Недостатньо коштів на рахунку.')
        elif s3 == 5:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='У вас вже нічого будувати.')

    elif call.data.startswith('vodka'):
        if int(r.hget(call.from_user.id, 'money')) >= 2:
            r.hincrby(call.from_user.id, 'money', -2)
            cl = int(r.hget(call.from_user.id, 'class'))
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Ви успішно купили горілку "Козаки"\n\U0001F54A + ' +
                                           vodka(call.from_user.id, cl))
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Недостатньо коштів на рахунку')

    elif call.data.startswith('weapon'):
        if r.hexists(call.from_user.id, 'weapon') == 0:
            r.hset(call.from_user.id, 'weapon', 0)
        if int(r.hget(call.from_user.id, 'weapon')) == 0:
            if int(r.hget(call.from_user.id, 'money')) >= 7:
                r.hincrby(call.from_user.id, 'money', -7)
                msg = 'Ви успішно купили колючий дрин'
                if int(r.hget(call.from_user.id, 'class')) == 14 or int(r.hget(call.from_user.id, 'class')) == 24:
                    r.hset(call.from_user.id, 'weapon', 4)
                    r.hset(call.from_user.id, 's_weapon', 3)
                    msg = 'Ви успішно купили биту'
                else:
                    r.hset(call.from_user.id, 'weapon', 1)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text=msg)
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Недостатньо коштів на рахунку')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='У вас вже є зброя')

    elif call.data.startswith('defense'):
        if r.hexists(call.from_user.id, 'defense') == 0:
            r.hset(call.from_user.id, 'defense', 0)
        if int(r.hget(call.from_user.id, 'defense')) == 0:
            if int(r.hget(call.from_user.id, 'money')) >= 8:
                r.hincrby(call.from_user.id, 'money', -8)
                r.hset(call.from_user.id, 'defense', 1)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Ви успішно купили колючий щит')
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Недостатньо коштів на рахунку')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='У вас вже є захисне спорядження')

    elif call.data.startswith('passport'):
        if int(r.hget(call.from_user.id, 'money')) >= 10:
            ran = random.randrange(0, len(names))
            r.hincrby(call.from_user.id, 'money', -10)
            r.hset(call.from_user.id, 'name', ran)
            if r.hexists(call.from_user.id, 'ac3') == 0:
                r.hset(call.from_user.id, 'ac3', 1)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Ви успішно купили трофейний паспорт')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Недостатньо коштів на рахунку')

    elif call.data.startswith('cabin'):
        if r.hexists(call.from_user.id, 'cabin') == 0:
            r.hset(call.from_user.id, 'cabin', 0)
        if int(r.hget(call.from_user.id, 'cabin')) == 0:
            if int(r.hget(call.from_user.id, 'money')) >= 30:
                r.hincrby(call.from_user.id, 'money', -30)
                r.hset(call.from_user.id, 'cabin', 1)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Ви успішно купили утеплену будку')
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Недостатньо коштів на рахунку')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='У вас вже є утееплена будка')

    elif call.data.startswith('woman'):
        if r.hexists(call.from_user.id, 'woman') == 0:
            r.hset(call.from_user.id, 'woman', 0)
        if int(r.hget(call.from_user.id, 'woman')) == 0:
            if int(r.hget(call.from_user.id, 'money')) >= 150:
                r.hincrby(call.from_user.id, 'money', -150)
                r.hset(call.from_user.id, 'woman', 1)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Ви успішно купили жінку')
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Недостатньо коштів на рахунку')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='У вас вже є жінка')

    elif call.data.startswith('pipe'):
        if int(r.hget(call.from_user.id, 'woman')) == 1:
            r.hset(call.from_user.id, 'woman', 0)
            r.hset(call.from_user.id, 'time5', 0)
            r.hset(call.from_user.id, 'spirit', 1713)
            r.hincrby(call.from_user.id, 'deaths', 5)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Ви успішно проміняли жінку на тютюн та люльку.\nНеобачний.')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Недостатньо жінок на рахунку')

    elif call.data.startswith('fragment'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            if r.hexists(call.from_user.id, 'defense') == 0:
                r.hset(call.from_user.id, 'defense', 0)
            if int(r.hget(call.from_user.id, 'defense')) == 0:
                if int(r.hget(call.from_user.id, 'money')) >= 10:
                    r.hincrby(call.from_user.id, 'money', -10)
                    r.hset(call.from_user.id, 'defense', 9)
                    r.hset(call.from_user.id, 's_defense', 7)
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='Ви успішно купили уламок бронетехніки')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='Недостатньо коштів на рахунку')
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='У вас вже є захисне спорядження')
        else:
            bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id, call.message.id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('mushroom'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            if r.hexists(call.from_user.id, 'defense') == 0:
                r.hset(call.from_user.id, 'defense', 0)
            if r.hexists(call.from_user.id, 'mushrooms') == 0:
                r.hset(call.from_user.id, 'mushrooms', 0)
            if int(r.hget(call.from_user.id, 'defense')) == 0:
                mushroom = int(r.hget(call.from_user.id, 'mushrooms'))
                if int(r.hget(call.from_user.id, 'class')) == 18 or int(r.hget(call.from_user.id, 'class')) == 28:
                    mushroom = 0
                if mushroom < 3:
                    if int(r.hget(call.from_user.id, 'intellect')) < 20:
                        if int(r.hget(call.from_user.id, 'money')) >= 60:
                            r.hincrby(call.from_user.id, 'money', -60)
                            r.hset(call.from_user.id, 'defense', 10)
                            r.hincrby(call.from_user.id, 'mushrooms', 1)
                            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                      text='Ви успішно купили мухомор королівський')
                        else:
                            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                      text='Недостатньо коштів на рахунку')
                    else:
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Ваш русак вже занадто розумний')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='Для вашого русака не передбачено більше трьох мухоморів')
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='У вас вже є захисне спорядження')
        else:
            bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id, call.message.id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('equipment'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            cl = int(r.hget(call.from_user.id, 'class'))
            if cl == 1 or cl == 11 or cl == 21:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 6:
                        r.hincrby(call.from_user.id, 'money', -6)
                        r.hset(call.from_user.id, 'weapon', 11)
                        r.hset(call.from_user.id, 's_weapon', 5)
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Ви успішно купили травмат')
                    else:
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Недостатньо коштів на рахунку')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='У вас вже є зброя')

            elif cl == 2 or cl == 12 or cl == 22:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 12:
                        r.hincrby(call.from_user.id, 'money', -12)
                        r.hset(call.from_user.id, 'weapon', 12)
                        r.hset(call.from_user.id, 's_weapon', 25)
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Ви успішно купили діамантове кайло')
                    else:
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Недостатньо коштів на рахунку')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='У вас вже є зброя')

            elif cl == 3 or cl == 13 or cl == 23:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 5:
                        r.hincrby(call.from_user.id, 'money', -5)
                        r.hset(call.from_user.id, 'weapon', 13)
                        r.hset(call.from_user.id, 's_weapon', 3)
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Ви успішно купили колоду з кіоску')
                    else:
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Недостатньо коштів на рахунку')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='У вас вже є зброя')

            elif cl == 4 or cl == 14 or cl == 24:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 7:
                        r.hincrby(call.from_user.id, 'money', -7)
                        r.hset(call.from_user.id, 'weapon', 14)
                        r.hset(call.from_user.id, 's_weapon', 1)
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Ви успішно купили сокиру Перуна')
                    else:
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Недостатньо коштів на рахунку')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='У вас вже є зброя')

            elif cl == 5 or cl == 15 or cl == 25:
                if int(r.hget(call.from_user.id, 'weapon')) == 0 and \
                        int(r.hget(call.from_user.id, 'defense')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 20:
                        r.hincrby(call.from_user.id, 'money', -20)
                        r.hset(call.from_user.id, 'weapon', 15)
                        r.hset(call.from_user.id, 'defense', 15)
                        r.hset(call.from_user.id, 's_weapon', 30)
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Ви успішно купили АК-47')
                    else:
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Недостатньо коштів на рахунку')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='У вас вже є зброя або захисне спорядження')

            elif cl == 6 or cl == 16 or cl == 26:
                if int(r.hget(call.from_user.id, 'defense')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 10:
                        r.hincrby(call.from_user.id, 'money', -10)
                        r.hset(call.from_user.id, 'defense', 16)
                        r.hset(call.from_user.id, 's_defense', 10)
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Ви успішно купили поліцейський щит')
                    else:
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Недостатньо коштів на рахунку')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='У вас вже є захисне спорядження')

            elif cl == 7 or cl == 17 or cl == 27:
                if int(r.hget(call.from_user.id, 'weapon')) == 0 and \
                        int(r.hget(call.from_user.id, 'defense')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 11:
                        r.hincrby(call.from_user.id, 'money', -11)
                        r.hset(call.from_user.id, 'weapon', 17)
                        r.hset(call.from_user.id, 'defense', 17)
                        r.hset(call.from_user.id, 's_weapon', 8)
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Ви успішно купили прапор новоросії')
                    else:
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Недостатньо коштів на рахунку')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='У вас вже є зброя або захисне спорядження')

            elif cl == 8 or cl == 18 or cl == 28:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 9:
                        r.hincrby(call.from_user.id, 'money', -9)
                        r.hset(call.from_user.id, 'weapon', 18)
                        r.hset(call.from_user.id, 's_weapon', 2)
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Ви успішно купили експлойт')
                    else:
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                  text='Недостатньо коштів на рахунку')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='У вас вже є зброя')

        else:
            bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id, call.message.id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('donate'):
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                  text='Один погон коштує 25 гривень. Для отримання погонів скиньте на карту потрібну'
                                       ' суму і введіть боту в пп \n/donated <будь-яке повідомлення>'
                                       '\nНарахування погонів триватиме до 24 годин.')

    elif call.data.startswith('tf2'):
        if int(r.hget(call.from_user.id, 'strap')) >= 1 and r.hexists(call.from_user.id, 'name') == 1:
            r.hincrby(call.from_user.id, 'strap', -1)
            r.hset(call.from_user.id, 'photo', 41)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Ви успішно змінили фото русаку')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Недостатньо погонів на рахунку')
    elif call.data.startswith('ricardo'):
        if int(r.hget(call.from_user.id, 'strap')) >= 1 and r.hexists(call.from_user.id, 'name') == 1:
            r.hincrby(call.from_user.id, 'strap', -1)
            r.hset(call.from_user.id, 'photo', 42)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Ви успішно змінили фото русаку')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Недостатньо погонів на рахунку')

    elif call.data.startswith('40_packs'):
        if int(r.hget(call.from_user.id, 'strap')) >= 1:
            r.hincrby(call.from_user.id, 'strap', -1)
            r.hincrby(call.from_user.id, 'packs', 40)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Ви успішно замовили 40 донбаських пакунків')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Недостатньо погонів на рахунку')

    elif call.data.startswith('premium'):
        if int(r.hget(call.from_user.id, 'strap')) >= 1 and int(r.hget(call.from_user.id, 'class')) > 0:
            r.hincrby(call.from_user.id, 'strap', -1)
            cl = int(r.hget(call.from_user.id, 'class'))
            if cl == 1 or cl == 11 or cl == 21:
                r.hset(call.from_user.id, 'photo', 43)
            if cl == 2 or cl == 12 or cl == 22:
                r.hset(call.from_user.id, 'photo', 44)
            if cl == 3 or cl == 13 or cl == 23:
                r.hset(call.from_user.id, 'photo', 45)
            if cl == 4 or cl == 14 or cl == 24:
                r.hset(call.from_user.id, 'photo', 46)
            if cl == 5 or cl == 15 or cl == 25:
                r.hset(call.from_user.id, 'photo', 47)
            if cl == 6 or cl == 16 or cl == 26:
                r.hset(call.from_user.id, 'photo', 48)
            if cl == 7 or cl == 17 or cl == 27:
                r.hset(call.from_user.id, 'photo', 49)
            if cl == 8 or cl == 18 or cl == 28:
                r.hset(call.from_user.id, 'photo', 50)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Ви успішно змінили фото русаку')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Недостатньо погонів на рахунку, або русак без класу')
    elif call.data.startswith('glid'):
        if int(r.hget(call.from_user.id, 'strength')) < 400 and int(r.hget(call.from_user.id, 'intellect')) < 5:
            if int(r.hget(call.from_user.id, 'strap')) >= 1 and r.hexists(call.from_user.id, 'name') == 1:
                r.hincrby(call.from_user.id, 'strap', -1)
                r.hincrby(call.from_user.id, 'strength', 400)
                r.hincrby(call.from_user.id, 'intellect', 4)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Ви успішно купили настоянку глоду')
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Недостатньо погонів на рахунку')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Твій русак не отримає жодного ефекту від цього товару')
    elif call.data.startswith('course'):
        if int(r.hget(call.from_user.id, 'strap')) >= 2 and int(r.hget(call.from_user.id, 'class')) > 0:
            r.hincrby(call.from_user.id, 'strap', -2)
            r.hset(call.from_user.id, 'class', 0)
            if int(r.hget(call.from_user.id, 'intellect')) < 5:
                r.hset(call.from_user.id, 'intellect', 5)
            if int(r.hget(call.from_user.id, 'photo')) <= 40:
                r.hset(call.from_user.id, 'photo', 0)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Ви успішно купили курс перекваліфікаації русаку')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Недостатньо погонів на рахунку, або русак без класу')

    elif call.data.startswith('fast_cellar'):
        if int(r.hget(call.from_user.id, 's3')) <= 2:
            if int(r.hget(call.from_user.id, 'strap')) >= 3:
                r.hincrby(call.from_user.id, 'strap', -3)
                r.hset(call.from_user.id, 's3', 5)
                r.hset(call.from_user.id, 'name2', random.randrange(0, len(names)),
                       {'strength2': random.randint(10, 50),
                        'intellect2': int(random.choice(['1', '1', '1', '1', '2'])),
                        'spirit2': 0, 'weapon2': 0, 's_weapon2': 0, 'defense2': 0, 's_defense2': 0,
                        'mushrooms2': 0, 'class2': 0, 'photo2': 0, 'injure2': 0, 'hp2': 0})
                r.hset(call.from_user.id, 'time22', 0)
                r.hset(call.from_user.id, 'time23', 0)
                bot.send_message(call.message.chat.id, '\U0001F412 У вас з`явився другий русак.\n'
                                                       'Змінити бойового русака можна командою /swap.')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Ви успішно побудували підвал максимального рівня')
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Недостатньо погонів на рахунку')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Пізно пришвидшувати будівництво')

    elif call.data.startswith('drop_w') and call.from_user.id == call.message.reply_to_message.from_user.id:
        if int(r.hget(call.from_user.id, 'weapon')) != 0:
            if int(r.hget(call.from_user.id, 'weapon')) == 16:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Зброю мусора неможливо викинути')
            else:
                if int(r.hget(call.from_user.id, 'weapon')) == 15 or int(r.hget(call.from_user.id, 'weapon')) == 17:
                    r.hset(call.from_user.id, 'weapon', 0)
                    r.hset(call.from_user.id, 's_weapon', 0)
                    r.hset(call.from_user.id, 'defense', 0)
                    r.hset(call.from_user.id, 's_defense', 0)
                else:
                    r.hset(call.from_user.id, 'weapon', 0)
                    r.hset(call.from_user.id, 's_weapon', 0)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Русак викинув зброю')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='В твого русака нема зброї')

    elif call.data.startswith('drop_d') and call.from_user.id == call.message.reply_to_message.from_user.id:
        if int(r.hget(call.from_user.id, 'defense')) != 0:
            if int(r.hget(call.from_user.id, 'defense')) == 15 or int(r.hget(call.from_user.id, 'defense')) == 17:
                r.hset(call.from_user.id, 'weapon', 0)
                r.hset(call.from_user.id, 's_weapon', 0)
                r.hset(call.from_user.id, 'defense', 0)
                r.hset(call.from_user.id, 's_defense', 0)
            else:
                r.hset(call.from_user.id, 'defense', 0)
                r.hset(call.from_user.id, 's_defense', 0)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='Русак викинув захисне спорядження')
        else:
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='В твого русака нема захисного спорядження')

    elif call.data.startswith('unpack') and call.from_user.id == call.message.reply_to_message.from_user.id:
        uid = call.from_user.id
        cl = int(r.hget(uid, 'class'))
        if int(r.hget(uid, 'money')) >= 20 or int(r.hget(uid, 'packs')) > 0:
            if int(r.hget(uid, 'packs')) > 0:
                r.hincrby(uid, 'packs', -1)
            else:
                r.hincrby(uid, 'money', -20)
            r.hincrby(uid, 'opened', 1)

            ran = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                                 weights=[20, 18, 15, 12, 10, 7, 6, 5, 3, 2, 1, 0.45, 0.45, 0.1])
            if ran == [1]:
                bot.edit_message_text('\u26AA В пакунку знайдено лише пил і гнилі недоїдки.',
                                      call.message.chat.id, call.message.id)
            elif ran == [2]:
                bot.edit_message_text('\u26AA В цьому пакунку лежить якраз те, що потрібно твоєму русаку '
                                      '(класове спорядження)! ' + icons[cl], call.message.chat.id, call.message.id)
                if cl == 1 or cl == 11 or cl == 21:
                    if int(r.hget(uid, 'weapon')) == 11:
                        r.hincrby(uid, 's_weapon', 5)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 11)
                        r.hset(uid, 's_weapon', 5)
                elif cl == 2 or cl == 12 or cl == 22:
                    if int(r.hget(uid, 'weapon')) == 12:
                        r.hincrby(uid, 's_weapon', 25)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 12)
                        r.hset(uid, 's_weapon', 25)
                elif cl == 3 or cl == 13 or cl == 23:
                    if int(r.hget(uid, 'weapon')) == 13:
                        r.hincrby(uid, 's_weapon', 3)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 13)
                        r.hset(uid, 's_weapon', 3)
                elif cl == 4 or cl == 14 or cl == 24:
                    if int(r.hget(uid, 'weapon')) == 14:
                        r.hincrby(uid, 's_weapon', 1)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 14)
                        r.hset(uid, 's_weapon', 1)
                elif cl == 5 or cl == 15 or cl == 25:
                    if int(r.hget(uid, 'weapon')) == 15:
                        r.hincrby(uid, 's_weapon', 30)
                    elif int(r.hget(uid, 'weapon')) != 2 and int(r.hget(uid, 'defense')) != 2 \
                            and int(r.hget(uid, 'defense')) != 10:
                        r.hset(uid, 'weapon', 15)
                        r.hset(uid, 's_weapon', 30)
                        r.hset(uid, 'defense', 15)
                elif cl == 6 or cl == 16 or cl == 26:
                    if int(r.hget(uid, 'defense')) == 16:
                        r.hincrby(uid, 's_defense', 10)
                    elif int(r.hget(uid, 'defense')) != 2 and int(r.hget(uid, 'defense')) != 10:
                        r.hset(uid, 'defense', 16)
                        r.hset(uid, 's_defense', 10)
                elif cl == 7 or cl == 17 or cl == 27:
                    if int(r.hget(uid, 'weapon')) == 17:
                        r.hincrby(uid, 's_weapon', 8)
                    elif int(r.hget(uid, 'weapon')) != 2 and int(r.hget(uid, 'defense')) != 2 and \
                            int(r.hget(uid, 'defense')) != 10:
                        r.hset(uid, 'weapon', 17)
                        r.hset(uid, 's_weapon', 8)
                        r.hset(uid, 'defense', 17)
                elif cl == 8 or cl == 18 or cl == 28:
                    if int(r.hget(uid, 'weapon')) == 18:
                        r.hincrby(uid, 's_weapon', 2)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 18)
                        r.hset(uid, 's_weapon', 2)
                else:
                    bot.edit_message_text('\u26AA В цьому пакунку лежать дивні речі, якими '
                                          'русак не вміє користуватись...', call.message.chat.id, call.message.id)
            elif ran == [3]:
                bot.edit_message_text('\u26AA Знайдено: \U0001F6E1\U0001F5E1 Колючий комплект (дрин і щит).',
                                      call.message.chat.id, call.message.id)
                if cl == 6 or cl == 16 or cl == 26:
                    if int(r.hget(uid, 'defense')) != 0:
                        r.hset(uid, 'defense', 1)
                else:
                    if int(r.hget(uid, 'weapon')) == 0:
                        r.hset(uid, 'weapon', 1)
                    if int(r.hget(uid, 'defense')) == 0:
                        r.hset(uid, 'defense', 1)
            elif ran == [4]:
                bot.edit_message_text('\u26AA Знайдено: пошкоджений уламок бронетехніки (здати на металобрухт).'
                                      '\n\U0001F4B5 + 4', call.message.chat.id, call.message.id)
                r.hincrby(uid, 'money', 4)
            elif ran == [5]:
                bot.edit_message_text('\u26AA Знайдено: \U0001F6E1 Уламок бронетехніки.\n\U0001F6E1 +7',
                                      call.message.chat.id, call.message.id)
                if int(r.hget(uid, 'defense')) == 0 or int(r.hget(uid, 'defense')) == 1:
                    r.hset(uid, 'defense', 9)
                    r.hset(uid, 's_defense', 7)
                elif int(r.hget(uid, 'defense')) != 10:
                    r.hincrby(uid, 's_defense', 7)
            elif ran == [6]:
                bot.edit_message_text('\U0001f535 Знайдено: \U0001F4B5 50 гривень.',
                                      call.message.chat.id, call.message.id)
                r.hincrby(uid, 'money', 50)
            elif ran == [7]:
                bot.edit_message_text('\U0001f535 Цей пакунок виявився ящиком горілки.\n\u2622 +20',
                                      call.message.chat.id, call.message.id)
                r.hincrby(uid, 'vodka', 20)
            elif ran == [8]:
                bot.edit_message_text('\U0001f535 В цьому пакунку лежить мертвий русак...\n\u2620\uFE0F +1',
                                      call.message.chat.id, call.message.id)
                r.hincrby(uid, 'deaths', 1)
            elif ran == [9]:
                if int(r.hget(uid, 'intellect')) < 20:
                    bot.edit_message_text('\U0001f7e3 Знайдено: \U0001F6E1 Мухомор королівський.',
                                          call.message.chat.id, call.message.id)
                    if int(r.hget(uid, 'defense')) != 2:
                        r.hset(uid, 'defense', 10)
                else:
                    bot.edit_message_text('\u26AA В пакунку знайдено лише пил і гнилі недоїдки.',
                                          call.message.chat.id, call.message.id)
            elif ran == [10]:
                bot.edit_message_text('\U0001f7e3 Дивно, але в цьому пакунку знайдено тютюн та люльку...'
                                      '\n\u2620\uFE0F +5', call.message.chat.id, call.message.id)
                r.hincrby(uid, 'deaths', 5)
            elif ran == [11]:
                emoji = random.choice(['\U0001F35C', '\U0001F35D', '\U0001F35B', '\U0001F957', '\U0001F32D'])
                bot.edit_message_text('\U0001f7e3 Крім гаманця з грошима, в цьому пакунку лежить багато гнилої бараболі'
                                      ' і закруток з помідорами (можна згодувати русаку).'
                                      '\n\u2B50 +1 \U0001F4B5 +300 ' + emoji + ' +1',
                                      call.message.chat.id, call.message.id)
                r.hincrby(uid, 'money', 300)
                r.hset(uid, 'time', 0)
                if r.hexists(uid, 'ac13') == 0:
                    r.hset(uid, 'ac13', 1)
            elif ran == [12]:
                bot.edit_message_text('\U0001f7e1 В цьому пакунку знайдено неушкоджений Бронежилет вагнерівця [Захист, '
                                      'міцність=50] - зменшує силу ворога на бій на 75%.',
                                      call.message.chat.id, call.message.id)
                r.hset(uid, 'defense', 2)
                r.hset(uid, 's_defense', 50)
            elif ran == [13]:
                if cl != 6 or cl != 16 or cl != 26:
                    bot.edit_message_text('\U0001f7e1 В цьому пакунку знайдено 40-мм ручний протитанковий гранатомет '
                                          'РПГ-7 і одну гранату до нього [Атака, міцність=1] - завдає ворогу важке пор'
                                          'анення (віднімає бойовий дух і спорядження, його сила, інтелект та '
                                          'бойовий дух впадуть втричі на 200 боїв).',
                                          call.message.chat.id, call.message.id)
                    r.hset(uid, 'weapon', 2)
                    r.hset(uid, 's_weapon', 1)
                else:
                    bot.edit_message_text('\U0001f7e1 В цьому пакунку знайдено неушкоджений Бронежилет вагнерівця '
                                          '[Захист, міцність=50] - зменшує силу ворога на бій на 75%, захищає від '
                                          'важких поранень.',
                                          call.message.chat.id, call.message.id)
                    r.hset(uid, 'defense', 2)
                    r.hset(uid, 's_defense', 50)
            elif ran == [14]:
                bot.edit_message_text('\U0001f7e1 В пакунку лежить дорога парадна форма якогось російського генерала.'
                                      '\n\U0001F31F +1',
                                      call.message.chat.id, call.message.id)
                r.hincrby(uid, 'strap', 1)
        else:
            bot.edit_message_text('Недостатньо коштів на рахунку.', call.message.chat.id, call.message.id)

    elif call.data.startswith('boost'):
        if r.hexists(call.from_user.id, 'gift1') == 0:
            if bot.get_chat_member(call.message.chat.id, call.from_user.id).status == 'left':
                r.hincrby(call.from_user.id, 'packs', 5)
                r.hset(call.from_user.id, 'gift1', 1)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Дякую за інтерес проявлений до бота! '
                                               'Буду вдячний за його поширення.\n\n'
                                               '\U0001F4E6 Отримано 5 пакунків\n\n'
                                               'Підпишись на канал щоб отримати більше!')
            else:
                r.hincrby(call.from_user.id, 'packs', 10)
                r.hset(call.from_user.id, 'gift1', 2)
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Дякую за інтерес проявлений до бота! '
                                               'Буду вдячний за його поширення.\n\n'
                                               '\U0001F4E6 Отримано 10 пакунків')
        else:
            if int(r.hget(call.from_user.id, 'gift1')) == 1:
                if bot.get_chat_member(call.message.chat.id, call.from_user.id).status != 'left':
                    r.hincrby(call.from_user.id, 'packs', 5)
                    r.hset(call.from_user.id, 'gift1', 2)
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='Дякую за інтерес проявлений до бота! '
                                                   'Буду вдячний за його поширення.\n\n'
                                                   '\U0001F4E6 Отримано 5 пакунків')
                else:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                              text='Підпишись на канал, щоб отримати більше подарунків.')
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                          text='Ти вже забрав свої пакунки.')


@bot.message_handler()
def messages(message):
    try:
        if 'Кубик' in message.text or 'кубик' in message.text:
            bot.send_dice(chat_id=message.chat.id, reply_to_message_id=message.id)

        elif 'Рандом' in message.text or 'рандом' in message.text or \
                'Казино' in message.text or 'казино' in message.text:
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEIjuhhS6oNEVDkBDkBUokJJLjTBRloBAACCQADT9w1GxCgVEna0OwQIQQ',
                             reply_to_message_id=message.id)

        elif message.text == '\U0001F346':
            bot.send_sticker(message.chat.id,
                             'CAACAgEAAxkBAAEJbHxho8TpMNv1z5ilwsnv5-ls4prPZQACowgAAuN4BAABejm_DcUkS2oiBA',
                             reply_to_message_id=message.id)

        elif message.text == '\U0001F351':
            bot.send_sticker(message.chat.id,
                             'CAACAgEAAxkBAAEJbIlho8a1VzFNc2lFs2mvQpIDruqNxQAChwgAAuN4BAABd8eOV12a0r4iBA',
                             reply_to_message_id=message.id)

        elif message.text == 'Чат хуйня':
            bot.reply_to(message, '+')

        elif message.text == 'N':
            bot.send_message(message.chat.id, 'I')

        elif message.chat.type == 'private':
            if r.hexists(message.from_user.id, 'intellect') == 1:
                if int(r.hget(message.from_user.id, 'intellect')) >= 5 and \
                        int(r.hget(message.from_user.id, 'class')) == 0:
                    if message.text.startswith('Обираю клас '):
                        if 'Хач' in message.text or 'хач' in message.text:
                            ran = random.randint(1, 5)
                            r.hset(message.from_user.id, 'photo', ran)
                            bot.send_photo(message.chat.id, photo=photos[ran], caption='Ти вибрав клас Хач.')
                            r.hset(message.from_user.id, 'class', 1)
                            r.hincrby(message.from_user.id, 'strength', 100)
                            r.hset(message.from_user.id, 'hach_time', 0)
                        elif 'Роботяга' in message.text or 'роботяга' in message.text:
                            ran = random.randint(6, 10)
                            r.hset(message.from_user.id, 'photo', ran)
                            bot.send_photo(message.chat.id, photo=photos[ran], caption='Ти вибрав клас Роботяга.')
                            r.hset(message.from_user.id, 'class', 2)
                        elif 'Фокусник' in message.text or 'фокусник' in message.text:
                            ran = random.randint(11, 15)
                            r.hset(message.from_user.id, 'photo', ran)
                            bot.send_photo(message.chat.id, photo=photos[ran], caption='Ти вибрав клас Фокусник.')
                            r.hset(message.from_user.id, 'class', 3)
                            r.hincrby(message.from_user.id, 'intellect', 1)
                            intellect(1, message.from_user.id)
                        elif 'Язичник' in message.text or 'язичник' in message.text:
                            ran = random.randint(16, 20)
                            r.hset(message.from_user.id, 'photo', ran)
                            bot.send_photo(message.chat.id, photo=photos[ran], caption='Ти вибрав клас Язичник.')
                            r.hset(message.from_user.id, 'class', 4)
                        elif 'Гарматне' in message.text or 'гарматне' in message.text:
                            ran = random.randint(21, 25)
                            r.hset(message.from_user.id, 'photo', ran)
                            bot.send_photo(message.chat.id, photo=photos[ran], caption='Ти вибрав клас Гарматне м`ясо.')
                            r.hset(message.from_user.id, 'class', 5)
                        elif 'Мусор' in message.text or 'мусор' in message.text:
                            ran = random.randint(26, 30)
                            r.hset(message.from_user.id, 'photo', ran)
                            bot.send_photo(message.chat.id, photo=photos[ran], caption='Ти вибрав клас Мусор.')
                            r.hset(message.from_user.id, 'class', 6)
                            r.hset(message.from_user.id, 'weapon', 16)
                        elif 'Малорос' in message.text or 'малорос' in message.text:
                            ran = random.randint(31, 35)
                            r.hset(message.from_user.id, 'photo', ran)
                            bot.send_photo(message.chat.id, photo=photos[ran], caption='Ти вибрав клас Малорос.')
                            r.hset(message.from_user.id, 'class', 7)
                            intellect(-2, message.from_user.id)
                        elif 'Хакер' in message.text or 'хакер' in message.text:
                            ran = random.randint(36, 40)
                            r.hset(message.from_user.id, 'photo', ran)
                            bot.send_photo(message.chat.id, photo=photos[ran], caption='Ти вибрав клас Хакер.')
                            r.hset(message.from_user.id, 'class', 8)
            if int(r.hget(message.from_user.id, 'intellect')) >= 12:
                if message.text == 'Покращити русака':
                    cl = int(r.hget(message.from_user.id, 'class'))
                    if cl == 1:
                        bot.reply_to(message, 'Ти покращив хача до Борцухи.')
                        r.hset(message.from_user.id, 'class', 11)
                        r.hincrby(message.from_user.id, 'strength', 100)
                    if cl == 2:
                        bot.reply_to(message, 'Ти покращив роботягу до Почесного алкаша.')
                        r.hset(message.from_user.id, 'class', 12)
                    if cl == 3:
                        bot.reply_to(message, 'Ти покращив фокусника до Злого генія.')
                        r.hset(message.from_user.id, 'class', 13)
                        intellect(2, message.from_user.id)
                    if cl == 4:
                        bot.reply_to(message, 'Ти покращив язичника до Скінхеда.')
                        r.hset(message.from_user.id, 'class', 14)
                    if cl == 5:
                        bot.reply_to(message, 'Ти покращив гарматне м`ясо до Орка.')
                        r.hset(message.from_user.id, 'class', 15)
                    if cl == 6:
                        bot.reply_to(message, 'Ти покращив мусора до Силовика.')
                        r.hset(message.from_user.id, 'class', 16)
                    if cl == 7:
                        bot.reply_to(message, 'Ти покращив малороса до Кремлебота.')
                        r.hset(message.from_user.id, 'class', 17)
                        r.hincrby(message.from_user.id, 'money', 60)
                        r.hset(message.from_user.id, 'mushrooms', 0)
                    if cl == 8:
                        bot.reply_to(message, 'Ти покращив хакера до Кіберзлочинця.')
                        r.hset(message.from_user.id, 'class', 18)
            if int(r.hget(message.from_user.id, 'intellect')) >= 20:
                if message.text == 'Вдосконалити русака':
                    cl = int(r.hget(message.from_user.id, 'class'))
                    if cl == 11:
                        bot.reply_to(message, 'Ти покращив борцуху до Грози Кавказу.')
                        r.hset(message.from_user.id, 'class', 21)
                        r.hset(message.from_user.id, 'hach_time2', 0)
                        r.hincrby(message.from_user.id, 'strength', 100)
                    if cl == 12:
                        bot.reply_to(message, 'Ти покращив почесного алкаша до П`яного майстра.')
                        r.hset(message.from_user.id, 'class', 22)
                        r.hset(message.from_user.id, 'worker', 0)
                    if cl == 13:
                        bot.reply_to(message, 'Ти покращив злого генія до Некроманта.')
                        r.hset(message.from_user.id, 'class', 23)
                    if cl == 14:
                        bot.reply_to(message, 'Ти покращив скінхеда до Білого вождя.')
                        r.hset(message.from_user.id, 'class', 24)
                    if cl == 15:
                        bot.reply_to(message, 'Ти покращив орка до Героя Новоросії.')
                        r.hset(message.from_user.id, 'class', 25)
                    if cl == 16:
                        bot.reply_to(message, 'Ти покращив силовика до Товариша майора.')
                        r.hset(message.from_user.id, 'class', 26)
                    if cl == 17:
                        bot.reply_to(message, 'Ти покращив кремлебота до Агента ФСБ.')
                        r.hset(message.from_user.id, 'class', 27)
                        r.hincrby(message.from_user.id, 'money', 100)
                    if cl == 18:
                        bot.reply_to(message, 'Ти покращив кіберзлочинця до Black Hat.')
                        r.hset(message.from_user.id, 'class', 28)

    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: len(query.query) == 0)
def default_query(inline_query):
    markup = types.InlineKeyboardMarkup()
    try:
        call = 'fight' + str(inline_query.from_user.first_name) + ',' + str(inline_query.from_user.id)
        r1 = types.InlineQueryResultArticle('1', 'Бій русаків',
                                            types.InputTextMessageContent(
                                                str(prepare_to_fight(inline_query.from_user.id,
                                                                     inline_query.from_user.first_name,
                                                                     inline_query.query))),
                                            reply_markup=markup.add(types.InlineKeyboardButton(text='Атакувати!',
                                                                                               callback_data=call)),
                                            thumb_url='https://i.ibb.co/0nFNwSH/rusak.png',
                                            description='надери комусь дупу\nнапиши & щоб відкрити інші режими')
        r2 = types.InlineQueryResultArticle('2', 'Ким ти був в минулому житті?',
                                            types.InputTextMessageContent(
                                                str('Ким ти був в минулому житті?\n\n' + pastLife())),
                                            thumb_url='https://i.ibb.co/mJ0SXzL/Past-lives'
                                                      '-2-56a6ede63df78cf772910470.jpg',
                                            description='можливо, воно було не таке нікчемне як зараз')
        r3 = types.InlineQueryResultArticle('3', 'Куди ти поїдеш на заробітки?',
                                            types.InputTextMessageContent(
                                                str('Куди ти поїдеш на заробітки?\n\n' + earnings())),
                                            thumb_url='https://i.ibb.co/ypDcLNc/Polunytsya-e1538080073461.jpg',
                                            description='добре там є, де нас нема')
        r4 = types.InlineQueryResultArticle('4', 'Визнач свої політичні координати',
                                            types.InputTextMessageContent(
                                                str('Мої політичні координати\n\n' + political())),
                                            thumb_url='https://i.ibb.co/XbGNVSS/maxresdefault.jpg',
                                            description='правачок чи лібераха?')
        r5 = types.InlineQueryResultArticle('5', 'Наскільки ви підходите один одному?',
                                            types.InputTextMessageContent('*звук мовчання*'),
                                            thumb_url='https://i.ibb.co/QDkHD0b/telltaale.jpg',
                                            description='вибирай дівку і залицяйся')
        r6 = types.InlineQueryResultArticle('6', 'Питай, що турбує',
                                            types.InputTextMessageContent('*звук мовчання*'),
                                            thumb_url=(
                                                'https://i.ibb.co/qkjYFDF/im610x343-Zelensky-notebook.jpg'),
                                            description='ну тобто треба щось написати')
        r7 = types.InlineQueryResultArticle('7', 'Зрадометр',
                                            types.InputTextMessageContent(str(zradoMoga())),
                                            thumb_url='https://i.ibb.co/7GJzmc4/Ea-PHB6-EWs-AAVER4.jpg',
                                            description='допоможе визначитись з певною подією')
        r8 = types.InlineQueryResultArticle('8', 'Якого розміру в тебе пісюн?',
                                            types.InputTextMessageContent(str(penis())),
                                            thumb_url='https://i.ibb.co/3FQYpgB/photo-2020-08-27-14-49-33.jpg',
                                            description='роздягайся')
        r9 = types.InlineQueryResultArticle('9', 'Вибір з кількох варіантів',
                                            types.InputTextMessageContent('*звук мовчання*'),
                                            thumb_url='https://i.ibb.co/HtK6FTR/o-1ej2111rn189p9qrabv1au81o1o1k.jpg',
                                            description='наприклад, "Бути чи/або не бути?"')
        r10 = types.InlineQueryResultArticle('10', 'Вибери для себе пиво',
                                             types.InputTextMessageContent('Бот радить тобі...\n\n' + beer()),
                                             thumb_url='https://i.ibb.co/rZbG1fD/image.jpg',
                                             description='або для когось іншого')
        r11 = types.InlineQueryResultArticle('11', 'Генератор випадкових чисел',
                                             types.InputTextMessageContent(generator(inline_query.query)),
                                             thumb_url='https://i.ibb.co/3TZsnyj/randomn.png',
                                             description='введи від 1 до 3 чисел (перші два проміжок, третє кількість)')
        r12 = types.InlineQueryResultArticle('12', 'Визнач своє походження',
                                             types.InputTextMessageContent('Моє походження:\n\n' + race()),
                                             thumb_url='https://i.ibb.co/7V4QmDL/nations.png',
                                             description='зараз бот проаналізує твої ДНК...')
        r13 = types.InlineQueryResultArticle('13', 'Який в тебе гендер?',
                                             types.InputTextMessageContent(gender()),
                                             thumb_url='https://i.ibb.co/LrH2D0W/gender.jpg',
                                             description='все дуже серйозно')
        bot.answer_inline_query(inline_query.id, [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13], cache_time=0)
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: query.query.startswith('&'))
def default_query(inline_query):
    markup = types.InlineKeyboardMarkup()
    markup2 = types.InlineKeyboardMarkup()
    markup3 = types.InlineKeyboardMarkup()
    try:
        call = 'fight' + str(inline_query.from_user.first_name) + ',' + \
               str(inline_query.from_user.id) + ',' + str(inline_query.query)
        call1 = 'fight' + str(inline_query.from_user.first_name) + ',' + \
                str(inline_query.from_user.id) + ',' + 'private,' + str(inline_query.query)
        call2 = 'fight' + str(inline_query.from_user.first_name) + ',' + \
                str(inline_query.from_user.id) + ',' + 'tournament,' + str(inline_query.query)
        r1 = types.InlineQueryResultArticle('1', 'Пошук суперника по силі',
                                            types.InputTextMessageContent(
                                                str(prepare_to_fight(inline_query.from_user.id,
                                                                     inline_query.from_user.first_name,
                                                                     inline_query.query))),
                                            reply_markup=markup.add(types.InlineKeyboardButton(text='Атакувати!',
                                                                                               callback_data=call)),
                                            thumb_url='https://i.ibb.co/0nFNwSH/rusak.png',
                                            description='введи різницю сили (мінімум 1)')
        r2 = types.InlineQueryResultArticle('2', 'Особисте запрошення',
                                            types.InputTextMessageContent(
                                                str(prepare_to_fight(inline_query.from_user.id,
                                                                     inline_query.from_user.first_name,
                                                                     'особисте_запрошення_2021' + inline_query.query))),
                                            reply_markup=markup2.add(types.InlineKeyboardButton(text='Атакувати!',
                                                                                                callback_data=call1)),
                                            thumb_url='https://i.ibb.co/0nFNwSH/rusak.png',
                                            description='введи @username')

        r3 = types.InlineQueryResultArticle('3', 'Турнірний режим',
                                            types.InputTextMessageContent(
                                                str(prepare_to_fight(inline_query.from_user.id,
                                                                     inline_query.from_user.first_name,
                                                                     'турнірний_режим_2021' + inline_query.query))),
                                            reply_markup=markup3.add(types.InlineKeyboardButton(text='Атакувати!',
                                                                                                callback_data=call2)),
                                            thumb_url='https://i.ibb.co/0nFNwSH/rusak.png',
                                            description='Режим Best of 5. Можна ввести @username. Без нагород.')
        bot.answer_inline_query(inline_query.id, [r1, r2, r3], cache_time=0)
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: len(query.query) > 0)
def custom_query(inline_query):
    try:
        r1 = types.InlineQueryResultArticle('1', str('Ким ' + inline_query.query + ' був в минулому житті?'),
                                            types.InputTextMessageContent(
                                                str('Ким ' + inline_query.query + ' був в минулому житті?\n\n' +
                                                    pastLife())),
                                            thumb_url='https://i.ibb.co/mJ0SXzL/Past-lives'
                                                      '-2-56a6ede63df78cf772910470.jpg',
                                            description='можливо, воно було не таке нікчемне як зараз')
        r2 = types.InlineQueryResultArticle('2', 'Куди ' + inline_query.query + ' поїде на заробітки?',
                                            types.InputTextMessageContent(
                                                str('Куди ' + inline_query.query + ' поїде на заробітки?\n\n' +
                                                    earnings())),
                                            thumb_url='https://i.ibb.co/ypDcLNc/Polunytsya-e1538080073461.jpg',
                                            description='добре там є, де нас нема')
        r3 = types.InlineQueryResultArticle('3', 'Визнач ' + inline_query.query + ' політичні координати',
                                            types.InputTextMessageContent(
                                                str(inline_query.query + ' політичні координати\n\n' + political())),
                                            thumb_url='https://i.ibb.co/XbGNVSS/maxresdefault.jpg',
                                            description='правачок чи лібераха?')
        r4 = types.InlineQueryResultArticle('4', 'Наскільки ви з ' + inline_query.query + ' підходите один одному?',
                                            types.InputTextMessageContent(
                                                str('Ви з ' + inline_query.query + ' підходите один одному на ' +
                                                    love())),
                                            thumb_url='https://i.ibb.co/QDkHD0b/telltaale.jpg',
                                            description='вибирай дівку і залицяйся')
        r5 = types.InlineQueryResultArticle('5', 'Питай, що турбує',
                                            types.InputTextMessageContent(
                                                str('\u2753 ' + inline_query.query + '\n\n' + question())),
                                            thumb_url=(
                                                'https://i.ibb.co/qkjYFDF/im610x343-Zelensky-notebook.jpg'),
                                            description='ну тобто треба щось написати')
        r6 = types.InlineQueryResultArticle('6', 'Зрадометр',
                                            types.InputTextMessageContent(
                                                str(inline_query.query + '\n\n' + zradoMoga())),
                                            thumb_url='https://i.ibb.co/7GJzmc4/Ea-PHB6-EWs-AAVER4.jpg',
                                            description='допоможе визначитись з певною подією')
        r7 = types.InlineQueryResultArticle('7', 'Якого розміру в тебе пісюн?',
                                            types.InputTextMessageContent(str(penis())),
                                            thumb_url='https://i.ibb.co/3FQYpgB/photo-2020-08-27-14-49-33.jpg',
                                            description='роздягайся')
        r8 = types.InlineQueryResultArticle('8', 'Вибір з кількох варіантів',
                                            types.InputTextMessageContent('\u2753' + inline_query.query +
                                                                          '\n\n' + choose(inline_query.query)),
                                            thumb_url='https://i.ibb.co/HtK6FTR/o-1ej2111rn189p9qrabv1au81o1o1k.jpg',
                                            description='наприклад, "Бути чи/або не бути?"')
        r9 = types.InlineQueryResultArticle('9', 'Вибери для ' + inline_query.query + ' пиво',
                                            types.InputTextMessageContent(
                                                 inline_query.query + ', я рекомендую тобі тобі...\n\n' + beer()),
                                            thumb_url='https://i.ibb.co/rZbG1fD/image.jpg',
                                            description='або для когось іншого')
        r10 = types.InlineQueryResultArticle('10', 'Генератор випадкових чисел',
                                             types.InputTextMessageContent(generator(inline_query.query)),
                                             thumb_url='https://i.ibb.co/3TZsnyj/randomn.png',
                                             description='введи від 1 до 3 чисел (перші два проміжок, третє кількість)')
        r11 = types.InlineQueryResultArticle('11', 'Визнач ' + inline_query.query + ' походження',
                                             types.InputTextMessageContent(
                                                 'Походження ' + inline_query.query + ':\n\n' + race()),
                                             thumb_url='https://i.ibb.co/7V4QmDL/nations.png',
                                             description='зараз бот проаналізує твої ДНК...')
        r12 = types.InlineQueryResultArticle('12', 'Який в тебе гендер?',
                                             types.InputTextMessageContent(gender()),
                                             thumb_url='https://i.ibb.co/LrH2D0W/gender.jpg',
                                             description='все дуже серйозно')
        bot.answer_inline_query(inline_query.id, [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12], cache_time=0)
    except Exception as e:
        print(e)


server = Flask(__name__)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=os.environ.get('APP_URL') + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
