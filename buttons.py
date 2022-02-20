from telebot import types


def goods():
    markup = types.InlineKeyboardMarkup()
    items = {'Горілка "Козаки" - 2 грн': 'vodka', 'Колючий дрин - 4 грн': 'weapon', 'Колючий щит - 5 грн': 'defense',
             'Аптечка - 4 грн': 'aid_kit', 'Трофейний паспорт - 10 грн': 'passport', 'Утеплена будка - 30 грн': 'cabin',
             'Жінка - 150 грн': 'woman', 'Тютюн та люлька - 1 жінка': 'pipe'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def donate_goods():
    markup = types.InlineKeyboardMarkup()
    items = {'TF2_heavy - 1 погон': 'tf2', 'Слов`янин Рікардо - 1 погон': 'ricardo',
             'Преміум-фото класу - 1 погон': 'premium', '40 пакунків - 1 погон': '40_packs',
             'Настоянка глоду - 1 погон': 'hawthorn', 'Курс перекваліфікації - 2 погони': 'course',
             'Велике будівництво - 3 погони': 'fast_cellar'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def merchant_goods():
    markup = types.InlineKeyboardMarkup()
    items = {'Купити уламок бронетехніки': 'fragment', 'Купити мухомор': 'mushroom',
             'Купити шапочку з фольги': 'foil', 'Купити спорядження свого класу': 'equipment'}
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


def battle_button_4():
    markup = types.InlineKeyboardMarkup()
    items = {'Відправити русака на міжчатовий бій': 'war_test_join'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def invent():
    markup = types.InlineKeyboardMarkup()
    items = {'Викинути зброю': 'drop_w', 'Викинути захист': 'drop_d', 'Викинути допомогу': 'drop_s'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def unpack():
    markup = types.InlineKeyboardMarkup()
    items = {'Так': 'unpack'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def create_clan():
    markup = types.InlineKeyboardMarkup()
    items = {'\U0001F4B5 250': 'create_hrn', '\U0001F31F 1': 'create_strap'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def invite():
    markup = types.InlineKeyboardMarkup()
    items = {'Прийняти в клан': 'invite'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def buy_tools():
    markup = types.InlineKeyboardMarkup()
    items = {'Купити сокиру': 'buy_axe', 'Купити кайло': 'buy_pickaxe'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup


def clan_set():
    markup = types.InlineKeyboardMarkup()
    items = {'Змінити назву на актуальну назву чату - \U0001F4B5 100': 'change_title',
             'Змінити режим набору': 'toggle_allow', 'Змінити режим входу в битву': 'toggle_war', 'Зарплата': 'salary',
             'Отримати список членів клану': 'get_members'}
    for key, value in items.items():
        markup.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup
