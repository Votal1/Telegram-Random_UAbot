from random import randint, choice
from config import r, bot
from variables import names, icons, weapons, defenses, supports, heads
from datetime import datetime
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_rusak():
    name = randint(0, len(names) - 1)
    strength = randint(100, 150)
    mind = int(choice(['1', '1', '1', '1', '2']))
    return name, strength, mind


def feed_rusak(intel):
    success = int(choice(['1', '1', '1', '1', '0']))
    strength = randint(1, 30)
    mind = 0
    if intel < 20:
        mind = int(choice(['1', '0', '0', '0', '0']))
    bd = int(choice(['2', '1', '1', '1', '1', '1', '1', '0', '0', '0',
                     '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']))
    return success, strength, mind, bd


def mine_salt(s2, w, day):
    success = int(choice(['1', '1', '1', '1', '0']))
    money = randint(3, 8)
    if s2 == 2:
        money += 1
    elif s2 >= 3:
        money += 1
    if w in (3, 5):
        money += 5
    mind = int(choice(['1', '0', '0', '0', '0', '0', '0', '0', '0', '0']))
    if s2 >= 4:
        mind = int(choice(['1', '0', '0', '0', '0']))
    if day in (5, 6):
        money *= 2
    return success, money, mind


def checkClan(uid, base=0, building='', level=0):
    if len(str(r.hget(uid, 'clan'))) > 5:
        cl = r.hget(uid, 'clan')
        if base > 0:
            if not int(r.hget('c' + cl.decode(), 'base')) >= base:
                return False
        if len(building) > 0:
            if level == 0:
                if int(r.hget('c' + cl.decode(), building)) == 0:
                    return False
            else:
                if int(r.hget('c' + cl.decode(), building)) != level:
                    return False
        return True
    else:
        return False


def wood(c, n):
    r.hincrby(c, 'wood', n)
    if int(r.hget(c, 'wood')) > 15000:
        r.hset(c, 'wood', 15000)


def stone(c, n):
    r.hincrby(c, 'stone', n)
    if int(r.hget(c, 'stone')) > 10000:
        r.hset(c, 'stone', 10000)


def cloth(c, n):
    r.hincrby(c, 'cloth', n)
    if int(r.hget(c, 'cloth')) > 5000:
        r.hset(c, 'cloth', 5000)


def brick(c, n):
    r.hincrby(c, 'brick', n)
    if int(r.hget(c, 'brick')) > 3000:
        r.hset(c, 'brick', 3000)


def checkLeader(uid, cid):
    if uid == int(r.hget('c' + str(cid), 'leader')) or str(uid).encode() in r.smembers('cl2' + str(cid)):
        return True
    else:
        return False


def q_points(uid, amount):
    if checkClan(uid) and int(r.hget('c' + r.hget(uid, 'clan').decode(), 'war')) == 1:
        qp = int(r.hget('c' + r.hget(uid, 'clan').decode(), 'q-points'))
        if qp < 500:
            points = 500 - qp
            if points - amount <= 0:
                amount = points
            r.hincrby('c' + r.hget(uid, 'clan').decode(), 'q-points', amount)
            r.hincrby('c' + r.hget(uid, 'clan').decode(), 'points', amount)


