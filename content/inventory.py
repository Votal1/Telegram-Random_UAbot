from config import r
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from constants.equipment import weapons, defenses, supports, heads, upgradable, \
    weapons1, defenses1, supports1, heads1


def invent_start():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='\U0001F510', callback_data='drop_open'),
               InlineKeyboardButton(text='\U0001F392', callback_data='backpack_open'),
               InlineKeyboardButton(text=f'🌀', callback_data='tape_all'))
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
    markup.add(InlineKeyboardButton(text='\u21A9\uFE0F', callback_data='backpack_return'))
    return markup


def put_in_backpack(markup, w, d, s, h):
    if w > 0 and d > 0:
        markup.add(InlineKeyboardButton(text=f'\u27A1\uFE0F\U0001F392 {weapons[w]}',
                                        callback_data='backpack_put_in_weapon'),
                   InlineKeyboardButton(text=f'\u27A1\uFE0F\U0001F392 {defenses[d]}',
                                        callback_data='backpack_put_in_defense'))
    elif w > 0:
        markup.add(InlineKeyboardButton(text=f'\u27A1\uFE0F\U0001F392 {weapons[w]}',
                                        callback_data='backpack_put_in_weapon'))
    elif d > 0:
        markup.add(InlineKeyboardButton(text=f'\u27A1\uFE0F\U0001F392 {defenses[d]}',
                                        callback_data='backpack_put_in_defense'))
    if s > 0 and h > 0:
        markup.add(InlineKeyboardButton(text=f'\u27A1\uFE0F\U0001F392 {supports[s]}',
                                        callback_data='backpack_put_in_support'),
                   InlineKeyboardButton(text=f'\u27A1\uFE0F\U0001F392 {heads[h]}',
                                        callback_data='backpack_put_in_head'))
    elif s > 0:
        markup.add(InlineKeyboardButton(text=f'\u27A1\uFE0F\U0001F392 {supports[s]}',
                                        callback_data='backpack_put_in_support'))
    elif h > 0:
        markup.add(InlineKeyboardButton(text=f'\u27A1\uFE0F\U0001F392 {heads[h]}',
                                        callback_data='backpack_put_in_head'))
    return markup


def upgrade_button(w, d, s, h):
    markup = InlineKeyboardMarkup()
    if w > 0 and d > 0:
        markup.add(InlineKeyboardButton(text=f'\u2B06\uFE0F {weapons[w]}',
                                        callback_data='tape_weapon'),
                   InlineKeyboardButton(text=f'\u2B06\uFE0F {defenses[d]}',
                                        callback_data='tape_defense'))
    elif w > 0:
        markup.add(InlineKeyboardButton(text=f'\u2B06\uFE0F {weapons[w]}',
                                        callback_data='tape_weapon'))
    elif d > 0:
        markup.add(InlineKeyboardButton(text=f'\u2B06\uFE0F {defenses[d]}',
                                        callback_data='tape_defense'))
    if s > 0 and h > 0:
        markup.add(InlineKeyboardButton(text=f'\u2B06\uFE0F {supports[s]}',
                                        callback_data='tape_support'),
                   InlineKeyboardButton(text=f'\u2B06\uFE0F {heads[h]}',
                                        callback_data='tape_head'))
    elif s > 0:
        markup.add(InlineKeyboardButton(text=f'\u2B06\uFE0F {supports[s]}',
                                        callback_data='tape_support'))
    elif h > 0:
        markup.add(InlineKeyboardButton(text=f'\u2B06\uFE0F {heads[h]}',
                                        callback_data='tape_head'))
    markup.add(InlineKeyboardButton(text='\u21A9\uFE0F', callback_data='backpack_return'))

    return markup


def upgrade_button2():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=f'\u2B06\uFE0F {weapons[7]}',
                                    callback_data='tape1_weapon'),
               InlineKeyboardButton(text=f'\u2B06\uFE0F {defenses[4]}',
                                    callback_data='tape1_defense'))
    markup.add(InlineKeyboardButton(text=f'\u2B06\uFE0F {supports[13]}',
                                    callback_data='tape1_support'),
               InlineKeyboardButton(text=f'\u2B06\uFE0F {heads[4]}',
                                    callback_data='tape1_head'))
    markup.add(InlineKeyboardButton(text='\u21A9\uFE0F', callback_data='backpack_return'))

    return markup


