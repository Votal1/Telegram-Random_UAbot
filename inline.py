from random import randint, choice, uniform, randrange, sample
from config import r
from variables import names, icons
from parameters import injure, schizophrenia, trance


def prepare_to_fight(uid, fn, q):
    if r.hexists(uid, 'name') == 0:
        return '\U0001F3DA В тебе немає русака.\n\n@RandomUA_bot <- отримати русака'
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
                c = randint(0, len(icons) - 1)

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
                    '\n\n\u2744\uFE0F @RandomUA_bot <- отримати русака')

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
    country = ['\U0001F1FA\U0001F1E6 Україна', '\U0001F1F5\U0001F1F1 Польща',
               '\U0001F1F7\U0001F1FA Росія (ганьба)', '\U0001F1E8\U0001F1FF Чехія',
               '\U0001F1ED\U0001F1FA Угорщина', '\U0001F1E9\U0001F1EA Німеччина',
               '\U0001F1F3\U0001F1F4 Норвегія', '\U0001F1E9\U0001F1F0 Данія',
               '\U0001F1FA\U0001F1F8 США', '\U0001F1E8\U0001F1E6 Канада',
               '\U0001F1F2\U0001F1FD Мексика', '\U0001F1EB\U0001F1F7 Франція',
               '\U0001F1E7\U0001F1EA Бельгія', '\U0001F1F3\U0001F1F1 Нідерланди',
               '\U0001F1EF\U0001F1F5 Японія', '\U0001F1F9\U0001F1ED Таїланд',
               '\U0001F1F2\U0001F1E9 Молдова', '\U0001F1E8\U0001F1ED Швейцарія',
               '\U0001F1EE\U0001F1F9 Італія', '\U0001F1F3\U0001F1EC Нігерія',
               '\U0001F1F9\U0001F1F7 Туреччина', '\U0001F1EC\U0001F1EA Грузія',
               '\U0001F1EE\U0001F1EA Ірландія', '\U0001F1EA\U0001F1F8 Іспанія',
               '\U0001F1E8\U0001F1F3 Китай', '\U0001F1EE\U0001F1F3 Індія',
               '\U0001F1E7\U0001F1F7 Бразилія', '\U0001F1E6\U0001F1FA Австралія',
               '\U0001F1EC\U0001F1E7 Великобританія', '\U0001F1E6\U0001F1F7 Аргентина',
               '\U0001F1E6\U0001F1EA ОАЕ', '\U0001F1F3\U0001F1FF Нова Зеландія',
               '\U0001F1E6\U0001F1F9 Австрія', '\U0001F1EA\U0001F1EA Естонія',
               '\U0001F1F1\U0001F1FB Латвія', '\U0001F1F1\U0001F1F9 Литва',
               '\U0001F1EE\U0001F1F1 Ізраїль', '\U0001F1F8\U0001F1EA Швеція']
    ran = choice(country)
    return ran


def political():
    a1 = choice(['Економічно праві - ', 'Економічно ліві - '])
    a2 = choice(['Авторитаризм - ', 'Лібертаріанство - '])
    ran = a1 + str(randint(0, 100)) + '%\n' + a2 + str(randint(0, 100)) + '%'
    return ran


def question():
    q = (['\U0001f7e9 Так \U0001f7e9', '\U0001f7e5 Ні \U0001f7e5', '\U0001f7eb Не скажу \U0001f7eb',
          '\u2B1B Неможливо передбачити \u2B1B', '\U0001f7e6 100% \U0001f7e6',
          '\u2B1C Ніколи \u2B1C', '\U0001f7ea Скорше так, ніж ні \U0001f7ea',
          '\U0001f7e7 Скорше ні, ніж так \U0001f7e7', '\U0001f7e8 Слава Україні! \U0001f7e6'
          ])
    ran = '-----|' + choice(q) + '|-----'
    return ran


def love():
    i = randint(0, 100)
    s = choice(['\U0001f3f3\uFE0F\u200D\U0001f308', '\U0001f3f3\uFE0F\u200D\u26A7\uFE0F', '\U0001f49a',
                '\U0001f49c', '\u2764\uFE0F', '\U0001f49e', '\U0001f496', '\U0001f498', '\U0001f485'])
    ran = str(s) + ' ' + str(i) + '% ' + str(s)
    return ran


def zradoMoga():
    ran = choice(['\U0001F1FA\U0001F1E6 Перемога \U0001F1FA\U0001F1E6', '\u2721 Зрада \U0001F1F7\U0001F1FA',
                  '\u23F3 Боротьба триває', '\U0001F1FA\U0001F1E6 Перемога \U0001F1FA\U0001F1E6',
                  '\u2721 Зрада \U0001F1F7\U0001F1FA'])
    return ran


