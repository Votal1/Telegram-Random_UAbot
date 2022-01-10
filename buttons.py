from telebot import types


def goods():
    markup = types.InlineKeyboardMarkup()
    items = {'Горілка "Козаки" - 2 грн': 'vodka', 'Колючий дрин - 7 грн': 'weapon', 'Колючий щит - 8 грн': 'defense',
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
