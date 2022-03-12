from random import randint, choice, uniform, randrange, sample
from config import r
from variables import names, icons
from parameters import injure, schizophrenia, trance


def prepare_to_fight(uid, fn, q):
    if r.hexists(uid, 'name') == 0:
        return 'В тебе немає русака.\n\n@Random_UAbot <- отримати русака'
    elif int(r.hget(uid, 'hp')) > 0:
        stats = r.hmget(uid, 'name', 'class', 'strength', 'intellect', 'spirit')
        r.hset(uid, 'firstname', fn)
        name = int(stats[0])
        c = int(stats[1])
        s = int(stats[2])
        s1 = s
        i = int(stats[3])
        bd = int(stats[4])

        if int(r.hget(uid, 'injure')) > 0:
            s, bd = injure(uid, s, bd, False)
        if int(r.hget(uid, 'sch')) > 0:
            i, bd = schizophrenia(uid, i, bd, False)
        if int(r.hget(uid, 'buff')) > 0:
            s, bd = trance(uid, s, bd, False)

        if c == 3:
            s = randint(10, 1000)
            i = randint(1, 10)
            bd = randint(0, 10000)
        elif c == 13 or c == 23:
            s = randint(200, 2000)
            i = randint(10, 20)
            bd = randint(0, 10000)
            if c == 23:
                c = randint(0, len(icons))

        query = ''
        try:
            q = q.split()
            if q[0].startswith('tr'):
                query = '\n\n\U0001F530 Турнірний режим \U0001F530'
                try:
                    if q[1].startswith('@'):
                        query += '\n\U0001F4E3 Викликаю на бій ' + q[1] + '!'
                except:
                    pass
            elif q[0].startswith('pr'):
                try:
                    if q[1].startswith('@'):
                        query += '\n\U0001F4E3 Викликаю на бій ' + q[1] + '!'
                except:
                    pass
            elif int(q[1]) > 0:
                s2 = s1 - int(q[1])
                if s2 < 1:
                    s2 = 1
                query = '\n\n\U0001F4E2 Розшукується суперник з силою від ' + \
                        str(s2) + ' до ' + str(s1 + int(q[1])) + '.'
        except:
            pass

        stats = str("\n\n\U0001F3F7 " + names[name] + ' ' + icons[c] +
                    '\n\U0001F4AA ' + str(s) +
                    ' \U0001F9E0 ' + str(i) +
                    ' \U0001F54A ' + str(bd) +
                    '\n\n@Random_UAbot <- отримати русака')

        return ' ' + fn + ' починає битву русаків!' + query + stats
    else:
        return '\U0001fac0 Русак лежить весь в крові.\nВін не може битись поки не поїсть, або не полікується.'


def pastLife():
    life = ['Звичайний совковий роботяга', 'Видатний письменник', 'Лауреат Нобелівської премії',
            'Кріпак з Черкащини', 'Англійський аристократ', 'Хитрий жид', 'Запорізький козак',
            'Житель Зеленого Клину', 'Кубанський козак', 'А ніким і не був, це твоє перше життя',
            'Мер Харкова', 'Польська курва', 'Раб з Африки', 'Boss of gym', 'Dungeon master',
            'Динозавр', 'Штурмбанфюрер', 'Донощик', 'Грязний циган', 'Депутат', 'Кримський хан',
            'Московський холоп', 'НКВСник', 'Партизан з УПА', "Слов`янський ремісник", 'Дівчина чорноброва',
            'Карпатський гуцул', 'Монгольський кінний лучник', 'Інквізитор', 'Викладач політеху',
            'Дитя Донбасу', 'Руський боярин', 'Собака', 'Кіт', 'Козак-характерник', 'Німецький єврей',
            'Робот з Boston Dynamics', 'Канадський українець', "Дощовий черв`як звичайний", 'Космонавт',
            'Пірат', 'Французька дворянка', 'Повія з Санкт-Петербурга', 'Американський агент',
            'Розбійник', 'Серійний вбивця', 'Безхатько', 'Сольовий торчок']
    ran = choice(life)
    return ran