def take_from_backpack(markup, item1=False, item2=False, item3=False, item4=False):
    if item1:
        markup.add(InlineKeyboardButton(text=f'\u2B05\uFE0F\U0001F392 {item1}', callback_data='backpack_take_first'))
    if item2:
        markup.add(InlineKeyboardButton(text=f'\u2B05\uFE0F\U0001F392 {item2}', callback_data='backpack_take_second'))
    if item3:
        markup.add(InlineKeyboardButton(text=f'\u2B05\uFE0F\U0001F392 {item3}', callback_data='backpack_take_third'))
    if item4:
        markup.add(InlineKeyboardButton(text=f'\u2B05\uFE0F\U0001F392 {item4}', callback_data='backpack_take_fourth'))
    return markup


def show_inventory(uid, full=False, upgrade=False):
    inv = r.hmget(uid, 'weapon', 'defense', 'support', 'head', 's_weapon', 's_defense', 's_support', 's_head')
    w, d, s, h = int(inv[0]), int(inv[1]), int(inv[2]), int(inv[3])

    if upgrade:
        i = 0
        tape = int(r.hget(uid, 'tape'))
        m1 = m2 = m3 = m4 = ''

        if check_set(w, d, s, h) == 1:
            msg = f'🌀 Ізострічка: {tape}\n\n\u2B06\uFE0F Ваше спорядження може бути відремонтоване за 1 ' \
                  f'ізострічку (міцність буде збільшена до 50)'
            return msg, upgrade_button2(), True, False
        else:
            if w in upgradable['weapon']:
                i += 1
                m1 = f'\U0001F5E1 {weapons[w]}\n'
            else:
                w = 0
            if d in upgradable['defense']:
                i += 1
                m2 = f'\U0001F6E1 {defenses[d]}\n'
            else:
                d = 0
            if s in upgradable['support']:
                i += 1
                m3 = f'\U0001F9EA {supports[s]}\n'
            else:
                s = 0
            if h in upgradable['head']:
                i += 1
                m4 = f'\U0001F3A9 {heads[h]}'
            else:
                h = 0

            if i:
                msg = f'🌀 Ізострічка: {tape}\n\n\u2B06\uFE0F Спорядження, яке можливо покращити:\n\n{m1}{m2}{m3}{m4}'
                return msg, upgrade_button(w, d, s, h), True, False
            else:
                return None, None, False, 'Нема спорядження, яке можна покращити'

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
        markup = invent_start()

    return msg, markup


