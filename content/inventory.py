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
    markup.add(InlineKeyboardButton(text='\U0001F510', callback_data='drop_open'))
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


def drop_item(cdata, uid):
    if cdata.startswith('drop_open'):
        msg, markup = show_inventory(uid, full=True)
        return msg, markup, True, False
    '''
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
    '''