def penis():
    normal = f'Твій пісюн - {uniform(5.0, 16.0):.2f} см'
    small = f'Твій мініган - {uniform(0.0, 5.0):.2f} см'
    big = f'Твій моцний гилун - {uniform(16.0, 40):.2f} см'
    rare = choice(['Найбільший член в чаті', 'Найменший член в чаті'])
    vg = 'В тебе немає пісюна \U0001F31A'
    decor = choice(['\U0001F346 ', '\U0001F955 ', '\U0001F446 ',
                    '\U0001F44C ', '\U0001F336 ', '\u2642\uFE0F '])
    ran = decor + choice([normal, normal, normal, normal, small, small, big, big, rare, vg])
    return ran


def choose(q):
    s = choice(['\ud83c\udfb0 ', '\U0001F449 ', '\u270D\uFE0F ', '\U0001F39B ',
                '\U0001F4DF ', '\u2696\uFE0F ', '\U0001F4CA ', '\u21AA\uFE0F '])
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
    beer1 = '\U0001F37A ' + choice(['Львівське різдвяне', 'Bud', 'Львівське 1715', 'Carlsberg', 'Kronenbourg Blanc',
                                    'Staropramen', 'Чернігівське', 'Оболонь', 'Stella Artois', 'Tuborg',
                                    'Corona Extra', 'Krušovice', 'Старий Мельник', 'Velkopopovicky Kozel', 'Heineken',
                                    'Faxe', 'Опілля Корифей', 'Опілля Княже', 'Закарпатське', 'Арсенал', 'Kalusher',
                                    'Kaluskie Exportove', 'Правда', 'Балтика', 'Zeman', 'Проскурівське', 'Zibert',
                                    'Тетерів', 'Вишневий Тетерів'])
    not_beer = choice(['\U0001F6AB Сьогодні не пити', '\U0001F37B Сходити в паб', '\U0001F95B Випити молока',
                       '\U0001F4AF Бахнути горілочки', '\U0001F377 Випити холодного вина',
                       '\U0001F492 Піти на пивзавод',
                       '\u2620\uFE0F Годі бухати, заїбав, здохнеш так скоро к хуям собачим'])
    ran = choice([beer1, beer1, beer1, beer1, not_beer])
    return ran


def generator(q):
    error = 'Неправильний запит\n[x] - число від 0 до x\n[x] [y] - число від x до y' \
            '\n[x] [y] [n<=10] - n випадкових чисел від x до y'
    try:
        numbers = q.split()
        if len(numbers) == 0:
            ran = '\U0001F3B2 Випадкове число від 1 до 100' + '\n\n' + str(randrange(1, 101))
            return ran
        elif len(numbers) == 1:
            number = int(q) + 1
            ran = '\U0001F3B2 Випадкове число від 1 до ' + str(q) + '\n\n' + str(randrange(1, number))
            return ran
        elif len(numbers) == 2:
            first = int(numbers[0])
            second = int(numbers[1]) + 1
            if first < second - 1:
                ran = '\U0001F3B3 Випадкове число від ' + str(first) + ' до ' + str(second - 1) \
                      + '\n\n' + str(randrange(first, second))
                return ran
            else:
                return error
        elif len(numbers) == 3:
            first = int(numbers[0])
            second = int(numbers[1]) + 1
            third = int(numbers[2])
            if first < second - 1 and third <= 10:
                ran = '\U0001F3B0 Випадкові числа від ' + str(first) + ' до ' + str(second - 1) + '\n\n'
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
    emoji = ['\U0001F5FF', '\u267F\uFE0F', '\U0001f978', '\U0001F468\u200D\U0001F3A4', '\U0001F469\u200D\U0001F3A4',
             '\U0001f977', '\U0001F9D9\u200D\u2640\uFE0F', '\U0001F9D9\u200D\u2642\uFE0F', '\U0001F99E',
             '\U0001F9DC\u200D\u2642\uFE0F', '\U0001F9DA\u200D\u2640\uFE0F', '\U0001fab5', '\u26C4\uFE0F',
             '\u2708\uFE0F', '\U0001F6F0', '\U0001F681', '\U0001F6F8', '\u26A7\uFE0F']
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
               'Трактор Deutz-Fahr 6165', 'Трактор Claas Xerion 5000', 'Буксирована артилерійська система 2Б16 Нона-К']
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


def donate_to_zsu():
    emoji = choice(['\U0001F4B3', '\U0001F4B8', '\U0001F4B5', '\U0001F4B6', '\U0001F4B0'])
    mode = randint(1, 5)
    if mode == 1:
        if randint(1, 2) == 1:
            money = 100
        else:
            money = randint(2, 10) * 100
    else:
        money = randint(20, 100)
    money_end = money % 10
    if money_end == 1:
        end = 'гривню.'
    elif 1 < money_end < 5:
        end = 'гривні.'
    else:
        end = 'гривень.'
    ran = f'{emoji} Я задоначу на ЗСУ {money} {end}'
    return ran