def c_shop(c, page):
    msg = ''
    markup = InlineKeyboardMarkup()
    if page == 1:
        msg = '\U0001F3EC Список доступних товарів:\n\nСовєцкій пайок - видається випадкова їжа:\n' \
              '\U0001F366 Пломбір натуральний - \U0001F54A +1000\n' \
              '\U0001F953 Ковбаса докторська - \U0001F54A +1000; \U0001F464 +5 або \U0001F44A +5\n' \
              '\U0001F35E Хліб справжній - [Допомога, міцність=1] - спрацьовує при годуванні і додає ' \
              '\U0001F54A +10000. Якщо допоміжне спорядження вже є, додає \U0001F54A +3000.'
        price = 4 if int(r.hget(c, 'side')) == 1 else 10
        markup.add(InlineKeyboardButton(text=f'Совєцкій пайок - {price} грн', callback_data='clan_ration'))
        if int(r.hget(c, 'build1')) == 1:
            msg += '\n\U0001F6E1 Уламок бронетехніки [Захист, міцність=7] - збільшує силу на бій на 30%, або' \
                   ' збільшує міцність захисту на 7. Після зношення повертаються 4 гривні.'
            markup.add(InlineKeyboardButton(text='Уламок бронетехніки - 15 грн', callback_data='clan_fragment'))
        elif int(r.hget(c, 'build1')) == 2:
            msg += '\n\U0001F3A9 Тактичний шолом [Шапка, міцність=40] - збільшує силу в дуелях і ' \
                   'міжчатових битвах на 31%.'
            markup.add(InlineKeyboardButton(text='Тактичний шолом - 50 грн', callback_data='clan_helmet'))
            msg += '\n\U0001F6A7 Міни [Захист, міцність=3] - з шансом 33% завдає ворогу 5 поранень і ' \
                   'зменшує міцність зброї на 5. Можливість використаит міни при захисті клану. ' \
                   'Бронежилет захищає від мін.'
            markup.add(InlineKeyboardButton(text='Міни - 20 грн', callback_data='clan_bombs'))
        elif int(r.hget(c, 'build1')) == 3:
            msg += '\n\U0001F5E1 Батіг [Атака, міцність=3] - збільшує силу в рейдах на 25%, або на 75%, ' \
                   'якщо нема жінки.'
            markup.add(InlineKeyboardButton(text='Батіг - 60 грн', callback_data='clan_lash'))
        elif int(r.hget(c, 'build1')) == 4:
            msg += '\n\U0001F344 Мухомор королівський [Допомога, міцність=1] - якщо у ворога більший інтелект, додає ' \
                   '+1 інтелекту (не діє проти фокусників). На бій зменшує свою силу на 50%.'
            markup.add(InlineKeyboardButton(text='Мухомор королівський - 100 грн', callback_data='clan_mushroom'))
        if int(r.hget(c, 'build3')) == 4:
            msg += '\n\U0001F695 Дизель [Допомога, міцність=5] - збільшує власну силу в битвах, міжчатових ' \
                   'битвах або рейдах на 25% (тільки для таксистів).'
            markup.add(InlineKeyboardButton(text='Дизель - 20 грн', callback_data='clan_diesel'))
        if int(r.hget(c, 'build5')) == 1:
            msg += '\n\U0001F5E1 АК-47 [Атака, міцність=30] - після перемоги активує ефект горілки.'
            markup.add(InlineKeyboardButton(text='АК-47 - 15 грн', callback_data='clan_ak'))
            msg += '\n\u2744\uFE0F Вушанка [Шапка, міцність=20] - збільшує ефективність бойового трансу на 2% за' \
                   ' кожен рівень алкоголізму.'
            markup.add(InlineKeyboardButton(text='Вушанка - 20 грн', callback_data='clan_ear'))
        elif int(r.hget(c, 'build5')) == 4:
            msg += '\n\U0001F9EA Цукор [Допомога, міцність=1] - збільшує силу при годуванні на 15 (до 3000 сили) або' \
                   ' зменшує шанс зменшити силу на 15% і додає 5 бойового трансу.'
            markup.add(InlineKeyboardButton(text='Цукор - 55 грн', callback_data='clan_sugar'))
            msg += '\n\U0001F37A Квас [Допомога, міцність=5] - русак не втече зі зміни. Додає 5 бойового трансу ' \
                   'за роботу в шахті.'
            markup.add(InlineKeyboardButton(text='Квас - 15 грн', callback_data='clan_kvs'))
        if int(r.hget(c, 'build6')) == 2:
            msg += '\n\U0001F464 Шапочка з фольги [Шапка, міцність=10] - захищає від втрати бойового духу при ' \
                   'жертвоприношеннях, при купівлі русак отримує 30 шизофренії.'
            markup.add(InlineKeyboardButton(text='Шапочка з фольги - 50 грн', callback_data='clan_foil'))
        elif int(r.hget(c, 'build6')) == 4:
            msg += '\n\U0001F476 Російське немовля - збільшує рейтинг на 88.'
            markup.add(InlineKeyboardButton(text='Російське немовля - 100 грн', callback_data='clan_children'))

        if int(r.hget(c, 'base')) == 11:
            msg += '\n\u2708\uFE0F БпЛА [Атака, міцність=1] - за кожен рівень майстерності збільшує силу в ' \
                   'масовій битві на 50% та збільшує шанс не втратити зброю на 18%.'
            markup.add(InlineKeyboardButton(text='БпЛА - \U0001F4B5 50.',
                                            callback_data='clan_uav'))

        markup.add(InlineKeyboardButton(text='\U0001F451', callback_data='clan_shop_2'),
                   InlineKeyboardButton(text='\U0001F69B', callback_data='clan_shop_3'),
                   InlineKeyboardButton(text='\U0001faac', callback_data='clan_shop_4'))

    if page == 2:
        msg = '\U0001F451 Товари для лідера і заступників:'
        if int(r.hget(c, 'monument')) == 1:
            msg += '\n\n\U0001F47E Потратити 10 руского духу на 5 \U0001F44A для кожного учасника клану.'
            markup.add(InlineKeyboardButton(text='\U0001F44A 5 - \U0001F47E 10',
                                            callback_data='clan_monument'))
        if int(r.hget(c, 'base')) == 9:
            msg += '\n\U0001F5E1\U0001F6E1 Колючий комплект - закупити всьому клану дрин і щит.'
            markup.add(InlineKeyboardButton(text='Колючий комплект - \U0001F333 200, \U0001faa8 100',
                                            callback_data='clan_spike'))
        if int(r.hget(c, 'base')) == 9:
            msg += '\n\u2622 Купити тим, хто відпрацював зміну по 10 горілки.'
            markup.add(InlineKeyboardButton(text='Горілка - \U0001F4B5 300',
                                            callback_data='clan_vodka'))
        if int(r.hget(c, 'base')) == 10:
            msg += '\n\U0001f7e1 РПГ-7 [Атака, міцність=1] - завдає ворогу 300 поранень (віднімає бойовий дух,' \
                   ' здоров`я і все спорядження).'
            markup.add(InlineKeyboardButton(text='РПГ-7 - \U0001F47E 250, \U0001F4B5 500',
                                            callback_data='clan_rpg'))
        if int(r.hget(c, 'base')) == 10:
            msg += '\n\U0001f7e1 Бронежилет вагнерівця [Захист, міцність=50] - зменшує силу ворога на бій на 75%' \
                   ' та частково захищає від РПГ-7.'
            markup.add(InlineKeyboardButton(text='Бронежилет - \U0001F47E 50, \U0001F4B5 500',
                                            callback_data='clan_armor'))
        if int(r.hget(c, 'build5')) == 4:
            msg += '\n\U0001F349 Закупити всьому клану Кавун базований [Шапка, міцність=∞] - збільшує зарплату за ' \
                   'роботу на соляній шахті на 5 та силу при годуванні на 5. ' \
                   'Кавун буде конфісковано, якщо при годуванні зменшиться сила.'
            markup.add(InlineKeyboardButton(text='Кавун - \U0001F47E 50, \U0001F4B5 200',
                                            callback_data='clan_watermelon'))
        if int(r.hget(c, 'build6')) == 3:
            msg += '\n\U0001F489 Вилікувати весь клан\n(\U0001fac0 +100).'
            markup.add(InlineKeyboardButton(text='Лікування - \U0001F4B5 10',
                                            callback_data='clan_heal'))
            msg += '\n\U0001F4B5 Перерозподіл багатств - 5 найбідніших учасників отримають по 100 гривень.'
            markup.add(InlineKeyboardButton(text='Перерозподіл - \U0001F47E 10, \U0001F4B5 500 ',
                                            callback_data='clan_money'))
        markup.add(InlineKeyboardButton(text='\U0001F3EC', callback_data='clan_shop_1'),
                   InlineKeyboardButton(text='\U0001F69B', callback_data='clan_shop_3'),
                   InlineKeyboardButton(text='\U0001faac', callback_data='clan_shop_4'))

    if page == 3:
        w, s, cl, b = r.hmget('resources', 'wood', 'stone', 'cloth', 'brick')
        msg = f"\U0001F69B Магазин ресурсів\n\nУ наявності:\n\U0001F333 Деревина: {int(w)}\n" \
              f"\U0001faa8 Камінь: {int(s)}\n\U0001F9F6 Тканина: {int(cl)}\n\U0001F9F1 Цегла: {int(b)}"
        if int(r.hget(c, 'wood')) >= 7500:
            markup.add(InlineKeyboardButton(text='Продати деревину - \U0001F333 1500 -> \U0001F4B5 500',
                                            callback_data='clan_sell_wood'))
        elif int(w) >= 1500:
            markup.add(InlineKeyboardButton(text='Купити деревину - \U0001F4B5 2000 -> \U0001F333 1500',
                                            callback_data='clan_buy_wood'))
        if int(r.hget(c, 'stone')) >= 5000:
            markup.add(InlineKeyboardButton(text='Продати камінь - \U0001faa8 1000 -> \U0001F4B5 500',
                                            callback_data='clan_sell_stone'))
        elif int(s) >= 1000:
            markup.add(InlineKeyboardButton(text='Купити камінь - \U0001F4B5 2000 -> \U0001faa8 1000',
                                            callback_data='clan_buy_stone'))
        if int(r.hget(c, 'cloth')) >= 2500:
            markup.add(InlineKeyboardButton(text='Продати тканину - \U0001F9F6 500 -> \U0001F4B5 500',
                                            callback_data='clan_sell_cloth'))
        elif int(cl) >= 500:
            markup.add(InlineKeyboardButton(text='Купити тканину - \U0001F4B5 2000 -> \U0001F9F6 500',
                                            callback_data='clan_buy_cloth'))
        if int(r.hget(c, 'brick')) >= 1500:
            markup.add(InlineKeyboardButton(text='Продати цеглу - \U0001F9F1 300 -> \U0001F4B5 500',
                                            callback_data='clan_sell_brick'))
        elif int(b) >= 300:
            markup.add(InlineKeyboardButton(text='Купити цеглу - \U0001F4B5 2000 -> \U0001F9F1 300',
                                            callback_data='clan_buy_brick'))
        if int(r.hget(c, 'technics')) >= 50:
            markup.add(InlineKeyboardButton(text='Продати радіотехніку - \U0001F4FB 50 -> \U0001F4B5 500',
                                            callback_data='clan_sell_radio'))
        if int(r.hget(c, 'codes')) >= 1:
            markup.add(InlineKeyboardButton(text='Продати код - \U0001F916 1 -> \U0001F4B5 500, \U0001F47E '
                                                 '50', callback_data='clan_sell_code'))
        markup.add(InlineKeyboardButton(text='\U0001F3EC', callback_data='clan_shop_1'),
                   InlineKeyboardButton(text='\U0001F451', callback_data='clan_shop_2'),
                   InlineKeyboardButton(text='\U0001faac', callback_data='clan_shop_4'))

    if page == 4:
        msg = f"\U0001faac Магазин бафів\n\n"
        if int(r.hget(c, 'war')) == 1:
            if int(r.hget(c, 'buff_1')) == 0:
                msg += '\U0001f7e2 Додаткова нагорода за рейди на клани (залежить від його рівня).\n'
                markup.add(InlineKeyboardButton(text='\U0001f7e2 - \U0001F47E 100 \U0001F9F6 200 '
                                                     '\U0001faa8 1000 \U0001F333 2000',
                                                callback_data='clan_buff_1'))
            if int(r.hget(c, 'buff_2')) == 0:
                msg += '\U0001f7e0 Вдвічі більше очків отримується за рейд на ворожий клан. ' \
                       'Вдвічі більше пакунків за перемогу у війні.\n'
                markup.add(InlineKeyboardButton(text='\U0001f7e0 - \U0001F4B5 10000',
                                                callback_data='clan_buff_2'))
            if int(r.hget(c, 'buff_3')) == 0:
                msg += '\U0001f534 Рейд може проводитись тільки на клан, з яким йде війна. В міжчатовій битві ' \
                       'проти такого клану - прибрано вплив рандому. Можливість бачити очки ворога.\n'
                markup.add(InlineKeyboardButton(text='\U0001f534 - \U0001F916 20 \U0001F4FB 100',
                                                callback_data='clan_buff_3'))

            if int(r.hget(c, 'buff_4')) == 0 and int(r.hget(c, 'base')) >= 4:
                msg += '\nОберіть один з наступних бафів:\n' \
                       '\U0001f7e3 За роботу на благо громади буде нараховано 1-3 квестових очків замість зарплати.\n'
                markup.add(InlineKeyboardButton(text='\U0001f7e3 - \U0001F9F6 200 \U0001F9F1 200',
                                                callback_data='clan_buff_4_0'))

                if int(r.hget(c, 'side')) == 1:
                    msg += '\U0001f7e3\U0001f7e3 +2 очка за звичайні квести.\n'
                    markup.add(InlineKeyboardButton(text='\U0001f7e3\U0001f7e3 - \U0001F9F1 300 \U0001F9F6 600 '
                                                         '\U0001faa8 1500 \U0001F333 3000',
                                                    callback_data='clan_buff_4_1_1'))
                    msg += '\U0001f7e3\U0001f7e3\U0001f7e3 Онулення квестових очків.\n'
                    markup.add(InlineKeyboardButton(text='\U0001f7e3\U0001f7e3\U0001f7e3 - \U0001F916 10 '
                                                         '\U0001F9F1\U0001F9F6\U0001faa8\U0001F333 25%',
                                                    callback_data='clan_buff_4_1_2'))

                elif int(r.hget(c, 'side')) == 2:
                    msg += '\U0001f7e3\U0001f7e3 1% шанс непомітно отримати квестове очко за перемогу в дуелі.\n'
                    markup.add(InlineKeyboardButton(text='\U0001f7e3\U0001f7e3 - \U0001F47E 180',
                                                    callback_data='clan_buff_4_2_1'))
                    msg += '\U0001f7e3\U0001f7e3\U0001f7e3 +12 квестових очків за охорону території.\n'
                    markup.add(InlineKeyboardButton(text='\U0001f7e3\U0001f7e3\U0001f7e3 - '
                                                         '\U0001F916 10 \U0001F47E 25%',
                                                    callback_data='clan_buff_4_2_2'))

                elif int(r.hget(c, 'side')) == 3:
                    msg += '\U0001f7e3\U0001f7e3 +10 квестових очків за пограбування гумконвою.\n'
                    markup.add(InlineKeyboardButton(text='\U0001f7e3\U0001f7e3 - \U0001F4FB 120 \U0001F4B5 2500',
                                                    callback_data='clan_buff_4_3_1'))
                    msg += '\U0001f7e3\U0001f7e3\U0001f7e3 +10 квестових очків за приєднання учасника в клан.\n'
                    markup.add(InlineKeyboardButton(text='\U0001f7e3\U0001f7e3\U0001f7e3 - \U0001F916 10 \U0001F4FB 25%',
                                                    callback_data='clan_buff_4_3_2'))

                elif int(r.hget(c, 'side')) == 4:
                    msg += '\U0001f7e3\U0001f7e3 Шанс знайти 1-2 квестові очка в пакунку замість радіотехніки.\n'
                    markup.add(InlineKeyboardButton(text='\U0001f7e3\U0001f7e3 - \U0001F4FB 50 \U0001F4B5 10000',
                                                    callback_data='clan_buff_4_4_1'))
                    msg += '\U0001f7e3\U0001f7e3\U0001f7e3 +250 квестових очків.\n'
                    markup.add(InlineKeyboardButton(text='\U0001f7e3\U0001f7e3\U0001f7e3 - \U0001F916 10 \U0001F4B5 25%',
                                                    callback_data='clan_buff_4_4_2'))

        else:
            msg += 'Вступіть в кланові війни, щоб купляти бафи\n/clan_war'

        markup.add(InlineKeyboardButton(text='\U0001F3EC', callback_data='clan_shop_1'),
                   InlineKeyboardButton(text='\U0001F451', callback_data='clan_shop_2'),
                   InlineKeyboardButton(text='\U0001F69B', callback_data='clan_shop_3'))

    return msg, markup