def show_backpack(uid):
    msg = '\U0001F392 Рюкзак:\n\n'
    markup = InlineKeyboardMarkup()

    inv = r.hmget(uid, 'weapon', 'defense', 'support', 'head', 's_weapon', 's_defense', 's_support', 's_head')
    w, d, s, h = int(inv[0]), int(inv[1]), int(inv[2]), int(inv[3])

    extra_slot = int(r.hget(uid, 'extra_slot'))
    if True:
        empty = 0
        free_slots = extra_slot + 1
        for item in range(1, extra_slot + 2):
            inv = r.hmget(uid, f'backpack_{item}', f'backpack_{item}_s', f'backpack_{item}_type')
            b1, b1s, b1t = int(inv[0]), int(inv[1]), inv[2].decode()

            if not b1:
                empty += 1
            else:
                free_slots -= 1
                item1 = False

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
                    if b1 == 3:
                        b1s = '∞'
                    msg += f'\U0001F3A9 Шапка: {item1}\nМіцність: {b1s}\n'

                markup.add(InlineKeyboardButton(text=f'\u2B05\uFE0F\U0001F392 {item1}',
                                                callback_data=f'backpack_take_{item}'))
        if extra_slot >= extra_slot + 1 - free_slots:
            markup = put_in_backpack(markup, w, d, s, h)

        if empty == extra_slot + 1:
            msg += '[Порожньо]'
    else:
        inv = r.hmget(uid, 'extra_slot', 'backpack_1', 'backpack_1_s', 'backpack_1_type',
                      'backpack_2', 'backpack_2_s', 'backpack_2_type',
                      'backpack_3', 'backpack_3_s', 'backpack_3_type',
                      'backpack_4', 'backpack_4_s', 'backpack_4_type')
        b1, b1s, b1t = int(inv[1]), int(inv[2]), inv[3].decode()
        b2, b2s, b2t = int(inv[4]), int(inv[5]), inv[6].decode()
        b3, b3s, b3t = int(inv[7]), int(inv[8]), inv[9].decode()
        b4, b4s, b4t = int(inv[10]), int(inv[11]), inv[12].decode()

        if not b1 and not b2 and not b3 and not b4:
            msg += '[Порожньо]'
            markup = put_in_backpack(markup, w, d, s, h)
        else:
            item1, item2, item3, item4 = False, False, False, False

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
                if b1 == 3:
                    b1s = '∞'
                msg += f'\U0001F3A9 Шапка: {item1}\nМіцність: {b1s}\n'

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
                if b2 == 3:
                    b2s = '∞'
                msg += f'\U0001F3A9 Шапка: {heads[b2]}\nМіцність: {b2s}\n'

            if b3t == 'weapon':
                item3 = weapons[b3]
                msg += f'\U0001F5E1 Зброя: {weapons[b3]}\nМіцність: {b3s}\n'
            elif b3t == 'defense':
                item3 = defenses[b3]
                msg += f'\U0001F6E1 Захист: {defenses[b3]}\nМіцність: {b3s}\n'
            elif b3t == 'support':
                item3 = supports[b3]
                msg += f'\U0001F9EA Допомога: {supports[b3]}\nМіцність: {b3s}\n'
            elif b3t == 'head':
                item3 = heads[b3]
                if b3 == 3:
                    b3s = '∞'
                msg += f'\U0001F3A9 Шапка: {heads[b3]}\nМіцність: {b3s}\n'

            if b4t == 'weapon':
                item4 = weapons[b4]
                msg += f'\U0001F5E1 Зброя: {weapons[b4]}\nМіцність: {b4s}\n'
            elif b4t == 'defense':
                item4 = defenses[b4]
                msg += f'\U0001F6E1 Захист: {defenses[b4]}\nМіцність: {b4s}\n'
            elif b4t == 'support':
                item4 = supports[b4]
                msg += f'\U0001F9EA Допомога: {supports[b4]}\nМіцність: {b4s}\n'
            elif b4t == 'head':
                item4 = heads[b4]
                if b4 == 3:
                    b4s = '∞'
                msg += f'\U0001F3A9 Шапка: {heads[b4]}\nМіцність: {b4s}\n'

            free_slots = 4
            for n in (b1, b2, b3, b4):
                if n:
                    free_slots -= 1
            if extra_slot >= 4 - free_slots:
                markup = put_in_backpack(markup, w, d, s, h)

            markup = take_from_backpack(markup, item1, item2, item3, item4)

    markup.add(InlineKeyboardButton(text='\u21A9\uFE0F', callback_data='backpack_return'))

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
            if int(r.hget(uid, 'support')) == 11:
                answer = 'Повістки не позбутись'
                return False, False, False, answer
            else:
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


def empty_backpack(cdata, uid):
    if not cdata:
        backpack = show_backpack(uid)[0]
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Так', callback_data='backpack_empty'))
        msg = f'{backpack}\n\nДійсно бажаєте викинути увесь вміст рюкзака?'
        return msg, markup

    if cdata.startswith('backpack_empty'):
        if r.hexists(uid, 'extra_slot'):
            extra_slot = int(r.hget(uid, 'extra_slot'))
            for slot in range(1, extra_slot + 2):
                r.hset(uid, f'backpack_{slot}', 0, {f'backpack_{slot}_s': 0, f'backpack_{slot}_type': 'empty'})
        answer = 'Рюкзак очищено'
        msg, markup = show_inventory(uid)
        return msg, markup, True, answer


