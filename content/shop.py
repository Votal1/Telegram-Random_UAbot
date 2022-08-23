from config import r
from methods import checkClan
from random import choices, choice
from variables import default, chm, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from content.quests import quest


def shop_msg(uid, mode):
    markup = InlineKeyboardMarkup()
    msg = ''
    if mode == 1:
        items = {'\u2622 Горілка "Козаки" - 2 грн': 'vodka', '\U0001F5E1 Колючий дрин - 4 грн': 'weapon',
                 '\U0001F6E1 Колючий щит - 5 грн': 'defense', '\U0001F9EA Аптечка - 4 грн': 'aid_kit',
                 '\U0001F4B3 Трофейний паспорт - 10 грн': 'passport', '\U0001F3DA Утеплена будка - 30 грн': 'cabin',
                 '\U0001F469\U0001F3FB Жінка - 150 грн': 'woman', '\U0001F6AC Тютюн та люлька - 1 жінка': 'pipe'}
        for key, value in items.items():
            if value == 'cabin' and r.hexists(uid, 'cabin') and int(r.hget(uid, 'cabin')) == 1:
                pass
            else:
                markup.add(InlineKeyboardButton(text=key, callback_data=value))
        markup.add(InlineKeyboardButton(text='\U0001F31F', callback_data='switch2'),
                   InlineKeyboardButton(text='\U0001F9C2', callback_data='switch3'))
        money = r.hget(uid, 'money').decode()
        msg = f'\U0001F4B5 Гривні: {money}\n\nОсь опис товарів, які можна придбати:\n\n\u2622 Горілка "Козаки" - ' \
              f'збільшує русаку бойовий дух на 10-70.\n\U0001F5E1 Колючий дрин [Атака]- зменшує перед боєм ' \
              f'бойовий дух ворогу, якщо атакувати його (не використовується, якщо бойовий дух ворога менший ' \
              f'за 300, обнуляє, якщо від 300 до 1000, зменшує на 1000, якщо від 1000 до 2500 і зменшує на ' \
              f'20/30/40%, якщо бойовий дух більше 2500).\n\U0001F6E1 Колючий щит [Захист] - працює так само ' \
              f'як дрин, тільки знижує бойовий дух тому, хто атакує.\n\U0001F9EA Аптечка [Допомога, міцність=5]' \
              f' - збільшує здоров`я на 5 і на 10 кожного бою.\n\U0001F4B3 Трофейний паспорт - поміняє ім`я ' \
              f'русака на інше, випадкове.\n\U0001F3DA Утеплена будка - 15 додаткової сили при кожному ' \
              f'годуванні русака (до 2000 сили). \n\U0001F469\U0001F3FB Жінка - раз в 9 днів народжуватиме ' \
              f'смачне російське немовля. Жінку треба провідувати кожен день командою \n/woman\n\U0001F6AC Тютюн ' \
              f'та люлька - на це можна проміняти жінку і піти в козацький похід (бойовий дух русака збільшиться ' \
              f'на 5000, а кількість вбитих русаків збільшиться на 5).'

    elif mode == 2:
        items = {'\U0001F943 Настоянка глоду - \U0001F31F 1 погон': 'hawthorn',
                 '\U0001F4E6 40 пакунків - \U0001F31F 1 погон': '40_packs',
                 '\u2721\uFE0F Ярмулка - \U0001F31F 1 погон': 'jew',
                 '\U0001F9FE Ресурси - \U0001F31F 2 погони': 'buy_resources',
                 '\U0001F3E0 Велике будівництво - \U0001F31F 3 погони': 'fast_cellar',
                 '\U0001F393 Курс перекваліфікації - \U0001F31F 4 погони': 'course'}
        markup.add(InlineKeyboardButton(text='\U0001F304 - \U0001F31F 1', callback_data='premium1'),
                   InlineKeyboardButton(text='\U0001F307 - \U0001F31F 1', callback_data='premium3'),
                   InlineKeyboardButton(text='\U0001F309 - \U0001F31F 1', callback_data='premium4'))
        for key, value in items.items():
            markup.add(InlineKeyboardButton(text=key, callback_data=value))
        markup.add(InlineKeyboardButton(text='\U0001F4B5', callback_data='switch1'),
                   InlineKeyboardButton(text='\U0001F9C2', callback_data='switch3'))
        strap = r.hget(uid, 'strap').decode()
        msg = f'\U0001F31F Погони російських генералів: {strap}\n\nОсь опис товарів, які можна придбати:\n\n' \
              f'\U0001F4F8 Заміна фото русака (ціна 1 погон):\n\U0001F304 Класове преміум фото 1 (Кадиров, Обеме, ' \
              f'Горшок, Тесак, Захарченко, Дерек Шовін, Янукович, Petya, Джонні Сінс, Чікатіло, Раян Гослінг, ' \
              f'Шойгу).\n\U0001F307 Класове преміум фото 2 (Хасбулла, Стаханов, Мавроді, Просвірін, Гіркін-Стрєлков, ' \
              f'Шварцнеггер, Медведчук в пікселі, Дуров, Доктор Попов, Каневський, Герасімов).\n' \
              f'\U0001F309 Класове преміум фото 3 (Тамаев Асхаб, Калашніков, Кашпіровський, Роберт Райт, Джамбо,' \
              f' Поліцейський з Рубльовки, Олег Царьов, Сноуден, Охлобистін, Ржавий, Лапенко, Жуков).' \
              f'\n\n\U0001F3CB\uFE0F\u200D\u2642\uFE0F Прокачка русака або клану:\n\U0001F943 Настоянка глоду ' \
              f'- буст для новачків. Якщо в русака менше 1000 сили і 5 інтелекту, то настоянка моментально додасть' \
              f' 400 сили і 4 інтелекту.\n\U0001F4E6 40 Донбаських пакунків\n' \
              f'\u2721\uFE0F Ярмулка [Шапка, міцність=7, імунітет_до_РПГ] - надає доступ до кошерних квестів' \
              f' (вдвічі більша нагорода, але і більша складність їх виконання). 100% шанс отримати сіль в ' \
              f'соляних шахтах. Міцність зменшується при взятті квестів.' \
              f'\n\U0001F9FE Ресурси для клану: ' \
              f'\U0001F333 2222 \U0001faa8 1111 \U0001F47E 33\n\U0001F3E0 Велике будівництво - додатковий підвал ' \
              f'найвищого рівня (покупка доступна до етапу 2. Купівля будівельних матеріалів).' \
              f'\n\U0001F393 Курс перекваліфікації - дозволяє русаку наново вибрати клас.'

    elif mode == 3:
        items = {'\U0001F4AA Сила - 5 \U0001F9C2': 'salt_strength',
                 '\U0001F531 Спорядження - 10 \U0001F9C2': 'salt_upgraded',
                 '\U0001F349 Кавун - 15 \U0001F9C2': 'salt_watermelon',
                 '\U0001F4FB\U0001F9F1\U0001F9F6 - 20 \U0001F9C2': 'salt_resources',
                 '\U0001F304 Фото - 8 \U0001F9C2': 'salt_photo',
                 '\U0001F309 Чмоня - 30 \U0001F9C2': 'salt_chm',
                 '\U0001F43D\U0001F41F Швайнокарась - 33 \U0001F9C2': 'salt_fish'}
        for key, value in items.items():
            if value == 'cabin' and r.hexists(uid, 'cabin') and int(r.hget(uid, 'cabin')) == 1:
                pass
            else:
                markup.add(InlineKeyboardButton(text=key, callback_data=value))
        markup.add(InlineKeyboardButton(text='\U0001F4B5', callback_data='switch1'),
                   InlineKeyboardButton(text='\U0001F31F', callback_data='switch2'))
        salt = int(r.hget(uid, 'salt'))
        msg = f'\U0001F9C2 Сіль: {salt}\n\nОсь опис товарів, які можна придбати:\n\n' \
              f'\U0001F4AA Збільшити силу на 30/20/10/5/3 (залежно від сили русака).\n' \
              f'\U0001F531 Покращене класове спорядження стандартної міцності.\n' \
              f'\U0001F349 Кавун базований - [Шапка, міцність=∞] - збільшує зарплату за роботу на соляній шахті ' \
              f'на 5 та силу при годуванні на 5. Кавун буде конфісковано, якщо при годуванні зменшиться сила.\n' \
              f'\U0001F4FB 22 \U0001F9F1 55 \U0001F9F6 111 - ресурси для клану.\n' \
              f'\U0001F304 Фото - заміна фотки русака на одне випадкове з 10 стандартних.\n' \
              f'\U0001F309 Чмоня - заміна фотки русака на одного з Чмонь, залежно від класу.\n' \
              f'\U0001F43D\U0001F41F Швайнокарась [Допомога, міцність=3, максимальна_міцність=3] - ' \
              f'може виконувати бажання русаків (відпочивати, нажертись, напитись).'

    return msg, markup


