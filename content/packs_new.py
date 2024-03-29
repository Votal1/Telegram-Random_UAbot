from config import r
from random import choice, choices, randint
from methods import checkClan, q_points
from parameters import vodka, increase_trance, hp, spirit
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from constants.classes import icons_simple
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

                ran = choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                              weights=[20, 18, 15, 12, 10, 7, 6, 5, 2, 1, 2, 1, 0.225, 0.225, 0.225, 0.225, 0.1])
                if ran == [1]:
                    if checkClan(uid, base=2, building='new_post') and choice([0, 1]) == 1:
                        if int(r.hget('c' + r.hget(uid, 'clan').decode(), 'buff_4')) == 41 and \
                                int(r.hget('c' + r.hget(uid, 'clan').decode(), 'q-points')) < 500:
                            msg = '\u26AA В пакунку знайдено робочу радіотехніку.\n\U0001fa99 +1'
                            q_points(uid, 1)
                        else:
                            msg = '\u26AA В пакунку знайдено робочу радіотехніку.\n\U0001F4FB +1'
                            r.hincrby('c' + r.hget(uid, 'clan').decode(), 'technics', 1)
                        quest(uid, 3, 3, 3)
                    else:
                        msg = '\u26AA В пакунку знайдено лише пил і гнилі недоїдки.'
                elif ran == [2]:
                    msg = '\u26AA В цьому пакунку лежить якраз те, що потрібно твоєму русаку (класове спорядження)! ' \
                          + icons_simple[cl]
                    if cl in (1, 11, 21) and int(r.hget(uid, 'weapon')) in (11, 22, 33):
                        r.hincrby(uid, 's_weapon', 5)
                    elif cl in (2, 12, 22) and int(r.hget(uid, 'weapon')) in (12, 23, 34):
                        r.hincrby(uid, 's_weapon', 25)
                    elif cl in (3, 13, 23) and int(r.hget(uid, 'weapon')) in (13, 24, 35):
                        r.hincrby(uid, 's_weapon', 3)
                    elif cl in (4, 14, 24) and int(r.hget(uid, 'weapon')) in (14, 25, 36):
                        r.hincrby(uid, 's_weapon', 1)
                    elif cl in (5, 15, 25) and int(r.hget(uid, 'weapon')) in (15, 26, 37):
                        r.hincrby(uid, 's_weapon', 30)
                    elif cl in (6, 16, 26) and int(r.hget(uid, 'defense')) in (16, 17, 18):
                        r.hincrby(uid, 's_defense', 10)
                    elif cl in (7, 17, 27) and int(r.hget(uid, 'weapon')) in (17, 28, 38):
                        r.hincrby(uid, 's_weapon', 8)
                    elif cl in (8, 18, 28) and int(r.hget(uid, 'weapon')) in (18, 29, 39):
                        r.hincrby(uid, 's_weapon', 2)
                    elif cl in (9, 19, 29) and int(r.hget(uid, 'weapon')) in (19, 30, 40):
                        r.hincrby(uid, 's_weapon', 8)
                    elif cl in (10, 20, 30) and int(r.hget(uid, 'weapon')) in (20, 31, 41):
                        r.hincrby(uid, 's_weapon', 10)
                    elif cl in (31, 32, 33) and int(r.hget(uid, 'support')) in (2, 9, 14):
                        r.hincrby(uid, 's_support', 5)
                    elif cl in (34, 35, 36) and int(r.hget(uid, 'weapon')) in (21, 32, 42):
                        r.hincrby(uid, 's_weapon', 15)
                    elif cl > 0:
                        markup.add(InlineKeyboardButton(text='Взяти спорядження', callback_data=f'pack_class_{uid}'))
                        msg += '\n#loot'
                    else:
                        msg = '\u26AA В цьому пакунку лежать дивні речі, якими русак не вміє користуватись...'
                elif ran == [3]:
                    msg = '\u26AA Знайдено: \U0001F6E1\U0001F5E1 Колючий комплект (дрин і щит).'
                    if int(r.hget(uid, 'weapon')) in (0, 16):
                        r.hset(uid, 'weapon', 1)
                        r.hset(uid, 's_weapon', 1)
                    elif int(r.hget(uid, 'weapon')) in (1, 7):
                        r.hincrby(uid, 's_weapon', 1)
                    if int(r.hget(uid, 'defense')) == 0:
                        r.hset(uid, 'defense', 1)
                        r.hset(uid, 's_defense', 1)
                    elif int(r.hget(uid, 'defense')) in (1, 4):
                        r.hincrby(uid, 's_defense', 1)
                elif ran == [4]:
                    msg = '\u26AA Знайдено: пошкоджений уламок бронетехніки (здати на металобрухт).\n\U0001F4B5 + 4'
                    r.hincrby(uid, 'money', 4)
                    quest(uid, 3, 1, 4)
                elif ran == [5]:
                    msg = '\u26AA Знайдено: \U0001F6E1 Уламок бронетехніки.\n'
                    quest(uid, 3, 3, 1)
                    if int(r.hget(uid, 'defense')) == 0:
                        r.hset(uid, 'defense', 9)
                        r.hset(uid, 's_defense', 7)
                        msg += '\U0001F6E1 7'
                    elif int(r.hget(uid, 'defense')) not in (1, 3, 4):
                        r.hincrby(uid, 's_defense', 7)
                        msg += '\U0001F6E1 +7'
                    else:
                        r.hincrby(uid, 'money', 10)
                        msg += '\U0001F4B5 +10'
                        quest(uid, 3, 1, 4)
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
                    num = 1
                    quest(uid, 1, -4)
                    if choice([1, 2, 3]) == 1 and int(r.hget(uid, 's5')) >= 2:
                        num = randint(2, 3)
                        msg = f'\U0001f535 В цьому пакунку лежать мертві русаки...\n\u2620\uFE0F +{num}'
                    r.hincrby(uid, 'deaths', num)
                    r.hincrby('all_deaths', 'deaths', num)
                elif ran == [9]:
                    if int(r.hget(uid, 'intellect')) < 20:
                        msg = '\U0001f7e3 Знайдено: \U0001F344 Мухомор королівський [Допомога, міцність=1] ' \
                              '- якщо в дуелі у ворога більший інтелект, додає +1 інтелекту.'
                        if int(r.hget(uid, 'support')) != 6:
                            markup.add(InlineKeyboardButton(text='Взяти мухомор', callback_data=f'pack_mushroom_{uid}'))
                            msg += '\n#loot'
                        elif int(r.hget(uid, 'support')) == 6:
                            r.hincrby(uid, 's_support', 1)
                    else:
                        msg = '\u26AA В пакунку знайдено лише пил і гнилі недоїдки.'
                elif ran == [10]:
                    extra = r.hget(uid, 'extra_slot')
                    if extra:
                        extra = int(extra) + 1
                    else:
                        extra = 1
                    ran = randint(1, extra)
                    r.hincrby(uid, 'tape', ran)
                    msg = f'\U0001f7e3 В пакунку знайдено ізострічку - незамінний компонент для покращення ' \
                          f'спорядження\n🌀 +{ran}'
                elif ran == [11]:
                    msg = '\U0001f7e3 В пакунку знайдено кілька упаковок фольги. З неї можна зробити непогану шапку ' \
                          'для русака.\n\U0001F464 +10'
                    r.hincrby(uid, 'sch', 10)
                    if int(r.hget(uid, 'head')) in (1, 7):
                        r.hincrby(uid, 's_head', 20)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти шапочку', callback_data=f'pack_foil_{uid}'))
                        msg += '\n#loot'
                elif ran == [12]:
                    emoji = choice(['\U0001F35C', '\U0001F35D', '\U0001F35B', '\U0001F957', '\U0001F32D'])
                    msg = '\U0001f7e3 Крім гаманця з грошима, в цьому пакунку лежить багато гнилої бараболі і ' \
                          'закруток з помідорами (можна згодувати русаку).\n\u2B50 +1 \U0001F4B5 +300 ' + emoji + ' +1'
                    r.hincrby(uid, 'money', 300)
                    r.hset(uid, 'time', 0)
                    if r.hexists(uid, 'ac13') == 0:
                        r.hset(uid, 'ac13', 1)
                    quest(uid, 3, 1, 4)

                elif ran == [13]:
                    msg = '\U0001f7e1 В цьому пакунку знайдено неушкоджений Бронежилет вагнерівця [Захист, ' \
                          'міцність=50] - зменшує силу ворога на бій на 75% та захищає від РПГ-7.'
                    if int(r.hget(uid, 'defense')) == 2:
                        r.hincrby(uid, 's_defense', 50)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти бронежилет', callback_data=f'pack_armor_{uid}'))
                        msg += '\n#loot'

                elif ran == [14]:
                    msg = '\U0001f7e1 В цьому пакунку знайдено 40-мм ручний протитанковий гранатомет РПГ-7 і одну ' \
                          'гранату до нього [Зброя, міцність=1] - завдає ворогу, який має більше ніж 2000 сили, ' \
                          'важке поранення (віднімає бойовий ' \
                          'дух, здоров`я і все спорядження, на 300 боїв бойовий дух впаде вдвічі а сила втричі).'
                    if int(r.hget(uid, 'weapon')) == 2:
                        r.hincrby(uid, 's_weapon', 1)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти РПГ-7', callback_data=f'pack_rpg_{uid}'))
                        msg += '\n#loot'

                elif ran == [15]:
                    markup.add(InlineKeyboardButton(text='Взяти Швайнокарася', callback_data=f'pack_fish_{uid}'))
                    msg = '\U0001f7e1 Швайнокарась [Допомога, міцність=3, максимальна_міцність=3] - ' \
                          'може виконувати бажання русаків (відпочивати, нажертись, напитись).\n#loot'
                elif ran == [16]:
                    msg = '\U0001f7e1 Ярмулка [Шапка, міцність=7, невразлива_до_РПГ] - надає доступ до кошерних ' \
                          'квестів (вдвічі більша нагорода, але і більша складність їх виконання). 100% шанс ' \
                          'отримати сіль в соляних шахтах. Міцність зменшується при взятті квестів.'
                    if int(r.hget(uid, 'head')) == 6:
                        r.hincrby(uid, 's_head', 7)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти ярмулку', callback_data=f'pack_jew_{uid}'))
                        msg += '\n#loot'
                elif ran == [17]:
                    msg = '\U0001f7e1 В пакунку лежить дорога парадна форма якогось російського генерала.\n' \
                          '\U0001F31F +1'
                    r.hincrby(uid, 'strap', 1)
            else:
                msg = 'Недостатньо коштів на рахунку.'

            return msg, markup

        elif cdata.startswith('pack_class_'):
            if cl == 1 or cl == 11 or cl == 21:
                if int(r.hget(uid, 'weapon')) in (11, 22, 33):
                    r.hincrby(uid, 's_weapon', 5)
                else:
                    r.hset(uid, 'weapon', 11)
                    r.hset(uid, 's_weapon', 5)
            elif cl == 2 or cl == 12 or cl == 22:
                if int(r.hget(uid, 'weapon')) in (12, 23, 34):
                    r.hincrby(uid, 's_weapon', 25)
                else:
                    r.hset(uid, 'weapon', 12)
                    r.hset(uid, 's_weapon', 25)
            elif cl == 3 or cl == 13 or cl == 23:
                if int(r.hget(uid, 'weapon')) in (13, 24, 35):
                    r.hincrby(uid, 's_weapon', 3)
                else:
                    r.hset(uid, 'weapon', 13)
                    r.hset(uid, 's_weapon', 3)
            elif cl == 4 or cl == 14 or cl == 24:
                if int(r.hget(uid, 'weapon')) in (14, 25, 36):
                    r.hincrby(uid, 's_weapon', 1)
                else:
                    r.hset(uid, 'weapon', 14)
                    r.hset(uid, 's_weapon', 1)
            elif cl == 5 or cl == 15 or cl == 25:
                if int(r.hget(uid, 'weapon')) in (15, 26, 37):
                    r.hincrby(uid, 's_weapon', 30)
                else:
                    r.hset(uid, 'weapon', 15)
                    r.hset(uid, 's_weapon', 30)
            elif cl == 6 or cl == 16 or cl == 26:
                if int(r.hget(uid, 'defense')) in (16, 17, 18):
                    r.hincrby(uid, 's_defense', 10)
                else:
                    r.hset(uid, 'defense', 16)
                    r.hset(uid, 's_defense', 10)
            elif cl == 7 or cl == 17 or cl == 27:
                if int(r.hget(uid, 'weapon')) in (17, 28, 38):
                    r.hincrby(uid, 's_weapon', 8)
                else:
                    r.hset(uid, 'weapon', 17)
                    r.hset(uid, 's_weapon', 8)
            elif cl == 8 or cl == 18 or cl == 28:
                if int(r.hget(uid, 'weapon')) in (18, 29, 39):
                    r.hincrby(uid, 's_weapon', 2)
                else:
                    r.hset(uid, 'weapon', 18)
                    r.hset(uid, 's_weapon', 2)
            elif cl == 9 or cl == 19 or cl == 29:
                if int(r.hget(uid, 'weapon')) in (19, 30, 40):
                    r.hincrby(uid, 's_weapon', 8)
                else:
                    r.hset(uid, 'weapon', 19)
                    r.hset(uid, 's_weapon', 8)
            elif cl == 10 or cl == 20 or cl == 30:
                if int(r.hget(uid, 'weapon')) in (20, 31, 41):
                    r.hincrby(uid, 's_weapon', 10)
                else:
                    r.hset(uid, 'weapon', 20)
                    r.hset(uid, 's_weapon', 10)
            elif cl == 31 or cl == 32 or cl == 33:
                if int(r.hget(uid, 'support')) in (2, 9, 14):
                    r.hincrby(uid, 's_support', 5)
                else:
                    r.hset(uid, 'support', 2)
                    r.hset(uid, 's_support', 5)
            elif cl == 34 or cl == 35 or cl == 36:
                if int(r.hget(uid, 'weapon')) in (21, 32, 42):
                    r.hincrby(uid, 's_weapon', 15)
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
            if int(r.hget(uid, 'head')) in (1, 7):
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