def show_inventory(uid):
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

    return msg


def auto_clan_settings(c):
    msg = 'Які налаштування бажаєте змінити?\n\nНазва: ' + r.hget(c, 'title').decode()
    if int(r.hget(c, 'allow')) == 0:
        msg += '\n\nВ клан може приєднатись кожен бажаючий.'
    else:
        msg += '\n\nВ клан можна приєднатись тільки з дозволу адміністраторів.'
    if int(r.hget(c, 'war_allow')) == 0:
        msg += '\n\nВ міжчатову битву може зайти кожен бажаючий.'
    elif int(r.hget(c, 'war_allow')) == 1:
        msg += '\n\nВ міжчатову битву в перші 10 хвилин може зайти тільки учасник клану.'
    else:
        msg += '\n\nВ міжчатову битву в можуть зайти тільки учасники клану.'
    if int(r.hget(c, 'salary')) == 0:
        msg += '\n\nЗа роботу не видається зарплата з кланових ресурсів.'
    else:
        msg += '\n\nЗа роботу з рахунку клану зніматиметься 8 гривень: 5 гривень робітнику, 3 - податок.'
    if int(r.hget(c, 'recruitment')) == 0:
        msg += '\n\nВ Соледарі не відкрито набір в клан. Щоб відкрити, треба платити по 3 радіотехніки в день.'
    else:
        msg += '\n\nВ Соледарі відкрито набір в клан.'
    if int(r.hget(c, 'notification')) == 0:
        msg += '\n\nСповіщення про конвой вимкнені. Щоб увімкнути, треба платити по 5 радіотехніки в день.'
    else:
        msg += '\n\nСповіщення про конвой увімкнені.'
    return msg


