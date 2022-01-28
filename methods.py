from random import randint, choice
from config import r, bot
from variables import names, icons


def get_rusak():
    name = randint(0, len(names) - 1)
    strength = randint(10, 50)
    mind = int(choice(['1', '1', '1', '1', '2']))
    return name, strength, mind


def feed_rusak(intel):
    success = int(choice(['1', '1', '1', '1', '0']))
    strength = randint(1, 30)
    mind = 0
    if intel < 20:
        mind = int(choice(['1', '0', '0', '0', '0']))
    bd = int(choice(['1', '0', '0']))
    return success, strength, mind, bd


def mine_salt(s2):
    success = int(choice(['1', '1', '1', '1', '0']))
    money = 5
    if s2 == 1:
        money = randint(3, 8)
    elif s2 == 2:
        money = randint(4, 9)
    elif s2 >= 3:
        money = randint(5, 10)
    mind = int(choice(['1', '0', '0', '0', '0', '0', '0', '0', '0', '0']))
    if s2 >= 4:
        mind = int(choice(['1', '0', '0', '0', '0']))
    return success, money, mind


def top(sett):
    try:
        everyone = r.smembers(sett)
        rating = {}
        for member in everyone:
            if sett != 111:
                try:
                    if bot.get_chat_member(sett, int(member)).status == 'left':
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
                rate = s + i * 10 + w + t * 20 + d * 30 + c * 88
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


def itop(uid, cid, chat):
    try:
        result = ''
        if chat == 'supergroup':
            everyone = r.smembers(cid)
            rating = {}
            for member in everyone:
                try:
                    stats = r.hmget(member, 'strength', 'intellect', 'wins', 'deaths', 'childs', 'trophy',  'username')
                    s = int(stats[0])
                    i = int(stats[1])
                    w = int(stats[2])
                    d = int(stats[3])
                    c = int(stats[4])
                    t = int(stats[5])
                    line = stats[6].decode()
                    rate = s + i * 10 + w + t * 20 + d * 30 + c * 88
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
                rate = s + i * 10 + w + t * 20 + d * 30 + c * 88
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


def ctop(sett):
    try:
        everyone = r.hkeys(sett)
        rating = {}
        for member in everyone:
            try:
                try:
                    i = int(r.hget('c' + member.decode(), 'base'))
                    if i > 0:
                        prefix = ['', 'Банда', 'Клан']
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