def earnings():
    country = ['\ud83c\uddfa\ud83c\udde6 Україна', '\ud83c\uddf5\ud83c\uddf1 Польща',
               '\ud83c\uddf7\ud83c\uddfa Росія (ганьба)', '\ud83c\udde8\ud83c\uddff Чехія',
               '\ud83c\udded\ud83c\uddfa Угорщина', '\ud83c\udde9\ud83c\uddea Німеччина',
               '\ud83c\uddf3\ud83c\uddf4 Норвегія', '\ud83c\udde9\ud83c\uddf0 Данія',
               '\ud83c\uddfa\ud83c\uddf8 США', '\ud83c\udde8\ud83c\udde6 Канада',
               '\ud83c\uddf2\ud83c\uddfd Мексика', '\ud83c\uddeb\ud83c\uddf7 Франція',
               '\ud83c\udde7\ud83c\uddea Бельгія', '\ud83c\uddf3\ud83c\uddf1 Нідерланди',
               '\ud83c\uddef\ud83c\uddf5 Японія', '\ud83c\uddf9\ud83c\udded Таїланд',
               '\ud83c\uddf2\ud83c\udde9 Молдова', '\ud83c\udde8\ud83c\udded Швейцарія',
               '\ud83c\uddee\ud83c\uddf9 Італія', '\ud83c\uddf3\ud83c\uddec Нігерія',
               '\ud83c\uddf9\ud83c\uddf7 Туреччина', '\ud83c\uddec\ud83c\uddea Грузія',
               '\ud83c\uddee\ud83c\uddea Ірландія', '\ud83c\uddea\ud83c\uddf8 Іспанія',
               '\ud83c\udde8\ud83c\uddf3 Китай', '\ud83c\uddee\ud83c\uddf3 Індія',
               '\ud83c\udde7\ud83c\uddf7 Бразилія', '\ud83c\udde6\ud83c\uddfa Австралія',
               '\ud83c\uddec\ud83c\udde7 Великобританія', '\ud83c\udde6\ud83c\uddf7 Аргентина',
               '\ud83c\udde6\ud83c\uddea ОАЕ', '\ud83c\uddf3\ud83c\uddff Нова Зеландія']
    ran = choice(country)
    return ran


def political():
    a1 = choice(['Економічно праві - ', 'Економічно ліві - '])
    a2 = choice(['Авторитаризм - ', 'Лібертаріанство - '])
    ran = a1 + str(randint(0, 100)) + '%\n' + a2 + str(randint(0, 100)) + '%'
    return ran


def question():
    q = (['\ud83d\udfe9 Так \ud83d\udfe9', '\ud83d\udfe5 Ні \ud83d\udfe5', '\ud83d\udfeb Не скажу \ud83d\udfeb',
          '\u2b1b\ufe0f Неможливо передбачити \u2b1b\ufe0f', '\ud83d\udfe6 100% \ud83d\udfe6',
          '\u2b1c\ufe0f Ніколи \u2b1c\ufe0f', '\ud83d\udfea Скорше так, ніж ні \ud83d\udfea',
          '\ud83d\udfe7 Скорше ні, ніж так \ud83d\udfe7', '\ud83d\udfe8 Слава Україні! \ud83d\udfe6'
          ])
    ran = '-----|' + choice(q) + '|-----'
    return ran


def love():
    i = randint(0, 100)
    s = choice(['\ud83c\udff3\u200d\ud83c\udf08', '\ud83d\udc9a', '\ud83d\udc9c', '\u2764\ufe0f',
                '\ud83d\udc9e', '\ud83d\udc96', '\ud83d\udc98', '\ud83d\udc85'])
    ran = str(s) + ' ' + str(i) + '% ' + str(s)
    return ran


def zradoMoga():
    ran = choice(['\ud83c\uddfa\ud83c\udde6 Перемога \ud83c\uddfa\ud83c\udde6', '\u2721 Зрада \ud83c\uddf7\ud83c\uddfa',
                  '\u23f3 Боротьба триває', '\ud83c\uddfa\ud83c\udde6 Перемога \ud83c\uddfa\ud83c\udde6',
                  '\u2721 Зрада \ud83c\uddf7\ud83c\uddfa'])
    return ran


def penis():
    normal = f'Твій пісюн - {uniform(5.0, 16.0):.2f} см'
    small = f'Твій мініган - {uniform(0.0, 5.0):.2f} см'
    big = f'Твій моцний гилун - {uniform(16.0, 40):.2f} см'
    rare = choice(['Найбільший член в чаті', 'Найменший член в чаті'])
    vg = 'В тебе немає пісюна \ud83c\udf1a'
    decor = choice(['\ud83c\udf46 ', '\ud83e\udd55 ', '\ud83d\udc46 ',
                    '\ud83d\udc4c ', '\ud83c\udf36 ', '\u2642\ufe0f '])
    ran = decor + choice([normal, normal, normal, normal, small, small, big, big, rare, vg])
    return ran