def com(data):
    msg = ''
    markup = InlineKeyboardMarkup()
    if data == 'full_list_1':
        markup.add(InlineKeyboardButton(text='Гра в русаків', callback_data='full_list_2'))
        markup.add(InlineKeyboardButton(text='Топ', callback_data='full_list_3'),
                   InlineKeyboardButton(text='Клани', callback_data='full_list_4'))
        markup.add(InlineKeyboardButton(text='Адміністраторські команди', callback_data='full_list_5'))
        msg = 'Інформаційні команди\n\n' \
              '/links - реклама, головний чат, творець\n' \
              '/help - як користуватись\n' \
              '/wiki - інформація щодо гри\n' \
              '/gruz200 - інфа по втратах окупантів\n' \
              '@Random_UAbot - вибрати одну з функцій рандому\n' \
              '/stat - випадкова статистика\n' \
              '/donate - сподобався бот?'
    elif data == 'full_list_2':
        markup.add(InlineKeyboardButton(text='Інформація', callback_data='full_list_1'))
        markup.add(InlineKeyboardButton(text='Топ', callback_data='full_list_3'),
                   InlineKeyboardButton(text='Клани', callback_data='full_list_4'))
        markup.add(InlineKeyboardButton(text='Адміністраторські команди', callback_data='full_list_5'))
        msg = 'Команди для гри в русаків\n\n' \
              '/donbass - взяти русака\n' \
              '/rusak - характеристики\n' \
              '@Random_UAbot - почати битву\n' \
              '@Random_UAbot & - три додаткові режими\n' \
              '/feed - погодувати русака\n' \
              '/quest - щоденні квести\n' \
              '/shop - магазин\n' \
              '/account - грошові запаси\n' \
              '/donate_shop - безтолкові штуки\n' \
              '/pack [number] - Донбаський пакунок\n' \
              '/woman - провідати жінку\n' \
              '/sacrifice - вбити свого русака\n' \
              '/class - вибрати русаку клас\n' \
              '/achieve - досягнення\n' \
              '/skills - вміння\n' \
              '/i - інвентар\n' \
              '/swap - змінити бойового русака (якщо є підвал)\n' \
              '/battle - почати масову битву\n' \
              '/war - почати міжчатову битву\n' \
              '/quit - вийти з міжчатової битви\n' \
              '/crash - зупинити міжчатову битву\n' \
              '/promo_code [код]- активувати бонус\n\n' \
              'Команди, доступні тільки в <a href="https://t.me/+cClR7rA-sZAyY2Uy">@soledar1</a>:\n' \
              '/mine - заробити гривні\n' \
              '/merchant - ' \
              'продає топову снарягу\n' \
              '/clan - доступні клани'
    elif data == 'full_list_3':
        markup.add(InlineKeyboardButton(text='Інформація', callback_data='full_list_1'))
        markup.add(InlineKeyboardButton(text='Гра в русаків', callback_data='full_list_2'))
        markup.add(InlineKeyboardButton(text='Клани', callback_data='full_list_4'))
        markup.add(InlineKeyboardButton(text='Адміністраторські команди', callback_data='full_list_5'))
        msg = 'Топ\n\n/ltop - топ цього чату\n/gtop - глобальний топ\n/itop - яке я місце в топі?\n' \
              '/ctop - топ чатів\n/passport - твої характеристики\n\nОпції для ltop та gtop:\n' \
              '-s, -d, -c, -w, -t, -p, -a'
    elif data == 'full_list_4':
        markup.add(InlineKeyboardButton(text='Інформація', callback_data='full_list_1'))
        markup.add(InlineKeyboardButton(text='Гра в русаків', callback_data='full_list_2'))
        markup.add(InlineKeyboardButton(text='Топ', callback_data='full_list_3'))
        markup.add(InlineKeyboardButton(text='Адміністраторські команди', callback_data='full_list_5'))
        msg = 'Команди для керування кланом\n\n/clan - створити / інформація про клан\n/join - приєднатись\n' \
              '/leave - покинути клан\n/kick [user id] - вигнати з клану\n/work - добувати ресурси\n/relax - ' \
              'відпочивати\n/invest [>0] - перекинути гроші\n/fascist - вибрати фашиста дня\n/clan_settings - ' \
              'налаштування, зарплата за роботу, список учасників\n/upgrade - покращити рівень клану\n/build - ' \
              'розвинути інфраструктуру\n/clan_shop - магазин (доступний на 3 рівні)\n/raid - грабувати інші клани\n' \
              '/guard - охоронятись від рейдів (доступно на 3 рівні)\n/promote - призначити заступника\n' \
              '/demote - видалити заступника'
    elif data == 'full_list_5':
        markup.add(InlineKeyboardButton(text='Інформація', callback_data='full_list_1'))
        markup.add(InlineKeyboardButton(text='Гра в русаків', callback_data='full_list_2'))
        markup.add(InlineKeyboardButton(text='Топ', callback_data='full_list_3'),
                   InlineKeyboardButton(text='Клани', callback_data='full_list_4'))
        markup.add(InlineKeyboardButton(text='Адміністраторські команди', callback_data='full_list_4'))
        msg = 'Адміністраторські команди\nБоту потрібне право банити та адмін з правом редагування групи має ' \
              'увімкнути їх командою /toggle_admin; використовувати команди можуть адміни з правом банити\n\n' \
              '/toggle_captcha - увімкнути капчу (міні-тест при приєднанні до чату)\n/ban [number][m/h/d] /unban\n' \
              '/mute [number][m/h/d/f] /unmute\n/moxir [number][m/h/d] - забрати стікери і медіа\n\nm - хвилини, ' \
              'h - години\nd - дні, f - назавжди'

    return msg, markup


