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
            msg += '\n\U0001F349 Закупити всьому клану Кавун базований [Шапка, міцність=1] - збільшує зарплату за ' \
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
                   InlineKeyboardButton(text='\U0001F69B', callback_data='clan_shop_3'))

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
                   InlineKeyboardButton(text='\U0001F451', callback_data='clan_shop_2'))
    return msg, markup


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
        msg = 'Команди для гри в русаків\n\n/donbass - взяти русака\n/rusak - характеристики\n@Random_UAbot - ' \
              'почати битву\n@Random_UAbot & - три додаткові режими\n/feed - погодувати русака\n' \
              '/shop - магазин\n/donate_shop - безтолкові штуки\n/pack - Донбаський пакунок\n/woman - провідати' \
              ' жінку\n/sacrifice - вбити свого русака\n/class - вибрати русаку клас\n/achieve - досягнення\n' \
              '/skills - вміння\n/i - інвентар\n/swap - змінити бойового русака (якщо є підвал)\n/battle - почати ' \
              'масову битву\n/war - почати міжчатову битву\n/quit - вийти з міжчатової битви\n/crash - ' \
              'зупинити міжчатову битву\n/promo_code [код]- активувати бонус\n\nКоманди, доступні тільки ' \
              'в <a href="https://t.me/+cClR7rA-sZAyY2Uy">@soledar1</a>:\n/mine - заробити гривні\n/merchant - ' \
              'продає топову снарягу\n/clan - доступні клани'
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
              '/leave - покинути клан\n/kick [user id] - вигнати з клану\n/work - добувати ресурси\n' \
              '/invest [>0] - перекинути гроші\n/fascist - вибрати фашиста дня\n/clan_settings - налаштування, ' \
              'зарплата за роботу, список учасників\n/upgrade - покращити рівень клану\n/build - розвинути ' \
              'інфраструктуру\n/clan_shop - магазин (доступний на 3 рівні)\n/raid - грабувати інші клани\n' \
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


