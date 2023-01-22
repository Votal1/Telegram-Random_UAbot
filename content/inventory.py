from config import r
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from variables import weapons, defenses, supports, heads


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
    markup.add(InlineKeyboardButton(text='\U0001F510', callback_data='drop_open'),
               InlineKeyboardButton(text='\U0001F392', callback_data='backpack_open'))
    return markup


def put_in_backpack(markup, w, d, s, h):
    if w > 0 and d > 0:
        markup.add(InlineKeyboardButton(text='Покласти зброю', callback_data='backpack_put_in_weapon'),
                   InlineKeyboardButton(text='Покласти захист', callback_data='backpack_put_in_defense'))
    elif w > 0:
        markup.add(InlineKeyboardButton(text='Покласти зброю', callback_data='backpack_put_in_weapon'))
    elif d > 0:
        markup.add(InlineKeyboardButton(text='Покласти захист', callback_data='backpack_put_in_defense'))
    if s > 0 and h > 0:
        markup.add(InlineKeyboardButton(text='Покласти допомогу', callback_data='backpack_put_in_support'),
                   InlineKeyboardButton(text='Покласти шапку', callback_data='backpack_put_in_head'))
    elif s > 0:
        markup.add(InlineKeyboardButton(text='Покласти допомогу', callback_data='backpack_put_in_support'))
    elif h > 0:
        markup.add(InlineKeyboardButton(text='Покласти шапку', callback_data='backpack_put_in_head'))
    return markup


def take_from_backpack(markup, item1=False, item2=False):
    if item1:
        markup.add(InlineKeyboardButton(text=f'\u2B05\uFE0F\U0001F392 {item1}', callback_data='backpack_take_first'))
    if item2:
        markup.add(InlineKeyboardButton(text=f'\u2B05\uFE0F\U0001F392 {item2}', callback_data='backpack_take_second'))
    return markup


def show_inventory(uid, full=False):
    inv = r.hmget(uid, 'weapon', 'defense', 'support', 'head', 's_weapon', 's_defense', 's_support', 's_head')
    w, d, s, h = int(inv[0]), int(inv[1]), int(inv[2]), int(inv[3])

    if w == 16:
        m1 = '\nМіцність: ∞'
    elif w == 0:
        m1 = '[Порожньо]'
    else:
        m1 = '\nМіцність: ' + inv[4].decode()

    if d == 0:
        m2 = '[Порожньо]'
    else:
        m2 = '\nМіцність: ' + inv[5].decode()

    if s == 0:
        m3 = '[Порожньо]'
    else:
        m3 = '\nМіцність: ' + inv[6].decode()

    if h == 0:
        m4 = '[Порожньо]'
    elif h == 3:
        m4 = '\nМіцність: ∞'
    else:
        m4 = '\nМіцність: ' + inv[7].decode()
    msg = f'\U0001F5E1 Зброя: {weapons[w]}{m1}\n\U0001F6E1 Захист: {defenses[d]}{m2}\n\U0001F9EA ' \
          f'Допомога: {supports[s]}{m3}\n\U0001F3A9 Шапка: {heads[h]}{m4}'

    if full:
        markup = invent(w, d, s, h)
    else:
        markup = invent0()

    return msg, markup


def show_backpack(uid):
    msg = '\U0001F392 Рюкзак:\n\n'
    markup = InlineKeyboardMarkup()

    inv = r.hmget(uid, 'weapon', 'defense', 'support', 'head', 's_weapon', 's_defense', 's_support', 's_head')
    w, d, s, h = int(inv[0]), int(inv[1]), int(inv[2]), int(inv[3])

    inv = r.hmget(uid, 'backpack_1', 'backpack_1_s', 'backpack_1_type',
                  'backpack_2', 'backpack_2_s', 'backpack_2_type', 'extra_slot')
    b1, b1s, b1t, b2, b2s, b2t = int(inv[0]), int(inv[1]), inv[2].decode(), int(inv[3]), int(inv[4]), inv[5].decode()
    extra_sloth = int(inv[6])

    if not b1 and not b2:
        msg += '[Порожньо]'
        markup = put_in_backpack(markup, w, d, s, h)
    else:
        item1, item2 = False, False

        if b1t == 'weapon':
            item1 = weapons[b1]
            msg += f'\U0001F5E1 Зброя: {item1}\nМіцність: {b1s}\n'
        elif b1t == 'defense':
            item1 = defenses[b1]
            msg += f'\U0001F6E1 Захист: {item1}\nМіцність: {b1s}\n'
        elif b1t == 'support':
            item1 = supports[b1]
            msg += f'\U0001F9EA Допомога: {item1}\nМіцність: {b1s}\n'
        elif b1t == 'head':
            item1 = heads[b1]
            msg += f'\U0001F3A9 Шапка: {item1}\nМіцність: {b1s}\n'

        if not b1 or not b2:
            if extra_sloth:
                markup = put_in_backpack(markup, w, d, s, h)
        else:
            if b2t == 'weapon':
                item2 = weapons[b2]
                msg += f'\U0001F5E1 Зброя: {weapons[b2]}\nМіцність: {b2s}\n'
            elif b2t == 'defense':
                item2 = defenses[b2]
                msg += f'\U0001F6E1 Захист: {defenses[b2]}\nМіцність: {b2s}\n'
            elif b2t == 'support':
                item2 = supports[b2]
                msg += f'\U0001F9EA Допомога: {supports[b2]}\nМіцність: {b2s}\n'
            elif b2t == 'head':
                item2 = heads[b2]
                msg += f'\U0001F3A9 Шапка: {heads[b2]}\nМіцність: {b2s}\n'

        markup = take_from_backpack(markup, item1, item2)

    return msg, markup


