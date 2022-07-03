from config import r
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def shop_msg(uid):
    markup = InlineKeyboardMarkup()
    items = {'\u2622 Горілка "Козаки" - 2 грн': 'vodka', '\U0001F5E1 Колючий дрин - 4 грн': 'weapon',
             '\U0001F6E1Колючий щит - 5 грн': 'defense', '\U0001F9EA Аптечка - 4 грн': 'aid_kit',
             '\U0001F4B3 Трофейний паспорт - 10 грн': 'passport', '\U0001F3DA Утеплена будка - 30 грн': 'cabin',
             '\U0001F469\U0001F3FB Жінка - 150 грн': 'woman', '\U0001F6AC Тютюн та люлька - 1 жінка': 'pipe'}
    for key, value in items.items():
        if value == 'cabin' and r.hexists(uid, 'cabin') and int(r.hget(uid, 'cabin')) == 1:
            pass
        else:
            markup.add(InlineKeyboardButton(text=key, callback_data=value))
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

    return msg, markup
