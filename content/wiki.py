from config import r
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def wiki_text(data):
    msg = ''
    markup = InlineKeyboardMarkup()
    if data == 'wiki_menu':
        markup.add(InlineKeyboardButton(text='\U0001F5E1 Бої', callback_data='wiki_duel'),
                   InlineKeyboardButton(text='\U0001F4C8 Розвиток', callback_data='wiki_grow_feed'),
                   InlineKeyboardButton(text='\U0001F9F3 Інвентар', callback_data='wiki_weapons_0'))
        markup.add(InlineKeyboardButton(text='\U0001F530 Клан', callback_data='wiki_clan'),
                   InlineKeyboardButton(text='\U0001F4DC Паспорт', callback_data='wiki_passport'))
        msg = '\U0001F1FA\U0001F1E6 @Random_UAbot - бот, який перенесе тебе в альтернативну реальність, у якій ти ' \
              'потрапляєш на Донбас і ловиш русаків.\nЇх можна розвивати, відправляти в бої проти інших ' \
              'русаків, об`єднувати в клани, а також - вбивати.\nТут можна знайти майже всю інформацію щодо гри.'
    elif data.startswith('wiki_duel'):
        markup.add(InlineKeyboardButton(text='\U0001F523 Шанси', callback_data='wiki_chances'),
                   InlineKeyboardButton(text='\U0001F4B0 Рейди', callback_data='wiki_raid'))
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
    elif data.startswith('wiki_chances'):
        markup.add(InlineKeyboardButton(text='\u2694\uFE0F Бої', callback_data='wiki_duel'),
                   InlineKeyboardButton(text='\U0001F4B0 Рейди', callback_data='wiki_raid'))
        msg = '\U0001F523 Шанси\n\nДуелі:\n' \
              'Шанс = сила * (1 + 0.1 * інтелект) * (1 + 0.0001 * бойовий дух)\n\n' \
              'У масових і міжчатових битвах, рейдах та охороні формула та сама, тільки додається ще 25% шансу за ' \
              'наявність зброї, захисту, допомоги та шапки.\n\n' \
              'Також на всі режими діють ці показники (після битви показник зменшиться на 1):\n' \
              '\U0001fa78 Поранення - втричі зменшує силу та вдвічі - бойовий дух.\n' \
              '\U0001F464 Шизофренія - втричі зменшує інтелект та вдвічі - бойовий дух.\n' \
              '\U0001F44A Бойовий транс - збільшує силу на 20% та бойовий дух - на 80%. Кількість трансу не може ' \
              'бути більшою, ніж кількість інтелекту.'
    elif data.startswith('wiki_raid'):
        markup.add(InlineKeyboardButton(text='\u2694\uFE0F Бої', callback_data='wiki_duel'),
                   InlineKeyboardButton(text='\U0001F523 Шанси', callback_data='wiki_chances'))
        msg = '\U0001F4B0 Рейди\n\nМожна проводити, починаючи з будь-якого рівня, але зарейдити можуть тільки, якщо ' \
              'ваш рівень, як мінімум, угруповання і склад, заповнений на 10%.\nЯкщо рейд проти клану - 70% шанс ' \
              'вкрасти ресурси, 20% - гроші, 10% - рускій дух.\n\nРейдові локації та нагороди:\n' \
              'Відділення монобанку - гроші, якщо в групі є 2 хакери\n' \
              'Магазин алкоголю - горілка, здоров`я, бойовий дух\n' \
              'АТБ, Сільпо - квас / цукор / кавун / годування, 50% - гроші\n' \
              'Епіцентр - ресурси\n' \
              'Макіївський роднічок - рускій дух\n\n' \
              'Перехоплення гумконвою - рейдовий режим, який можуть активувати тільки танкісти. Сила - ' \
              '2000000, оновлюється раз в день. Нагорода - по 1 пакунку за кожні 20000 сили команди. ' \
              'За повне розграбування додається 5 пакунків.\n' \
              'Ставок швайнокарасів - можна активувати, якщо у всієї команди будуть швайнокарасі.\n' \
              'Синагога - можна активувати, перебуваючи у кланівій війні та якщо у всієї команди будуть ярмулки.' \
              '\n\nЗа будь-який рейд є 5% шанс випадіння \U0001F916 секретного коду.'

    elif data.startswith('wiki_clan'):
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
    elif data.startswith('wiki_com'):
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
    elif data.startswith('wiki_coa'):
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
    elif data.startswith('wiki_aso'):
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
    elif data.startswith('wiki_org'):
        markup.add(InlineKeyboardButton(text='\U0001f7e5 Комуна', callback_data='wiki_com'),
                   InlineKeyboardButton(text='\U0001f7e6 Коаліція', callback_data='wiki_coa'))
        markup.add(InlineKeyboardButton(text='\U0001f7e9 Асоціація', callback_data='wiki_aso'),
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

    elif data.startswith('wiki_grow_feed'):
        markup.add(InlineKeyboardButton(text='\U0001F9C2 Сіль', callback_data='wiki_grow_mine'),
                   InlineKeyboardButton(text='\U0001F919 Класи', callback_data='wiki_grow_class'))
        msg = '\U0001F4C8 Розвиток\n\nУ русака є дві основні характеристики - \U0001F4AA сила та \U0001F9E0 інтелект.' \
              '\n\n\U0001F372 Годуючи, можна збільшити силу на 1-30 та інтелект на 1 (шанс 20%). В магазині можна ' \
              'купити утеплену будку, яка збільшуватиме силу на 15 до 2000 сили. Якщо в русака від 3000 сили, то вона' \
              ' може зменшитись з шансом 20%, а якщо більше 4000 - 40%. Також є 20% шанс шо русак захворіє і нічо не ' \
              'зміниться.\nЗ шансом 30% годування збільшить \U0001F54A бойовий дух на 1000, а з шансом 5% - до ' \
              'максимуму(10000).\nМаксимальна кількість інтелекту - 20.'
    elif data.startswith('wiki_grow_mine'):
        markup.add(InlineKeyboardButton(text='\U0001F372 Розвиток', callback_data='wiki_grow_feed'),
                   InlineKeyboardButton(text='\U0001F919 Класи', callback_data='wiki_grow_class'))
        msg = '\u2692 Соляні шахти (/mine)- місце, де можна заробити гроші (3-8) або інтелект (шанс 10%), ' \
              'відпрацювавши зміну. ' \
              'Повністю прокачавши майстерність (/skills) можна заробляти на 2 гривні більше, збільшити шанс ' \
              'отримати інтелект до 20% та зразу отримати 2 інтелекту. Якщо інтелект максимальний - може бути ' \
              'додатково видано 20 гривень. В суботу і неділю зарплата вдвічі більша. Також 20% шанс, що русак ' \
              'втече і нап`ється. 25% шанс забрати з собою одну сіль.\n\n' \
              '\U0001F9C2 Також сіль можна отримати виконуючи щоденні квести (/quest). Витрачати її можна в ' \
              'спеціальному магазині на підвищення сили або інші товари.'
    elif data.startswith('wiki_grow_class'):
        markup.add(InlineKeyboardButton(text='\U0001F372 Розвиток', callback_data='wiki_grow_feed'),
                   InlineKeyboardButton(text='\U0001F9C2 Сіль', callback_data='wiki_grow_mine'))
        msg = 'Розвинувши інтелект до певного рівня, можна вибрати клас (/class). Вплив класів на розвиток:\n' \
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

    elif data.startswith('wiki_weapons_0'):
        markup.add(InlineKeyboardButton(text='\U0001fa96 Класове спорядження', callback_data='wiki_weapons_class'))
        markup.add(InlineKeyboardButton(text='\U0001F5E1 Зброя', callback_data='wiki_weapons_1'),
                   InlineKeyboardButton(text='\U0001F6E1 Захист', callback_data='wiki_weapons_2'))
        markup.add(InlineKeyboardButton(text='\U0001F9EA Допомога', callback_data='wiki_weapons_3'),
                   InlineKeyboardButton(text='\U0001F3A9 Шапка', callback_data='wiki_weapons_4'))
        msg = '\U0001F9F3 Інвентар (/i) вміщує спорядження чотирьох типів - Зброя, Захист, Допомога та Шапка. ' \
              'Зазвичай зброя використовується в дуелях при атаці, захист в дуелях, коли кидаєш бій, ' \
              'а допомога і шапка - в певних випадках.\n\n' \
              '\U0001F510 В інвентарі можна викинути непотрібне спорядження, для того, щоб купити або отримати нове ' \
              'з успішних рейдів, оскільки в багатьох випадках воно не заміняється автоматично.'

    elif data.startswith('wiki_weapons_class'):
        markup.add(InlineKeyboardButton(text='\U0001F9F3 Інвентар', callback_data='wiki_weapons_0'))
        markup.add(InlineKeyboardButton(text='\U0001F5E1 Зброя', callback_data='wiki_weapons_1'),
                   InlineKeyboardButton(text='\U0001F6E1 Захист', callback_data='wiki_weapons_2'))
        markup.add(InlineKeyboardButton(text='\U0001F9EA Допомога', callback_data='wiki_weapons_3'),
                   InlineKeyboardButton(text='\U0001F3A9 Шапка', callback_data='wiki_weapons_4'))
        msg = '\U0001F9F3 Список класового спорядження та додаткові ефекти від їхніх покращених версій ' \
              '(отримуються тоді, коли міцність класового спорядження досягає десятикратного значення)\n\n' \
              '\U0001F919 Травмат [Зброя, міцність=5] - зменшує силу ворога на бій на 50%.\n' \
              '\u2B06\uFE0F Револьвер - також зменшує інтелект та бойовий дух ворога на бій на 50%.\n' \
              '\U0001F9F0 Діамантове кайло [Зброя, міцність=25] - збільшує силу, інтелект і бойовий дух ' \
              'на 20%.\n' \
              '\u2B06\uFE0F Незеритове кайло - 66% шанс не зменшити міцність в дуелях.\n' \
              '\U0001F52E Колода з кіоску [Зброя, міцність=3] - міняє твої характеристики з ворогом на бій.\n' \
              '\u2B06\uFE0F Колода Таро - передає 5 своєї шизофренії ворогу.\n' \
              '\U0001F5FF Сокира Перуна [Зброя, міцність=1] - при перемозі забирає весь бойовий дух ворога, ' \
              'при поразці ворог забирає твій.\n' \
              '\u2B06\uFE0F Рунічна сокира Перуна - при поразці ворог отримує 5 поранень або шизофренії.\n' \
              '\U0001fa96 АК-47 [Зброя, міцність=30] - після перемоги активує ефект горілки.\n' \
              '\u2B06\uFE0F АКМ - +25% сили в міжчатових битвах.\n' \
              '\U0001F46E Гумова палиця [Зброя, міцність=∞] - постійна зброя. В дуелі ігнорує бойовий дух двох ' \
              'сторін. Якщо є поліцейський щит - ігнорує лише бойовий дух ворога.\n' \
              '\U0001F46E Поліцейський щит [Захист, міцність=10] - зменшує силу ворога на 20% як і в захисті, ' \
              'так і в атаці.\n' \
              '\u2B06\uFE0F Важкий поліцейський щит - ігнорує РПГ та міни.\n' \
              '\U0001F921 Прапор новоросії [Зброя, міцність=8] - додаткова перемога за перемогу в дуелі.\n' \
              '\u2B06\uFE0F Прапор СРСР - +2 бойового трансу за перемогу в дуелі.\n' \
              '\U0001F4DF Експлойт [Зброя, міцність=2] - шанс активувати здібність хакера - 99%.\n' \
              '\u2B06\uFE0F Rootkit - Black Hat може отримати до 10 гривень.\n' \
              '\u26D1 Медична пилка [Зброя, міцність=8] - якщо у ворога нема поранень - завдає 1, якщо ' \
              'більше 4 - лікує 10 і забирає 10 здоров`я.\n' \
              '\u2B06\uFE0F Ампутатор - зменшує міцність захисту ворога на 3 або лікує до 15 поранень.\n' \
              '\U0001F6AC Скляна пляшка [Зброя, міцність=10] - зменшує інтелект ворогу на 10.\n' \
              '\u2B06\uFE0F Кастет - завдає ворогу 1 поранення і шизофренію.\n' \
              '\U0001F695 Дизель [Допомога, міцність=5] - збільшує власну силу в битвах, міжчатових битвах ' \
              'або рейдах на 25%.\n' \
              '\u2B06\uFE0F Ракетне паливо - збільшує силу групи на 15% при розграбуванні гумконвоїв ' \
              '(стакається).\n\U0001F396 Палаш [Зброя, міцність=15] - +50% сили проти русаків без клану.\n' \
              '\u2B06\uFE0F Золотий палаш - додаткові +50% сили проти тих, хто не має погонів ' \
              'російських генералів.'
    elif data.startswith('wiki_weapons_1'):
        markup.add(InlineKeyboardButton(text='\U0001fa96 Класове спорядження', callback_data='wiki_weapons_class'))
        markup.add(InlineKeyboardButton(text='\U0001F9F3 Інвентар', callback_data='wiki_weapons_0'),
                   InlineKeyboardButton(text='\U0001F6E1 Захист', callback_data='wiki_weapons_2'))
        markup.add(InlineKeyboardButton(text='\U0001F9EA Допомога', callback_data='wiki_weapons_3'),
                   InlineKeyboardButton(text='\U0001F3A9 Шапка', callback_data='wiki_weapons_4'))
        msg = '\U0001F5E1 Список зброї\n\n' \
              '\u26AA Колючий дрин [міцність=1] - перед боєм онуляє ворогу бойовий дух, якщо його значення ' \
              'від 300 до 1000, зменшує на 1000, якщо від 1000 до 2500 і зменшує на 20/30/40%, якщо бойовий ' \
              'дух більше 2500). Можна купити в магазині.\n' \
              '\u26AA Бита [міцність=3] - те саме, що і колючий дрин, але зі збільшеною міцністю. Доступний для ' \
              'покупки в магазині Скінхеду чи Білому вождю.\n' \
              '\U0001f535 БпЛА [міцність=1] - за кожен рівень майстерності (/skills) збільшує силу в масовій битві ' \
              'на 50% та збільшує шанс не втратити зброю на 18%. Можна купити в мандрівного торговця або в Лізі.\n' \
              '\U0001f7e3 Батіг [міцність=3] - збільшує силу в рейдах на 25%, або на 75%, якщо нема жінки. ' \
              'Доступно для покупки в Асоціації.\n' \
              '\U0001f7e1 РПГ-7 - [міцність=1] - віднімає ворогу бойовий дух, здоров`я і все спорядження, завдає 300 ' \
              'поранень. Можна знайти в пакунках або купити в Ордені.'
    elif data.startswith('wiki_weapons_2'):
        markup.add(InlineKeyboardButton(text='\U0001fa96 Класове спорядження', callback_data='wiki_weapons_class'))
        markup.add(InlineKeyboardButton(text='\U0001F5E1 Зброя', callback_data='wiki_weapons_1'),
                   InlineKeyboardButton(text='\U0001F9F3 Інвентар', callback_data='wiki_weapons_0'))
        markup.add(InlineKeyboardButton(text='\U0001F9EA Допомога', callback_data='wiki_weapons_3'),
                   InlineKeyboardButton(text='\U0001F3A9 Шапка', callback_data='wiki_weapons_4'))
        msg = '\U0001F6E1 Список захисного спорядження\n\n' \
              '\u26AA Колючий щит [міцність=1] - перед боєм онуляє атакуючому ворогу бойовий дух, якщо його значення ' \
              'від 300 до 1000, зменшує на 1000, якщо від 1000 до 2500 і зменшує на 20/30/40%, якщо бойовий ' \
              'дух більше 2500). Можна купити в магазині.\n' \
              '\u26AA Уламок бронетехніки [міцність=7] - збільшує силу на бій на 30%. Після зношення отримаєте ' \
              '4 гривні. Можна знайти в пакунку або купити в мандрівного торговця.\n' \
              '\U0001f535 Міни [міцність=3] - з шансом 33% завдає ворогу 5 поранень і зменшує міцність зброї на 5. ' \
              'Можливість використати міни при захисті клану. Бронежилет захищає від мін. ' \
              'Доступні для покупки в торговця та в Коаліції.\n' \
              '\U0001f7e1 Бронежилет вагнерівця [міцність=50] - зменшує силу ворога на бій на 75% та захищає від' \
              ' РПГ-7. Можна знайти в пакунках або купити в Ордені.'
    elif data.startswith('wiki_weapons_3'):
        markup.add(InlineKeyboardButton(text='\U0001fa96 Класове спорядження', callback_data='wiki_weapons_class'))
        markup.add(InlineKeyboardButton(text='\U0001F5E1 Зброя', callback_data='wiki_weapons_1'),
                   InlineKeyboardButton(text='\U0001F6E1 Захист', callback_data='wiki_weapons_2'))
        markup.add(InlineKeyboardButton(text='\U0001F9F3 Інвентар', callback_data='wiki_weapons_0'),
                   InlineKeyboardButton(text='\U0001F3A9 Шапка', callback_data='wiki_weapons_4'))
        msg = '\U0001F9EA Список допоміжного спорядження\n\n' \
              '\u26AA Аптечка [міцність=5] - збільшує здоров`я на 5 при купівлі і на 10 в дуелі. Якщо слот допомоги' \
              ' зайнятий - додає 50 здоров`я. Можна купити в магазині.\n' \
              '\u26AA Сокира [міцність=3] - дає можливість добути 1-10 деревини, поки не побудований клан. ' \
              'Можна купити в Банді.\n' \
              '\u26AA Кайло [міцність=3] - дає можливість добути 1-5 каміння, поки не побудований клан. ' \
              'Можна купити в Банді.\n' \
              '\u26AA Хліб справжній [міцність=1] - додає \U0001F54A +10000 при годуванні. ' \
              'Якщо допоміжне спорядження вже є, додає \U0001F54A +3000. Можна купити в Гільдії.\n' \
              '\U0001f535 Цукор [міцність=2] - збільшує силу за годування на 15 (до 3000) або' \
              ' зменшує шанс зменшення сили на 15%. Додає 5 бойового трансу. Можна купити в мандрівного торговця, ' \
              'отримати в рейдах, купити в Корпорації.\n' \
              '\U0001f535 Квас [міцність=5] - русак не втече зі зміни. Додає 5 бойового трансу за роботу в шахті.' \
              ' Можна купити в мандрівного торговця, отримати в рейдах, купити в Корпорації.\n' \
              '\U0001f7e3 Мухомор королівський [міцність=1] - якщо у ворога більший інтелект, додає +1 інтелекту ' \
              '(не діє проти фокусників). На бій зменшує свою силу на 50%.\n' \
              '\U0001f7e1 Швайнокарась [міцність=3, максимальна_міцність=3] - може виконувати бажання русаків ' \
              '(відпочивати, нажертись, напитись).'
    elif data.startswith('wiki_weapons_4'):
        markup.add(InlineKeyboardButton(text='\U0001fa96 Класове спорядження', callback_data='wiki_weapons_class'))
        markup.add(InlineKeyboardButton(text='\U0001F5E1 Зброя', callback_data='wiki_weapons_1'),
                   InlineKeyboardButton(text='\U0001F6E1 Захист', callback_data='wiki_weapons_2'))
        markup.add(InlineKeyboardButton(text='\U0001F9EA Допомога', callback_data='wiki_weapons_3'),
                   InlineKeyboardButton(text='\U0001F9F3 Інвентар', callback_data='wiki_weapons_0'))
        msg = '\U0001F3A9 Список шапок\n\n' \
              '\U0001f535 Вушанка [міцність=20] - збільшує ефективність бойового трансу на 2% за кожен рівень' \
              ' алкоголізму (/skills). Можна купити в мандрівного торговця або в Союзі.\n' \
              '\U0001f535 Кавун базований [міцність=∞] - збільшує силу за годування і гроші за зміну на 5. ' \
              'Зникає тільки тоді, коли сила за годування зменшиться. Можна купити в мандрівного торговця, ' \
              'отримати в рейдах, купити в Корпорації.\n' \
              '\U0001f535 Кавуняча крінжа [міцність=1] - збільшує силу за годування і гроші за зміну на 5. ' \
              'Можна отримати в Ордені, якщо зникає кавун.\n' \
              '\U0001f7e3 Шапочка з фольги [міцність=10] - захищає від втрати бойового духу при жертвоприношеннях. ' \
              'При купівлі в торговця чи в Ордені русак отримує 30 шизофренії, а при отриманні з пакунків - 10.\n' \
              '\U0001f7e3 Тактичний шолом [міцність=40] - збільшує силу в дуелях і міжчатових битвах на 31%. ' \
              'Можна купити в Коаліції.\n' \
              '\U0001f7e1 Ярмулка [міцність=7, імунітет_до_РПГ] - надає доступ до кошерних квестів (вдвічі більша ' \
              'нагорода, але і більша складність їх виконання). 100% шанс отримати сіль в соляних шахтах. ' \
              'Міцність зменшується при взятті квестів. Можна знайти в пакунку або купити в магазині за погон.'

    elif data.startswith('wiki_passport'):
        markup.add(InlineKeyboardButton(text='\U0001F4E6 Пакунки', callback_data='wiki_pack'),
                   InlineKeyboardButton(text='\u2B50 Досягнення', callback_data='wiki_achieve'))
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
              'Рейтинг = сила + інтелект * 10 + перемоги + трофеї * 10 + вбивства * 14 + немовлята * 88\n\n' \
              '\u26CF Промокоди - невелика нагорода, яку можна отримати один раз, активувавши командою ' \
              '/promo_code <промокод>. Промокод, який зміцнює спорядження:\n' \
              + r.hget('promo_code', 'strength_promo_code').decode()
    elif data.startswith('wiki_pack'):
        markup.add(InlineKeyboardButton(text='\U0001F4DC Паспорт', callback_data='wiki_passport'),
                   InlineKeyboardButton(text='\u2B50 Досягнення', callback_data='wiki_achieve'))
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
    elif data.startswith('wiki_achieve'):
        markup.add(InlineKeyboardButton(text='\U0001F4DC Паспорт', callback_data='wiki_passport'),
                   InlineKeyboardButton(text='\U0001F4E6 Пакунки', callback_data='wiki_pack'))
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