def drop_item(cdata, uid):
    if cdata.startswith('drop_open'):
        msg, markup = show_inventory(uid, full=True)
        return msg, markup, True, False

    elif cdata.startswith('drop_w'):
        if int(r.hget(uid, 'weapon')) != 0:
            if int(r.hget(uid, 'weapon')) == 16:
                answer = 'Зброю мусора неможливо викинути'
                return False, False, False, answer
            else:
                r.hset(uid, 'weapon', 0)
                r.hset(uid, 's_weapon', 0)
                cl = int(r.hget(uid, 'class'))
                if cl == 6 or cl == 16 or cl == 26:
                    r.hset(uid, 'weapon', 16)

                msg, markup = show_inventory(uid)
                answer = 'Русак викинув зброю'
                return msg, markup, True, answer
        else:
            answer = 'В твого русака нема зброї'
            return False, False, False, answer

    elif cdata.startswith('drop_d'):
        if int(r.hget(uid, 'defense')) != 0:
            r.hset(uid, 'defense', 0)
            r.hset(uid, 's_defense', 0)

            msg, markup = show_inventory(uid)
            answer = 'Русак викинув захисне спорядження'
            return msg, markup, True, answer
        else:
            answer = 'В твого русака нема захисного спорядження'
            return False, False, False, answer

    elif cdata.startswith('drop_s'):
        if int(r.hget(uid, 'support')) != 0:
            r.hset(uid, 'support', 0)
            r.hset(uid, 's_support', 0)

            msg, markup = show_inventory(uid)
            answer = 'Русак викинув допоміжне спорядження'
            return msg, markup, True, answer
        else:
            answer = 'В твого русака нема допоміжного спорядження'
            return False, False, False, answer

    elif cdata.startswith('drop_h'):
        if int(r.hget(uid, 'head')) != 0:
            r.hset(uid, 'head', 0)
            r.hset(uid, 's_head', 0)

            msg, markup = show_inventory(uid)
            answer = 'Русак викинув шапку'
            return msg, markup, True, answer
        else:
            answer = 'В твого русака нема шапки'
            return False, False, False, answer


def change_item(cdata, uid):
    forbidden = {'weapon': (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32),
                 'defense': (16, 17),
                 'support': (2, 9),
                 'head': ()}
    if cdata.startswith('backpack_open'):
        if uid == 456514639:

            if not r.hexists(uid, 'backpack_1'):
                r.hset(uid, 'backpack_1', 0, {'backpack_1_s': 0, 'backpack_1_type': 'empty', 'extra_slot': 0,
                                              'backpack_2': 0, 'backpack_2_s': 0, 'backpack_2_type': 'empty'})

            msg, markup = show_backpack(uid)
            return msg, markup, True, False
        else:
            answer = 'Ого, кнопка!'
            return False, False, False, answer

    elif cdata.startswith('backpack_put_in'):
        item_type = cdata.split('_')[3]
        item, s_item = int(r.hget(uid, item_type)), int(r.hget(uid, f's_{item_type}'))

        if int(r.hget(uid, 'backpack_1')):
            if not int(r.hget(uid, 'backpack_2')) and int(r.hget(uid, 'extra_slot')):
                slot = 2
            else:
                slot = 0
        else:
            slot = 1

        if item:
            if slot:
                if item not in forbidden[item_type]:
                    r.hset(uid, item_type, 0, {f's_{item_type}': 0, f'backpack_{slot}': item,
                                               f'backpack_{slot}_s': s_item, f'backpack_{slot}_type': item_type})
                    msg, markup = show_inventory(uid)
                    answer = 'Русак поклав спорядження в рюкзак'
                    return msg, markup, True, answer
                else:
                    answer = 'Класове спорядження неможливо покласти в рюкзак'
                    return False, False, False, answer
            else:
                answer = 'В рюкзаку немає місця'
                return False, False, False, answer
        else:
            answer = 'В твого русака нема цього спорядження'
            return False, False, False, answer

    elif cdata.startswith('backpack_take_'):
        place = cdata.split('_')[2]
        slot = 0
        if place == 'first':
            slot = 1
        elif place == 'second':
            slot = 2

        inv = r.hmget(uid, f'backpack_{slot}', f'backpack_{slot}_s', f'backpack_{slot}_type')
        b, bs, item_type = int(inv[0]), int(inv[1]), inv[2].decode()

        inv = r.hmget(uid, item_type, f's_{item_type}')
        item, s_item = int(inv[0]), int(inv[1])

        if b:
            if item not in forbidden[item_type]:
                r.hset(uid, item_type, b, {f's_{item_type}': bs, f'backpack_{slot}': item,
                                           f'backpack_{slot}_s': s_item})
                if not item:
                    r.hset(uid, f'backpack_{slot}_type', 'empty')
                msg, markup = show_inventory(uid)
                answer = 'Русак дістав спорядження з рюкзака'
                return msg, markup, True, answer
            else:
                answer = 'Класове спорядження неможливо покласти в рюкзак'
                return False, False, False, answer
        else:
            answer = 'В рюкзаку нема цього спорядження'
            return False, False, False, answer
