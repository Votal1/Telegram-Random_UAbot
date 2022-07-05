from config import r
from random import randint
from datetime import datetime


def quests(uid):
    msg = '\U0001F4F0 Щоденні квести\n\n'
    head = int(r.hget(uid, 'head'))
    q1 = ['', '\U0001F3C6 Виграти в 10 дуелях', '\u2622 Купити 5 горілки',
          '\U0001F3DF Взяти участь в 3 міжчатових битвах', '\u26CF Відпрацювати зміну на соляній шахті',
          '\u2620\uFE0F Подивитись втрати окупантів', '\u2694 Взяти участь у 3 масових битвах']
    q1t = [0, 10, 5, 3, 1, 1, 3]

    q2 = ['', '\U0001F3C6 Виграти в 50 дуелях', '\u2694 Виграти у масовій битві',
          '\U0001F469\U0001F3FB Провідати жінку',
          '\U0001F6AC Сходити в козацький похід, або знайти мертвого русака в пакунку',
          '\U0001F4E6 Відкрити 10 пакунків', '\u2694 Взяти участь у битві в Чорнобаївці']
    q2t = [0, 50, 1, 1, 1, 10, 1]

    if int(r.hget(uid, 'qt')) != datetime.now().day:
        r.hset(uid, 'qt', datetime.now().day)

        if head != 6:
            ran1 = randint(1, len(q1) - 1)
            while int(r.hget(uid, 'time1')) == datetime.now().day and ran1 == 4:
                ran1 = randint(1, len(q1) - 1)
            r.hset(uid, 'q1', ran1, {'q1t': q1t[ran1]})

        else:
            ran1 = randint(1, len(q2) - 1)
            r.hset(uid, 'q1', -ran1, {'q1t': q2t[ran1]})

    q = r.hmget(uid, 'q1', 'q1t', 'q2', 'q2t', 'q3', 'q3t')
    if int(q[0]) == 0 and int(q[2]) == 0 and int(q[4]) == 0:
        msg += '\u2705 Всі завдання на сьогодні виконані.'
    else:
        if int(q[0]) > 0:
            msg += f"{q1[int(q[0])]}\n\U0001F9C2 Нагорода - 1 сіль\n" \
                   f"\U0001F4CA Прогрес - {q1t[int(q[0])] - int(q[1])}/{q1t[int(q[0])]}"
        elif int(q[0]) < 0:
            msg += f"{q2[-int(q[0])]}\n\U0001F9C2 Нагорода - 2 солі\n" \
                   f"\U0001F4CA Прогрес - {q2t[-int(q[0])] - int(q[1])}/{q2t[-int(q[0])]}"\

    return msg


def quest(uid, number, unit):
    try:
        q, qt = f'q{number}', f'q{number}t'
        if int(r.hget(uid, 'qt')) == datetime.now().day and int(r.hget(uid, qt)) > 0 and int(r.hget(uid, q)) == unit:
            r.hincrby(uid, qt, -1)
            if int(r.hget(uid, qt)) <= 0:
                if int(r.hget(uid, q)) > 0:
                    r.hincrby(uid, 'salt', 1)
                elif int(r.hget(uid, q)) < 0:
                    r.hincrby(uid, 'salt', 2)
                r.hset(uid, q, 0)
    except:
        pass
