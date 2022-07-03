from config import r
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def shop_msg(uid, mode):
    markup = InlineKeyboardMarkup()
    msg = ''
    if mode == 1:
        items = {'\u2622 Горілка "Козаки" - 2 грн': 'vodka', '\U0001F5E1 Колючий дрин - 4 грн': 'weapon',
                 '\U0001F6E1Колючий щит - 5 грн': 'defense', '\U0001F9EA Аптечка - 4 грн': 'aid_kit',
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
                 '\U0001F9FE Ресурси - \U0001F31F 2 погони': 'buy_resources',
                 '\U0001F393 Курс перекваліфікації - \U0001F31F 2 погони': 'course',
                 '\U0001F3E0 Велике будівництво - \U0001F31F 3 погони': 'fast_cellar'}
        markup.add(InlineKeyboardButton(text='\U0001F304 - \U0001F31F 1', callback_data='premium1'),
                   InlineKeyboardButton(text='\U0001F307 - \U0001F31F 1', callback_data='premium3'),
                   InlineKeyboardButton(text='\U0001F309 - \U0001F31F 1', callback_data='premium2'))
        for key, value in items.items():
            markup.add(InlineKeyboardButton(text=key, callback_data=value))
        markup.add(InlineKeyboardButton(text='\U0001F4B5', callback_data='switch1'),
                   InlineKeyboardButton(text='\U0001F9C2', callback_data='switch3'))
        strap = r.hget(uid, 'strap').decode()
        msg = f'\U0001F31F Погони російських генералів: {strap}\n\nОсь опис товарів, які можна придбати:\n\n' \
              f'\U0001F4F8 Заміна фото русака (ціна 1 погон):\n\U0001F304 Класове преміум фото 1 (Кадиров, Обеме, ' \
              f'Горшок, Тесак, Захарченко, Дерек Шовін, Янукович, Petya, Джонні Сінс, Чікатіло, Раян Гослінг, ' \
              f'Шойгу).\n\U0001F307 Класове преміум фото 2 (Хасбулла, Стаханов, Мавроді, Просвірін, Гіркін-Стрєлков, ' \
              f'Шварцнеггер, Медведчук в пікселі, Дуров, Доктор Попов, Каневський, Герасімов).\n\U0001F309 Класовий ' \
              f'Чмоня.\n\n\U0001F3CB\uFE0F\u200D\u2642\uFE0F Прокачка русака або клану:\n\U0001F943 Настоянка глоду ' \
              f'- буст для новачків. Якщо в русака менше 1000 сили і 5 інтелекту, то настоянка моментально додасть' \
              f' 400 сили і 4 інтелекту.\n\U0001F4E6 40 Донбаських пакунків\n\U0001F9FE Ресурси для клану: ' \
              f'\U0001F333 2222 \U0001faa8 1111 \U0001F47E 33\n\U0001F393 Курс перекваліфікації - дозволяє русаку ' \
              f'наново вибрати клас.\n\U0001F3E0 Велике будівництво - додатковий підвал найвищого рівня (покупка ' \
              f'доступна до етапу 2. Купівля будівельних матеріалів).'

    elif mode == 3:
        markup.add(InlineKeyboardButton(text='\U0001F4B5', callback_data='switch1'),
                   InlineKeyboardButton(text='\U0001F31F', callback_data='switch2'))
        salt = 0
        msg = f'\U0001F9C2 Сіль: {salt}\n\nНезабаром відкриття...'

    return msg, markup
