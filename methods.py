from random import randint, choice
from config import r, bot
from variables import names, icons
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


def mine_salt(s2, w):
    success = int(choice(['1', '1', '1', '1', '0']))
    money = randint(3, 8)
    if s2 == 2:
        money += 1
    elif s2 >= 3:
        money += 1
    if w == 3:
        money += 7
    mind = int(choice(['1', '0', '0', '0', '0', '0', '0', '0', '0', '0']))
    if s2 >= 4:
        mind = int(choice(['1', '0', '0', '0', '0']))
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
        markup.add(InlineKeyboardButton(text=f'Совєцкій пайок - {price} грн', callback_data='ration'))
        if int(r.hget(c, 'build1')) == 1:
            msg += '\n\U0001F6E1 Уламок бронетехніки [Захист, міцність=7] - збільшує силу на бій на 30%, або' \
                   ' збільшує міцність захисту на 7. Після зношення повертаються 4 гривні.'
            markup.add(InlineKeyboardButton(text='Уламок бронетехніки - 15 грн', callback_data='clan_fragment'))
        elif int(r.hget(c, 'build1')) == 2:
            msg += '\n\U0001F3A9 Тактичний шолом [Шапка, міцність=40] - збільшує силу в дуелях і ' \
                   'міжчатових битвах на 12%.'
            markup.add(InlineKeyboardButton(text='Тактичний шолом - 50 грн', callback_data='clan_helmet'))
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
        elif int(r.hget(c, 'build5')) == 4:
            msg += '\n\U0001F9EA Цукор [Допомога, міцність=1] - збільшує силу при годуванні на 15 (до 3000 сили) або' \
                   ' зменшує шанс зменшити силу на 15% і додає 5 бойового трансу.'
            markup.add(InlineKeyboardButton(text='Цукор - 55 грн', callback_data='clan_sugar'))
        if int(r.hget(c, 'build6')) == 2:
            msg += '\n\U0001F464 Шапочка з фольги [Шапка, міцність=10] - захищає від втрати бойового духу при ' \
                   'жертвоприношеннях, при купівлі русак отримує 30 шизофренії.'
            markup.add(InlineKeyboardButton(text='Шапочка з фольги - 50 грн', callback_data='clan_foil'))
        elif int(r.hget(c, 'build6')) == 4:
            msg += '\n\U0001F476 Російське немовля - збільшує рейтинг на 88.'
            markup.add(InlineKeyboardButton(text='Російське немовля - 100 грн', callback_data='clan_children'))
        markup.add(InlineKeyboardButton(text='\U0001F451', callback_data='clan_shop_2'),
                   InlineKeyboardButton(text='\U0001F69B', callback_data='clan_shop_3'))
    if page == 2:
        msg = '\U0001F451 Товари для лідера і заступників:'
        if int(r.hget(c, 'monument')) == 1:
            msg += '\n\n\U0001F47E Потратити 10 руского духу на 5 \U0001F44A для кожного учасника клану.'
            markup.add(InlineKeyboardButton(text='\U0001F44A 5 - \U0001F47E 10',
                                            callback_data='monument'))
        if int(r.hget(c, 'base')) == 9:
            msg += '\n\U0001F5E1\U0001F6E1 Колючий комплект - закупити всьому клану дрин і щит.'
            markup.add(InlineKeyboardButton(text='Колючий комплект - \U0001F333 200, \U0001faa8 100',
                                            callback_data='clan_spike'))
        if int(r.hget(c, 'base')) == 9:
            msg += '\n\u2622 Купити тим, хто відпрацював зміну по 10 горірки.'
            markup.add(InlineKeyboardButton(text='Горілка - \U0001F4B5 300',
                                            callback_data='clan_vodka'))
        if int(r.hget(c, 'base')) == 10:
            msg += '\n\U0001f7e1 РПГ-7 [Атака, міцність=1] - завдає ворогу 300 поранень (віднімає бойовий дух,' \
                   ' здоров`я і все спорядження).'
            markup.add(InlineKeyboardButton(text='РПГ-7 - \U0001F47E 200, \U0001F4B5 2000',
                                            callback_data='clan_rpg'))
        if int(r.hget(c, 'base')) == 10:
            msg += '\n\U0001f7e1 Бронежилет вагнерівця [Захист, міцність=50] - зменшує силу ворога на бій на 75%' \
                   ' та захищає від РПГ-7.'
            markup.add(InlineKeyboardButton(text='Бронежилет - \U0001F47E 50, \U0001F4B5 1000',
                                            callback_data='clan_armor'))
        if int(r.hget(c, 'build5')) == 4:
            msg += '\n\U0001F349 Закупити всьому клану Кавун базований [Шапка, міцність=1] - збільшує зарплату за ' \
                   'роботу на соляній шахті на 7. Кавун буде конфісковано, якщо при годуванні зменшиться сила.'
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
                   InlineKeyboardButton(text='\U0001F69B', callback_data='clan_shop_3'))
    if page == 3:
        msg = '\U0001F69B Магазин ресурсів:\n\nНезабаром відкриття...'
        markup.add(InlineKeyboardButton(text='\U0001F3EC', callback_data='clan_shop_1'),
                   InlineKeyboardButton(text='\U0001F451', callback_data='clan_shop_2'))
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
            if chat == 'supergroup':
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
                        title = r.hget('war_battle' + member.decode(), 'title').decode()
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