async def top(sett, uid, text):
    try:
        if r.hexists(uid, 'top_ts') == 0:
            r.hset(uid, 'top_ts', 0)
        if int(datetime.now().timestamp()) - int(r.hget(uid, 'top_ts')) >= 60:
            r.hset(uid, 'top_ts', int(datetime.now().timestamp()))
            everyone = r.smembers(sett)
            rating = {}
            for member in everyone:
                if sett != 111:
                    try:
                        st = await bot.get_chat_member(sett, int(member))
                        if st.status == 'left':
                            r.srem(sett, int(member))
                            continue
                    except:
                        r.srem(sett, int(member))
                try:
                    stats = r.hmget(member, 'strength', 'intellect', 'wins', 'deaths', 'childs', 'trophy',
                                    'class', 'username')
                    s = int(stats[0])
                    i = int(stats[1])
                    w = int(stats[2])
                    d = int(stats[3])
                    c = int(stats[4])
                    t = int(stats[5])
                    cl = int(stats[6])
                    line = stats[7].decode() + ' ' + icons[cl] + '\n\U0001F4AA ' + str(s) + \
                                               ' \U0001F9E0 ' + str(i) + ' \u2620\uFE0F ' + str(d) + \
                                               ' \U0001F476 ' + str(c) + '\n\U0001F3C6 ' + str(w) + \
                                               ' \U0001F3C5 ' + str(t) + '\n'
                    try:
                        if text.split(' ')[1] == '-s':
                            rate = s
                        elif text.split(' ')[1] == '-w':
                            rate = w
                        elif text.split(' ')[1] == '-d':
                            rate = d
                        elif text.split(' ')[1] == '-c':
                            rate = c
                        elif text.split(' ')[1] == '-t':
                            rate = t
                        elif text.split(' ')[1] == '-p':
                            rate = int(r.hget(member, 'opened'))
                            line = f'{line[:-1]} \U0001F4E6 {rate}\n'
                        elif text.split(' ')[1] == '-a':
                            rate = int(r.hget(member, 'vodka'))
                            line = f'{line[:-1]} \u2622 {rate}\n'
                        else:
                            raise Exception
                    except:
                        rate = s + i * 10 + w + t * 10 + d * 14 + c * 88
                    rating.update({line: rate})
                except:
                    continue
            s_rating = sorted(rating, key=rating.get, reverse=True)
            result = ''
            place = 1
            for n in s_rating:
                place1 = str(place) + '. '
                result += place1 + n
                place += 1
                if place == 11:
                    break
            if sett == 111:
                return 'Глобальний рейтинг власників русаків \n\n' + result
            else:
                return 'Чатовий рейтинг власників русаків \n\n' + result

    except:
        return 'Недостатньо інформації для створення рейтингу.'