def change_item(cdata, uid):
    forbidden = {'weapon': (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                            27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42),
                 'defense': (16, 17, 18),
                 'support': (2, 6, 9, 11, 14),
                 'head': ()}
    if cdata.startswith('backpack_open'):
        if not r.hexists(uid, 'extra_slot'):
            r.hset(uid, 'extra_slot', 0)
        extra_slot = int(r.hget(uid, 'extra_slot'))
        for slot in range(1, extra_slot + 2):
            if not r.hexists(uid, f'backpack_{slot}'):
                r.hset(uid, f'backpack_{slot}', 0, {f'backpack_{slot}_s': 0, f'backpack_{slot}_type': 'empty'})

        msg, markup = show_backpack(uid)
        return msg, markup, True, False

    elif cdata.startswith('backpack_return'):
        msg, markup = show_inventory(uid)
        return msg, markup, True, False

    elif cdata.startswith('backpack_put_in'):
        item_type = cdata.split('_')[3]
        item, s_item = int(r.hget(uid, item_type)), int(r.hget(uid, f's_{item_type}'))
        extra = int(r.hget(uid, 'extra_slot'))

        for n in range(1, extra + 2):
            if extra >= n - 1 and not int(r.hget(uid, f'backpack_{n}')):
                slot = n
                break
        else:
            slot = 0

        if item:
            if slot:
                cl = int(r.hget(uid, 'class'))
                if item not in forbidden[item_type] or allow_class_item(cl, item, item_type):
                    r.hset(uid, item_type, 0, {f's_{item_type}': 0, f'backpack_{slot}': item,
                                               f'backpack_{slot}_s': s_item, f'backpack_{slot}_type': item_type})
                    msg, markup = show_inventory(uid)
                    answer = 'Русак поклав спорядження в рюкзак'
                    return msg, markup, True, answer
                else:
                    answer = 'Це спорядження неможливо покласти в рюкзак'
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
        elif place == 'third':
            slot = 3
        elif place == 'fourth':
            slot = 4
        elif place in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
            slot = int(place)

        inv = r.hmget(uid, f'backpack_{slot}', f'backpack_{slot}_s', f'backpack_{slot}_type')
        b, bs, item_type = int(inv[0]), int(inv[1]), inv[2].decode()

        if b:
            inv = r.hmget(uid, item_type, f's_{item_type}', 'class')
            item, s_item, cl = int(inv[0]), int(inv[1]), int(inv[2])
            if item not in forbidden[item_type] or allow_class_item(cl, item, item_type):
                if b not in forbidden[item_type] or allow_class_item(cl, b, item_type):
                    r.hset(uid, item_type, b, {f's_{item_type}': bs, f'backpack_{slot}': item,
                                               f'backpack_{slot}_s': s_item})
                    if not item:
                        r.hset(uid, f'backpack_{slot}_type', 'empty')
                    msg, markup = show_inventory(uid)
                    answer = 'Русак дістав спорядження з рюкзака'
                    return msg, markup, True, answer
                else:
                    answer = 'Це спорядження неможливо взяти з рюкзака'
                    return False, False, False, answer
            else:
                answer = 'Це спорядження неможливо взяти з рюкзака, бо ваше неможливо покласти'
                return False, False, False, answer
        else:
            answer = 'В рюкзаку нема цього спорядження'
            return False, False, False, answer


def allow_class_item(cl, item, item_type='empty'):
    if cl in (1, 11, 21) and item in (11, 22, 33):
        return True
    elif cl in (2, 12, 22) and item in (12, 23, 34):
        return True
    elif cl in (3, 13, 23) and item in (13, 24, 35):
        return True
    elif cl in (4, 14, 24) and item in (14, 25, 36):
        return True
    elif cl in (5, 15, 25) and item in (15, 26, 37):
        return True
    elif cl in (6, 16, 26) and item in (16, 17, 18):
        if item_type == 'weapon':
            return False
        else:
            return True
    elif cl in (7, 17, 27) and item in (17, 28, 38):
        return True
    elif cl in (8, 18, 28) and item in (18, 29, 39):
        return True
    elif cl in (9, 19, 29) and item in (19, 30, 40):
        return True
    elif cl in (10, 20, 30) and item in (20, 31, 41):
        return True
    elif cl in (31, 32, 33) and item in (2, 9, 14):
        return True
    elif cl in (34, 35, 36) and item in (21, 32, 42):
        return True
    else:
        return False


