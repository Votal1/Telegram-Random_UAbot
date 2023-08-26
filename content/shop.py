from config import r
from methods import checkClan
from random import choices, choice
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from constants.photos import default, chmonya, girkin, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12
from content.quests import quest


def shop_msg(uid, mode):
    markup = InlineKeyboardMarkup()
    msg = ''
    if mode == 1:
        markup.add(InlineKeyboardButton(text='\u2622 1 - \U0001F4B5 2', callback_data='vodka'),
                   InlineKeyboardButton(text='\u2622 5 - \U0001F4B5 12', callback_data='5_vodka'),
                   InlineKeyboardButton(text='\u2622 20 - \U0001F4B5 50', callback_data='20_vodka'))
        items = {'\U0001F5E1 Колючий дрин - \U0001F4B5 4': 'weapon',
                 '\U0001F6E1 Колючий щит - \U0001F4B5 5': 'defense',
                 '\U0001F9EA Аптечка - \U0001F4B5 5': 'aid_kit',
                 '\U0001F4B3 Трофейний паспорт - \U0001F4B5 10': 'passport',
                 '\U0001F3DA Утеплена будка - \U0001F4B5 30': 'cabin',
                 '\U0001F469\U0001F3FB Жінка - \U0001F4B5 150': 'woman',
                 '\U0001F6AC Тютюн та люлька - \U0001F469\U0001F3FB 1': 'pipe'}
        for key, value in items.items():
            if value == 'cabin' and r.hexists(uid, 'cabin') and int(r.hget(uid, 'cabin')) == 1:
                pass
            else:
                markup.add(InlineKeyboardButton(text=key, callback_data=value))
        markup.add(InlineKeyboardButton(text='\U0001F31F', callback_data='switch2'),
                   InlineKeyboardButton(text='\U0001F9C2', callback_data='switch3'))
        money = r.hget(uid, 'money').decode()
        msg = f'\U0001F4B5 Гривні: {money}\n\nОсь опис товарів, які можна придбати:\n\n\u2622 Горілка "Козаки" - ' \
              f'збільшує русаку бойовий дух на 10-70.\n\U0001F5E1 Колючий дрин [Зброя] - перед боєм онуляє ворогу ' \
              f'бойовий дух, якщо його значення від 300 до 1000, зменшує на 1000, якщо від 1000 до 2500 і зменшує ' \
              f'на 20/30/40%, якщо бойовий дух більше 2500).\n\U0001F6E1 Колючий щит [Захист] - працює так само ' \
              f'як дрин, тільки знижує бойовий дух тому, хто атакує.\n\U0001F9EA Аптечка [Допомога, міцність=10]' \
              f' - збільшує здоров`я на 5 і на 10 кожного бою. Якщо слот допомоги зайнятий - додає 50 здоров`я\n' \
              f'\U0001F4B3 Трофейний паспорт - поміняє ім`я русака на інше, випадкове.' \
              f'\n\U0001F3DA Утеплена будка - 15 додаткової сили при кожному ' \
              f'годуванні русака (до 5000 сили). \n\U0001F469\U0001F3FB Жінка - раз в 9 днів народжуватиме ' \
              f'смачне російське немовля. Жінку треба провідувати кожен день командою \n/woman\n\U0001F6AC Тютюн ' \
              f'та люлька - на це можна проміняти жінку і піти в козацький похід (бойовий дух русака збільшиться ' \
              f'на 5000, а кількість вбитих русаків збільшиться на 5).'

    elif mode == 2:
        items = {'\U0001F943 Настоянка глоду - \U0001F31F 1': 'hawthorn',
                 '\u2697\uFE0F Копіум - \U0001F31F 1': 'copium',
                 '\U0001F4E6 40 пакунків - \U0001F31F 1': '40_packs',
                 '\u2721\uFE0F Ярмулка - \U0001F31F 1': 'jew',
                 '\U0001F9FE Ресурси - \U0001F31F 2': 'buy_resources',
                 '\U0001F393 Курс перекваліфікації - \U0001F31F 3': 'course',
                 '\U0001F3E0 Велике будівництво - \U0001F31F 3': 'fast_cellar',
                 '\U0001F392 Тактичний рюкзак - \U0001F31F 5': 'expand_backpack1',
                 '\U0001F392 Тактичний рюкзак - \U0001F31F 10': 'expand_backpack2',
                 '\U0001F392 Тактичний рюкзак - \U0001F31F 20': 'expand_backpack3'}
        markup.add(InlineKeyboardButton(text='\U0001F304 - \U0001F31F 1', callback_data='premium1'),
                   InlineKeyboardButton(text='\U0001F307 - \U0001F31F 1', callback_data='premium3'),
                   InlineKeyboardButton(text='\U0001F309 - \U0001F31F 1', callback_data='premium4'))
        for key, value in items.items():
            if value == 'fast_cellar' and int(r.hget(uid, 's3')) > 2:
                pass
            elif value == 'expand_backpack1':
                if r.hexists(uid, 'extra_slot') and int(r.hget(uid, 'extra_slot')) == 0:
                    markup.add(InlineKeyboardButton(text=key, callback_data=value))
            elif value == 'expand_backpack2':
                if r.hexists(uid, 'extra_slot') and int(r.hget(uid, 'extra_slot')) == 1:
                    markup.add(InlineKeyboardButton(text=key, callback_data=value))
            elif value == 'expand_backpack3':
                if r.hexists(uid, 'extra_slot') and int(r.hget(uid, 'extra_slot')) == 2:
                    markup.add(InlineKeyboardButton(text=key, callback_data=value))
            else:
                markup.add(InlineKeyboardButton(text=key, callback_data=value))
        if str(uid).encode() in r.smembers('prigozhin'):
            markup.add(InlineKeyboardButton(text='\U0001F304 Пригожин - \U0001F31F 1', callback_data='prigozhin'))
        markup.add(InlineKeyboardButton(text='\U0001F9C2 5 - \U0001F31F 1', callback_data='5_salt'),
                   InlineKeyboardButton(text='🧳 5 - \U0001F31F 1', callback_data='5_gifts'))
        markup.add(InlineKeyboardButton(text='\U0001F4B5', callback_data='switch1'),
                   InlineKeyboardButton(text='\U0001F9C2', callback_data='switch3'))
        strap = r.hget(uid, 'strap').decode()
        msg = f'\U0001F31F Погони російських генералів: {strap}\n\nОсь опис товарів, які можна придбати:\n\n' \
              f'\U0001F4F8 Заміна фото русака (ціна 1 погон):\n\U0001F304 Класове преміум фото 1 (Кадиров, Обеме, ' \
              f'Горшок, Тесак, Захарченко, Дерек Шовін, Янукович, Petya, Джонні Сінс, Чікатіло, Раян Гослінг, ' \
              f'Шойгу).\n\U0001F307 Класове преміум фото 2 (Хасбулла, Стаханов, Мавроді, Просвірін, Стрємоусов, ' \
              f'Шварценеггер, Медведчук в пікселі, Дуров, Доктор Попов, Дядя Мопс, Каневський, Герасімов).\n' \
              f'\U0001F309 Класове преміум фото 3 (Тамаев Асхаб, Калашніков, Кашпіровський, Роберт Райт, Джамбо,' \
              f' Поліцейський з Рубльовки, Олег Царьов, Сноуден, Охлобистін, Ржавий, Лапенко, Жуков).' \
              f'\n\n\U0001F3CB\uFE0F\u200D\u2642\uFE0F Прокачка русака або клану:\n\U0001F943 Настоянка глоду ' \
              f'- буст для новачків. Якщо в русака менше ніж 1000 сили і 5 інтелекту, то настоянка моментально' \
              f' додасть 1000 сили і 4 інтелекту.\n' \
              f'\u2697\uFE0F Копіум - відновлює здоров`я, очищує організм від мухоморів, лікує до 300 поранень ' \
              f'та шизи. Якщо в русака менше ніж 5000 сили - можна погодувати ще раз.\n' \
              f'\U0001F4E6 40 Донбаських пакунків\n' \
              f'\u2721\uFE0F Ярмулка [Шапка, міцність=7, імунітет_до_РПГ] - надає доступ до кошерних квестів' \
              f' (вдвічі більша нагорода, але і більша складність їх виконання). 100% шанс отримати сіль в ' \
              f'соляних шахтах. Міцність зменшується при взятті квестів.' \
              f'\n\U0001F9FE Ресурси для клану: ' \
              f'\U0001F333 2222 \U0001faa8 1111 \U0001F47E 33\n' \
              f'\U0001F393 Курс перекваліфікації - дозволяє русаку ' \
              f'наново вибрати клас.\n\U0001F3E0 Велике будівництво - додатковий підвал ' \
              f'найвищого рівня (покупка доступна до етапу 2. Купівля будівельних матеріалів).\n' \
              f'\U0001F392 Тактичний рюкзак - можливість складати в рюкзак більше предметів.'

    elif mode == 3:
        items = {'\U0001F4AA Сила - 5 \U0001F9C2': 'salt_strength',
                 '🌀 Ізострічка - 8 \U0001F9C2': 'salt_upgraded',
                 '\U0001F349 Кавун - 15 \U0001F9C2': 'salt_watermelon',
                 '\U0001F4FB\U0001F9F1\U0001F9F6 - 20 \U0001F9C2': 'salt_resources',
                 '\U0001F43D\U0001F41F Швайнокарась - 33 \U0001F9C2': 'salt_fish'}
        for key, value in items.items():
            markup.add(InlineKeyboardButton(text=key, callback_data=value))
        markup.add(InlineKeyboardButton(text='\U0001F304 - 8 \U0001F9C2', callback_data='salt_photo'),
                   InlineKeyboardButton(text='\U0001F307 - 20 \U0001F9C2', callback_data='salt_chm'),
                   InlineKeyboardButton(text='\U0001F309 - 30 \U0001F9C2', callback_data='salt_girkin'))
        markup.add(InlineKeyboardButton(text='\U0001F4B5', callback_data='switch1'),
                   InlineKeyboardButton(text='\U0001F31F', callback_data='switch2'))
        salt = int(r.hget(uid, 'salt'))
        msg = f'\U0001F9C2 Сіль: {salt}\n\nОсь опис товарів, які можна придбати:\n\n' \
              f'\U0001F4AA Збільшити силу на 30/20/10/5/3 (залежно від сили русака).\n' \
              f'🌀 Ізострічка - використовується для покращення спорядження.\n' \
              f'\U0001F349 Кавун базований - [Шапка, міцність=∞] - збільшує зарплату за роботу на соляній шахті ' \
              f'на 5 та силу при годуванні на 5. Кавун буде конфісковано, якщо при годуванні зменшиться сила.\n' \
              f'\U0001F4FB 22 \U0001F9F1 55 \U0001F9F6 111 - ресурси для клану.\n' \
              f'\U0001F304 Фото - заміна фотки русака на одне випадкове з 10 стандартних.\n' \
              f'\U0001F307 Чмоня - заміна фотки русака на одного з Чмонь, залежно від класу.\n' \
              f'\U0001F309 Гіркін - заміна фотки русака на одне з фото Гіркіна, залежно від класу.\n' \
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
                if st < 3000:
                    up = 30
                elif st < 4000:
                    up = 20
                elif st < 5000:
                    up = 10
                elif st < 8000:
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
        if int(r.hget(uid, 'salt')) >= 8:
            r.hincrby(uid, 'tape', 1)
            r.hincrby(uid, 'salt', -8)
            r.hincrby(uid, 'purchase', 1)
            return 'Ізострічку успішно придбано.'
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
            current_photo = r.hget(uid, 'photo').decode()
            ran = ''
            if cl == 0:
                ran = choice(default)
                while ran == current_photo:
                    ran = choice(default)
            elif cl == 1 or cl == 11 or cl == 21:
                ran = choice(p1)
                while ran == current_photo:
                    ran = choice(p1)
            elif cl == 2 or cl == 12 or cl == 22:
                ran = choice(p2)
                while ran == current_photo:
                    ran = choice(p2)
            elif cl == 3 or cl == 13 or cl == 23:
                ran = choice(p3)
                while ran == current_photo:
                    ran = choice(p3)
            elif cl == 4 or cl == 14 or cl == 24:
                ran = choice(p4)
                while ran == current_photo:
                    ran = choice(p4)
            elif cl == 5 or cl == 15 or cl == 25:
                ran = choice(p5)
                while ran == current_photo:
                    ran = choice(p5)
            elif cl == 6 or cl == 16 or cl == 26:
                ran = choice(p6)
                while ran == current_photo:
                    ran = choice(p6)
            elif cl == 7 or cl == 17 or cl == 27:
                ran = choice(p7)
                while ran == current_photo:
                    ran = choice(p7)
            elif cl == 8 or cl == 18 or cl == 28:
                ran = choice(p8)
                while ran == current_photo:
                    ran = choice(p8)
            elif cl == 9 or cl == 19 or cl == 29:
                ran = choice(p9)
                while ran == current_photo:
                    ran = choice(p9)
            elif cl == 10 or cl == 20 or cl == 30:
                ran = choice(p10)
                while ran == current_photo:
                    ran = choice(p10)
            elif cl == 31 or cl == 32 or cl == 33:
                ran = choice(p11)
                while ran == current_photo:
                    ran = choice(p11)
            elif cl == 34 or cl == 35 or cl == 36:
                ran = choice(p12)
                while ran == current_photo:
                    ran = choice(p12)
            r.hset(uid, 'photo', ran)
            return 'Ви успішно змінили фото русаку'
        else:
            return 'Недостатньо солі на рахунку.'

    elif cdata.startswith('salt_chm'):
        if int(r.hget(uid, 'salt')) >= 20:
            cl = int(r.hget(uid, 'class'))
            r.hincrby(uid, 'salt', -20)
            r.hincrby(uid, 'purchase', 1)
            if cl == 0:
                r.hset(uid, 'photo', chmonya[0])
            elif cl == 1 or cl == 11 or cl == 21:
                r.hset(uid, 'photo', chmonya[1])
            elif cl == 2 or cl == 12 or cl == 22:
                r.hset(uid, 'photo', chmonya[2])
            elif cl == 3 or cl == 13 or cl == 23:
                r.hset(uid, 'photo', chmonya[3])
            elif cl == 4 or cl == 14 or cl == 24:
                r.hset(uid, 'photo', chmonya[4])
            elif cl == 5 or cl == 15 or cl == 25:
                r.hset(uid, 'photo', chmonya[5])
            elif cl == 6 or cl == 16 or cl == 26:
                r.hset(uid, 'photo', chmonya[6])
            elif cl == 7 or cl == 17 or cl == 27:
                r.hset(uid, 'photo', chmonya[7])
            elif cl == 8 or cl == 18 or cl == 28:
                r.hset(uid, 'photo', chmonya[8])
            elif cl == 9 or cl == 19 or cl == 29:
                r.hset(uid, 'photo', chmonya[9])
            elif cl == 10 or cl == 20 or cl == 30:
                r.hset(uid, 'photo', chmonya[10])
            elif cl == 31 or cl == 32 or cl == 33:
                r.hset(uid, 'photo', chmonya[11])
            elif cl == 34 or cl == 35 or cl == 36:
                r.hset(uid, 'photo', chmonya[12])
            return 'Ви успішно змінили фото русаку'
        else:
            return 'Недостатньо солі на рахунку.'

    elif cdata.startswith('salt_girkin'):
        if int(r.hget(uid, 'salt')) >= 30:
            cl = int(r.hget(uid, 'class'))
            r.hincrby(uid, 'salt', -30)
            r.hincrby(uid, 'purchase', 1)
            if cl == 0:
                r.hset(uid, 'photo', girkin[0])
            elif cl == 1 or cl == 11 or cl == 21:
                r.hset(uid, 'photo', girkin[1])
            elif cl == 2 or cl == 12 or cl == 22:
                r.hset(uid, 'photo', girkin[2])
            elif cl == 3 or cl == 13 or cl == 23:
                r.hset(uid, 'photo', girkin[3])
            elif cl == 4 or cl == 14 or cl == 24:
                r.hset(uid, 'photo', girkin[4])
            elif cl == 5 or cl == 15 or cl == 25:
                r.hset(uid, 'photo', girkin[5])
            elif cl == 6 or cl == 16 or cl == 26:
                r.hset(uid, 'photo', girkin[6])
            elif cl == 7 or cl == 17 or cl == 27:
                r.hset(uid, 'photo', girkin[7])
            elif cl == 8 or cl == 18 or cl == 28:
                r.hset(uid, 'photo', girkin[8])
            elif cl == 9 or cl == 19 or cl == 29:
                r.hset(uid, 'photo', girkin[9])
            elif cl == 10 or cl == 20 or cl == 30:
                r.hset(uid, 'photo', girkin[10])
            elif cl == 31 or cl == 32 or cl == 33:
                r.hset(uid, 'photo', girkin[11])
            elif cl == 34 or cl == 35 or cl == 36:
                r.hset(uid, 'photo', girkin[12])
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