async def itop(uid, cid, chat):
    try:
        if r.hexists(uid, 'top_ts') == 0:
            r.hset(uid, 'top_ts', 0)
        if int(datetime.now().timestamp()) - int(r.hget(uid, 'top_ts')) >= 60:
            r.hset(uid, 'top_ts', int(datetime.now().timestamp()))
            result = ''
            if chat == 'supergroup' and cid != -1001211933154:
                everyone = r.smembers(cid)
                rating = {}
                for member in everyone:
                    try:
                        stats = r.hmget(member, 'strength', 'intellect', 'wins', 'deaths', 'childs',
                                        'trophy',  'username')
                        s = int(stats[0])
                        i = int(stats[1])
                        w = int(stats[2])
                        d = int(stats[3])
                        c = int(stats[4])
                        t = int(stats[5])
                        line = stats[6].decode()
                        rate = s + i * 10 + w + t * 10 + d * 14 + c * 88
                        rating.update({line: rate})
                    except:
                        continue
                s_rating = sorted(rating, key=rating.get, reverse=True)
                place = 1
                for n in s_rating:
                    place1 = str(place) + '. '
                    place += 1
                    if r.hget(uid, 'username').decode() == n:
                        result = '\U0001F3C6 Твоє місце в чатовому рейтингу: \n' + place1 + n + '\n'
                        break
            everyone = r.smembers(111)
            rating = {}
            for member in everyone:
                try:
                    stats = r.hmget(member, 'strength', 'intellect', 'wins', 'deaths', 'childs', 'trophy', 'username')
                    s = int(stats[0])
                    i = int(stats[1])
                    w = int(stats[2])
                    d = int(stats[3])
                    c = int(stats[4])
                    t = int(stats[5])
                    line = stats[6].decode()
                    rate = s + i * 10 + w + t * 10 + d * 14 + c * 88
                    rating.update({line: rate})
                except:
                    continue
            s_rating = sorted(rating, key=rating.get, reverse=True)
            place = 1
            for n in s_rating:
                place1 = str(place) + '. '
                place += 1
                if r.hget(uid, 'username').decode() == n:
                    result += '\U0001F3C6 Твоє місце в глобальному рейтингу: \n' + place1 + n
                    break
            return result
    except:
        return 'Недостатньо інформації для створення рейтингу.'


