from config import r
from random import choice
from datetime import datetime


def quests(uid):
    q1 = ['', '\U0001F3C6 Виграти в 10 дуелях', '\u2622 Купити 5 горілки',
          '\U0001F3DF Взяти участь в 3 міжчатових битвах', '\u26CF Відпрацювати зміну на соляній шахті',
          '\u2620\uFE0F Подивитись втрати окупантів', '\u2694 Взяти участь в масовій битві']
    q1t = ['', 10, 5, 3, 1, 1, 1]

    if int(r.hget(uid, 'qt')) != datetime.now().day:
        r.hset(uid, 'qt', datetime.now().day)
        ran1 = choice(q1)

        while int(r.hget(uid, 'qt')) != datetime.now().day and ran1 == 4:
            ran1 = choice(q1)

        r.hset(uid, 'q1', ran1, {'q1t': q1t.index()})