def salt_shop(uid, cdata):
    if cdata.startswith('salt_strength'):
        if int(r.hget(uid, 'injure')) <= 0:
            if int(r.hget(uid, 'salt')) >= 5:
                r.hincrby(uid, 'salt', -5)
                r.hincrby(uid, 'purchase', 1)
                st = int(r.hget(uid, 'strength'))
                s4 = int(r.hget(uid, 's4'))
                if st < 2000:
                    up = 30
                elif st < 3000:
                    up = 20
                elif st < 4000:
                    up = 10
                elif st < 5000:
                    up = 5
                else:
                    up = 3
                if s4 >= 5:
                    up = int(up * 1.4)
                r.hincrby(uid, 'strength', up)
                quest(uid, 3, 2, 4)
                if s4 < 2:
                    if choices([1, 0], [10, 90]) == [1]:
                        msg = f'Передозування!\n\U0001F4AA +{up}'
                    else:
                        msg = f'\U0001F4AA +{up}'
                else:
                    if choices([1, 0], [5, 95]) == [1]:
                        msg = f'Передозування!\n\U0001F4AA +{up}'
                    else:
                        msg = f'\U0001F4AA +{up}'

                return msg
            else:
                return 'Недостатньо солі на рахунку.'
        else:
            return 'Поранений русак не може отримати силу від солі.'

    elif cdata.startswith('salt_upgraded'):
        if int(r.hget(uid, 'salt')) >= 10:
            cl = int(r.hget(uid, 'class'))
            if cl == 0:
                return 'Ваш русак не має класу.'
            if cl in (1, 11, 21) and int(r.hget(uid, 'weapon')) == 0:
                r.hset(uid, 'weapon', 22)
                r.hincrby(uid, 's_weapon', 5)
            elif cl in (2, 12, 22) and int(r.hget(uid, 'weapon')) == 0:
                r.hset(uid, 'weapon', 23)
                r.hset(uid, 's_weapon', 25)
            elif cl in (3, 13, 23) and int(r.hget(uid, 'weapon')) == 0:
                r.hset(uid, 'weapon', 24)
                r.hset(uid, 's_weapon', 3)
            elif cl in (4, 14, 24) and int(r.hget(uid, 'weapon')) == 0:
                r.hset(uid, 'weapon', 25)
                r.hset(uid, 's_weapon', 1)
            elif cl in (5, 15, 25) and int(r.hget(uid, 'weapon')) == 0:
                r.hset(uid, 'weapon', 26)
                r.hset(uid, 's_weapon', 30)
            elif cl in (6, 16, 26) and int(r.hget(uid, 'defense')) == 0:
                r.hset(uid, 'defense', 17)
                r.hset(uid, 's_defense', 10)
            elif cl in (7, 17, 27) and int(r.hget(uid, 'weapon')) == 0:
                r.hset(uid, 'weapon', 28)
                r.hset(uid, 's_weapon', 8)
            elif cl in (8, 18, 28) and int(r.hget(uid, 'weapon')) == 0:
                r.hset(uid, 'weapon', 29)
                r.hset(uid, 's_weapon', 2)
            elif cl in (9, 19, 29) and int(r.hget(uid, 'weapon')) == 0:
                r.hset(uid, 'weapon', 30)
                r.hset(uid, 's_weapon', 8)
            elif cl in (10, 20, 30) and int(r.hget(uid, 'weapon')) == 0:
                r.hset(uid, 'weapon', 31)
                r.hset(uid, 's_weapon', 10)
            elif cl in (31, 32, 33) and int(r.hget(uid, 'support')) == 0:
                r.hset(uid, 'support', 9)
                r.hset(uid, 's_support', 5)
            elif cl in (34, 35, 36) and int(r.hget(uid, 'weapon')) == 0:
                r.hset(uid, 'weapon', 32)
                r.hset(uid, 's_weapon', 15)
            else:
                return 'У вас вже є спорядження цього типу'
            r.hincrby(uid, 'salt', -10)
            r.hincrby(uid, 'purchase', 1)
            return 'Покращене класове спорядження успішно придбано.'
        else:
            return 'Недостатньо солі на рахунку.'

    elif cdata.startswith('salt_watermelon'):
        if int(r.hget(uid, 'salt')) >= 15:
            if int(r.hget(uid, 'head')) == 0:
                r.hset(uid, 'head', 3)
                r.hset(uid, 's_head', 1)
                r.hincrby(uid, 'salt', -15)
                r.hincrby(uid, 'purchase', 1)
                return 'Ви успішно купили кавун базований'
            else:
                return 'У вас вже є шапка'
        else:
            return 'Недостатньо солі на рахунку.'

    elif cdata.startswith('salt_resources'):
        if int(r.hget(uid, 'salt')) >= 20:
            if checkClan(uid):
                c = 'c' + r.hget(uid, 'clan').decode()
                r.hincrby(uid, 'salt', -20)
                r.hincrby(uid, 'purchase', 1)
                r.hincrby(c, 'technics', 22)
                r.hincrby(c, 'brick', 55)
                r.hincrby(c, 'cloth', 111)
                return 'Ви успішно купили ресурси для клану.'
            else:
                return 'Для купівлі ресурсів треба бути в клані'
        else:
            return 'Недостатньо солі на рахунку.'

    elif cdata.startswith('salt_photo'):
        if int(r.hget(uid, 'salt')) >= 8:
            cl = int(r.hget(uid, 'class'))
            r.hincrby(uid, 'salt', -8)
            r.hincrby(uid, 'purchase', 1)
            if cl == 0:
                r.hset(uid, 'photo', choice(default))
            elif cl == 1 or cl == 11 or cl == 21:
                r.hset(uid, 'photo', choice(p1))
            elif cl == 2 or cl == 12 or cl == 22:
                r.hset(uid, 'photo', choice(p2))
            elif cl == 3 or cl == 13 or cl == 23:
                r.hset(uid, 'photo', choice(p3))
            elif cl == 4 or cl == 14 or cl == 24:
                r.hset(uid, 'photo', choice(p4))
            elif cl == 5 or cl == 15 or cl == 25:
                r.hset(uid, 'photo', choice(p5))
            elif cl == 6 or cl == 16 or cl == 26:
                r.hset(uid, 'photo', choice(p6))
            elif cl == 7 or cl == 17 or cl == 27:
                r.hset(uid, 'photo', choice(p7))
            elif cl == 8 or cl == 18 or cl == 28:
                r.hset(uid, 'photo', choice(p8))
            elif cl == 9 or cl == 19 or cl == 29:
                r.hset(uid, 'photo', choice(p9))
            elif cl == 10 or cl == 20 or cl == 30:
                r.hset(uid, 'photo', choice(p10))
            elif cl == 31 or cl == 32 or cl == 33:
                r.hset(uid, 'photo', choice(p11))
            elif cl == 34 or cl == 35 or cl == 36:
                r.hset(uid, 'photo', choice(p12))
            return 'Ви успішно змінили фото русаку'
        else:
            return 'Недостатньо солі на рахунку.'

    elif cdata.startswith('salt_chm'):
        if int(r.hget(uid, 'salt')) >= 30:
            cl = int(r.hget(uid, 'class'))
            r.hincrby(uid, 'salt', -30)
            r.hincrby(uid, 'purchase', 1)
            if cl == 0:
                r.hset(uid, 'photo', default[4])
            elif cl == 1 or cl == 11 or cl == 21:
                r.hset(uid, 'photo', chm[0])
            elif cl == 2 or cl == 12 or cl == 22:
                r.hset(uid, 'photo', chm[1])
            elif cl == 3 or cl == 13 or cl == 23:
                r.hset(uid, 'photo', chm[2])
            elif cl == 4 or cl == 14 or cl == 24:
                r.hset(uid, 'photo', chm[3])
            elif cl == 5 or cl == 15 or cl == 25:
                r.hset(uid, 'photo', chm[4])
            elif cl == 6 or cl == 16 or cl == 26:
                r.hset(uid, 'photo', chm[5])
            elif cl == 7 or cl == 17 or cl == 27:
                r.hset(uid, 'photo', chm[6])
            elif cl == 8 or cl == 18 or cl == 28:
                r.hset(uid, 'photo', chm[7])
            elif cl == 9 or cl == 19 or cl == 29:
                r.hset(uid, 'photo', chm[8])
            elif cl == 10 or cl == 20 or cl == 30:
                r.hset(uid, 'photo', chm[9])
            elif cl == 31 or cl == 32 or cl == 33:
                r.hset(uid, 'photo', chm[10])
            elif cl == 34 or cl == 35 or cl == 36:
                r.hset(uid, 'photo', chm[11])
            return 'Ви успішно змінили фото русаку'
        else:
            return 'Недостатньо солі на рахунку.'

    elif cdata.startswith('salt_fish'):
        if int(r.hget(uid, 'salt')) >= 33:
            if int(r.hget(uid, 'support')) == 0:
                r.hset(uid, 'support', 10)
                r.hset(uid, 's_support', 3)
                r.hincrby(uid, 'salt', -33)
                r.hincrby(uid, 'purchase', 1)
                return 'Ви успішно купили Швайнокарася'
            else:
                return 'У вас вже є допоміжне спорядження'
        else:
            return 'Недостатньо солі на рахунку.'