async def ctop(sett, uid):
    try:
        if r.hexists(uid, 'top_ts') == 0:
            r.hset(uid, 'top_ts', 0)
        if int(datetime.now().timestamp()) - int(r.hget(uid, 'top_ts')) >= 60:
            r.hset(uid, 'top_ts', int(datetime.now().timestamp()))
            everyone = r.hkeys(sett)
            rating = {}
            for member in everyone:
                try:
                    try:
                        i = int(r.hget('c' + member.decode(), 'base'))
                        if i > 0:
                            prefix = ['', 'Банда', 'Клан', 'Гільдія', 'Угруповання',
                                      'Комуна', 'Коаліція', 'Асоціація', 'Організація',
                                      'Союз', 'Орден', 'Ліга', 'Корпорація']
                            title = '<i>' + prefix[i] + '</i> ' + r.hget('c' + member.decode(), 'title').decode()
                        else:
                            title = r.hget('war_battle' + member.decode(), 'title').decode()
                    except:
                        title = r.hget('war_battle' + member.decode(), 'title').decode().\
                            replace('<', '.').replace('>', '.')
                    if '@' in title:
                        continue
                    stats = int(r.hget(222, member))
                    line = title + '\n\U0001F3C5 ' + str(stats) + '\n'
                    rating.update({line: stats})
                except:
                    continue
            s_rating = sorted(rating, key=rating.get, reverse=True)
            result = ''
            place = 1
            for n in s_rating:
                place1 = str(place) + '. '
                result += place1 + n
                place += 1
                if place == 11:
                    break
            return 'Рейтинг найсильніших чатів\n\n' + result

    except:
        return 'Недостатньо інформації для створення рейтингу.'
