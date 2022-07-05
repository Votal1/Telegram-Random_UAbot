from config import r
from random import choice, choices
from methods import checkClan
from variables import icons
from parameters import vodka
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from content.quests import quest


def open_pack(uid, cdata, edit):
    markup = InlineKeyboardMarkup()
    msg = ''
    if uid == int(cdata.split('_')[2]):
        cl = int(r.hget(uid, 'class'))
        if cdata.startswith('pack_unpack_'):
            if int(r.hget(uid, 'money')) >= 20 or int(r.hget(uid, 'packs')) > 0:
                if int(r.hget(uid, 'packs')) > 0:
                    r.hincrby(uid, 'packs', -1)
                else:
                    r.hincrby(uid, 'money', -20)
                r.hincrby(uid, 'opened', 1)
                r.hincrby('all_opened', 'packs', 1)
                quest(uid, 1, -5)

                ran = choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                              weights=[20, 18, 15, 12, 10, 7, 6, 5, 3, 2, 1, 0.225, 0.225, 0.225, 0.225, 0.1])
                if ran == [1]:
                    if checkClan(uid, base=2, building='new_post') and choice([0, 1]) == 1:
                        msg = '\u26AA В пакунку знайдено робочу радіотехніку.\n\U0001F4FB +1'
                        r.hincrby('c' + r.hget(uid, 'clan').decode(), 'technics', 1)
                    else:
                        msg = '\u26AA В пакунку знайдено лише пил і гнилі недоїдки.'
                elif ran == [2]:
                    msg = '\u26AA В цьому пакунку лежить якраз те, що потрібно твоєму русаку (класове спорядження)! ' \
                          + icons[cl]
                    if cl in (1, 11, 21) and int(r.hget(uid, 'weapon')) in (11, 22):
                        r.hincrby(uid, 's_weapon', 5)
                        if int(r.hget(uid, 's_weapon')) >= 50:
                            r.hset(uid, 'weapon', 22)
                    elif cl in (2, 12, 22) and int(r.hget(uid, 'weapon')) in (12, 23):
                        r.hincrby(uid, 's_weapon', 25)
                        if int(r.hget(uid, 's_weapon')) >= 250:
                            r.hset(uid, 'weapon', 23)
                    elif cl in (3, 13, 23) and int(r.hget(uid, 'weapon')) in (13, 24):
                        r.hincrby(uid, 's_weapon', 3)
                        if int(r.hget(uid, 's_weapon')) >= 30:
                            r.hset(uid, 'weapon', 24)
                    elif cl in (4, 14, 24) and int(r.hget(uid, 'weapon')) in (14, 25):
                        r.hincrby(uid, 's_weapon', 1)
                        if int(r.hget(uid, 's_weapon')) >= 10:
                            r.hset(uid, 'weapon', 25)
                    elif cl in (5, 15, 25) and int(r.hget(uid, 'weapon')) in (15, 26):
                        r.hincrby(uid, 's_weapon', 30)
                        if int(r.hget(uid, 's_weapon')) >= 300:
                            r.hset(uid, 'weapon', 26)
                    elif cl in (6, 16, 26) and int(r.hget(uid, 'defense')) in (16, 27):
                        r.hincrby(uid, 's_defense', 10)
                        if int(r.hget(uid, 's_defense')) >= 100:
                            r.hset(uid, 'defense', 17)
                    elif cl in (7, 17, 27) and int(r.hget(uid, 'weapon')) in (17, 28):
                        r.hincrby(uid, 's_weapon', 8)
                        if int(r.hget(uid, 's_weapon')) >= 80:
                            r.hset(uid, 'weapon', 28)
                    elif cl in (8, 18, 28) and int(r.hget(uid, 'weapon')) in (18, 29):
                        r.hincrby(uid, 's_weapon', 2)
                        if int(r.hget(uid, 's_weapon')) >= 20:
                            r.hset(uid, 'weapon', 29)
                    elif cl in (9, 19, 29) and int(r.hget(uid, 'weapon')) in (19, 30):
                        r.hincrby(uid, 's_weapon', 8)
                        if int(r.hget(uid, 's_weapon')) >= 80:
                            r.hset(uid, 'weapon', 30)
                    elif cl in (10, 20, 30) and int(r.hget(uid, 'weapon')) in (20, 31):
                        r.hincrby(uid, 's_weapon', 10)
                        if int(r.hget(uid, 's_weapon')) >= 100:
                            r.hset(uid, 'weapon', 31)
                    elif cl in (31, 32, 33) and int(r.hget(uid, 'support')) in (2, 9):
                        r.hincrby(uid, 's_support', 5)
                        if int(r.hget(uid, 's_support')) >= 50:
                            r.hset(uid, 'support', 9)
                    elif cl in (34, 35, 36) and int(r.hget(uid, 'weapon')) in (21, 32):
                        r.hincrby(uid, 's_weapon', 15)
                        if int(r.hget(uid, 's_weapon')) >= 150:
                            r.hset(uid, 'weapon', 32)
                    elif cl > 0:
                        markup.add(InlineKeyboardButton(text='Взяти спорядження', callback_data=f'pack_class_{uid}'))
                    else:
                        msg = '\u26AA В цьому пакунку лежать дивні речі, якими русак не вміє користуватись...'
                elif ran == [3]:
                    msg = '\u26AA Знайдено: \U0001F6E1\U0001F5E1 Колючий комплект (дрин і щит).'
                    if int(r.hget(uid, 'weapon')) == 0:
                        r.hset(uid, 'weapon', 1)
                        r.hset(uid, 's_weapon', 1)
                    elif int(r.hget(uid, 'weapon')) == 1:
                        r.hincrby(uid, 's_weapon', 1)
                    if int(r.hget(uid, 'defense')) == 0:
                        r.hset(uid, 'defense', 1)
                        r.hset(uid, 's_defense', 1)
                    elif int(r.hget(uid, 'defense')) == 1:
                        r.hincrby(uid, 's_defense', 1)
                elif ran == [4]:
                    msg = '\u26AA Знайдено: пошкоджений уламок бронетехніки (здати на металобрухт).\n\U0001F4B5 + 4'
                    r.hincrby(uid, 'money', 4)
                    quest(uid, 3, 1, 4)
                elif ran == [5]:
                    msg = '\u26AA Знайдено: \U0001F6E1 Уламок бронетехніки.\n\U0001F6E1 +7'
                    quest(uid, 3, 3, 1)
                    if int(r.hget(uid, 'defense')) == 0 or int(r.hget(uid, 'defense')) == 1 or \
                            int(r.hget(uid, 'defense')) == 3:
                        r.hset(uid, 'defense', 9)
                        r.hset(uid, 's_defense', 7)
                    else:
                        r.hincrby(uid, 's_defense', 7)
                elif ran == [6]:
                    msg = '\U0001f535 Знайдено: \U0001F4B5 50 гривень.'
                    r.hincrby(uid, 'money', 50)
                    quest(uid, 3, 1, 4)
                elif ran == [7]:
                    vo = 0
                    for v in range(20):
                        vo += int(vodka(uid))
                    msg = f'\U0001f535 Цей пакунок виявився ящиком горілки.\n\u2622 +20 \U0001F54A +{vo}'
                elif ran == [8]:
                    msg = '\U0001f535 В цьому пакунку лежить мертвий русак...\n\u2620\uFE0F +1'
                    r.hincrby(uid, 'deaths', 1)
                    r.hincrby('all_deaths', 'deaths', 1)
                    quest(uid, 1, -4)
                elif ran == [9]:
                    if int(r.hget(uid, 'intellect')) < 20:
                        if int(r.hget(uid, 'support')) != 6:
                            markup.add(InlineKeyboardButton(text='Взяти мухохор', callback_data=f'pack_mushroom_{uid}'))
                        elif int(r.hget(uid, 'support')) == 6:
                            r.hincrby(uid, 's_support', 1)
                        msg = '\U0001f7e3 Знайдено: \U0001F6E1 Мухомор королівський.'
                    else:
                        msg = '\u26AA В пакунку знайдено лише пил і гнилі недоїдки.'
                elif ran == [10]:
                    msg = '\U0001f7e3 В пакунку знайдено кілька упаковок фольги. З неї можна зробити непогану шапку ' \
                          'для русака.\n\U0001F464 +10'
                    r.hincrby(uid, 'sch', 10)
                    if int(r.hget(uid, 'head')) == 1:
                        r.hincrby(uid, 's_head', 20)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти шапочку', callback_data=f'pack_foil_{uid}'))
                elif ran == [11]:
                    emoji = choice(['\U0001F35C', '\U0001F35D', '\U0001F35B', '\U0001F957', '\U0001F32D'])
                    msg = '\U0001f7e3 Крім гаманця з грошима, в цьому пакунку лежить багато гнилої бараболі і ' \
                          'закруток з помідорами (можна згодувати русаку).\n\u2B50 +1 \U0001F4B5 +300 ' + emoji + ' +1'
                    r.hincrby(uid, 'money', 300)
                    r.hset(uid, 'time', 0)
                    if r.hexists(uid, 'ac13') == 0:
                        r.hset(uid, 'ac13', 1)
                    quest(uid, 3, 1, 4)
                elif ran == [12]:
                    if int(r.hget(uid, 'defense')) == 2:
                        r.hincrby(uid, 's_defense', 50)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти бронежилет', callback_data=f'pack_armor_{uid}'))
                        msg = '\U0001f7e1 В цьому пакунку знайдено неушкоджений Бронежилет вагнерівця [Захист, ' \
                              'міцність=50] - зменшує силу ворога на бій на 75% та захищає від РПГ-7.'

                elif ran == [13]:
                    if int(r.hget(uid, 'weapon')) == 2:
                        r.hincrby(uid, 's_weapon', 1)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти РПГ-7', callback_data=f'pack_rpg_{uid}'))
                    msg = '\U0001f7e1 В цьому пакунку знайдено 40-мм ручний протитанковий гранатомет РПГ-7 і одну ' \
                          'гранату до нього [Атака, міцність=1] - завдає ворогу важке поранення (віднімає бойовий ' \
                          'дух, здоров`я і все спорядження, на 300 боїв бойовий дух впаде вдвічі а сила втричі).'
                elif ran == [14]:
                    if int(r.hget(uid, 'support')) == 10:
                        r.hset(uid, 's_support', 3)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти Швайнокарася', callback_data=f'pack_fish_{uid}'))
                    msg = '\U0001f7e1 Швайнокарась [Допомога, міцність=3, максимальна_міцність=3] - ' \
                          'може виконувати бажання русаків (відпочивати, нажертись, напитись).'
                elif ran == [15]:
                    if int(r.hget(uid, 'head')) == 6:
                        r.hset(uid, 's_head', 6)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти ярмулку', callback_data=f'pack_jew_{uid}'))
                    msg = '\U0001f7e1 Ярмулка [Шапка, міцність=, імунітет_до_РПГ] - надає доступ до кошерних квестів' \
                          ' (вдвічі більша нагорода, але і більша складність їх виконання). 100% шанс отримати ' \
                          'сіль в соляних шахтах. Міцність зменшується при взятті квестів.'
                elif ran == [16]:
                    msg = '\U0001f7e1 В пакунку лежить дорога парадна форма якогось російського генерала.\n' \
                          '\U0001F31F +1'
                    r.hincrby(uid, 'strap', 1)
            else:
                msg = 'Недостатньо коштів на рахунку.'

            return msg, markup

        elif cdata.startswith('pack_class_'):
            if cl == 1 or cl == 11 or cl == 21:
                if int(r.hget(uid, 'weapon')) in (11, 22):
                    r.hincrby(uid, 's_weapon', 5)
                    if int(r.hget(uid, 's_weapon')) >= 50:
                        r.hset(uid, 'weapon', 22)
                else:
                    r.hset(uid, 'weapon', 11)
                    r.hset(uid, 's_weapon', 5)
            elif cl == 2 or cl == 12 or cl == 22:
                if int(r.hget(uid, 'weapon')) in (12, 23):
                    r.hincrby(uid, 's_weapon', 25)
                    if int(r.hget(uid, 's_weapon')) >= 250:
                        r.hset(uid, 'weapon', 23)
                else:
                    r.hset(uid, 'weapon', 12)
                    r.hset(uid, 's_weapon', 25)
            elif cl == 3 or cl == 13 or cl == 23:
                if int(r.hget(uid, 'weapon')) in (13, 24):
                    r.hincrby(uid, 's_weapon', 3)
                    if int(r.hget(uid, 's_weapon')) >= 30:
                        r.hset(uid, 'weapon', 24)
                else:
                    r.hset(uid, 'weapon', 13)
                    r.hset(uid, 's_weapon', 3)
            elif cl == 4 or cl == 14 or cl == 24:
                if int(r.hget(uid, 'weapon')) in (14, 25):
                    r.hincrby(uid, 's_weapon', 1)
                    if int(r.hget(uid, 's_weapon')) >= 10:
                        r.hset(uid, 'weapon', 25)
                else:
                    r.hset(uid, 'weapon', 14)
                    r.hset(uid, 's_weapon', 1)
            elif cl == 5 or cl == 15 or cl == 25:
                if int(r.hget(uid, 'weapon')) in (15, 26):
                    r.hincrby(uid, 's_weapon', 30)
                    if int(r.hget(uid, 's_weapon')) >= 300:
                        r.hset(uid, 'weapon', 26)
                else:
                    r.hset(uid, 'weapon', 15)
                    r.hset(uid, 's_weapon', 30)
            elif cl == 6 or cl == 16 or cl == 26:
                if int(r.hget(uid, 'defense')) in (16, 17):
                    r.hincrby(uid, 's_defense', 10)
                    if int(r.hget(uid, 's_defense')) >= 100:
                        r.hset(uid, 'defense', 17)
                else:
                    r.hset(uid, 'defense', 16)
                    r.hset(uid, 's_defense', 10)
            elif cl == 7 or cl == 17 or cl == 27:
                if int(r.hget(uid, 'weapon')) in (17, 28):
                    r.hincrby(uid, 's_weapon', 8)
                    if int(r.hget(uid, 's_weapon')) >= 80:
                        r.hset(uid, 'weapon', 28)
                else:
                    r.hset(uid, 'weapon', 17)
                    r.hset(uid, 's_weapon', 8)
            elif cl == 8 or cl == 18 or cl == 28:
                if int(r.hget(uid, 'weapon')) in (18, 29):
                    r.hincrby(uid, 's_weapon', 2)
                    if int(r.hget(uid, 's_weapon')) >= 20:
                        r.hset(uid, 'weapon', 29)
                else:
                    r.hset(uid, 'weapon', 18)
                    r.hset(uid, 's_weapon', 2)
            elif cl == 9 or cl == 19 or cl == 29:
                if int(r.hget(uid, 'weapon')) in (19, 30):
                    r.hincrby(uid, 's_weapon', 8)
                    if int(r.hget(uid, 's_weapon')) >= 80:
                        r.hset(uid, 'weapon', 30)
                else:
                    r.hset(uid, 'weapon', 19)
                    r.hset(uid, 's_weapon', 8)
            elif cl == 10 or cl == 20 or cl == 30:
                if int(r.hget(uid, 'weapon')) in (20, 31):
                    r.hincrby(uid, 's_weapon', 10)
                    if int(r.hget(uid, 's_weapon')) >= 100:
                        r.hset(uid, 'weapon', 31)
                else:
                    r.hset(uid, 'weapon', 20)
                    r.hset(uid, 's_weapon', 10)
            elif cl == 31 or cl == 32 or cl == 33:
                if int(r.hget(uid, 'support')) in (2, 9):
                    r.hincrby(uid, 's_support', 5)
                    if int(r.hget(uid, 's_support')) >= 50:
                        r.hset(uid, 'support', 9)
                else:
                    r.hset(uid, 'support', 2)
                    r.hset(uid, 's_support', 5)
            elif cl == 34 or cl == 35 or cl == 36:
                if int(r.hget(uid, 'weapon')) in (21, 32):
                    r.hincrby(uid, 's_weapon', 15)
                    if int(r.hget(uid, 's_weapon')) >= 150:
                        r.hset(uid, 'weapon', 32)
                else:
                    r.hset(uid, 'weapon', 21)
                    r.hset(uid, 's_weapon', 15)
            return edit, None

        elif cdata.startswith('pack_mushroom_'):
            if int(r.hget(uid, 'intellect')) < 20:
                if int(r.hget(uid, 'support')) == 6:
                    r.hincrby(uid, 's_support', 1)
                else:
                    r.hset(uid, 'support', 6)
                    r.hset(uid, 's_support', 1)
            return edit, None

        elif cdata.startswith('pack_foil_'):
            if int(r.hget(uid, 'head')) == 1:
                r.hincrby(uid, 's_head', 20)
            else:
                r.hset(uid, 'head', 1)
                r.hset(uid, 's_head', 20)
            return edit, None

        elif cdata.startswith('pack_armor_'):
            if int(r.hget(uid, 'defense')) == 2:
                r.hincrby(uid, 's_defense', 50)
            else:
                r.hset(uid, 'defense', 2)
                r.hset(uid, 's_defense', 50)
            return edit, None

        elif cdata.startswith('pack_rpg_'):
            if int(r.hget(uid, 'weapon')) == 2:
                r.hincrby(uid, 's_weapon', 1)
            else:
                r.hset(uid, 'weapon', 2)
                r.hset(uid, 's_weapon', 1)
            return edit, None

        elif cdata.startswith('pack_fish_'):
            if int(r.hget(uid, 'support')) == 10:
                r.hset(uid, 's_support', 3)
            else:
                r.hset(uid, 'support', 10)
                r.hset(uid, 's_support', 3)
            return edit, None

        elif cdata.startswith('pack_jew_'):
            if int(r.hget(uid, 'head')) == 6:
                r.hincrby(uid, 's_head', 7)
            else:
                r.hset(uid, 'head', 6)
                r.hset(uid, 's_head', 7)
            return edit, None

        else:
            return False

    return False
