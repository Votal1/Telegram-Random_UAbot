from config import r
from methods import checkClan, q_points
from parameters import damage_head
from random import randint
from datetime import datetime

q1 = ['', '\U0001F3C6 Виграти в 10 дуелях', '\u2622 Купити горілку 5 разів',
      '\U0001F3DF Взяти участь в 3 міжчатових битвах', '\u26CF Відпрацювати зміну на соляній шахті',
      '\u2620\uFE0F Подивитись втрати окупантів', '\u2694 Взяти участь у 3 масових битвах']
q1t = [0, 10, 5, 3, 1, 1, 3]
q1p = ['', '\U0001F3C6 Виграти в 50 дуелях', '\u2694 Виграти у масовій битві',
       '\U0001F469\U0001F3FB Провідати жінку',
       '\U0001F6AC Сходити в козацький похід, або знайти мертвого русака в пакунку',
       '\U0001F4E6 Відкрити 10 пакунків', '\u2694 Взяти участь у битві в Чорнобаївці']
q1pt = [0, 50, 1, 1, 1, 10, 1]

q2 = ['', '\U0001F4B0 Сходити в рейд', '\U0001F47E Виграти міжчатову битву з своїм кланом',
      '\U0001F4B5 Інвестувати в клан від 50 гривень']
q2t = [0, 1, 1, 1]
q2p = ['', '\U0001F35E Купити совєцкій пайок', '\U0001F44A Отримати бойовий транс від монументу',
       '\U0001F319 Відпочити після роботи']
q2pt = [0, 1, 1, 1]

q31 = ['', '\U0001F333 Попрацювати на благо громади', '\u2744\uFE0F Купити / отримати вушанку',
       '\U0001F6E1 Купити / знайти в пакунку уламок бронетехніки']
q31t = [0, 1, 1, 1]
q31p = ['', '\U0001F9F0 Купити ящик горілки', '\U0001F6AC Взяти участь у битві в темному провулку',
        '\U0001F46E Вступити в бій з товаришом майором 3 рази']
q31pt = [0, 1, 1, 3]

q32 = ['', '\U0001F3DF Перемогти в міжчатовій битві 5 разів', '\U0001F35C Погодувати русака',
       '\U0001F3C6 Купити горілку, маючи 10000 бойового духу']
q32t = [0, 5, 1, 1]
q32p = ['', '\U0001F5FF Провести 10 боїв проти хачів', '\U0001F396 Програти дуель проти генерала',
        '\U0001fa96 Провести 3 міжчатові битви разом з гарматним м`ясом']
q32pt = [0, 10, 1, 3]

q33 = ['', '\U0001F469\U0001F3FB Купити батіг або жінку', '\U0001F4B0 Набрати 100000 сили в рейді',
       '\U0001F69B Пограбувати гумконвой або знайти радіотехніку в пакунку']
q33t = [0, 1, 1, 1]
q33p = ['', '\U0001F919 Провести 30 боїв проти ворога без зброї', '\U0001F52E Отримати шизофренію від фокусів',
        '\U0001F921 Перемогти малороса 20 разів']
q33pt = [0, 30, 1, 20]

q34 = ['', '\U0001F4B5 Знайти гроші в пакунку', '\U0001F9C2 Купити силу на сольовому ринку',
       '\U0001F9EA Купити щось в клановому магазині']
q34t = [0, 1, 1, 1]
q34p = ['', '\u26D1 Зменшити здоров`я до 0 в дуелях', '\U0001F695 Однією дією отримати 10 донбаських пакунків',
        '\U0001F4DF Виграти в дуелі так, щоб ворог використав Rootkit']
q34pt = [0, 1, 1, 1]


