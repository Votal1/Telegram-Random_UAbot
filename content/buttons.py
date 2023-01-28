from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def choose_lang():
    markup = InlineKeyboardMarkup()
    items = {'\U0001F1FA\U0001F1E6': 'choose_lang_uk', '\U0001F1EC\U0001F1E7': 'choose_lang_en'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def battle_button():
    markup = InlineKeyboardMarkup()
    items = {'Відправити русака на бій': 'join'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def battle_button_2():
    markup = InlineKeyboardMarkup()
    items = {'Відправити русака на бій': 'join', 'Почати битву': 'start_battle'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def battle_button_3():
    markup = InlineKeyboardMarkup()
    items = {'Відправити русака на міжчатовий бій': 'war_join'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def battle_button_4():
    markup = InlineKeyboardMarkup()
    items = {'Відправити русака на рейд': 'raid_join'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def invent(w, d, s, h):
    markup = InlineKeyboardMarkup()
    if w > 0 and d > 0:
        markup.add(InlineKeyboardButton(text='Викинути зброю', callback_data='drop_w'),
                   InlineKeyboardButton(text='Викинути захист', callback_data='drop_d'))
    elif w > 0:
        markup.add(InlineKeyboardButton(text='Викинути зброю', callback_data='drop_w'))
    elif d > 0:
        markup.add(InlineKeyboardButton(text='Викинути захист', callback_data='drop_d'))
    if s > 0 and h > 0:
        markup.add(InlineKeyboardButton(text='Викинути допомогу', callback_data='drop_s'),
                   InlineKeyboardButton(text='Викинути шапку', callback_data='drop_h'))
    elif s > 0:
        markup.add(InlineKeyboardButton(text='Викинути допомогу', callback_data='drop_s'))
    elif h > 0:
        markup.add(InlineKeyboardButton(text='Викинути шапку', callback_data='drop_h'))
    return markup


def invent0():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='\U0001F510', callback_data='drop_open'))
    return markup


def unpack(uid):
    markup = InlineKeyboardMarkup()
    items = {'Так': f'pack_unpack_{uid}'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def gift_unpack(uid):
    markup = InlineKeyboardMarkup()
    items = {'Так': f'gift_unpack_{uid}'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def create_clan():
    markup = InlineKeyboardMarkup()
    items = {'\U0001F4B5 250': 'create_hrn', '\U0001F31F 1': 'create_strap'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def invite():
    markup = InlineKeyboardMarkup()
    items = {'Прийняти в клан': 'invite'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def buy_tools():
    markup = InlineKeyboardMarkup()
    items = {'Купити сокиру': 'buy_axe', 'Купити кайло': 'buy_pickaxe'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def clan_set():
    markup = InlineKeyboardMarkup()
    items = {'Змінити назву на актуальну назву чату - \U0001F4B5 100': 'change_title',
             'Змінити режим набору': 'toggle_allow', 'Змінити режим входу в битву': 'toggle_war', 'Зарплата': 'salary',
             'Змінити набір': 'recruit', 'Змінити сповіщення': 'notification',
             'Отримати список членів клану': 'get_members'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup
