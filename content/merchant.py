from random import choice
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def merchant_msg(slot, strap, tape):
    slot1 = choice([1, 2, 3])
    slot2 = choice([1, 2, 3])
    slot3 = choice([1, 2, 3])
    markup = InlineKeyboardMarkup()
    if slot == 2:
        tape *= 2
    elif slot == 3:
        tape *= 4
    msg = 'Прийшов мандрівний торговець, приніс різноманітні товари.\n\n'
    if slot1 == 1:
        msg += '🗡 Батіг [Зброя, міцність=5, ціна=125] - +15% сили в рейді, +33% якщо в русака нема жінки.'
        markup.add(InlineKeyboardButton(text='🗡 Купити батіг', callback_data='fragment'))
    if slot1 == 2:
        msg += '\u2708\uFE0F БпЛА [Зброя, міцність=1, ціна=90] - за кожен рівень майстерності збільшує силу в ' \
               'масовій битві на 50% та збільшує шанс не втратити зброю на 18%.'
        markup.add(InlineKeyboardButton(text='\u2708\uFE0F Купити БпЛА', callback_data='uav'))
    if slot1 == 3:
        msg += '\U0001F6A7 Міни [Захист, міцність=3, ціна=30] - з шансом 33% завдає ворогу 5 поранень і ' \
               'зменшує міцність зброї на 5. Можливість використати міни при захисті клану.'
        markup.add(InlineKeyboardButton(text='\U0001F6A7 Купити міни', callback_data='bombs'))

    if slot2 == 1:
        msg += '\n\U0001F344 Мухомор королівський [Допомога, міцність=1, ціна=60] - якщо у ворога більший ' \
               'інтелект, додає +1 інтелекту (не діє проти фокусників). На бій зменшує свою силу на 50%. ' \
               'Максимальна кількість покупок на русака - 3.\n'
        markup.add(InlineKeyboardButton(text='\U0001F344 Купити мухомор', callback_data='mushroom'))
    if slot2 == 2:
        msg += '\n\U0001F9EA Цукор [Допомога, міцність=2, ціна=150] - збільшує силу за годування на 15 (до 5000) або' \
               ' зменшує шанс зменшення сили на 15%, додає 5 бойового трансу. \n'
        markup.add(InlineKeyboardButton(text='\U0001F9EA Купити цукор', callback_data='sugar'))
    if slot2 == 3:
        msg += '\n\U0001F37A Квас [Допомога, міцність=5, ціна=35] - русак не втече зі зміни. Додає 5 бойового трансу ' \
               'за роботу в шахті.\n'
        markup.add(InlineKeyboardButton(text='\U0001F37A Купити квас', callback_data='kvs'))

    if slot3 == 1:
        msg += '🕶 Тактичний шолом [міцність=40, ціна=70] - збільшує силу в дуелях і міжчатових битвах на 31%.'
        markup.add(InlineKeyboardButton(text='🕶 Купити тактичний шолом', callback_data='helmet'))
    if slot3 == 2:
        msg += '\u2744\uFE0F Вушанка [Шапка, міцність=20, ціна=30] - збільшує ефективність бойового трансу на 2% за' \
               ' кожен рівень алкоголізму.'
        markup.add(InlineKeyboardButton(text='\u2744\uFE0F Купити вушанку', callback_data='ear'))
    if slot3 == 3:
        msg += '\U0001F349 Кавун базований [Шапка, ціна=333] - збільшує силу за годування і гроші за зміну на 5. ' \
               'Зникає тільки тоді, коли сила за годування зменшиться.'
        markup.add(InlineKeyboardButton(text='\U0001F349 Купити кавун базований', callback_data='watermelon'))

    msg += '\n\n\U0001F919 Травмат [Зброя, міцність=5, ціна=6] - зменшує силу ворога на бій на 50%.\n' \
           '\U0001F9F0 Діамантове кайло [Зброя, міцність=25, ціна=15] - збільшує силу, інтелект і бойовий дух на ' \
           '20%.\n' \
           '\U0001F52E Колода з кіоску [Зброя, міцність=3, ціна=5] - міняє твої характеристики з ворогом на бій.\n' \
           '\U0001F5FF Сокира Перуна [Зброя, міцність=1, ціна=7] - при перемозі забирає весь бойовий дух ворога, ' \
           'при поразці ворог забирає твій.\n' \
           '\U0001fa96 АК-47 [Зброя, міцність=30, ціна=20] - після перемоги активує ефект горілки.\n' \
           '\U0001F46E Поліцейський щит [Захист, міцність=10, ціна=10] - зменшує силу ворога на 20%.\n' \
           '\U0001F921 Прапор новоросії [Зброя, міцність=8, ціна=5] - додаткова перемога за перемогу в дуелі.\n' \
           '\U0001F4DF Експлойт [Зброя, міцність=2, ціна=9] - шанс активувати здібність хакера - 99%.\n' \
           '\u26D1 Медична пилка [Зброя, міцність=8, ціна=10] - якщо у ворога нема поранень - завдає 1. Лікує ворогу' \
           ' від 4 до 10 поранень або шизофренії і забирає 10 здоров`я.\n' \
           '\U0001F6AC Скляна пляшка [Зброя, міцність=10, ціна=5] - зменшує інтелект ворогу на 10.\n' \
           '\U0001F695 Солярка [Допомога, міцність=5, ціна=15] - збільшує власну силу в битвах, міжчатових битвах ' \
           'або рейдах на 25%.\n' \
           '\U0001F396 Палаш [Зброя, міцність=15, ціна=10] - +100% сили проти русаків без клану, +25% в іншому випадку.'
    markup.add(InlineKeyboardButton(text='\U0001F5E1 Купити спорядження свого класу', callback_data='equipment'))

    msg += f'\n\n🎒 Тактичний рюкзак [слоти={slot}, ціна=🌟{strap}🌀{tape}] - ' \
           f'збільшує кількість слотів спорядження та кількість можливої ізострічки з пакунків'
    markup.add(InlineKeyboardButton(text=f'🎒 Купити рюкзак - 🌟{strap} 🌀{tape}', callback_data='merchant_backpack'))

    return msg, markup