def upgrade_item(cdata, uid):
    if not r.hexists(uid, 'tape'):
        r.hset(uid, 'tape', 0)
    if cdata.startswith('tape_all'):
        msg, markup, response, answer = show_inventory(uid, upgrade=True)
        return msg, markup, response, answer
    elif cdata.startswith('tape1'):
        item_type = cdata.split('_')[1]
        tape = int(r.hget(uid, 'tape'))
        inv = r.hmget(uid, 'weapon', 'defense', 'support', 'head', 's_weapon', 's_defense', 's_support', 's_head')
        w, d, s, h = int(inv[0]), int(inv[1]), int(inv[2]), int(inv[3])
        if check_set(w, d, s, h) == 1:
            if tape >= 1:
                if int(r.hget(uid, f's_{item_type}')) < 50:
                    r.hset(uid, f's_{item_type}', 50)
                    r.hincrby(uid, 'tape', -1)
                    answer = f'Спорядження відремонтовано\nВитрачено: 🌀 1'
                    msg, markup = show_inventory(uid)
                    return msg, markup, True, answer
                else:
                    answer = 'Необхідне спорядження, міцність якого менша 50'
                    return False, False, False, answer
            else:
                answer = 'Необхідна 1 ізострічка'
                return False, False, False, answer
        else:
            answer = 'Зараз у вас немає такої можливості'
            return False, False, False, answer

    else:
        item_type = cdata.split('_')[1]
        item = int(r.hget(uid, item_type))
        tape = int(r.hget(uid, 'tape'))
        if item in upgradable[item_type]:

            price = 1
            if item_type == 'weapon' and item in (22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32):
                price = 3
            elif item_type == 'defense' and item == 17:
                price = 3
            elif item_type == 'support' and item == 9:
                price = 3

            if tape >= price:
                upgrade_to = item1 = item2 = 0
                if cdata.startswith('tape_weapon'):
                    upgrade_to = weapons1[item]
                    item1 = weapons[item]
                    item2 = weapons[upgrade_to]
                    if item == 16:
                        r.hset(uid, f's_{item_type}', 1)
                elif cdata.startswith('tape_defense'):
                    upgrade_to = defenses1[item]
                    item1 = defenses[item]
                    item2 = defenses[upgrade_to]
                elif cdata.startswith('tape_support'):
                    upgrade_to = supports1[item]
                    item1 = supports[item]
                    item2 = supports[upgrade_to]
                    if item == 1:
                        r.hset(uid, f's_{item_type}', 40)
                elif cdata.startswith('tape_head'):
                    upgrade_to = heads1[item]
                    item1 = heads[item]
                    item2 = heads[upgrade_to]
                answer = f'Покращено "{item1}" до "{item2}"\nВитрачено: 🌀 {price}'
                r.hincrby(uid, 'tape', -price)
                r.hset(uid, item_type, upgrade_to)
                msg, markup = show_inventory(uid)
                return msg, markup, True, answer
            else:
                answer = f'Необхідно ізострічок: {price}'
                return False, False, False, answer
        else:
            answer = 'Це спорядження неможливо покращити'
            return False, False, False, answer


def check_set(w, d, s, h):
    if w in (7, 38) and d == 4 and s in (13, 14) and h == 4:
        return 1
    elif w in (2, 8, 33, 37, 39, 40) and d in (2, 18) and s == 15 and h == 2:
        return 2
    elif w in (9, 43, 36, 41) and d == 10 and s in (16, 17, 18, 19, 20) and h == 7:
        return 3
    elif w in (10, 42) and d == 5 and s == 12 and h == 6:
        return 4
    elif w in (6, 34, 35) and d == 6 and s in (10, 11) and h == 3:
        return 5
    return 0
