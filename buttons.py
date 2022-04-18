from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def goods():
    markup = InlineKeyboardMarkup()
    items = {'Горілка "Козаки" - 2 грн': 'vodka', 'Колючий дрин - 4 грн': 'weapon', 'Колючий щит - 5 грн': 'defense',
             'Аптечка - 4 грн': 'aid_kit', 'Трофейний паспорт - 10 грн': 'passport', 'Утеплена будка - 30 грн': 'cabin',
             'Жінка - 150 грн': 'woman', 'Тютюн та люлька - 1 жінка': 'pipe'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def donate_goods():
    markup = InlineKeyboardMarkup()
    items = {'Преміум-фото класу - 1 погон': 'premium1', 'Класовий чмоня - 1 погон': 'premium2',
             '40 пакунків - 1 погон': '40_packs', 'Настоянка глоду - 1 погон': 'hawthorn',
             'Курс перекваліфікації - 2 погони': 'course', 'Велике будівництво - 3 погони': 'fast_cellar'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def merchant_goods():
    markup = InlineKeyboardMarkup()
    items = {'Купити уламок бронетехніки': 'fragment', 'Купити мухомор': 'mushroom',
             'Купити шапочку з фольги': 'foil', 'Купити спорядження свого класу': 'equipment'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def skill_set():
    markup = InlineKeyboardMarkup()
    items = {'Прокачати алкоголізм': 'alcohol', 'Прокачати майстерність': 'master',
             'Продовжити будівництво': 'cellar'}
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


def invent(w, d, s):
    markup = InlineKeyboardMarkup()
    if w > 0:
        markup.add(InlineKeyboardButton(text='Викинути зброю', callback_data='drop_w'))
    if d > 0:
        markup.add(InlineKeyboardButton(text='Викинути захист', callback_data='drop_d'))
    if s > 0:
        markup.add(InlineKeyboardButton(text='Викинути допомогу', callback_data='drop_s'))
    return markup


def unpack():
    markup = InlineKeyboardMarkup()
    items = {'Так': 'unpack'}
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
             'Отримати список членів клану': 'get_members'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup


def cmm():
    markup = InlineKeyboardMarkup()
    items = {'Інформація': 'full_list_1', 'Гра в русаків': 'full_list_2', 'Гра в русаків: Топ': 'full_list_3',
             'Гра в русаків: Клани': 'full_list_4', 'Адміністраторські команди': 'full_list_5'}
    for key, value in items.items():
        markup.add(InlineKeyboardButton(text=key, callback_data=value))
    return markup