def wiki_text(data):
    msg = ''
    markup = InlineKeyboardMarkup()
    if data == 'wiki_menu':
        markup.add(InlineKeyboardButton(text='\U0001F5E1 Бої', callback_data='wiki_duel'),
                   InlineKeyboardButton(text='\U0001F4C8 Розвиток', callback_data='wiki_grow_feed'))
        markup.add(InlineKeyboardButton(text='\U0001F530 Клан', callback_data='wiki_clan'),
                   InlineKeyboardButton(text='\U0001F4DC Паспорт', callback_data='wiki_passport'))
        msg = '\U0001F1FA\U0001F1E6 @Random_UAbot - бот, який перенесе тебе в альтернативну реальність, у якій ти ' \
              'потрапляєш на Донбас і ловиш русаків.\nЇх можна розвивати, відправляти в бої проти інших ' \
              'русаків, об`єднувати в клани, а також - вбивати.\nТут можна знайти майже всю інформацію щодо гри.'
    if data.startswith('wiki_duel'):
        markup.add(InlineKeyboardButton(text='\U0001F523', callback_data='wiki_chances'),
                   InlineKeyboardButton(text='\U0001F4B0', callback_data='wiki_raid'))
        msg = '\u2694\uFE0F Існує 4 типи боїв:\n\n\U0001F5E1 Дуелі - проводяться за викликом бота в інлайн режимі. ' \
              'Нагорода - бойовий дух та гроші. Якщо ворожий русак вдвічі слабший - грошової нагороди не буде, рівн' \
              'ий по силі - 0-3 гривні, вдвічі сильніший - 1-3 гривні. В дуелях використовується більшість спорядже' \
              'ння. Також можливий пошук ворога по силі, особисте запрошення та турнірний режим, в якому нема нагор' \
              'од та не діють деякі вміння. Щоб запустити ці режими, при виклику бота додайте &\n' \
              '\U0001fac0 Здоров`я - параметр, необхідний для дуелей. Якщо здоров`я більше 90 - сила збільшиться на' \
              ' 10%, якщо 0 - потрібно лікування.\n\n' \
              '\U0001F30D Міжчатові битви (/war) - 5 русаків з одного чату проти 5 з іншого. Нагорода - 3 гривні та' \
              ' трофей. Якщо битись за Соледар - нагорода 3-10 гривень. Якщо битись кланом - 6 гривень.\n\n' \
              '\U0001F5FA Масові битви (/battle) - "батл-рояль" від 5 русаків. Нагорода - 5 гривень, якщо русаків 10' \
              ' - 10 гривень і трофей. Існують різні локації (більшість з них доступні в битві на 10 русаків) з спец' \
              'іальними нагородами та класові локації з нагородою для певного класу.\n\n' \
              '\U0001F4B0 Рейди (/raid) - 5 русаків в своєму клані збираються проводити рейд на інший клан або локац' \
              'ію. Можна проводити раз в годину.'
    if data.startswith('wiki_chances'):
        markup.add(InlineKeyboardButton(text='\u2694\uFE0F', callback_data='wiki_duel'),
                   InlineKeyboardButton(text='\U0001F4B0', callback_data='wiki_raid'))
        msg = '\U0001F523 Шанси\n\nДуелі:\n' \
              'Шанс = сила * (1 + 0.1 * інтелект) * (1 + 0.0001 * бойовий дух)\n\n' \
              'У масових і міжчатових битвах, рейдах та охороні формула та сама, тільки додається ще 25% шансу за ' \
              'наявність зброї, захисту, допомоги та шапки.\n\n' \
              'Також на всі режими діють ці показники (після битви показник зменшиться на 1):\n' \
              '\U0001fa78 Поранення - втричі зменшує силу та вдвічі - бойовий дух.\n' \
              '\U0001F464 Шизофренія - втричі зменшує інтелект та вдвічі - бойовий дух.\n' \
              '\U0001F44A Бойовий транс - збільшує силу на 20% та бойовий дух - на 80%. Кількість трансу не може ' \
              'бути більшою, ніж кількість інтелекту.'
    if data.startswith('wiki_raid'):
        markup.add(InlineKeyboardButton(text='\u2694\uFE0F', callback_data='wiki_duel'),
                   InlineKeyboardButton(text='\U0001F523', callback_data='wiki_chances'))
        msg = '\U0001F4B0 Рейди\n\nМожна проводити, починаючи з будь-якого рівня, але зарейдити можуть тільки, якщо ' \
              'ваш рівень, як мінімум, угруповання і склад, заповнений на 10%.\nЯкщо рейд проти клану - 70% шанс ' \
              'вкрасти ресурси, 20% - гроші, 10% - рускій дух.\n\nРейдові локації та нагороди:\n' \
              'Відділення монобанку - гроші, якщо в групі є 2 хакери\n' \
              'Магазин алкоголю - горілка, здоров`я, бойовий дух\n' \
              'АТБ, Сільпо - квас / цукор / кавун / годування, 50% - гроші\n' \
              'Епіцентр - ресурси\n\n' \
              'Перехоплення гумконвою - секретний рейдовий режим, який можуть активувати тільки танкісти. Сила - ' \
              '2000000, оновлюється раз в день. Нагорода - по 1 пакунку за кожні 20000 сили команди. Нагорода за ' \
              'повне розграбування - 20 пакунків.\n\n' \
              'За будь-який рейд є 5% шанс випадіння \U0001F916 секретного коду.'

    if data.startswith('wiki_clan'):
        markup.add(InlineKeyboardButton(text='\U0001f7e5 Комуна', callback_data='wiki_com'),
                   InlineKeyboardButton(text='\U0001f7e6 Коаліція', callback_data='wiki_coa'))
        markup.add(InlineKeyboardButton(text='\U0001f7e9 Асоціація', callback_data='wiki_aso'),
                   InlineKeyboardButton(text='\U0001f7e8 Організація', callback_data='wiki_org'))
        msg = '\U0001F530 Клан - об`єднання русаків, яке з кожним рівнем додає більше бонусів.\n' \
              'Всі команди для керування кланом є у /commands.\n' \
              'Творець клану стає лідером. Заступники можуть бути призначеі лідером і мати майже такі самі можливості' \
              ' як лідер.\n\nРівні кланів:\n\n\U0001f6d6 Банда - можливість обирати фашиста дня, добувати та зберігат' \
              'и деревину і каміння.\n' \
              '\U0001F3E0 Клан - \U0001F4B5 +6 гривень та \U0001F47E +1 рускій дух за перемоги в міжчатових боях, ' \
              'якщо серед учасників всі з клану.\n' \
              '\U0001F3E1 Гільдія - \U0001F4B5 +34% за роботу на шахтах Соледару.\n' \
              '\U0001F3D8 Угруповання - \U0001F4B5 шанс подвоїти грошову нагороду за перемогу в дуелях.\n\n' \
              'Далі доведеться вибрати один з чотирьох рівнів, які є відсиланням на політичний компас.'
    if data.startswith('wiki_com'):
        markup.add(InlineKeyboardButton(text='\U0001F530', callback_data='wiki_clan'),
                   InlineKeyboardButton(text='\U0001f7e6 Коаліція', callback_data='wiki_coa'))
        markup.add(InlineKeyboardButton(text='\U0001f7e9 Асоціація', callback_data='wiki_aso'),
                   InlineKeyboardButton(text='\U0001f7e8 Організація', callback_data='wiki_org'))
        msg = '\U0001f7e5 Комуна\n' \
              'Ресурси в клані добуваються в максимальному обсязі. Ціна на совєцкій пайок зменшена з 10 до 4 гривень.' \
              '\n\nІнфраструктура:\n' \
              'Тракторний завод - можливість купувати уламки бронетехніки та зміцнювати ними броню до 50.\n' \
              'Пивний ларьок - роботяги добувають вдвічі білье ресурсів.\n' \
              'Падік - здібність гопніка буде дійсна, якщо на рахунку до 200 гривень.\n' \
              'Тюрма - сила мусора при охороні збільшиться на 100%.\n\n' \
              '\U0001f7e5 Союз\n' \
              'Можливість закупити всьому клану дрини і щити за 200 деревини і 100 каміння. Можливість закупити ' \
              'горілку тим, хто відпрацював зміну.' \
              '\n\nІнфраструктура:\n' \
              'Воєнкомат - можливість купити АК-47 та вушанку або безкоштовно отримати за охорону.\n' \
              'Гулаг - за покидання клану сила двох русаків зменшиться на 20%. За роботу чи охорону буде шанс ' \
              'отримати додаткове годування по 1% за кожну тисячу деревини, каменю, тканини і цегли.'
    if data.startswith('wiki_coa'):
        markup.add(InlineKeyboardButton(text='\U0001f7e5 Комуна', callback_data='wiki_com'),
                   InlineKeyboardButton(text='\U0001F530', callback_data='wiki_clan'))
        markup.add(InlineKeyboardButton(text='\U0001f7e9 Асоціація', callback_data='wiki_aso'),
                   InlineKeyboardButton(text='\U0001f7e8 Організація', callback_data='wiki_org'))
        msg = '\U0001f7e6 Коаліція\n' \
              'За купівлю бойового трансу за рускій дух - додатково збільшиться бойовий дух на 50%. +2 руского духу' \
              ' за перемогу у міжчатових битвах.' \
              '\n\nІнфраструктура:\n' \
              'Штаб тероборони - можливість купувати тактичний шолом та міни. Зменшує ефективність ворожих рейдів на ' \
              '33%.\n' \
              'Березова роща - якщо язичник застосує сокиру Перуна проти іншого язичника - обидва отримають ' \
              'по 10000 бойового духу\n' \
              'Генеральська дача - присутність генерала в міжчатовій битві додатково принесе 1 рускій дух за ' \
              'перемогу.\n' \
              'Казарма - +20% сили гарматному м`ясу в міжчатових битвах.\n\n' \
              '\U0001f7e6 Орден\n' \
              'Можливість купляти РПГ-7 та Бронежилет вагнерівця за кланові гроші і рускій рух для лідера та' \
              ' заступників.' \
              '\n\nІнфраструктура:\n' \
              'Ферма - годування русака лікує до 30 поранень. Можливість зберегти кавун ще на 1 годування.\n' \
              'Ядерний бункер - шизофренія не впливатиме негативно на міжчатові битви, рейди та охорону, а навпаки - ' \
              'додаватиме 5 інтелекту. Можливість купляти шапочки з фольги.'
    if data.startswith('wiki_aso'):
        markup.add(InlineKeyboardButton(text='\U0001f7e5 Комуна', callback_data='wiki_com'),
                   InlineKeyboardButton(text='\U0001f7e6 Коаліція', callback_data='wiki_coa'))
        markup.add(InlineKeyboardButton(text='\U0001F530', callback_data='wiki_clan'),
                   InlineKeyboardButton(text='\U0001f7e8 Організація', callback_data='wiki_org'))
        msg = '\U0001f7e9 Асоціація\n' \
              'Зменшує силу локацій в рейдах на 50%. При отриманні грошової нагороди - ' \
              'ви отримаєте 20% гривень на власний рахунок.' \
              '\n\nІнфраструктура:\n' \
              'Dungeon - можливість купувати батіг (+25% сили в рейдах, або +75%, якщо нема жінки).\n' \
              'Бійцівський клуб - втричі більший шанс кинути прогином хачам.\n' \
              'Циганський табір - 20% шанс фокусникам вкрасти грошову нагороду ворога в дуелях.\n' \
              'Радіовежа - малорос в міжчатовій битві надсилає 3 шизофренії випадковому ворогу.\n\n' \
              '\U0001f7e9 Ліга\n' \
              'Якщо під час рейду виявлено, що ціль має більше ресурсів - рейдери вкрадуть вдвічі більше. ' \
              'Можливість грабувати гумконвой без танкістів. В такому випадку, шанс активувати цей режим - 20%. ' \
              'Можливість купувати БпЛА.' \
              '\n\nІнфраструктура:\n' \
              'Готель - максимальна кількість учасників збільшується до 10. Можливість вступати в клан в будь-який ' \
              'момент (не треба чекати тиждень після вступу в попередній клан, а 3 години).\n' \
              'Офіс Червоного Хреста - можливість лікувати весь клан, та проводити перерозподіл багатств - за 500 ' \
              'гривень з скарбниці по 100 гривень 5 найбіднішим учасникам.'
    if data.startswith('wiki_org'):
        markup.add(InlineKeyboardButton(text='\U0001f7e5 Комуна', callback_data='wiki_com'),
                   InlineKeyboardButton(text='\U0001f7e6 Коаліція', callback_data='wiki_coa'))
        markup.add(InlineKeyboardButton(text='\U0001f7e9Асоціація', callback_data='wiki_aso'),
                   InlineKeyboardButton(text='\U0001F530', callback_data='wiki_clan'))
        msg = '\U0001f7e8 Організація\n' \
              'Скасовуються податки. +6 гривень в кланову скарбницю за перемогу в міжчатовій битві.' \
              '\n\nІнфраструктура:\n' \
              'Біолабораторія - можливість купувати королівські мухомори (тим, в кого русак має до 20 інтелекту).\n' \
              'Аптека - патологоанатом з аптечкою отримуватиме по 10 гривень за воскрешання русаків.\n' \
              'АЗС - можливість купити дизель в клановому магазині для таксистів.\n' \
              'Дата-центр - здібність хакера надсилатиме стільки ж грошей в скарбницю клану.\n\n' \
              '\U0001f7e8 Корпорація\n' \
              'За інвестиції від 1000 гривень інвестор отримає по пакунку за кожні 20 гривень. +1% до сили охорони ' \
              'за кожну тисячу гривень у скарбниці (максимум 200%).' \
              '\n\nІнфраструктура:\n' \
              'Торговий центр - можливість купити Цукор і квас для себе та Кавун базований для всього клану.\n' \
              'Невільничий ринок - можливість купувати російських немовлят. Нові русаки з`являтимуться з 500+ сили.'

    if data.startswith('wiki_grow_feed'):
        markup.add(InlineKeyboardButton(text='\u2692', callback_data='wiki_grow_mine'),
                   InlineKeyboardButton(text='\U0001F349', callback_data='wiki_grow_support'),
                   InlineKeyboardButton(text='\U0001F919', callback_data='wiki_grow_class'))
        msg = '\U0001F4C8 Розвиток\n\nУ русака є дві основні характеристики - \U0001F4AA сила та \U0001F9E0 інтелект.' \
              '\n\n\U0001F372 Годуючи, можна збільшити силу на 1-30 та інтелект на 1 (шанс 20%). В магазині можна ' \
              'купити утеплену будку, яка збільшуватиме силу на 15 до 2000 сили. Якщо в русака від 3000 сили, то вона' \
              ' може зменшитись з шансом 20%, а якщо більше 4000 - 40%. Також є 20% шанс шо русак захворіє і нічо не ' \
              'зміниться.\nЗ шансом 30% годування збільшить \U0001F54A бойовий дух на 1000, а з шансом 5% - до ' \
              'максимуму(10000).\nМаксимальна кількість інтелекту - 20.'
    if data.startswith('wiki_grow_mine'):
        markup.add(InlineKeyboardButton(text='\U0001F372', callback_data='wiki_grow_feed'),
                   InlineKeyboardButton(text='\U0001F349', callback_data='wiki_grow_support'),
                   InlineKeyboardButton(text='\U0001F919', callback_data='wiki_grow_class'))
        msg = '\u2692 Соляні шахти - місце, де можна заробити гроші (3-8) або інтелект (шанс 10%), відпрацювавши ' \
              'зміну. Повністю прокачавши майстерність (/skills) можна заробляти на 2 гривні більше, збільшити шанс ' \
              'отримати інтелект до 20% та зразу отримати 2 інтелекту. Якщо інтелект максимальний - може бути ' \
              'додатково видано 20 гривень. В суботу і неділю зарплата вдвічі більша. Також 20% шанс, що русак ' \
              'втече і нап`ється. 25% шанс забрати з собою одну сіль.'
    if data.startswith('wiki_grow_support'):
        markup.add(InlineKeyboardButton(text='\U0001F372', callback_data='wiki_grow_feed'),
                   InlineKeyboardButton(text='\u26CF', callback_data='wiki_grow_mine'),
                   InlineKeyboardButton(text='\U0001F919', callback_data='wiki_grow_class'))
        msg = 'Спорядження, яке впливає на розвиток:\n\U0001F344 Мухомор королівський - в дуелі збільшує інтелект на ' \
              '1, якщо русак б`ється проти розумнішого. Можна купити до 3 штук в мандрівного торговця.\n' \
              '\U0001F35E Хліб справжній - збільшує шанс отримати 10000 бойового духу за годування до 100%.\n' \
              '\U0001F9EA Цукор - збільшує силу за годування на 15 (до 3000) або зменшує шанс зменшення сили на ' \
              '15%.\n\U0001F349 Кавун базований - збільшує силу за годування і гроші за зміну на 5. Зникає тільки ' \
              'тоді, коли сила за годування зменшиться.'
    if data.startswith('wiki_grow_class'):
        markup.add(InlineKeyboardButton(text='\U0001F372', callback_data='wiki_grow_feed'),
                   InlineKeyboardButton(text='\u2692', callback_data='wiki_grow_mine'),
                   InlineKeyboardButton(text='\U0001F349', callback_data='wiki_grow_support'))
        msg = 'Розвинувши інтелект до певного рівня, можна вибрати клас. Вплив класів на розвиток:\n' \
              '\U0001F919\U0001F919\U0001F919 Гроза Кавказу кожен день може збільшувати силу на 10 та один раз - ' \
              'на 200.\n\U0001F9F0 Роботяга не хворіє, але вдвічі більше п`є.\n' \
              '\U0001F9F0\U0001F9F0 - Почесний алкаш швидше качає вміння.\n' \
              '\U0001F9F0\U0001F9F0\U0001F9F0 - П`яний майстер - при певній умові може годуватись два рази.\n' \
              '\U0001F52E Фокусник та Злий геній отримують додатковий інтелект при виборі класу.\n' \
              '\U0001F921 Малорос може анулювати інтелект за мухомори всім в чаті.\n' \
              '\U0001F4DF\U0001F4DF Кіберзлочинець точно може успішно відпрацювати зміну, та купувати необмежену ' \
              'кількість мухоморів в торговця.\n' \
              '\U0001F6AC\U0001F6AC Зек вдвічі збільшує бонус сили від утепленої будки.\n' \
              '\U0001F396 Офіцер може отримати інтелект в міжчатових битвах.'

    if data.startswith('wiki_passport'):
        markup.add(InlineKeyboardButton(text='\U0001F4E6', callback_data='wiki_pack'),
                   InlineKeyboardButton(text='\u2B50', callback_data='wiki_achieve'))
        msg = '\U0001F4DC Паспорт\n\n' \
              '\U0001F3C6 Перемоги можна отримати за... перемоги в дуелях, масових та міжчатових битвах.\n' \
              '\U0001F3C5 Трофеї можна отримати за перемоги в масових та міжчатових битвах.\n' \
              '\u2620\uFE0F Русаків можна вбивати, продавши жінку. Також можна зарізати свого ' \
              'або знайти в пакунку чужого.\n' \
              '\U0001F476 Немовлят можна отримувати провідуючи жінку, за фашиста дня і за досягнення.\n' \
              '\u2622 Найпростіший спосіб отримати горілку - купити в магазині.\n' \
              '\U0001F4E6 Донбаські пакунки можна придбати командою /pack або купити в \n/donate_shop\n' \
              '\u26CF Вміння можна качати в /skills\n' \
              '\u2B50 /achieve - подивитись досягнення (ачівки - фрази з українських пісень).\n\n' \
              '\U0001F947 Формула розрахунку рейтингу:\n' \
              'Рейтинг = сила + інтелект * 10 + перемоги + трофеї * 10 + вбивства * 14 + немовлята * 88'
    if data.startswith('wiki_pack'):
        markup.add(InlineKeyboardButton(text='\U0001F4DC', callback_data='wiki_passport'),
                   InlineKeyboardButton(text='\u2B50', callback_data='wiki_achieve'))
        msg = 'Предмети в пакунках і шанси випадіння:\n\n' \
              '\u26AA Нічого - 20% (або радіотехніка)\n' \
              '\u26AA Спорядження класу - 18%\n' \
              '\u26AA Дрин і щит - 15%\n' \
              '\u26AA 4 гривні - 12%\n' \
              '\u26AA Уламок - 10%\n' \
              '\U0001f535 50 гривень - 7%\n' \
              '\U0001f535 20 горілки - 6%\n' \
              '\U0001f535 Мертвий русак - 5%\n' \
              '\U0001f7e3 Мухомор королівський - 3%\n' \
              '\U0001f7e3 Шапочка з фольги - 2%\n' \
              '\U0001f7e3 300 грн, годування і ачівка - 1%\n' \
              '\U0001f7e1 РПГ-7 - 0.225%\n' \
              '\U0001f7e1 Бронежилет - 0.225%\n' \
              '\U0001f7e1 Швайнокарась - 0.225%\n' \
              '\U0001f7e1 Ярмулка - 0.225%\n' \
              '\U0001f7e1 Погон російського генерала - 0.1%'
    if data.startswith('wiki_achieve'):
        markup.add(InlineKeyboardButton(text='\U0001F4DC', callback_data='wiki_passport'),
                   InlineKeyboardButton(text='\U0001F4E6', callback_data='wiki_pack'))
        msg = 'Досягнення і як їх отримати:\n\n' \
              '\u26AA Хто не з нами, той нехай йде собі до сраки - попрацювати в Соледарі за допомогою секретної ' \
              'команди\n' \
              '\u26AA І москаля нема, немає москаля - влаштувати одне вбивство\n' \
              '\u26AA Моя фамілія Залупа - купити трофейний паспорт\n' \
              '\u26AA Наливай, куме, горілки стаканчик - випити 150 горілки \n' \
              '\u26AA Бігає по полю весело кабанчик - погодувати русака 15 разів\n' \
              '\U0001f535 Геніальний розум, великий чоловік - набрати 20 інтелекту\n' \
              '\U0001f535 Гордо і достойно ти живеш свій вік - набрати 2000 сили\n' \
              '\U0001f535 Зараз розберемося, кому належить вулиця - увійти в масову битву і нажати /achieve\n' \
              '\U0001f535 Ах лента за лентою набої подавай - Купити спорядження свого класу в торговця\n' \
              '\U0001f7e3 Ніколи не плач на радість орді - набрати 10000 бойового духу і виконати команду /achieve\n' \
              '\U0001f7e3 Ворога знищено, як був наказ - набрати 1000 перемог\n' \
              '\U0001f7e3 Я заводжу хімікат, розпочинаю атентат - вибити з пакунків\n' \
              '\U0001f7e3 А до берега тихо хвилі несуть поранені душі живих кораблів - бути в стані бойового трансу ' \
              'з пораненням і шизофренією\n' \
              '\U0001f534 Я мав купу бабок, я мав купу справ - інвестувати в клан мінімум 500 гривень за раз\n' \
              '\U0001f534 Танцюй і пий, поки живий - отримати як мінімум чверть бонусу від моргу в міжчатовій битві\n' \
              '\U0001f534 Кривавий пастор - влаштувати 15 вбивств і з`їсти 15 російських немовлят'

    if not data == 'wiki_menu':
        markup.add(InlineKeyboardButton(text='\u21A9\uFE0F', callback_data='wiki_menu'))
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