def check_slot(uid, cdata):
    stats = r.hmget(uid, 'class', 'weapon', 'defense', 'support', 'head')
    cl, w, d, s, h = int(stats[0]), int(stats[1]), int(stats[2]), int(stats[3]), int(stats[4]),
    if cdata.startswith('pack_class_'):
        if cl in (6, 16, 26):
            if d in (0, 16, 17, 18):
                return True
        elif cl in (31, 32, 33):
            if s in (0, 2, 9, 14):
                return True
        else:
            if w == 0 or 10 < w < 43:
                return True
    elif cdata.startswith('pack_rpg_'):
        if w in (0, 2, 16):
            return True
    elif cdata.startswith('pack_armor_'):
        if d in (0, 2):
            return True
    elif cdata.startswith('pack_mushroom_'):
        if s in (0, 6):
            return True
    elif cdata.startswith('pack_fish_'):
        if s in (0, 10):
            return True
    elif cdata.startswith('pack_foil_'):
        if h in (0, 1, 7):
            return True
    elif cdata.startswith('pack_jew_'):
        if h in (0, 6):
            return True
    return False


def open_pack2(uid, cdata, edit, count):
    markup = InlineKeyboardMarkup()
    msg = ''
    if uid == int(cdata.split('_')[2]):
        cl = int(r.hget(uid, 'class'))
        if cdata.startswith('pack_unpack_'):
            if int(r.hget(uid, 'money')) >= 20 or int(r.hget(uid, 'packs')) >= count:
                if int(r.hget(uid, 'packs')) >= count:
                    r.hincrby(uid, 'packs', -count)
                else:
                    r.hincrby(uid, 'money', -20)
                r.hincrby(uid, 'opened', 1)
                r.hincrby('all_opened', 'packs', 1)
                quest(uid, 1, -5)

                rewards = {
                    'nothing': 0,
                    'class': 0,
                    'spike': 0,
                    '4grn': 0,
                    'fragment': 0,
                    '50grn': 0,
                    'vodka': 0,
                    'dead': 0,
                    'mushroom': 0,
                    'foil': 0,
                    'tape': 0,
                    '300grn': 0,
                    'rpg': 0,
                    'armor': 0,
                    'fish': 0,
                    'cap': 0,
                    'strap': 0
                }

                for n in range(count):
                    ran = choices([
                        'nothing',
                        'class',
                        'spike',
                        '4grn',
                        'fragment',
                        '50grn',
                        'vodka',
                        'dead',
                        'mushroom',
                        'tape',
                        'foil',
                        '300grn',
                        'rpg',
                        'armor',
                        'fish',
                        'cap',
                        'strap'
                    ],
                        weights=[20, 18, 15, 12, 10, 7, 6, 5, 2, 1, 2, 1, 0.225, 0.225, 0.225, 0.225, 0.1])
                    rewards[ran[0]] += 1
                if rewards['nothing']:
                    np = checkClan(uid, base=2, building='new_post')
                    buff = points_limit = False
                    technics = nothing = points = 0
                    if np:
                        buff = int(r.hget('c' + r.hget(uid, 'clan').decode(), 'buff_4')) == 41
                        points = int(r.hget('c' + r.hget(uid, 'clan').decode(), 'q-points')) < 500
                    for n in range(rewards['nothing']):
                        if np and choice([0, 1]) == 1:
                            if buff and points_limit:
                                points += 1
                            else:
                                technics += 1
                        else:
                            nothing += 1
                    if nothing:
                        if count > 1:
                            msg += f'\n\u26AA Пил і гнилі недоїдки - {nothing}'
                        else:
                            msg += '\u26AA В пакунку знайдено лише пил і гнилі недоїдки.'
                    if technics:
                        quest(uid, 3, 3, 3)
                        r.hincrby('c' + r.hget(uid, 'clan').decode(), 'technics', technics)
                        if count > 1:
                            msg += f'\n\u26AA \U0001F4FB +{technics}'
                        else:
                            msg += f'\u26AA В пакунку знайдено робочу радіотехніку.\n\U0001F4FB +{technics}'
                    if points:
                        quest(uid, 3, 3, 3)
                        q_points(uid, points)
                        if count > 1:
                            msg += f'\n\u26AA \U0001fa99 +{points}'
                        else:
                            msg += f'\u26AA В пакунку знайдено робочу радіотехніку.\n\U0001fa99 +{points}'
                if rewards['class']:
                    if count == 1:
                        msg = f'\u26AA В цьому пакунку лежить якраз те, що потрібно твоєму русаку ' \
                              f'(класове спорядження)! {icons_simple[cl]}'
                        if cl in (1, 11, 21) and int(r.hget(uid, 'weapon')) in (11, 22, 33):
                            r.hincrby(uid, 's_weapon', 5)
                        elif cl in (2, 12, 22) and int(r.hget(uid, 'weapon')) in (12, 23, 34):
                            r.hincrby(uid, 's_weapon', 25)
                        elif cl in (3, 13, 23) and int(r.hget(uid, 'weapon')) in (13, 24, 35):
                            r.hincrby(uid, 's_weapon', 3)
                        elif cl in (4, 14, 24) and int(r.hget(uid, 'weapon')) in (14, 25, 36):
                            r.hincrby(uid, 's_weapon', 1)
                        elif cl in (5, 15, 25) and int(r.hget(uid, 'weapon')) in (15, 26, 37):
                            r.hincrby(uid, 's_weapon', 30)
                        elif cl in (6, 16, 26) and int(r.hget(uid, 'defense')) in (16, 17, 18):
                            r.hincrby(uid, 's_defense', 10)
                        elif cl in (7, 17, 27) and int(r.hget(uid, 'weapon')) in (17, 28, 38):
                            r.hincrby(uid, 's_weapon', 8)
                        elif cl in (8, 18, 28) and int(r.hget(uid, 'weapon')) in (18, 29, 39):
                            r.hincrby(uid, 's_weapon', 2)
                        elif cl in (9, 19, 29) and int(r.hget(uid, 'weapon')) in (19, 30, 40):
                            r.hincrby(uid, 's_weapon', 8)
                        elif cl in (10, 20, 30) and int(r.hget(uid, 'weapon')) in (20, 31, 41):
                            r.hincrby(uid, 's_weapon', 10)
                        elif cl in (31, 32, 33) and int(r.hget(uid, 'support')) in (2, 9, 14):
                            r.hincrby(uid, 's_support', 5)
                        elif cl in (34, 35, 36) and int(r.hget(uid, 'weapon')) in (21, 32, 42):
                            r.hincrby(uid, 's_weapon', 15)
                        if cl > 0:
                            markup.add(InlineKeyboardButton(text='Взяти спорядження',
                                                            callback_data=f'pack_class_{uid}'))
                            msg += '\n#loot'
                        else:
                            msg = '\u26AA В цьому пакунку лежать дивні речі, якими русак не вміє користуватись...'
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти спорядження',
                                                        callback_data=f'pack_class_{uid}_{rewards["class"]}'))
                        msg += f'\n\u26AA {icons_simple[cl]} - {rewards["class"]}'
                if rewards['spike']:
                    if count == 1:
                        msg = '\u26AA Знайдено: \U0001F6E1\U0001F5E1 Колючий комплект (дрин і щит).'
                    else:
                        msg += f'\n\u26AA \U0001F6E1\U0001F5E1 - {rewards["spike"]}'
                    if int(r.hget(uid, 'weapon')) in (0, 16):
                        r.hset(uid, 'weapon', 1)
                        r.hset(uid, 's_weapon', rewards['spike'])
                    elif int(r.hget(uid, 'weapon')) in (1, 7):
                        r.hincrby(uid, 's_weapon', rewards['spike'])
                    if int(r.hget(uid, 'defense')) == 0:
                        r.hset(uid, 'defense', 1)
                        r.hset(uid, 's_defense', rewards['spike'])
                    elif int(r.hget(uid, 'defense')) in (1, 4):
                        r.hincrby(uid, 's_defense', rewards['spike'])
                if rewards['4grn']:
                    money = rewards['fragment'] * 4
                    if count == 1:
                        msg = '\n\u26AA Знайдено: пошкоджений уламок бронетехніки (здати на металобрухт).' \
                              f'\n\U0001F4B5 +{money}'
                    else:
                        msg += f'\n\u26AA \U0001F4B5 +{money}'
                    r.hincrby(uid, 'money', money)
                    quest(uid, 3, 1, 4)
                if rewards['fragment']:
                    strength = rewards['fragment']
                    if count == 1:
                        msg = '\u26AA Знайдено: \U0001F6E1 Уламок бронетехніки.\n'
                    quest(uid, 3, 3, 1)
                    if int(r.hget(uid, 'defense')) == 0:
                        r.hset(uid, 'defense', 9)
                        r.hset(uid, 's_defense', strength * 7)
                        if count == 1:
                            msg += '\U0001F6E1 7'
                        else:
                            msg += f'\n\u26AA \U0001F6E1 +{strength * 7}'
                    elif int(r.hget(uid, 'defense')) not in (1, 3, 4, 6):
                        r.hincrby(uid, 's_defense', strength * 7)
                        if count == 1:
                            msg += '\U0001F6E1 +7'
                        else:
                            msg += f'\n\u26AA \U0001F6E1 +{strength * 7}'
                    else:
                        r.hincrby(uid, 'money', strength * 10)
                        if count == 1:
                            msg += '\U0001F4B5 +10'
                        else:
                            msg += f'\n\u26AA \U0001F4B5 +{strength * 10}'
                        quest(uid, 3, 1, 4)
                if rewards['50grn']:
                    if count == 1:
                        msg = '\U0001f535 Знайдено: \U0001F4B5 50 гривень.'
                    else:
                        msg += f'\n\U0001f535 \U0001F4B5 +{rewards["50grn"] * 50}'
                    r.hincrby(uid, 'money', rewards['50grn'] * 50)
                    quest(uid, 3, 1, 4)
                if rewards['vodka']:
                    vo = 0
                    for v in range(rewards['vodka'] * 20):
                        if vo < 10000:
                            vo += int(vodka(uid))
                    if vo > 10000:
                        vo = 10000
                    if count == 1:
                        msg = f'\U0001f535 Цей пакунок виявився ящиком горілки.\n\u2622 +20 \U0001F54A +{vo}'
                    else:
                        msg += f'\n\U0001f535 \u2622 +{rewards["vodka"]}'
                if rewards['dead']:
                    quest(uid, 1, -4)
                    s5 = int(r.hget(uid, 's5')) >= 2
                    num = 0
                    for n in range(rewards['dead']):
                        num += 1
                        if choice([1, 2, 3]) == 1 and s5:
                            num += randint(1, 2)
                    if count == 1:
                        msg = f'\U0001f535 В цьому пакунку лежать мертві русаки...\n\u2620\uFE0F +{num}'
                    else:
                        msg += f'\n\U0001f535 \u2620\uFE0F +{num}'
                    r.hincrby(uid, 'deaths', num)
                    r.hincrby('all_deaths', 'deaths', num)
                if rewards['mushroom']:
                    mushroom = rewards['mushroom']
                    if int(r.hget(uid, 'intellect')) < 20:
                        if count == 1:
                            msg = '\U0001f7e3 Знайдено: \U0001F344 Мухомор королівський [Допомога, міцність=1] ' \
                                  '- якщо в дуелі у ворога більший інтелект, додає +1 інтелекту.\n#loot'
                        if int(r.hget(uid, 'support')) != 6:
                            markup.add(InlineKeyboardButton(text='Взяти мухомор',
                                                            callback_data=f'pack_mushroom_{uid}_{mushroom}'))
                        elif int(r.hget(uid, 'support')) == 6:
                            r.hincrby(uid, 's_support', mushroom)
                    else:
                        if count == 1:
                            msg = '\u26AA В пакунку знайдено лише пил і гнилі недоїдки.'
                        else:
                            msg += f'\n\U0001f7e3 \U0001F344 +{mushroom}'
                if rewards['tape']:
                    extra = r.hget(uid, 'extra_slot')
                    if extra:
                        extra = int(extra) + 1
                    else:
                        extra = 1
                    ran = 0
                    for n in range(rewards['tape']):
                        ran += randint(1, extra)
                    r.hincrby(uid, 'tape', ran)
                    if count == 1:
                        msg = f'\U0001f7e3 В пакунку знайдено ізострічку - незамінний компонент для покращення ' \
                              f'спорядження\n🌀 +{ran}'
                    else:
                        msg += f'\n\U0001f7e3 🌀 +{ran}'
                if rewards['foil']:
                    ran = rewards['foil']
                    if count == 1:
                        msg = '\U0001f7e3 В пакунку знайдено кілька упаковок фольги. З неї можна зробити' \
                              ' непогану шапку для русака.\n\U0001F464 +10'
                    else:
                        msg += f'\n\U0001f7e3 \U0001F464 +{ran * 10}'
                    r.hincrby(uid, 'sch', ran * 10)
                    if int(r.hget(uid, 'head')) in (1, 7) and count == 1:
                        r.hincrby(uid, 's_head', ran * 20)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти шапочку', callback_data=f'pack_foil_{uid}_{ran}'))
                        if count == 1:
                            msg += '\n#loot'
                if rewards['300grn']:
                    ran = rewards['300grn']
                    emoji = choice(['\U0001F35C', '\U0001F35D', '\U0001F35B', '\U0001F957', '\U0001F32D'])
                    if count == 1:
                        msg = f'\U0001f7e3 Крім гаманця з грошима, в цьому пакунку лежить багато гнилої бараболі і ' \
                              f'закруток з помідорами (можна згодувати русаку).\n\u2B50 +1 \U0001F4B5 +300 {emoji} +1'
                    else:
                        msg += f'\n\U0001f7e3 \U0001F4B5 +{ran * 300} {emoji} +1'
                    r.hincrby(uid, 'money', ran * 300)
                    r.hset(uid, 'time', 0)
                    if r.hexists(uid, 'ac13') == 0:
                        r.hset(uid, 'ac13', 1)
                    quest(uid, 3, 1, 4)
                if rewards['armor']:
                    ran = rewards['armor']
                    if count == 1:
                        msg = '\U0001f7e1 В цьому пакунку знайдено неушкоджений Бронежилет вагнерівця [Захист, ' \
                              'міцність=50] - зменшує силу ворога на бій на 75% та захищає від РПГ-7.'
                    else:
                        msg += f'\n\U0001f7e1 Бронежилет вагнерівця - {ran}'
                    if int(r.hget(uid, 'defense')) == 2 and count == 1:
                        r.hincrby(uid, 's_defense', 50)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти бронежилет',
                                                        callback_data=f'pack_armor_{uid}_{ran}'))
                        if count == 1:
                            msg += '\n#loot'
                if rewards['rpg']:
                    ran = rewards['rpg']
                    if count == 1:
                        msg = '\U0001f7e1 В цьому пакунку знайдено 40-мм ручний протитанковий гранатомет РПГ-7 і одну' \
                              ' гранату до нього [Зброя, міцність=1] - завдає ворогу, який має більше ніж 2000 сили, ' \
                              'важке поранення (віднімає бойовий ' \
                              'дух, здоров`я і все спорядження, на 300 боїв бойовий дух впаде вдвічі а сила втричі).'
                    else:
                        msg += f'\n\U0001f7e1 РПГ-7 - {ran}'
                    if int(r.hget(uid, 'weapon')) == 2 and count == 1:
                        r.hincrby(uid, 's_weapon', 1)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти РПГ-7', callback_data=f'pack_rpg_{uid}_{ran}'))
                        if count == 1:
                            msg += '\n#loot'
                if rewards['fish']:
                    ran = rewards['fish']
                    markup.add(InlineKeyboardButton(text='Взяти Швайнокарася', callback_data=f'pack_fish_{uid}_{ran}'))
                    if count == 1:
                        msg = '\U0001f7e1 Швайнокарась [Допомога, міцність=3, максимальна_міцність=3] - ' \
                              'може виконувати бажання русаків (відпочивати, нажертись, напитись).\n#loot'
                    else:
                        msg += f'\n\U0001f7e1 Швайнокарась - {ran}'
                if rewards['cap']:
                    ran = rewards['cap']
                    if count == 1:
                        msg = '\U0001f7e1 Ярмулка [Шапка, міцність=7, невразлива_до_РПГ] - надає доступ до кошерних ' \
                              'квестів (вдвічі більша нагорода, але і більша складність їх виконання). 100% шанс ' \
                              'отримати сіль в соляних шахтах. Міцність зменшується при взятті квестів.'
                    else:
                        msg += f'\n\U0001f7e1 Ярмулка - {ran}'
                    if int(r.hget(uid, 'head')) == 6 and count == 1:
                        r.hincrby(uid, 's_head', 7)
                    else:
                        markup.add(InlineKeyboardButton(text='Взяти ярмулку', callback_data=f'pack_jew_{uid}_{ran}'))
                        if count == 1:
                            msg += '\n#loot'
                if rewards['strap']:
                    ran = rewards['strap']
                    if count == 1:
                        msg = '\U0001f7e1 В пакунку лежить дорога парадна форма якогось російського генерала.\n' \
                              '\U0001F31F +1'
                    else:
                        msg += f'\n\U0001f7e1 \U0001F31F +{ran}'
                    r.hincrby(uid, 'strap', ran)
            else:
                msg = 'Недостатньо коштів на рахунку.'

            return msg, markup

        elif cdata.startswith('pack_class_'):
            if cl == 1 or cl == 11 or cl == 21:
                if int(r.hget(uid, 'weapon')) in (11, 22, 33):
                    r.hincrby(uid, 's_weapon', 5)
                else:
                    r.hset(uid, 'weapon', 11)
                    r.hset(uid, 's_weapon', 5)
            elif cl == 2 or cl == 12 or cl == 22:
                if int(r.hget(uid, 'weapon')) in (12, 23, 34):
                    r.hincrby(uid, 's_weapon', 25)
                else:
                    r.hset(uid, 'weapon', 12)
                    r.hset(uid, 's_weapon', 25)
            elif cl == 3 or cl == 13 or cl == 23:
                if int(r.hget(uid, 'weapon')) in (13, 24, 35):
                    r.hincrby(uid, 's_weapon', 3)
                else:
                    r.hset(uid, 'weapon', 13)
                    r.hset(uid, 's_weapon', 3)
            elif cl == 4 or cl == 14 or cl == 24:
                if int(r.hget(uid, 'weapon')) in (14, 25, 36):
                    r.hincrby(uid, 's_weapon', 1)
                else:
                    r.hset(uid, 'weapon', 14)
                    r.hset(uid, 's_weapon', 1)
            elif cl == 5 or cl == 15 or cl == 25:
                if int(r.hget(uid, 'weapon')) in (15, 26, 37):
                    r.hincrby(uid, 's_weapon', 30)
                else:
                    r.hset(uid, 'weapon', 15)
                    r.hset(uid, 's_weapon', 30)
            elif cl == 6 or cl == 16 or cl == 26:
                if int(r.hget(uid, 'defense')) in (16, 17, 18):
                    r.hincrby(uid, 's_defense', 10)
                else:
                    r.hset(uid, 'defense', 16)
                    r.hset(uid, 's_defense', 10)
            elif cl == 7 or cl == 17 or cl == 27:
                if int(r.hget(uid, 'weapon')) in (17, 28, 38):
                    r.hincrby(uid, 's_weapon', 8)
                else:
                    r.hset(uid, 'weapon', 17)
                    r.hset(uid, 's_weapon', 8)
            elif cl == 8 or cl == 18 or cl == 28:
                if int(r.hget(uid, 'weapon')) in (18, 29, 39):
                    r.hincrby(uid, 's_weapon', 2)
                else:
                    r.hset(uid, 'weapon', 18)
                    r.hset(uid, 's_weapon', 2)
            elif cl == 9 or cl == 19 or cl == 29:
                if int(r.hget(uid, 'weapon')) in (19, 30, 40):
                    r.hincrby(uid, 's_weapon', 8)
                else:
                    r.hset(uid, 'weapon', 19)
                    r.hset(uid, 's_weapon', 8)
            elif cl == 10 or cl == 20 or cl == 30:
                if int(r.hget(uid, 'weapon')) in (20, 31, 41):
                    r.hincrby(uid, 's_weapon', 10)
                else:
                    r.hset(uid, 'weapon', 20)
                    r.hset(uid, 's_weapon', 10)
            elif cl == 31 or cl == 32 or cl == 33:
                if int(r.hget(uid, 'support')) in (2, 9, 14):
                    r.hincrby(uid, 's_support', 5)
                else:
                    r.hset(uid, 'support', 2)
                    r.hset(uid, 's_support', 5)
            elif cl == 34 or cl == 35 or cl == 36:
                if int(r.hget(uid, 'weapon')) in (21, 32, 42):
                    r.hincrby(uid, 's_weapon', 15)
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
            if int(r.hget(uid, 'head')) in (1, 7):
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