def re_roll(uid, change1, change2, change3):
    head = int(r.hget(uid, 'head'))
    if head != 6:
        if change1:
            ran1 = randint(1, len(q1) - 1)
            while int(r.hget(uid, 'time1')) == datetime.now().day and ran1 == 4:
                ran1 = randint(1, len(q1) - 1)
            while ran1 == change1:
                ran1 = randint(1, len(q1) - 1)
                while int(r.hget(uid, 'time1')) == datetime.now().day and ran1 == 4:
                    ran1 = randint(1, len(q1) - 1)
            r.hset(uid, 'q1', ran1, {'q1t': q1t[ran1]})

        if checkClan(uid, building='wall'):

            if change2:
                ran2 = randint(1, len(q2) - 1)
                while ran2 == change2:
                    ran2 = randint(1, len(q2) - 1)
                r.hset(uid, 'q2', ran2, {'q2t': q2t[ran2]})

            if change3:
                side = int(r.hget('c' + r.hget(uid, 'clan').decode(), 'side'))
                if side == 1:
                    ran1 = randint(1, len(q31) - 1)
                    while int(r.hget(uid, 'clan_time')) == datetime.now().day and ran1 == 1:
                        ran1 = randint(1, len(q31) - 1)
                    while ran1 == change3:
                        ran1 = randint(1, len(q31) - 1)
                    r.hset(uid, 'q3', ran1, {'q3t': q31t[ran1]})
                elif side == 2:
                    ran1 = randint(1, len(q32) - 1)
                    while int(r.hget(uid, 'time')) == datetime.now().day and ran1 == 2:
                        ran1 = randint(1, len(q32) - 1)
                    while ran1 == change3:
                        ran1 = randint(1, len(q32) - 1)
                    r.hset(uid, 'q3', ran1, {'q3t': q32t[ran1]})
                elif side == 3:
                    ran1 = randint(1, len(q33) - 1)
                    while ran1 == change3:
                        ran1 = randint(1, len(q33) - 1)
                    r.hset(uid, 'q3', ran1, {'q3t': q33t[ran1]})
                elif side == 4:
                    ran1 = randint(1, len(q34) - 1)
                    while int(r.hget(uid, 'salt')) < 5 and ran1 == 2:
                        ran1 = randint(1, len(q34) - 1)
                    while ran1 == change3:
                        ran1 = randint(1, len(q34) - 1)
                    r.hset(uid, 'q3', ran1, {'q3t': q34t[ran1]})

    else:
        if change1:
            ran1 = randint(1, len(q1p) - 1)
            while ran1 == -change1:
                ran1 = randint(1, len(q1p) - 1)
            r.hset(uid, 'q1', -ran1, {'q1t': q1pt[ran1]})

        if checkClan(uid, building='wall'):

            if change2:
                ran2 = randint(1, len(q2p) - 1)
                while ran2 == -change2:
                    ran2 = randint(1, len(q2p) - 1)
                r.hset(uid, 'q2', -ran2, {'q2t': q2pt[ran2]})

            side = int(r.hget('c' + r.hget(uid, 'clan').decode(), 'side'))

            if change3:
                if side == 1:
                    ran1 = randint(1, len(q31p) - 1)
                    while ran1 == -change3:
                        ran1 = randint(1, len(q31p) - 1)
                    r.hset(uid, 'q3', -ran1, {'q3t': q31pt[ran1]})
                elif side == 2:
                    ran1 = randint(1, len(q32p) - 1)
                    while ran1 == -change3:
                        ran1 = randint(1, len(q32p) - 1)
                    r.hset(uid, 'q3', -ran1, {'q3t': q32pt[ran1]})
                elif side == 3:
                    ran1 = randint(1, len(q33p) - 1)
                    while ran1 == -change3:
                        ran1 = randint(1, len(q33p) - 1)
                    r.hset(uid, 'q3', -ran1, {'q3t': q33pt[ran1]})
                elif side == 4:
                    ran1 = randint(1, len(q34p) - 1)
                    while ran1 == -change3:
                        ran1 = randint(1, len(q34p) - 1)
                    r.hset(uid, 'q3', -ran1, {'q3t': q34pt[ran1]})