def choose(q):
    s = choice(['\ud83c\udfb0 ', '\ud83d\udc49 ', '\u270d ', '\ud83c\udf9b ',
                '\ud83d\udcdf ', '\u2696 ', '\ud83d\udcca ', '\u21aa\ufe0f '])
    q = q.replace(' чи ', '2a2b').replace(' або ', '2a2b').replace('?', '')
    q = q.replace(' ', '1a2b')
    q = q.replace('2a2b', ' ').split()
    end = []
    for i in q:
        i = i.replace('1a2b', ' ').strip()
        end.append(i)
    ran = s + choice(end)
    return ran


def beer():
    beer1 = '\ud83c\udf7a ' + choice(['Львівське різдвяне', 'Bud', 'Львівське 1715', 'Carlsberg', 'Kronenbourg Blanc',
                                      'Staropramen', 'Чернігівське', 'Оболонь', 'Stella Artois', 'Tuborg',
                                      'Corona Extra', 'Krušovice', 'Старий Мельник', 'Velkopopovicky Kozel', 'Heineken',
                                      'Faxe', 'Опілля Корифей', 'Опілля Княже', 'Закарпатське', 'Арсенал', 'Kalusher',
                                      'Kaluskie Exportove', 'Правда', 'Балтика', 'Zeman', 'Проскурівське', 'Zibert',
                                      'Тетерів', 'Вишневий Тетерів'])
    not_beer = choice(['\ud83d\udeab Сьогодні не пити', '\ud83c\udf7b Сходити в паб', '\ud83e\udd5b Випити молока',
                       '\ud83d\udcaf Бахнути горілочки', '\ud83c\udf77 Випити холодного вина',
                       '\ud83d\udc92 Піти на пивзавод', '\u2620 Годі бухати, заїбав, здохнеш так скоро к хуям собачим'])
    ran = choice([beer1, beer1, beer1, beer1, not_beer])
    return ran


def generator(q):
    error = 'Неправильний запит\n[x] - число від 0 до x\n[x] [y] - число від x до y' \
            '\n[x] [y] [n<=10] - n випадкових чисел від x до y'
    try:
        numbers = q.split()
        if len(numbers) == 0:
            ran = '\ud83c\udfb2 Випадкове число від 1 до 100' + '\n\n' + str(randrange(1, 101))
            return ran
        elif len(numbers) == 1:
            number = int(q) + 1
            ran = '\ud83c\udfb2 Випадкове число від 1 до ' + str(q) + '\n\n' + str(randrange(1, number))
            return ran
        elif len(numbers) == 2:
            first = int(numbers[0])
            second = int(numbers[1]) + 1
            if first < second - 1:
                ran = '\ud83c\udfb3 Випадкове число від ' + str(first) + ' до ' + str(second - 1) \
                      + '\n\n' + str(randrange(first, second))
                return ran
            else:
                return error
        elif len(numbers) == 3:
            first = int(numbers[0])
            second = int(numbers[1]) + 1
            third = int(numbers[2])
            if first < second - 1 and third <= 10:
                ran = '\ud83c\udfb0 Випадкові числа від ' + str(first) + ' до ' + str(second - 1) + '\n\n'
                for i in range(third):
                    a = randrange(first, second)
                    ran += str(a) + '\n'
                return ran
            else:
                return error
        else:
            return error
    except:
        return error


def race():
    races = ["Східний слов'янин", "Західний слов'янин", "Південний слов'янин", "Балтієць",
             'Кельт', 'Германець', 'Скандинав', 'Британець', 'Вірмен',
             'Циган', 'Італієць', 'Іспанець', 'Француз', 'Грек',
             'Албанець', 'Фіно-угорець', 'Мокша', 'Тюрк', 'Татар',
             'Кавказець', 'Індієць', 'Іранець', 'Монгол', 'Кореєць',
             'Японець', 'Китаєць', 'Сибіряк', 'Індонезієць', 'Семіт',
             'Негроїд', 'Австралоїд', 'Корінний американець']
    choice1 = ['Арієць', 'Українець', 'Єврей', 'Циган', 'Кельт', 'Германець', 'Негроїд',
               'Скандинав', 'Британець', 'Італієць', 'Іспанець', 'Француз', 'Грек']
    variant = choice([1, 2, 2, 3, 3, 3, 3, 4, 5])
    ran = ''

    if variant == 1:
        ran = '100% - ' + choice(choice1)
    elif variant > 1:
        try:
            n = 90
            percents = []
            for i in range(variant):
                if i == variant - 1:
                    percent = 100 - sum(percents)
                    percents.append(percent)
                else:
                    percent = randrange(1, n)
                    percents.append(percent)
                    n = n - percent
            percents.sort(reverse=True)
            random_values = sample(races, k=variant)
            for i in range(variant):
                ran = ran + str(percents[i]) + '% - ' + random_values[i] + '\n'
        except:
            ran = '100% - ' + choice(choice1)

    return ran


def gender():
    emoji = ['\ud83d\uddff', '\u267f\ufe0f', '\ud83e\udd78', '\ud83d\udc68\u200d\ud83c\udfa4', '\ud83e\udddc',
             '\ud83e\uddd1\u200d\ud83c\udfa4', '\ud83d\udc69\u200d\ud83c\udfa4', '\ud83e\udd77', '\ud83e\udd9e',
             '\ud83e\uddd9\u200d\u2640', '\ud83e\uddda', '\ud83e\udeb5', '\u26c4\ufe0f', '\u2708\ufe0f', '\ud83d\udef0',
             '\ud83d\ude81', '\ud83d\udef8', '\u26a7']
    genders = ['Протитанковий ракетний комплекс FGM-148 Javelin', 'ПТКР BGM-71 TOW', 'Самозарядний пістолет Форт-14',
               'Пістолет Desert Eagle', 'Пістолет-кулемет STEN', 'Автомат Калашникова модернізований', 'Кулемет M240',
               'Пістолетний унітарний патрон 9×19 мм Парабелум', 'Кулемет КМ-7,62', 'Самозарядна гвинтівка Gewehr 41',
               'Багатоцільовий вертольіт PZL W-3 Sokół', 'Багатоцільовий гелікоптер ВМ-4 «Джміль»', 'Кулемет MG-42',
               'Пістолет-кулемет Heckler & Koch MP5', 'Пістолет Walther P38', 'Болтова гвинтівка Vz.24/G24(t)',
               'Пістолет-кулемет MP-40', 'Гвинтівка Mauser 98k', 'Автомат Вулкан-М', 'ПТРК Скіф', 'Пістолет Mauser C96',
               '40-мм ручний протитанковий гранатомет РПГ-7', 'Автомат Ґаліль', 'Карабін мисливський Зброяр Z-10 ',
               'Снайперська гвинтівка Stealth Recon Scout', 'Автоматичний гранатомет УАГ-40', 'Гвинтівка FG-42',
               'Великокаліберна снайперська гвинтівка  Barrett M82', 'Багатоцільовий вертольіт NHI NH90',
               'Підствольний гранатомет ГП-25 «Костьор»', 'Атомний підводний човен з балістичними ракетами',
               'Ударний вертоліт Мі-24ПУ1', 'Протитанкова рушниця Panzerbüchse 35(p)', 'Вогнемет Flammenwerfer 35',
               'Переносна протитанкова безвідкатна гармата Panzerfaust', 'Реактивний піхотний вогнемет РПВ «Джміль»',
               'Переносний зенітно-ракетний комплекс FIM-92 Stinger', 'Автомат FN SCAR', 'Автоматична гвинтівка M4',
               'Розвідувально-ударний вертоліт Boeing–Sikorsky RAH-66 Comanche', 'Автоматична гвинтівка M16',
               'Проміжний патрон для сучасних автоматичних гвинтівок 5,56×45 мм', 'Пістолет-кулемет Thompson M1',
               'Основний бойовий танк БМ Оплот', 'Основний бойовий танк Т-84', 'Бронетранспортер БТР-7',
               'Авіадесантний бронетранспортер БТР-Д', 'Бронеавтомобіль KrAZ-MPV Shrek One',
               'Безпілотний літальний апарат Bayraktar TB2', 'Патрульний катер типу «Айленд»',
               'Береговий ракетний комплекс РК-360МЦ «Нептун»', '152-мм самохідна гармата-гаубиця vz.77 «Дана»',
               'Легкий тактичний позадорожній бронеавтомобіль HMMWV', 'Багатоцільовий гелікоптер МСБ-2',
               'Трактор NewHolland T7HD', 'Трактор CLAAS AXION 960 TT', 'Трактор Fendt 942 Vario ProfiPlus Gen6',
               'Трактор JohnDeere 6250R', 'Трактор Massey Ferguson5400', 'Трактор Case IH 125',
               'Трактор Deutz-Fahr 6165', 'Трактор Claas Xerion 5000']
    ran = choice(emoji) + ' Я по гендеру... \n\n' + choice(genders)
    return ran


def roll_push_ups():
    n = randint(1, 3)
    if n == 1:
        step = ' підхід.'
    else:
        step = ' підходи.'
    ran = str(randint(15, 50)) + ' віджимань за ' + str(n) + step
    return ran