def quests(uid):
    msg = '\U0001F4F0 Щоденні квести'
    head = int(r.hget(uid, 'head'))

    if int(r.hget(uid, 'qt')) != datetime.now().day:
        r.hset(uid, 'qt', datetime.now().day)

        if head != 6:
            ran1 = randint(1, len(q1) - 1)
            while int(r.hget(uid, 'time1')) == datetime.now().day and ran1 == 4:
                ran1 = randint(1, len(q1) - 1)
            r.hset(uid, 'q1', ran1, {'q1t': q1t[ran1]})

            if checkClan(uid, building='wall'):
                ran2 = randint(1, len(q2) - 1)
                r.hset(uid, 'q2', ran2, {'q2t': q2t[ran2]})

                side = int(r.hget('c' + r.hget(uid, 'clan').decode(), 'side'))
                if side == 1:
                    ran1 = randint(1, len(q31) - 1)
                    while int(r.hget(uid, 'clan_time')) == datetime.now().day and ran1 == 1:
                        ran1 = randint(1, len(q31) - 1)
                    r.hset(uid, 'q3', ran1, {'q3t': q31t[ran1]})
                elif side == 2:
                    ran1 = randint(1, len(q32) - 1)
                    while int(r.hget(uid, 'time')) == datetime.now().day and ran1 == 2:
                        ran1 = randint(1, len(q32) - 1)
                    r.hset(uid, 'q3', ran1, {'q3t': q32t[ran1]})
                elif side == 3:
                    ran1 = randint(1, len(q33) - 1)
                    r.hset(uid, 'q3', ran1, {'q3t': q33t[ran1]})
                elif side == 4:
                    ran1 = randint(1, len(q34) - 1)
                    while int(r.hget(uid, 'salt')) < 5 and ran1 == 2:
                        ran1 = randint(1, len(q34) - 1)
                    r.hset(uid, 'q3', ran1, {'q3t': q34t[ran1]})

        else:
            damage_head(uid)
            ran1 = randint(1, len(q1p) - 1)
            r.hset(uid, 'q1', -ran1, {'q1t': q1pt[ran1]})

            if checkClan(uid, building='wall'):
                ran2 = randint(1, len(q2p) - 1)
                r.hset(uid, 'q2', -ran2, {'q2t': q2pt[ran2]})

                side = int(r.hget('c' + r.hget(uid, 'clan').decode(), 'side'))
                if side == 1:
                    ran1 = randint(1, len(q31p) - 1)
                    r.hset(uid, 'q3', -ran1, {'q3t': q31pt[ran1]})
                elif side == 2:
                    ran1 = randint(1, len(q32p) - 1)
                    r.hset(uid, 'q3', -ran1, {'q3t': q32pt[ran1]})
                elif side == 3:
                    ran1 = randint(1, len(q33p) - 1)
                    r.hset(uid, 'q3', -ran1, {'q3t': q33pt[ran1]})
                elif side == 4:
                    ran1 = randint(1, len(q34p) - 1)
                    r.hset(uid, 'q3', -ran1, {'q3t': q34pt[ran1]})

    q = r.hmget(uid, 'q1', 'q1t', 'q2', 'q2t', 'q3', 'q3t')
    if int(q[0]) == 0 and int(q[2]) == 0 and int(q[4]) == 0:
        msg += '\n\n\u2705 Всі завдання на сьогодні виконані.'
    elif int(q[0]) == 0 and not checkClan(uid, building='wall'):
        r.hset(uid, 'q2', 0, {'q2t': 0, 'q3': 0, 'q3t': 0})
        msg += '\n\n\u2705 Всі завдання на сьогодні виконані.'
    else:
        if int(q[0]) > 0:
            msg += f"\n\n{q1[int(q[0])]}\n\U0001F9C2 Нагорода - 1 сіль\n" \
                   f"\U0001F4CA Прогрес - {q1t[int(q[0])] - int(q[1])}/{q1t[int(q[0])]}"
        elif int(q[0]) < 0:
            msg += f"\n\n{q1p[-int(q[0])]}\n\U0001F9C2 Нагорода - 2 солі\n" \
                   f"\U0001F4CA Прогрес - {q1pt[-int(q[0])] - int(q[1])}/{q1pt[-int(q[0])]}"
        if checkClan(uid, building='wall'):
            if int(q[2]) > 0:
                msg += f"\n\n{q2[int(q[2])]}\n\U0001F9C2 Нагорода - 1 сіль\n" \
                       f"\U0001F4CA Прогрес - {q2t[int(q[2])] - int(q[3])}/{q2t[int(q[2])]}"
            elif int(q[2]) < 0:
                msg += f"\n\n{q2p[-int(q[2])]}\n\U0001F9C2 Нагорода - 2 солі\n" \
                       f"\U0001F4CA Прогрес - {q2pt[-int(q[2])] - int(q[3])}/{q2pt[-int(q[2])]}"

            side = int(r.hget('c' + r.hget(uid, 'clan').decode(), 'side'))
            if int(q[4]) > 0:
                if side == 1:
                    msg += f"\n\n{q31[int(q[4])]}\n\U0001F9C2 Нагорода - 1 сіль\n" \
                           f"\U0001F4CA Прогрес - {q31t[int(q[4])] - int(q[5])}/{q31t[int(q[4])]}"
                elif side == 2:
                    msg += f"\n\n{q32[int(q[4])]}\n\U0001F9C2 Нагорода - 1 сіль\n" \
                           f"\U0001F4CA Прогрес - {q32t[int(q[4])] - int(q[5])}/{q32t[int(q[4])]}"
                elif side == 3:
                    msg += f"\n\n{q33[int(q[4])]}\n\U0001F9C2 Нагорода - 1 сіль\n" \
                           f"\U0001F4CA Прогрес - {q33t[int(q[4])] - int(q[5])}/{q33t[int(q[4])]}"
                elif side == 4:
                    msg += f"\n\n{q34[int(q[4])]}\n\U0001F9C2 Нагорода - 1 сіль\n" \
                           f"\U0001F4CA Прогрес - {q34t[int(q[4])] - int(q[5])}/{q34t[int(q[4])]}"

            elif int(q[4]) < 0:
                if side == 1:
                    msg += f"\n\n{q31p[-int(q[4])]}\n\U0001F9C2 Нагорода - 2 солі\n" \
                           f"\U0001F4CA Прогрес - {q31pt[-int(q[4])] - int(q[5])}/{q31pt[-int(q[4])]}"
                elif side == 2:
                    msg += f"\n\n{q32p[-int(q[4])]}\n\U0001F9C2 Нагорода - 2 солі\n" \
                           f"\U0001F4CA Прогрес - {q32pt[-int(q[4])] - int(q[5])}/{q32pt[-int(q[4])]}"
                elif side == 3:
                    msg += f"\n\n{q33p[-int(q[4])]}\n\U0001F9C2 Нагорода - 2 солі\n" \
                           f"\U0001F4CA Прогрес - {q33pt[-int(q[4])] - int(q[5])}/{q33pt[-int(q[4])]}"
                elif side == 4:
                    msg += f"\n\n{q34p[-int(q[4])]}\n\U0001F9C2 Нагорода - 2 солі\n" \
                           f"\U0001F4CA Прогрес - {q34pt[-int(q[4])] - int(q[5])}/{q34pt[-int(q[4])]}"

            if int(r.hget('c' + r.hget(uid, 'clan').decode(), 'war')) == 1:
                if int(q[0]) > 0 or int(q[2]) > 0 or int(q[4]) > 0:
                    if int(r.hget('c' + r.hget(uid, 'clan').decode(), 'buff_4')) == 11:
                        msg += '\n\n\U0001fa99 +3 за кожен виконаний квест'
                    else:
                        msg += '\n\n\U0001fa99 +1 за кожен виконаний квест'

                elif int(q[0]) < 0 or int(q[2]) < 0 or int(q[4]) < 0:
                    if int(r.hget('c' + r.hget(uid, 'clan').decode(), 'buff_5')) > 0:
                        msg += '\n\n\U0001fa99 +2 за кожен виконаний квест'
                    else:
                        msg += '\n\n\U0001fa99 +1 за кожен виконаний квест'

    return msg


def quest(uid, number, unit, side=0):
    try:
        if side > 0:
            if int(r.hget('c' + r.hget(uid, 'clan').decode(), 'side')) != side:
                raise Exception
        q, qt = f'q{number}', f'q{number}t'
        if int(r.hget(uid, 'qt')) == datetime.now().day and int(r.hget(uid, qt)) > 0 and int(r.hget(uid, q)) == unit:
            r.hincrby(uid, qt, -1)
            if int(r.hget(uid, qt)) <= 0:

                if int(r.hget(uid, q)) > 0:
                    r.hincrby(uid, 'salt', 1)
                    if checkClan(uid) and int(r.hget('c' + r.hget(uid, 'clan').decode(), 'buff_4')) == 11:
                        q_points(uid, 3)
                    else:
                        q_points(uid, 1)

                elif int(r.hget(uid, q)) < 0:
                    r.hincrby(uid, 'salt', 2)
                    if checkClan(uid) and int(r.hget('c' + r.hget(uid, 'clan').decode(), 'buff_5')) > 0:
                        q_points(uid, 2)
                    else:
                        q_points(uid, 1)

                r.hset(uid, q, 0)
    except:
        pass
