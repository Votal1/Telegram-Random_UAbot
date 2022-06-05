from random import randint, choice, choices
from datetime import datetime, timedelta
from os import environ
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputTextMessageContent, InlineQueryResultArticle
from aiogram.utils.executor import start_webhook

from config import r, TOKEN, bot, dp
from variables import names, icons, class_name, weapons, defenses, supports, heads, sudoers, \
    p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, premium, premium2, chm, default
from inline import prepare_to_fight, pastLife, earnings, political, love, \
    question, zradoMoga, penis, choose, beer, generator, race, gender, roll_push_ups
from parameters import spirit, vodka, intellect, hp, damage_support, damage_head, increase_trance
from buttons import goods, donate_goods, skill_set, battle_button, battle_button_2, battle_button_3, \
    battle_button_4, invent, unpack, create_clan, clan_set, invite, buy_tools
from fight import fight, war, great_war, start_raid, guard_power
from methods import get_rusak, feed_rusak, mine_salt, checkClan, checkLeader, com, wiki_text, c_shop, top, itop, ctop, \
    wood, stone, cloth, brick
from merchant import merchant_msg

from requests import get
from bs4 import BeautifulSoup

import logging
import sentry_sdk

sentry_sdk.init(environ.get('SENTRY'))
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['gruz200', 'orki', 'z', 'poter_net', 'fertilizer', 'ruskie_idut_nahuy'])
async def gruz200(message):
    try:
        url = 'https://minusrus.com/'
        page = get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        title = '\U0001F437\U0001F436 ' + soup.find('div', 'title').text + ' на ' \
                + soup.find('span', 'date__label').text
        os = soup.find('div', 'amount-details').find_all('span')
        t = soup.find_all('span', 'card__amount-total')
        msg = title + '\n\n\u2620\uFE0F Вбито: ' + os[1].text + '\n\U0001fa78 Поранено: ' + os[3].text + \
                      '\n\u26D3 Взято в полон: ' + os[5].text + '\n\U0001F690 ББМ: ' + t[1].text + \
                      '\n\U0001F69C Танки: ' + t[2].text + '\n\U0001F525 Артилерія: ' + t[3].text + \
                      '\n\u2708\uFE0F Літаки: ' + t[4].text + '\n\U0001F681 Гелікоптери: ' + t[5].text + \
                      '\n\U0001F6A2 Кораблі та катери: ' + t[6].text + '\n\U0001F921 Жириновський, Медведчук, Шарій'
        await message.reply(msg)
    except:
        await message.reply('minusrus.com', disable_web_page_preview=True)


@dp.message_handler(commands=['start'])
async def send_welcome(message):
    if message.chat.type == 'private':
        await message.reply('Почнемо.\n\nЗайди в який-небудь чат (наприклад цей), напиши @Random_UAbot, а далі думаю'
                            'все зрозумієш.\nДля деяких команд потрібно додати текст, бажано зі сенсом (логічно, так?'
                            ').\n\nЩоб взяти русака напиши команду \n/donbass\nДетальна інформація про русаків -'
                            '\nhttps://t.me/randomuanews/4.', disable_web_page_preview=True)


@dp.message_handler(commands=['help'])
async def get_help(message):
    await message.reply('Зайди в який-небудь чат (наприклад цей), напиши @Random_UAbot, а далі думаю все зрозумієш.\n'
                        'Для деяких команд потрібно додати текст, бажано зі сенсом (логічно, так?).\n\n'
                        'Щоб взяти русака напиши команду \n/donbass\n/commands - всі команди\n/wiki - вся інфа по грі\n'
                        '@randomuanews - новини', disable_web_page_preview=True)


@dp.message_handler(commands=['links'])
async def handle_links(message):
    await message.reply('<a href="https://t.me/+cClR7rA-sZAyY2Uy">@soledar1</a> - місце, де збираються люди з усіх '
                        'куточків України, щоб похизуватись своїми бойовими русаками!\n'
                        '@randomuanews - новини, патчноути, опитування\n\n'
                        '@borykva - осередок цебулізму\n'
                        '@ukrnastup - осередок сучасного українського націоналізму\n'
                        '@golovkaothuya - крінж і шітпост, рекомендую\n@digital_anon - подкасти\n'
                        '@archive_st - брендові стікери\n'
                        '<a href="https://t.me/vota_l">@vota_l</a> - завдяки ньому ти натиснув цю кнопку',
                        parse_mode='HTML', disable_web_page_preview=True)


@dp.message_handler(commands=['toggle_admin'])
async def toggle_admin(message):
    try:
        st = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if st.status == 'creator' or st.can_change_info is True:
            if r.hexists('f' + str(message.chat.id), 'admin') == 0:
                r.hset('f' + str(message.chat.id), 'admin', 0)
            if int(r.hget('f' + str(message.chat.id), 'admin')) == 0:
                r.hset('f' + str(message.chat.id), 'admin', 1)
                await message.reply('Адмінські команди УВІМКНЕНО')
            else:
                r.hset('f' + str(message.chat.id), 'admin', 0)
                await message.reply('Адмінські команди ВИМКНЕНО')
    except:
        pass


@dp.message_handler(commands=['toggle_captcha'])
async def toggle_admin(message):
    try:
        st = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if int(r.hget('f' + str(message.chat.id), 'admin')) == 1:
            if st.status == 'creator' or st.can_change_info is True:
                if r.hexists('f' + str(message.chat.id), 'captcha') == 0:
                    r.hset('f' + str(message.chat.id), 'captcha', 0)
                if int(r.hget('f' + str(message.chat.id), 'captcha')) == 0:
                    r.hset('f' + str(message.chat.id), 'captcha', 1)
                    await message.reply('Капча УВІМКНЕНА')
                else:
                    r.hset('f' + str(message.chat.id), 'captcha', 0)
                    await message.reply('Капча ВИМКНЕНА')
    except:
        pass


@dp.message_handler(commands=['ban', 'unban'])
async def ban(message):
    try:
        uid = message.reply_to_message.from_user.id
        st = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if int(r.hget('f' + str(message.chat.id), 'admin')) == 1:
            if st.status == 'creator' or st.can_restrict_members is True:
                msg = message.reply_to_message.from_user.first_name + ' вигнаний з чату'
                if message.text.startswith('/unban'):
                    await bot.unban_chat_member(message.chat.id, uid, only_if_banned=True)
                    await message.answer(message.reply_to_message.from_user.first_name + ' може повертатись в чат.')
                else:
                    try:
                        a = message.text.split(' ')
                        if a[1].endswith('m'):
                            await bot.kick_chat_member(message.chat.id, uid,
                                                       until_date=datetime.now() + timedelta(minutes=int(a[1][:-1])))
                            await message.answer(msg + ' на ' + a[1][:-1] + ' хвилин.')
                        elif a[1].endswith('h'):
                            await bot.kick_chat_member(message.chat.id, uid,
                                                       until_date=datetime.now() + timedelta(hours=int(a[1][:-1])))
                            await message.answer(msg + ' на ' + a[1][:-1] + ' годин.')
                        elif a[1].endswith('d'):
                            await bot.kick_chat_member(message.chat.id, uid,
                                                       until_date=datetime.now() + timedelta(days=int(a[1][:-1])))
                            await message.answer(msg + ' на ' + a[1][:-1] + ' днів.')
                        else:
                            raise Exception
                    except:
                        await bot.kick_chat_member(message.chat.id, uid)
                        await message.answer(msg + '.')
    except:
        pass


@dp.message_handler(commands=['mute', 'unmute'])
async def mute(message):
    try:
        uid = message.reply_to_message.from_user.id
        st = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if int(r.hget('f' + str(message.chat.id), 'admin')) == 1:
            if st.status == 'creator' or st.can_restrict_members is True:
                msg = message.reply_to_message.from_user.first_name
                if message.text.startswith('/unmute'):
                    await bot.restrict_chat_member(message.chat.id, uid,
                                                   can_send_messages=True, can_send_media_messages=True,
                                                   can_send_other_messages=True, can_add_web_page_previews=True)
                    await message.answer('З ' + message.reply_to_message.from_user.first_name + ' знято всі обмеження.')
                else:
                    try:
                        a = message.text.split(' ')
                        if a[1].endswith('m'):
                            await bot.restrict_chat_member(message.chat.id, uid,
                                                           until_date=datetime.now() + timedelta(
                                                               minutes=int(a[1][:-1])),
                                                           can_send_messages=False)
                            msg += ' посидить ' + a[1][:-1] + ' хвилин без права голосу.'
                            await message.answer(msg)
                        elif a[1].endswith('h'):
                            await bot.restrict_chat_member(message.chat.id, uid,
                                                           until_date=datetime.now() + timedelta(hours=int(a[1][:-1])),
                                                           can_send_messages=False)
                            msg += ' посидить ' + a[1][:-1] + ' годин без права голосу.'
                            await message.answer(msg)
                        elif a[1].endswith('d'):
                            await bot.restrict_chat_member(message.chat.id, uid,
                                                           until_date=datetime.now() + timedelta(days=int(a[1][:-1])),
                                                           can_send_messages=False)
                            msg += ' посидить ' + a[1][:-1] + ' днів без права голосу.'
                            await message.answer(msg)
                        elif a[1].endswith('f'):
                            await bot.restrict_chat_member(message.chat.id, uid,
                                                           can_send_messages=False)
                            msg += ' назавжди залишається без права голосу.'
                            await message.answer(msg)
                        else:
                            raise Exception
                    except:
                        await bot.restrict_chat_member(message.chat.id, uid,
                                                       until_date=datetime.now() + timedelta(hours=12),
                                                       can_send_messages=False)
                        msg += ' посидить 12 годин без права голосу.'
                        await message.answer(msg)
    except:
        pass


@dp.message_handler(commands=['moxir'])
async def moxir(message):
    try:
        uid = message.reply_to_message.from_user.id
        st = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if int(r.hget('f' + str(message.chat.id), 'admin')) == 1:
            if st.status == 'creator' or st.can_restrict_members is True:
                msg = 'У ' + message.reply_to_message.from_user.first_name + ' забрали стікери і медіа'
                try:
                    a = message.text.split(' ')
                    if a[1].endswith('m'):
                        await bot.restrict_chat_member(message.chat.id, uid,
                                                       until_date=datetime.now() + timedelta(minutes=int(a[1][:-1])),
                                                       can_send_messages=True, can_send_media_messages=False,
                                                       can_add_web_page_previews=False, can_send_other_messages=False)
                        await message.answer(msg + ' на ' + a[1][:-1] + ' хвилин.')
                    elif a[1].endswith('h'):
                        await bot.restrict_chat_member(message.chat.id, uid,
                                                       until_date=datetime.now() + timedelta(hours=int(a[1][:-1])),
                                                       can_send_messages=True, can_send_media_messages=False,
                                                       can_add_web_page_previews=False, can_send_other_messages=False)
                        await message.answer(msg + ' на ' + a[1][:-1] + ' годин.')
                    elif a[1].endswith('d'):
                        await bot.restrict_chat_member(message.chat.id, uid,
                                                       until_date=datetime.now() + timedelta(days=int(a[1][:-1])),
                                                       can_send_messages=True, can_send_media_messages=False,
                                                       can_add_web_page_previews=False, can_send_other_messages=False)
                        await message.answer(msg + ' на ' + a[1][:-1] + ' днів.')
                    else:
                        raise Exception
                except:
                    await bot.restrict_chat_member(message.chat.id, uid,
                                                   can_send_messages=True, can_send_media_messages=False,
                                                   can_send_other_messages=False, can_add_web_page_previews=False)
                    await message.answer(msg + '.')
    except:
        pass


@dp.message_handler(content_types=["new_chat_members"])
async def handler_new_member(message):
    try:
        if int(r.hget('f' + str(message.chat.id), 'captcha')) == 1:
            user_name = message.new_chat_members[0].first_name
            markup = InlineKeyboardMarkup()
            if choice([1, 2]) == 1:
                markup.add(InlineKeyboardButton(text='\U0001F35E', callback_data='captcha_true'),
                           InlineKeyboardButton(text='\U0001F353', callback_data='captcha_false'))
            else:
                markup.add(InlineKeyboardButton(text='\U0001F353', callback_data='captcha_false'),
                           InlineKeyboardButton(text='\U0001F35E', callback_data='captcha_true'))
            await bot.restrict_chat_member(message.chat.id, message.new_chat_members[0].id, can_send_messages=False)
            await message.reply(f'\u274E {user_name}, цей чат під охороною. Дай відповідь на одне питання.\n\n'
                                f'Що таке паляниця?', reply_markup=markup)
    except:
        pass


@dp.message_handler(commands=['donbass'])
async def donbass(message):
    markup = InlineKeyboardMarkup()
    await message.reply(text='\U0001F3DA Ти приходиш на Донбас - чудове місце для полювання на русаків',
                        reply_markup=markup.add(InlineKeyboardButton(text='Знайти русака', callback_data='getrusak')))


@dp.message_handler(commands=['rusak'])
async def my_rusak(message):
    mid = message.from_user.id
    try:
        if r.hexists(mid, 'name'):
            r_photo, cl, inj, ms = '', '', '', ''
            name = names[int(r.hget(mid, 'name'))]
            c = int(r.hget(mid, 'class'))
            if c != 0:
                cl = '\n' + icons[c] + ' Клас: ' + class_name[c]
            stats = r.hmget(mid, 'strength', 'intellect', 'spirit', 'injure', 'mushrooms', 'hp', 'sch', 'buff', 'photo')
            if int(stats[3]) > 0:
                inj = '\n\U0001fa78 Поранення: ' + stats[3].decode()
            if int(stats[6]) > 0:
                inj += '\n\U0001F464 Шизофренія: ' + stats[6].decode()
            if int(stats[7]) > 0:
                inj += '\n\U0001F44A Бойовий транс: ' + stats[7].decode()
            if int(stats[4]) > 0:
                ms = '\n\U0001F344 Мухомори: ' + stats[4].decode()
            photo_text = '\U0001F412 Твій русак:\n\n\U0001F3F7 Ім`я: ' + name + \
                         '\n\U0001F4AA Сила: ' + stats[0].decode() + '\n\U0001F9E0 Інтелект: ' + stats[1].decode() + \
                         '\n\U0001F54A Бойовий дух: ' + stats[2].decode() + '\n\U0001fac0 Здоров`я: ' + \
                         stats[5].decode() + cl + ms + inj
            await message.reply_photo(stats[8].decode(), caption=photo_text)
        else:
            await message.reply('\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на \n/donbass')
    except Exception as e:
        await bot.send_message(456514639, f'{e}\n{mid}')


@dp.message_handler(commands=['feed'])
async def feed(message):
    try:
        try:
            r.hset(message.from_user.id, 'username', message.from_user.username)
            if message.chat.type != 'private':
                r.sadd(message.chat.id, message.from_user.id)
                r.sadd(111, message.from_user.id)
            if message.chat.type == 'supergroup':
                r.hset('f' + str(message.chat.id), 'title', message.chat.title)
        except:
            pass
        if not datetime.now().day == int(r.hget(message.from_user.id, 'time')):
            r.hset(message.from_user.id, 'time', datetime.now().day)
            r.hset(message.from_user.id, 'hp', 100)
            if checkClan(message.from_user.id, building='build5', level=2) and\
                    int(r.hget(message.from_user.id, 'injure')) > 0:
                r.hincrby(message.from_user.id, 'injure', -30)
                if int(r.hget(message.from_user.id, 'injure')) < 0:
                    r.hset(message.from_user.id, 'injure', 0)
            stats = r.hmget(message.from_user.id, 'strength', 'intellect')
            fr = feed_rusak(int(stats[1]))
            r.hincrby(message.from_user.id, 'eat', 1)
            success = fr[0]
            cl = int(r.hget(message.from_user.id, 'class'))
            if cl == 2 or cl == 12 or cl == 22:
                success = 1
            if success == 1:
                try:
                    if int(r.hget(message.from_user.id, 'cabin')) == 1 and int(stats[0]) <= 2000:
                        ran = fr[1] + 15
                        if cl == 20 or cl == 30:
                            ran += 15
                        r.hincrby(message.from_user.id, 'strength', ran)
                    else:
                        ran = fr[1]
                        r.hincrby(message.from_user.id, 'strength', ran)
                except:
                    ran = fr[1]
                    r.hincrby(message.from_user.id, 'strength', ran)
                bd = fr[3]
                if int(r.hget(message.from_user.id, 'support')) == 5:
                    bd = 2
                    damage_support(message.from_user.id)
                emoji = choice(['\U0001F35C', '\U0001F35D', '\U0001F35B', '\U0001F957', '\U0001F32D'])
                word = 'зросла'
                h = int(r.hget(message.from_user.id, 'head'))
                ran2 = 5 if h in (3, 5) else 0
                if h == 5:
                    r.hset(message.from_user.id, 'head', 0, {'s_head': 0})
                ran += ran2
                r.hincrby(message.from_user.id, 'strength', ran2)
                if int(stats[0]) > 3000:
                    if int(stats[0]) > 4000:
                        if int(r.hget(message.from_user.id, 'support')) == 7:
                            decrease = choices([1, 0], [75, 25])
                            damage_support(message.from_user.id)
                            increase_trance(5, message.from_user.id)
                        else:
                            decrease = choices([1, 0], [50, 50])
                    else:
                        if int(r.hget(message.from_user.id, 'support')) == 7:
                            decrease = choices([1, 0], [95, 5])
                            damage_support(message.from_user.id)
                            increase_trance(5, message.from_user.id)
                        else:
                            decrease = choices([1, 0], [80, 20])
                    if decrease == [0]:
                        word = 'зменшилась'
                        r.hincrby(message.from_user.id, 'strength', -2 * ran)
                        if int(r.hget(message.from_user.id, 'head')) == 3:
                            if checkClan(message.from_user.id, building='build5', level=2):
                                r.hset(message.from_user.id, 'head', 5, {'s_head': 1})
                            else:
                                r.hset(message.from_user.id, 'head', 0, {'s_head': 0})
                else:
                    if int(r.hget(message.from_user.id, 'support')) == 7:
                        ran += 15
                        r.hincrby(message.from_user.id, 'strength', 15)
                        damage_support(message.from_user.id)
                        increase_trance(5, message.from_user.id)
                msg = f"{emoji} Твій {names[int(r.hget(message.from_user.id, 'name'))]} смачно поїв.\n\n" \
                      f"Сила {word} на {ran}.\n"
                if fr[2] == 1:
                    msg += 'Інтелект збільшився на 1.\n'
                    intellect(1, message.from_user.id)
                if bd == 2:
                    msg += 'Русак сьогодні в гарному настрої. Бойовий дух збільшився на 10000.'
                    spirit(10000, message.from_user.id, 0)
                    await message.reply_photo('https://i.ibb.co/bK2LrSD/feed.jpg', caption=msg)
                elif bd == 1:
                    msg += 'Русак сьогодні в гарному настрої. Бойовий дух збільшився на 1000.'
                    spirit(1000, message.from_user.id, 0)
                    await message.reply(msg)
                else:
                    await message.reply(msg)
            else:
                await message.reply('\U0001F9A0 Твій русак сьогодні захворів. Сили від їжі не прибавилось.')
        elif datetime.now().day == int(r.hget(message.from_user.id, 'time')):
            await message.reply('Твій русак сьогодні їв, хватить з нього')
    except:
        await message.reply('\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на \n/donbass')


@dp.message_handler(commands=['mine', 'minecraft'])
async def mine(message):
    if message.chat.id == -1001211933154:
        try:
            if r.hexists(message.from_user.id, 'time1') == 0:
                r.hset(message.from_user.id, 'time1', 0)
            if not datetime.now().day == int(r.hget(message.from_user.id, 'time1')):
                ms = mine_salt(int(r.hget(message.from_user.id, 's2')), int(r.hget(message.from_user.id, 'head')),
                               datetime.today().weekday())
                r.hset(message.from_user.id, 'time1', datetime.now().day)
                if message.text.startswith('/minecraft'):
                    if r.hexists(message.from_user.id, 'ac1') == 0:
                        r.hset(message.from_user.id, 'ac1', 1)
                success = ms[0]
                cl = int(r.hget(message.from_user.id, 'class'))
                if cl == 2 or cl == 12 or cl == 22:
                    success = choice([0, 0, 1, 1, 1])
                if int(r.hget(message.from_user.id, 'support')) == 8:
                    success = 1
                    increase_trance(5, message.from_user.id)
                    damage_support(message.from_user.id)
                if success == 1:
                    money = ms[1]
                    if cl == 2 or cl == 12 or cl == 22:
                        money = money * 3
                    if checkClan(message.from_user.id, base=3):
                        money = int(money * 1.34)
                    r.hincrby(message.from_user.id, 'money', money)
                    msg = '\u26CF Твій ' + names[int(r.hget(message.from_user.id, 'name'))] + \
                          ' успішно відпрацював зміну на соляній шахті.\n\n\U0001F4B5 ' \
                          'Зароблено гривень: ' + str(money) + '.'
                    if ms[2] == 1:
                        msg += '\nРусак сьогодні працював з новітніми технологіями.\n'
                        if int(r.hget(message.from_user.id, 'intellect')) < 20:
                            msg += '\U0001F9E0 +1'
                            intellect(1, message.from_user.id)
                        else:
                            msg += '\U0001F4B5 +20'
                            r.hincrby(message.from_user.id, 'money', 20)
                    await message.reply(msg)
                else:
                    if cl == 2 or cl == 12 or cl == 22:
                        msg = '\U0001F37A Твій роботяга втік з-під нагляду. Його знайшли п`яним біля шахти.\n\u2622 +5'
                        if cl == 12 or cl == 22:
                            msg = msg + ' \U0001F4B5 + 8'
                            r.hincrby(message.from_user.id, 'money', 8)
                        r.hincrby(message.from_user.id, 'vodka', 5)
                        r.hincrby('all_vodka', 'vodka', 5)
                        await message.reply(msg)
                    else:
                        await message.reply('\U0001F37A Твій русак втік з-під нагляду. Його знайшли п`яним біля шахти'
                                            '.\n\u2622 +1')
                        r.hincrby(message.from_user.id, 'vodka', 1)
                        r.hincrby('all_vodka', 'vodka', 1)
                        if int(r.hget(message.from_user.id, 'class')) == 18 or \
                                int(r.hget(message.from_user.id, 'class')) == 28:
                            r.hset(message.from_user.id, 'time1', 0)
            elif datetime.now().day == int(r.hget(message.from_user.id, 'time1')):
                await message.reply('Твій русак сьогодні відпрацював зміну.')
        except:
            await message.reply('\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на \n/donbass')


@dp.message_handler(commands=['stat'])
async def stat(message):
    if message.chat.type == 'private':
        try:
            ran = randint(1, 20)
            msg = ''
            if ran == 1:
                msg = '\U0001F465 Кількість користувачів: ' + str(r.scard('everyone'))
            elif ran == 2:
                msg = '\U0001F530 Кількість кланів: ' + str(r.scard('clans'))
            elif ran == 3:
                msg = '\U0001F3C6 Проведено дуелей: ' + r.hget('all_wins', 'wins').decode()
            elif ran == 4:
                msg = '\U0001F3C5 Отримано трофеїв: ' + r.hget('all_trophy', 'trophy').decode()
            elif ran == 5:
                msg = '\u2620\uFE0F Мирна русня: ' + r.hget('all_deaths', 'deaths').decode()
            elif ran == 6:
                msg = '\U0001F476 З`їдено немовлят: ' + r.hget('all_children', 'children').decode()
            elif ran == 7:
                msg = '\u2622 Випито горілки: ' + r.hget('all_vodka', 'vodka').decode()
            elif ran == 8:
                msg = '\U0001F4E6 Відкрито пакунків: ' + r.hget('all_opened', 'packs').decode()
            elif ran == 9:
                ha4 = r.scard('class-1') + r.scard('class-11') + r.scard('class-21')
                ha41 = int(r.hget('win_rate', 'win-1')) + int(r.hget('win_rate', 'win-11')) + int(
                    r.hget('win_rate', 'win-21'))
                ha42 = int(r.hget('win_rate', 'lose-1')) + int(r.hget('win_rate', 'lose-11')) + int(
                    r.hget('win_rate', 'lose-21'))
                ha43 = ha41 / (ha41 + ha42) * 100
                msg = f'\U0001F919 Кількість хачів: {ha4}\n\U0001F3C6 Він рейт: {round(ha43, 2)}'
            elif ran == 10:
                rab = r.scard('class-2') + r.scard('class-12') + r.scard('class-22')
                rab1 = int(r.hget('win_rate', 'win-2')) + int(r.hget('win_rate', 'win-12')) + int(
                    r.hget('win_rate', 'win-22'))
                rab2 = int(r.hget('win_rate', 'lose-2')) + int(r.hget('win_rate', 'lose-12')) + int(
                    r.hget('win_rate', 'lose-22'))
                rab3 = rab1 / (rab1 + rab2) * 100
                msg = f'\U0001F9F0 Кількість роботяг: {rab}\n\U0001F3C6 Він рейт: {round(rab3, 2)}'
            elif ran == 11:
                mag = r.scard('class-3') + r.scard('class-13') + r.scard('class-23')
                mag1 = int(r.hget('win_rate', 'win-3')) + int(r.hget('win_rate', 'win-13')) + int(
                    r.hget('win_rate', 'win-23'))
                mag2 = int(r.hget('win_rate', 'lose-3')) + int(r.hget('win_rate', 'lose-13')) + int(
                    r.hget('win_rate', 'lose-23'))
                mag3 = mag1 / (mag1 + mag2) * 100
                msg = f'\U0001F52E Кількість фокусників: {mag}\n\U0001F3C6 Він рейт: {round(mag3, 2)}'
            elif ran == 12:
                pag = r.scard('class-4') + r.scard('class-14') + r.scard('class-24')
                pag1 = int(r.hget('win_rate', 'win-4')) + int(r.hget('win_rate', 'win-14')) + int(
                    r.hget('win_rate', 'win-24'))
                pag2 = int(r.hget('win_rate', 'lose-4')) + int(r.hget('win_rate', 'lose-14')) + int(
                    r.hget('win_rate', 'lose-24'))
                pag3 = pag1 / (pag1 + pag2) * 100
                msg = f'\U0001F5FF Кількість язичників: {pag}\n\U0001F3C6 Він рейт: {round(pag3, 2)}'
            elif ran == 13:
                meat = r.scard('class-5') + r.scard('class-15') + r.scard('class-25')
                meat1 = int(r.hget('win_rate', 'win-5')) + int(r.hget('win_rate', 'win-15')) + int(
                    r.hget('win_rate', 'win-25'))
                meat2 = int(r.hget('win_rate', 'lose-5')) + int(r.hget('win_rate', 'lose-15')) + int(
                    r.hget('win_rate', 'lose-25'))
                meat3 = meat1 / (meat1 + meat2) * 100
                msg = f'\U0001fa96 Кількість гарматного м`яса: {meat}\n\U0001F3C6 Він рейт: {round(meat3, 2)}'
            elif ran == 14:
                mys = r.scard('class-6') + r.scard('class-16') + r.scard('class-26')
                mys1 = int(r.hget('win_rate', 'win-6')) + int(r.hget('win_rate', 'win-16')) + int(
                    r.hget('win_rate', 'win-26'))
                mys2 = int(r.hget('win_rate', 'lose-6')) + int(r.hget('win_rate', 'lose-16')) + int(
                    r.hget('win_rate', 'lose-26'))
                mys3 = mys1 / (mys1 + mys2) * 100
                msg = f'\U0001F46E Кількість мусорів: {mys}\n\U0001F3C6 Він рейт: {round(mys3, 2)}'
            elif ran == 15:
                mal = r.scard('class-7') + r.scard('class-17') + r.scard('class-27')
                mal1 = int(r.hget('win_rate', 'win-7')) + int(r.hget('win_rate', 'win-17')) + int(
                    r.hget('win_rate', 'win-27'))
                mal2 = int(r.hget('win_rate', 'lose-7')) + int(r.hget('win_rate', 'lose-17')) + int(
                    r.hget('win_rate', 'lose-27'))
                mal3 = mal1 / (mal1 + mal2) * 100
                msg = f'\U0001F921 Кількість малоросів: {mal}\n\U0001F3C6 Він рейт: {round(mal3, 2)}'
            elif ran == 16:
                hak = r.scard('class-8') + r.scard('class-18') + r.scard('class-28')
                hak1 = int(r.hget('win_rate', 'win-8')) + int(r.hget('win_rate', 'win-18')) + int(
                    r.hget('win_rate', 'win-28'))
                hak2 = int(r.hget('win_rate', 'lose-8')) + int(r.hget('win_rate', 'lose-18')) + int(
                    r.hget('win_rate', 'lose-28'))
                hak3 = hak1 / (hak1 + hak2) * 100
                msg = f'\U0001F4DF Кількість хакерів: {hak}\n\U0001F3C6 Він рейт: {round(hak3, 2)}'
            elif ran == 17:
                med = r.scard('class-9') + r.scard('class-19') + r.scard('class-29')
                med1 = int(r.hget('win_rate', 'win-9')) + int(r.hget('win_rate', 'win-19')) + int(
                    r.hget('win_rate', 'win-29'))
                med2 = int(r.hget('win_rate', 'lose-9')) + int(r.hget('win_rate', 'lose-19')) + int(
                    r.hget('win_rate', 'lose-29'))
                med3 = med1 / (med1 + med2) * 100
                msg = f'\u26D1 Кількість медиків: {med}\n\U0001F3C6 Він рейт: {round(med3, 2)}'
            elif ran == 18:
                gop = r.scard('class-10') + r.scard('class-20') + r.scard('class-30')
                gop1 = int(r.hget('win_rate', 'win-10')) + int(r.hget('win_rate', 'win-20')) + int(
                    r.hget('win_rate', 'win-30'))
                gop2 = int(r.hget('win_rate', 'lose-10')) + int(r.hget('win_rate', 'lose-20')) + int(
                    r.hget('win_rate', 'lose-30'))
                gop3 = gop1 / (gop1 + gop2) * 100
                msg = f'\U0001F6AC Кількість гопніків: {gop}\n\U0001F3C6 Він рейт: {round(gop3, 2)}'
            elif ran == 19:
                tax = r.scard('class-31') + r.scard('class-32') + r.scard('class-33')
                tax1 = int(r.hget('win_rate', 'win-31')) + int(r.hget('win_rate', 'win-32')) + int(
                    r.hget('win_rate', 'win-33'))
                tax2 = int(r.hget('win_rate', 'lose-31')) + int(r.hget('win_rate', 'lose-32')) + int(
                    r.hget('win_rate', 'lose-33'))
                tax3 = tax1 / (tax1 + tax2) * 100
                msg = f'\U0001F695 Кількість таксистів: {tax}\n\U0001F3C6 Він рейт: {round(tax3, 2)}'
            elif ran == 20:
                gen = r.scard('class-34') + r.scard('class-35') + r.scard('class-36')
                gen1 = int(r.hget('win_rate', 'win-34')) + int(r.hget('win_rate', 'win-35')) + int(
                    r.hget('win_rate', 'win-36'))
                gen2 = int(r.hget('win_rate', 'lose-34')) + int(r.hget('win_rate', 'lose-35')) + int(
                    r.hget('win_rate', 'lose-36'))
                gen3 = gen1 / (gen1 + gen2) * 100
                msg = f'\U0001F396 Кількість офіцерів: {gen}\n\U0001F3C6 Він рейт: {round(gen3, 2)}'
            await message.reply(msg)
        except:
            pass


@dp.message_handler(commands=['sacrifice'])
async def sacrifice(message):
    try:
        if r.hexists(message.from_user.id, 'time2') == 0:
            r.hset(message.from_user.id, 'time2', 0)
        if datetime.now().day != int(r.hget(message.from_user.id, 'time2')) \
                and r.hexists(message.from_user.id, 'strength') == 1 \
                and int(r.hget(message.from_user.id, 'strength')) != 0:
            markup = InlineKeyboardMarkup()
            await message.reply('\U0001F52A Вбити свого русака?\n\nУ всіх русаків в цьому чаті зменшиться '
                                'бойовий дух на 10%.',
                                reply_markup=markup.add(InlineKeyboardButton(text='Принести в жертву русака',
                                                                             callback_data='sacrifice')))
        else:
            await message.reply('Робити жертвоприношення русаків можна раз в день, і якщо є живий русак.')
    except:
        pass


@dp.message_handler(commands=['fascist'])
async def fascist(message):
    try:
        if int(r.hget('c' + str(message.chat.id), 'base')) > 0 and len(r.smembers(message.chat.id)) >= 14:
            if r.hexists('f' + str(message.chat.id), 'time3') == 0:
                r.hset('f' + str(message.chat.id), 'time3', 0)
            if int(r.hget('f' + str(message.chat.id), 'time3')) != int(datetime.now().day):
                r.hset('f' + str(message.chat.id), 'time3', datetime.now().day)
                ran = []
                for member in r.smembers(message.chat.id):
                    mem = int(member)
                    try:
                        st = await bot.get_chat_member(message.chat.id, mem)
                        if st.status == 'left' or st.status == 'kicked' or st.status == 'banned':
                            r.srem(message.chat.id, mem)
                        else:
                            ran.append(member)
                    except:
                        r.srem(message.chat.id, mem)
                ran = choice(ran)
                ran = int(ran)
                r.hset('f' + str(message.chat.id), 'username', r.hget(ran, 'username').decode())
                r.hincrby(ran, 'childs', 1)
                r.hincrby('all_children', 'children', 1)
                pin = await message.reply('\U0001F468\U0001F3FB\u200D\u2708\uFE0F @' +
                                          r.hget('f' + str(message.chat.id), 'username').decode() +
                                          ' сьогодні займає посаду Фашист дня! Йому видано одне \U0001F476 '
                                          'російське немовля!')
                try:
                    try:
                        await bot.unpin_chat_message(chat_id=pin.chat.id,
                                                     message_id=int(r.hget('f' + str(message.chat.id), 'pin')))
                    except:
                        pass
                    await bot.pin_chat_message(chat_id=pin.chat.id, message_id=pin.message_id,
                                               disable_notification=True)
                    r.hset('f' + str(message.chat.id), 'pin', pin.message_id)
                except:
                    pass

            else:
                await message.reply('\U0001F468\U0001F3FB\u200D\u2708\uFE0F Сьогодні вже вибраний фашист дня - ' +
                                    r.hget('f' + str(message.chat.id), 'username').decode())
        else:
            raise Exception
    except:
        await message.reply('Фашиста дня можна обирати раз в добу і в чатах,'
                            ' де є від 14 власників русаків (з юзернеймами) та заснований клан.')


@dp.message_handler(commands=['shop'])
async def shop(message):
    try:
        if r.hexists(message.from_user.id, 'money') == 0:
            r.hset(message.from_user.id, 'money', 20)
        else:
            pass
        if r.hexists(message.from_user.id, 'childs') == 0:
            await message.reply('У тебе ще не було русаків.\n\nРусака можна отримати, сходивши на /donbass')
        else:
            money = r.hget(message.from_user.id, 'money').decode()
            msg = f'\U0001F4B5 Гривні: {money}\n\nОсь опис товарів, які можна придбати:\n\n\u2622 Горілка "Козаки" - ' \
                  f'збільшує русаку бойовий дух на 10-70.\n\U0001F5E1 Колючий дрин [Атака]- зменшує перед боєм ' \
                  f'бойовий дух ворогу, якщо атакувати його (не використовується, якщо бойовий дух ворога менший ' \
                  f'за 300, обнуляє, якщо від 300 до 1000, зменшує на 1000, якщо від 1000 до 2500 і зменшує на ' \
                  f'20/30/40%, якщо бойовий дух більше 2500).\n\U0001F6E1 Колючий щит [Захист] - працює так само ' \
                  f'як дрин, тільки знижує бойовий дух тому, хто атакує.\n\U0001F9EA Аптечка [Допомога, міцність=5]' \
                  f' - збільшує здоров`я на 5 і на 10 кожного бою.\n\U0001F4B3 Трофейний паспорт - поміняє ім`я ' \
                  f'русака на інше, випадкове.\n\U0001F3DA Утеплена будка - 15 додаткової сили при кожному ' \
                  f'годуванні русака (до 2000 сили). \n\U0001F469\U0001F3FB Жінка - раз в 9 днів народжуватиме ' \
                  f'смачне російське немовля. Жінку треба провідувати кожен день командою \n/woman\n\U0001F6AC Тютюн ' \
                  f'та люлька - на це можна проміняти жінку і піти в козацький похід (бойовий дух русака збільшиться ' \
                  f'на 5000, а кількість вбитих русаків збільшиться на 5).'
            await bot.send_message(message.from_user.id, msg, reply_markup=goods())
            if message.chat.type != 'private':
                await message.reply('Надіслано в пп.')
    except:
        pass


@dp.message_handler(commands=['passport'])
async def passport(message):
    if r.hexists(message.from_user.id, 'wins') == 1:
        stats = r.hmget(message.from_user.id, 'wins', 'trophy', 'deaths', 'childs', 'vodka', 'opened', 'clan')
        sk = r.hmget(message.from_user.id, 's1', 's2', 's3')
        skill = int((int(sk[0]) + int(sk[1]) + int(sk[2])) * 100 / 20)
        ac = 0
        acs = r.hmget(message.from_user.id, 'ac1', 'ac2', 'ac3', 'ac4', 'ac5',
                      'ac6', 'ac7', 'ac8', 'ac9', 'ac10', 'ac11', 'ac12', 'ac13', 'ac14', 'ac15', 'ac16')
        for a in acs:
            try:
                ac += int(a)
            except:
                pass
        clan1 = ''
        if checkClan(message.from_user.id):
            clan1 = '\n\U0001F3E0 Клан: ' + r.hget('c' + stats[6].decode(), 'title').decode()
        await message.reply('\U0001F4DC ' + message.from_user.first_name +
                            '\n\n\U0001F3C6 Кількість перемог: ' + stats[0].decode() +
                            '\n\U0001F3C5 Кількість трофеїв: ' + stats[1].decode() +
                            '\n\u2620\uFE0F Вбито русаків: ' + stats[2].decode() +
                            '\n\U0001F476 З`їдено немовлят: ' + stats[3].decode() +
                            '\n\u2622 Випито горілки: ' + stats[4].decode() +
                            '\n\U0001F4E6 Відкрито пакунків: ' + stats[5].decode() + clan1 +
                            '\n\u26CF Скіли: ' + str(skill) + '%' +
                            '\n\u2B50 Досягнення: ' + str(int(ac * 100 / 32)) + '%')


@dp.message_handler(commands=['woman'])
async def woman(message):
    try:
        if r.hexists(message.from_user.id, 'time4') == 0:
            r.hset(message.from_user.id, 'time4', 0)
        if int(r.hget(message.from_user.id, 'woman')) == 1:
            if int(r.hget(message.from_user.id, 'time4')) != datetime.now().day:
                if r.hexists(message.from_user.id, 'time5') == 0:
                    r.hset(message.from_user.id, 'time5', 0)
                r.hset(message.from_user.id, 'time4', datetime.now().day)
                r.hincrby(message.from_user.id, 'time5', 1)
                if int(r.hget(message.from_user.id, 'time5')) >= 9:
                    await message.reply('\U0001F469\U0001F3FB Ти провідав жінку. Вона народила \U0001F476 '
                                        'немовля. В тебе буде смачний сніданок!')
                    r.hincrby(message.from_user.id, 'childs', 1)
                    r.hincrby('all_children', 'children', 1)
                    r.hset(message.from_user.id, 'time5', 0)
                else:
                    await message.reply('\U0001F469\U0001F3FB Ти провідав жінку. Вона на ' +
                                        r.hget(message.from_user.id, 'time5').decode() + ' місяці.')
            else:
                await message.reply('\U0001F469\U0001F3FB Ти знову провідав жінку. Вона на ' +
                                    r.hget(message.from_user.id, 'time5').decode() + ' місяці.')
    except:
        pass


@dp.message_handler(commands=['ltop'])
async def l_top(message):
    try:
        msg = await top(message.chat.id, message.from_user.id, message.text)
        await message.reply(msg)
    except:
        pass


@dp.message_handler(commands=['gtop'])
async def g_top(message):
    try:
        msg = await top(111, message.from_user.id, message.text)
        await message.reply(msg)
    except:
        pass


@dp.message_handler(commands=['itop'])
async def i_top(message):
    try:
        msg = await itop(message.from_user.id, message.chat.id, message.chat.type)
        await message.reply(msg)
    except:
        pass


@dp.message_handler(commands=['ctop'])
async def c_top(message):
    try:
        msg = await ctop(222, message.from_user.id)
        await message.reply(msg, parse_mode='HTML')
    except:
        pass


@dp.message_handler(commands=['class'])
async def classes(message):
    msg = 'Класи русаків:\n\n\n' \
          'Хач \U0001F919 - якщо у ворога нема зброї - додає 30 бойового духу та збільшує свою ' \
          'силу на 15%, а якщо є - зменшує силу на 15%.\n\n' \
          'Роботяга \U0001F9F0 - йому заборонено хворіти. В шахті заробляє втричі більше грошей,' \
          ' але вдвічі більший шанс забухати (п`є в 5 раз більше). \n\n' \
          'Фокусник \U0001F52E - моментально додає 1 інтелекту. 80% шанс ігнорувати дрин ворога ' \
          'і навести на нього шизофренію, перед початком бою показує випадкові характеристики.\n\n' \
          'Язичник \U0001F5FF - вдвічі збільшує бойовий дух в дуелях. При перемозі отримує' \
          ' втричі більше бойового духу.\n\n' \
          'Гарматне м`ясо \U0001fa96 - +50% сили в бою, якщо є АК-47 (зброя, яку можна придбати в ' \
          'мандрівного торговця). 1% шанс отримати поранення в бою від АК-47 (втрачає весь бойовий' \
          ' дух, здоров`я, все спорядження, на 150 боїв вдвічі зменшує бойовий дух та втричі - силу).\n\n' \
          'Мусор \U0001F46E - має постійну зброю, яка перед боєм ігнорує бойовий дух двох сторін.' \
          ' Якщо є захист, ігнорує лише бойовий дух ворога.\n+30% сили при охороні клану від рейдерів.\n\n' \
          'Малорос \U0001F921 - моментально віднімає 2 інтелекту. При жертві віднімає у всіх' \
          ' русаків чату інтелект, який вони здобули від мухоморів (їх можна буде знову купити). ' \
          'Якщо інтелект не зняло, віднімає 90% бойового духу. Мінімальний шанс перемоги збільшено ' \
          'до 20%.\n\nХакер \U0001F4DF - при поразці є 18% підняти собі бойовий дух, знизити ворогу' \
          ' і заробити гривню.\n\n' \
          'Медик \u26D1 -  якщо у ворога менше ніж 50 здоров`я, то медик лікує йому 5. В іншому' \
          ' випадку з шансом 20% завдає поранення на 2 бої. Наявність медика вдвічі збільшує ' \
          'загальну силу загону в міжчатових битвах.\n\n' \
          'Гопнік \U0001F6AC - лікується від поранення та шизофренії втричі швидше. Додаткові дві гривні за кожну ' \
          'перемогу, якщо на рахунку менше 100 гривень.\n+50% сили в рейдах\n\n' \
          'Таксист \U0001F695 - за перемогу в битві на 10 русаків отримує Донбаський пакунок.\n\n' \
          'Офіцер \U0001F396 - платний клас з платними покращеннями. Вибір офіцера коштує \U0001F4B5 500 ' \
          'грн. Збільшує силу в дуелях на 30% (заміть 10%), якщо більше ніж 90 здоров`я. 2% шанс збільшити ' \
          'інтелект на 1 у міжчатовій битві.\n\n\n'\
          'Щоб подивитись другий рівень класів натисни /class_2\n' \
          'Якщо твій русак вже набрав 5 інтелекту, можеш вибрати один з цих класів (один раз на ' \
          'одного русака), написавши сюди "Обираю клас " і назву класу.'
    try:
        await bot.send_message(message.from_user.id, msg)
        if message.chat.type != 'private':
            await message.reply('Надіслано в пп.')
    except:
        pass


@dp.message_handler(commands=['class_2'])
async def classes_2(message):
    msg = 'Класи русаків:\n\n\n' \
          'Борцуха \U0001F919\U0001F919 - якщо у ворога нема зброї' \
          ', є шанс активувати один з прийомів при перемозі. Чим більша сила ворога, тим більший ' \
          'цей шанс. Кидок через стегно: -50-100 бойового духу ворогу. Млин: +50-100 бойового духу.' \
          ' Кидок прогином: +2 гривні (10% шанс).\n\n' \
          'Почесний алкаш \U0001F9F0\U0001F9F0 - наполовину зменшує кількість потрібних перемог та' \
          ' горілки для прокачки майстерності та алкоголізму. Навіть якщо в шахті нап`ється, йому ' \
          'буде видано 8 гривень.\n\n' \
          'Злий геній \U0001F52E\U0001F52E - +2 інтелекту, колода з кіоску мінятиме лише ті ' \
          'характеристики, які у ворога більші.\n\n' \
          'Скінхед \U0001F5FF\U0001F5FF - збільшує силу на 20% якщо у ворога менше трофеїв. ' \
          'Подвоєний бойовий дух в боях з хачами. Замість купівлі дрина буде видана зброя з ' \
          'аналогічним ефектом - Бита [Атака, міцність=3].\n\n' \
          'Орк \U0001fa96\U0001fa96 - додає +2.5% сили на бій за кожне з`їдене немовля ' \
          '(максимум 50%).\n\n' \
          'Силовик \U0001F46E\U0001F46E - ігнорує інтелект, якщо він не менший. Якщо є щит, а інтелект і' \
          ' сила у ворога більші - ігнорує силу. Здібність не діє проти інших мусорів.\n\n' \
          'Кремлебот \U0001F921\U0001F921 - одноразова премія - 200 гривень. Онуляє рахунок мухоморів. ' \
          'Можливість купляти горілку за перемоги, якщо нема грошей.\n\n' \
          'Кіберзлочинець \U0001F4DF\U0001F4DF - отримує доступ до баз даних - якщо напився на ' \
          'роботі, то може працювати ще раз; можливість купляти мухомори без обмежень.\n\n' \
          'Нарколог \u26D1\u26D1 - якщо у ворога від 50 здоров`я - з шансом 20% додає на 1 ' \
          'поранення більше за кожен мухомор і зменшує здоров`я на рівень алкоголізму ворога.\n\n' \
          'Зек \U0001F6AC\U0001F6AC - подвоює бонус сили від утепленої будки. Зменшує бойовий дух ворога на 20%, ' \
          'а якщо в нього менше перемог - на 40%. Ця здібність не діє проти мусорів.\n\n' \
          'Далекобійник \U0001F695\U0001F695 - жінки на 50 гривень дешевші. +3% ресурсів за роботу в клані за кожен ' \
          'невідкритий пакунок (максимум 120%).\n\n' \
          'Воєнний злочинець \U0001F396\U0001F396 - \U0001F3C5 50 трофеїв. Якщо русак такого класу в міжчатовій битві' \
          ' один - збільшує свою силу на 25% за кожне гарматне м`ясо та зменшує бойовий дух ворогам на 5%.\n\n\n' \
          'Щоб подивитись третій рівень класів натисни /class_3\n' \
          'Якщо твій русак вже набрав 12 інтелекту і вибрав клас, можеш ' \
          'покращити клас, написавши сюди "Покращити русака".'
    try:
        await bot.send_message(message.from_user.id, msg)
        if message.chat.type != 'private':
            await message.reply('Надіслано в пп.')
    except:
        pass


@dp.message_handler(commands=['class_3'])
async def classes_3(message):
    msg = 'Класи русаків:\n\n\n' \
          'Гроза Кавказу \U0001F919\U0001F919\U0001F919 - моментально збільшує силу на 200. ' \
          '+10 сили і +1000 бойового духу якщо вперше за день в бою зустрів хача.\n\n' \
          'П`яний майстер \U0001F9F0\U0001F9F0\U0001F9F0 - якщо русак вже їв, 0% шанс в бою ' \
          'отримати талон на їжу (додаткове годування). Шанс збільшується на 1% за кожні два рівня ' \
          'алкоголізму.\n\n' \
          'Некромант \U0001F52E\U0001F52E\U0001F52E - при захисті збільшує інтелект на 5% за кожну' \
          ' смерть (максимум 35%). При атаці збільшує силу на 3% за кожну смерть ворога ' \
          '(максимум 33%). Якщо у ворога 0 хп - лікує його на 10 і збільшує свій \U0001F44A ' \
          'бойовий транс на 5.\n\n' \
          'Білий вождь \U0001F5FF\U0001F5FF\U0001F5FF - збільшує бойовий дух на 1% за кожен трофей ' \
          '(максимум 50%). Якщо весь загін міжчатової битви з одного клану - збільшує загальну силу' \
          ' на 25% і додає кожному 250 бойового духу.\n\n' \
          'Герой Новоросії \U0001fa96\U0001fa96\U0001fa96 - якщо більше ніж 300 сили: ' \
          'обидва русаки можуть отримати поранення на 150 боїв (якщо в героя є АК-47), з шансом 10%' \
          ' в бою герой і ворог отримають невелике поранення (герой: +1 \U0001fa78, ворог +5-10' \
          '\U0001fa78).\n\n' \
          'Товариш майор \U0001F46E\U0001F46E\U0001F46E - 20% шанс вилучити в ворога зброю при ' \
          'захисті і захист при атаці і отримати щит або підняти його міцність на 10 (не діє проти' \
          ' інших мусорів).\n\n' \
          'Агент ФСБ \U0001F921\U0001F921\U0001F921 - одноразова премія - 300 гривень. В бою проти ' \
          'русака без класу є 5% шанс перетворити його в малороса. За це агент отримує 20 гривень. ' \
          'Можливість на території ворожого клану вкрасти гроші командою clan.\n\n' \
          'Black Hat \U0001F4DF\U0001F4DF\U0001F4DF - здібність хакера тепер додає по гривні за ' \
          'кожні 50 гривень на рахунку ворога (1-5 гривень).\n\n' \
          'Патологоанатом \u26D1\u26D1\u26D1 - якщо у ворога менше ніж 50 здоров`я - лікує ' \
          'поранення і шизофренію на 1, 25% шанс отримати за це 2 гривні і по одній гривні ' \
          'додатково за лікування цих захворювань. Якщо у ворога 0 здоров`я - лікує йому 20 і ' \
          'отримує 5 гривень.\n\n' \
          'Мародер \U0001F6AC\U0001F6AC\U0001F6AC - на рейдових локаціях грабує вдвічі більше. Якщо рейд проти клану ' \
          '- при програші зменшує силу ворожої охорони на 10% за кожного мародера в групі.\n\n' \
          'Танкіст \U0001F695\U0001F695\U0001F695 - під час пошуку цілі для рейду +20% шанс активувати ' \
          'Пограбування гумконвоїв (стакається).\n\n' \
          'Генерал \U0001F396\U0001F396\U0001F396 - \U0001F31F 1 погон. Здібність залежить від клану. Комуна - 20% ' \
          'шанс отримати секретні коди при роботі. Коаліція - додатковий рускій дух за перемогу. Асоціація - при ' \
          'охороні - збільшує силу гумконвою на 500000. Організація - збільшує грошову нагороду у міжчатових ' \
          'битвах до 9.\n\n\n' \
          'Якщо твій русак вже набрав 20 інтелекту і покращив клас, можеш ще раз ' \
          'покращити клас, написавши сюди "Вдосконалити русака".'
    try:
        await bot.send_message(message.from_user.id, msg)
        if message.chat.type != 'private':
            await message.reply('Надіслано в пп.')
    except:
        pass


@dp.message_handler(commands=['merchant'])
async def merchant(message):
    if message.chat.id == -1001211933154:
        if r.hexists('soledar', 'merchant_day') == 0:
            r.hset('soledar', 'merchant_day', 0)
            r.hset('soledar', 'merchant_hour', randint(18, 22))
        if int(r.hget('soledar', 'merchant_day')) != datetime.now().day and \
                int(r.hget('soledar', 'merchant_hour')) == datetime.now().hour:
            msg, markup = merchant_msg()
            pin = await message.reply(msg, reply_markup=markup)
            r.hset('soledar', 'merchant_day', datetime.now().day)
            r.hset('soledar', 'merchant_hour_now', datetime.now().hour)
            r.hset('soledar', 'merchant_hour', randint(18, 22))
            try:
                await bot.unpin_chat_message(chat_id=pin.chat.id, message_id=int(r.hget('soledar', 'pin')))
            except:
                pass
            await bot.pin_chat_message(chat_id=pin.chat.id, message_id=pin.message_id, disable_notification=True)
            r.hset('soledar', 'pin', pin.message_id)

        else:
            msg = 'Мандрівний торговець приходить раз в день у випадкову годину (від 18 до 22).\n' \
                  'Продає універсальний захист, рідкісні гриби та спорядження для всіх класів.'
            if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                    int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
                msg = msg + '\n\nТорговець прийшов:\nt.me/c/1211933154/' + r.hget('soledar', 'pin').decode()
            await message.answer(msg, disable_web_page_preview=True)
    else:
        msg = 'Мандрівний торговець приходить увечері в <a href="https://t.me/+cClR7rA-sZAyY2Uy">@soledar1</a>.'
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            msg = msg + '\n\nТорговець прийшов:\nt.me/c/1211933154/' + r.hget('soledar', 'pin').decode()
        await message.answer(msg, disable_web_page_preview=True, parse_mode='HTML')


@dp.message_handler(commands=['donate'])
async def donate(message):
    markup = InlineKeyboardMarkup()
    await message.answer('Якщо хтось хоче підтримати автора, то можне задонатити і отримати\n'
                         '\U0001F31F погон російського генерала, який можна потратити в \n/donate_shop:'
                         '\n\n<code>5375414105409873</code>',
                         reply_markup=markup.add(InlineKeyboardButton(text='Як отримати погони?',
                                                                      callback_data='donate')), parse_mode='HTML')


@dp.message_handler(commands=['donated'])
async def donated(message):
    if message.chat.type == 'private':
        full_text = '<code>' + str(message.from_user.id) + '</code>\n' + str(message.from_user.first_name) + ' ' + \
                    str(message.from_user.last_name) + '\n@' + str(message.from_user.username) + '\n\n' + message.text
        await bot.send_message(456514639, full_text, parse_mode='HTML')
        await bot.send_message(message.chat.id, '\u2705', reply_to_message_id=message.message_id)
        if message.from_user.id == 456514639:
            try:
                code = message.text.split(' ')
                r.hincrby(int(code[1]), 'strap', int(code[2]))
                await bot.send_message(message.chat.id, '\u2705', reply_to_message_id=message.message_id)
                await bot.send_message(int(code[1]), 'Нараховано:\n\n\U0001F31F Погон російського генерала: ' + code[2])
            except:
                await bot.send_message(message.chat.id, '\u274E', reply_to_message_id=message.message_id)


@dp.message_handler(commands=['donate_shop'])
async def donate_shop(message):
    try:
        if r.hexists(message.from_user.id, 'strap') == 0:
            r.hset(message.from_user.id, 'strap', 0)
        strap = r.hget(message.from_user.id, 'strap').decode()
        msg = f'\U0001F31F Погони російських генералів: {strap}\n\nОсь опис товарів, які можна придбати:\n\n' \
              f'\U0001F4F8 Заміна фото русака (ціна 1 погон):\n\U0001F304 Класове преміум фото 1 (Кадиров, Обеме, ' \
              f'Горшок, Тесак, Захарченко, Дерек Шовін, Янукович, Petya, Джонні Сінс, Чікатіло, Раян Гослінг, ' \
              f'Шойгу).\n\U0001F307 Класове преміум фото 2 (Хасбулла, Стаханов, Мавроді, Просвірін, Гіркін-Стрєлков, ' \
              f'Шварцнеггер, Медведчук в пікселі, Дуров, Доктор Попов, Каневський, Герасімов).\n\U0001F309 Чмоня.\n\n' \
              f'\U0001F3CB\uFE0F\u200D\u2642\uFE0F Прокачка русака або клану:\n\U0001F943 Настоянка глоду - буст ' \
              f'для новачків. Якщо в русака менше 1000 сили і 5 інтелекту, то настоянка моментально додасть 400 ' \
              f'сили і 4 інтелекту.\n\U0001F4E6 40 Донбаських пакунків\n\U0001F9FE Ресурси для клану: ' \
              f'\U0001F333 2222 \U0001faa8 1111 \U0001F47E 33\n\U0001F393 Курс перекваліфікації - дозволяє русаку ' \
              f'наново вибрати клас.\n\U0001F3E0 Велике будівництво - додатковий підвал найвищого рівня (покупка ' \
              f'доступна до етапу 2. Купівля будівельних матеріалів).'
        await bot.send_message(message.from_user.id, msg, reply_markup=donate_goods())
        if message.chat.type != 'private':
            await message.reply('Надіслано в пп.')
    except:
        pass


@dp.message_handler(commands=['promo_code'])
async def promo_code(message):
    try:
        if message.chat.type != 'private':
            await bot.delete_message(message.chat.id, message.message_id)
        else:
            msg = message.text.split(' ')[1]
            uid = str(message.from_user.id).encode()
            if msg.encode() in r.smembers('promo_codes'):
                if msg.startswith('soledar') and uid not in r.smembers('first_code'):
                    r.sadd('first_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'packs', 10)
                    r.hincrby(message.from_user.id, 'vodka', 50)
                    r.hincrby('all_vodka', 'vodka', 50)
                    await message.reply('\u26CF Соледарський промокод активовано!\n\U0001F4E6 +10 \u2622 +50')
                elif msg.startswith('n') and uid not in r.smembers('second_code'):
                    msg = '\u26CF Хакерський промокод активовано!\n\U0001F4E6 +10 \U0001F4B5 +100 \u2622 +50'
                    r.sadd('second_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'packs', 10)
                    r.hincrby(message.from_user.id, 'money', 100)
                    r.hincrby(message.from_user.id, 'vodka', 50)
                    r.hincrby('all_vodka', 'vodka', 50)
                    if checkClan(message.from_user.id):
                        c = 'c' + r.hget(message.from_user.id, 'clan').decode()
                        if message.from_user.id == int(r.hget(c, 'leader')):
                            r.hincrby('c' + r.hget(message.from_user.id, 'clan').decode(), 'codes', 1)
                            msg += '\n\U0001F916 +1'
                    await message.reply(msg)
                elif msg.startswith('mine') and uid not in r.smembers('third_code'):
                    r.sadd('third_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'packs', 30)
                    r.hset(message.from_user.id, 'weapon', 12)
                    r.hset(message.from_user.id, 's_weapon', 50)
                    await message.reply('\u26CF Промокод Майнкрафту активовано!\n \U0001F4E6 +30 \U0001F5E1 +50')
    except:
        pass


@dp.message_handler(commands=['battle'])
async def battle(message):
    if message.chat.type != 'private':
        if r.hexists('battle' + str(message.chat.id), 'start') == 0:
            if r.hexists('battle' + str(message.chat.id), 'ts') == 0:
                r.hset('battle' + str(message.chat.id), 'ts', 0)
            if int(datetime.now().timestamp()) - int(r.hget('battle' + str(message.chat.id), 'ts')) > 5:
                r.hset('battle' + str(message.chat.id), 'ts', int(datetime.now().timestamp()))
                try:
                    await bot.delete_message(message.chat.id, message.message_id)
                    a = await bot.send_message(message.chat.id, '\u2694 Починається битва...\n\n',
                                               reply_markup=battle_button())
                    r.hset('battle' + str(message.chat.id), 'start', a.message_id)
                    r.hset('battle' + str(message.chat.id), 'starter', message.from_user.id)
                    try:
                        await bot.pin_chat_message(a.chat.id, a.message_id, disable_notification=True)
                        r.hset('battle' + str(message.chat.id), 'pin', a.message_id)
                    except:
                        pass
                except:
                    pass
        else:
            try:
                await bot.send_message(message.chat.id, '\U0001F5E1 Підготовка до битви тут\n\nКількість бійців: ' +
                                       str(r.scard('fighters' + str(message.chat.id))),
                                       reply_to_message_id=int(r.hget('battle' + str(message.chat.id), 'start')))
                await bot.delete_message(message.chat.id, message.message_id)
            except:
                try:
                    await bot.delete_message(message.chat.id, int(r.hget('battle' + str(message.chat.id), 'start')))
                except:
                    pass
                r.hdel('battle' + str(message.chat.id), 'start')
                for mem in r.smembers('fighters' + str(message.chat.id)):
                    r.srem('fighters' + str(message.chat.id), mem)
                try:
                    await bot.delete_message(message.chat.id, message.message_id)
                except:
                    pass


@dp.message_handler(commands=['war'])
async def war_battle(message):
    banned = [-1001646765307, -1001475102262, -714355096, 557298328, 530769095, 470411500, 1767253195]
    c = await bot.get_chat_members_count(message.chat.id)
    if message.chat.type != 'private' and c >= 10 \
            and '@' not in message.chat.title and message.chat.id not in banned and message.from_user.id not in banned:
        if r.hexists('war_battle' + str(message.chat.id), 'start') == 0:
            try:
                await bot.delete_message(message.chat.id, message.message_id)
            except:
                pass
            emoji = choice(['\U0001F3DF', '\U0001F3AA', '\U0001F30E', '\U0001F30D', '\U0001F30F'])
            a = await bot.send_message(message.chat.id, emoji + ' Починається міжчатова битва...\n\n',
                                       reply_markup=battle_button_3())
            r.hset('war_battle' + str(message.chat.id), 'start', a.message_id)
            r.hset('war_battle' + str(message.chat.id), 'title', message.chat.title)
            r.hset('war_battle' + str(message.chat.id), 'starter', message.from_user.id)
            r.hset('war_battle' + str(message.chat.id), 'war_ts', int(datetime.now().timestamp()))
            r.sadd('started_battles', message.chat.id)
            try:
                await bot.pin_chat_message(a.chat.id, a.message_id, disable_notification=True)
                r.hset('war_battle' + str(message.chat.id), 'pin', a.message_id)
            except:
                pass
        elif '@' not in message.chat.title:
            try:
                msg = '\U0001F5E1 Підготовка до міжчатової битви тут.\n\nКількість наших бійців: ' \
                      + str(r.scard('fighters_2' + str(message.chat.id)))
                await bot.send_message(message.chat.id, msg,
                                       reply_to_message_id=int(r.hget('war_battle' + str(message.chat.id), 'start')))
                try:
                    await bot.delete_message(message.chat.id, message.message_id)
                except:
                    pass
            except:
                try:
                    await bot.delete_message(message.chat.id, message.message_id)
                    await bot.delete_message(message.chat.id, int(r.hget('war_battle' + str(message.chat.id), 'start')))
                except:
                    pass
                r.hdel('war_battle' + str(message.chat.id), 'start')
                r.srem('battles', message.chat.id)
                for member in r.smembers('fighters_2' + str(message.chat.id)):
                    r.hdel(member, 'in_war')
                    r.srem('fighters_2' + str(message.chat.id), member)


@dp.message_handler(commands=['crash'])
async def crash(message):
    try:
        st = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if message.from_user.id in sudoers or st.status == 'creator' or st.can_restrict_members is True:
            r.hdel('war_battle' + str(message.chat.id), 'start')
            r.srem('battles', message.chat.id)
            for member in r.smembers('fighters_2' + str(message.chat.id)):
                r.hdel(member, 'in_war')
                r.srem('fighters_2' + str(message.chat.id), member)
            try:
                await bot.unpin_chat_message(message.chat.id, int(r.hget('war_battle' + str(message.chat.id), 'pin')))
            except:
                pass
            await message.reply('\u2705')
    except:
        pass


@dp.message_handler(commands=['quit'])
async def quit_from_battle(message):
    try:
        if int(datetime.now().timestamp()) - int(r.hget(message.from_user.id, 'w_ts')) > 1800:
            cid = r.hget(message.from_user.id, 'in_war').decode()
            r.hdel(message.from_user.id, 'in_war')
            r.srem('fighters_2' + cid, message.chat.id)
            await message.reply('\u2705')
        else:
            await bot.send_message(message.from_user.id, 'Покидати міжчатові битви можна тільки раз в пів години.')
    except:
        pass


@dp.message_handler(commands=['achieve'])
async def achievements(message):
    try:
        full_list = ['', '\u26AA Хто не з нами, той нехай йде собі до сраки', '\u26AA І москаля нема, немає москаля',
                     '\u26AA Моя фамілія Залупа', '\u26AA Наливай, куме, горілки стаканчик',
                     '\u26AA Бігає по полю весело кабанчик', '\U0001f535 Геніальний розум, великий чоловік',
                     '\U0001f535 Гордо і достойно ти живеш свій вік',
                     '\U0001f535 Зараз розберемося, кому належить вулиця',
                     '\U0001f535 Ах лента за лентою набої подавай', '\U0001f7e3 Ніколи не плач на радість орді',
                     '\U0001f7e3 Ворога знищено, як був наказ', '\U0001f7e3 Я заводжу хімікат, розпочинаю атентат',
                     '\U0001f7e3 А до берега тихо хвилі несуть поранені душі живих кораблів',
                     '\U0001f534 Я мав купу бабок, я мав купу справ', '\U0001f534 Танцюй і пий, поки живий',
                     '\U0001f534 Кривавий пастор']

        acs = r.hmget(message.from_user.id, 'ac1', 'ac2', 'ac3', 'ac4', 'ac5',
                      'ac6', 'ac7', 'ac8', 'ac9', 'ac10', 'ac11', 'ac12', 'ac13', 'ac14', 'ac15', 'ac16')

        if isinstance(acs[1], type(None)):
            if int(r.hget(message.from_user.id, 'deaths')) >= 1:
                r.hset(message.from_user.id, 'ac2', 1)
        if isinstance(acs[3], type(None)):
            if int(r.hget(message.from_user.id, 'vodka')) >= 150:
                r.hset(message.from_user.id, 'ac4', 1)
        if isinstance(acs[4], type(None)):
            if int(r.hget(message.from_user.id, 'eat')) >= 15:
                r.hset(message.from_user.id, 'ac5', 1)
        if isinstance(acs[5], type(None)):
            if int(r.hget(message.from_user.id, 'intellect')) >= 20:
                r.hset(message.from_user.id, 'ac6', 1)
        if isinstance(acs[6], type(None)):
            if int(r.hget(message.from_user.id, 'strength')) >= 2000:
                r.hset(message.from_user.id, 'ac7', 1)
        if isinstance(acs[7], type(None)):
            if int(r.hget(message.from_user.id, 'spirit')) >= 10000:
                r.hset(message.from_user.id, 'ac8', 1)
        if isinstance(acs[8], type(None)):
            if int(r.hget(message.from_user.id, 'wins')) >= 1000:
                r.hset(message.from_user.id, 'ac9', 1)
        if isinstance(acs[9], type(None)):
            if str(message.from_user.id).encode() in r.smembers('fighters' + str(message.chat.id)):
                r.hset(message.from_user.id, 'ac10', 1)
        if isinstance(acs[10], type(None)):
            if int(r.hget(message.from_user.id, 'weapon')) >= 11 or \
                    int(r.hget(message.from_user.id, 'defense')) >= 11 or \
                    int(r.hget(message.from_user.id, 'support')) == 2:
                r.hset(message.from_user.id, 'ac11', 1)
        if isinstance(acs[11], type(None)):
            if int(r.hget(message.from_user.id, 'deaths')) >= 15 and int(r.hget(message.from_user.id, 'childs')) >= 15:
                r.hset(message.from_user.id, 'ac12', 1)
        if isinstance(acs[13], type(None)):
            if int(r.hget(message.from_user.id, 'injure')) > 0 and int(r.hget(message.from_user.id, 'sch')) > 0 and \
                    int(r.hget(message.from_user.id, 'buff')) > 0:
                r.hset(message.from_user.id, 'ac14', 1)

        acl = ['', 'ac1', 'ac2', 'ac3', 'ac4', 'ac5', 'ac6', 'ac7', 'ac10', 'ac11',
               'ac8', 'ac9', 'ac13', 'ac14', 'ac15', 'ac16', 'ac12']
        acs = r.hmget(message.from_user.id, 'ac1', 'ac2', 'ac3', 'ac4', 'ac5',
                      'ac6', 'ac7', 'ac10', 'ac11', 'ac8', 'ac9', 'ac13', 'ac14', 'ac15', 'ac16', 'ac12')

        reply = '\u2B50 Досягнення ' + message.from_user.first_name + ':\n\n'
        new, new_a, number = '', 0, 1
        for ac in acs:
            if str(ac) == 'None':
                number = number + 1
                continue
            elif ac.decode() == '1':
                new_a = new_a + 1
                new = 'Отримано нові досягнення!\n\U0001F476 + ' + str(new_a) + '\n'
                r.hincrby(message.from_user.id, 'childs', 1)
                r.hincrby('all_children', 'children', 1)
                r.hset(message.from_user.id, acl[number], 2)
                reply += full_list[number] + '\n'
            elif ac.decode() == '2':
                reply += full_list[number] + '\n'

            number = number + 1
        await message.reply(new + reply)
    except:
        pass


@dp.message_handler(commands=['i'])
async def inventory(message):
    try:
        inv = r.hmget(message.from_user.id, 'weapon', 'defense', 'support', 'head',
                      's_weapon', 's_defense', 's_support', 's_head')
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

        await message.reply(f'\U0001F5E1 Зброя: {weapons[w]}{m1}\n\U0001F6E1 Захист: {defenses[d]}{m2}\n\U0001F9EA '
                            f'Допомога: {supports[s]}{m3}\n\U0001F3A9 Шапка: {heads[h]}{m4}',
                            reply_markup=invent(w, d, s, h))
    except:
        await message.reply('\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на \n/donbass')


@dp.message_handler(commands=['pack'])
async def pack(message):
    if r.hexists(message.from_user.id, 'name') == 1:
        packs = int(r.hget(message.from_user.id, 'packs'))
        if packs != 0:
            await message.reply('\U0001F4E6 Донбаські пакунки: ' + str(packs) + '\n\nВідкрити?',
                                reply_markup=unpack())
        else:
            await message.reply('\U0001F4E6 Донбаський пакунок коштує \U0001F4B5 20 гривень.'
                                '\n\nКупити один і відкрити?', reply_markup=unpack())
    else:
        await message.reply('\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на \n/donbass')


@dp.message_handler(commands=['skills'])
async def skills(message):
    try:
        s = r.hmget(message.from_user.id, 's1', 's2', 's3')
        s1, s2, s3 = int(s[0]), int(s[1]), int(s[2])
        s11, s22, s221, s222 = s1, s2, 0, 0
        intel = ' гривень, а шанс підняти інтелект - 10%. '
        if s2 == 1:
            s221, s222 = 3, 8
        elif s2 == 2:
            s221, s222 = 4, 9
        elif s2 == 3:
            s221, s222 = 5, 10
        else:
            s221, s222 = 5, 10
            intel = ' гривень, а шанс підняти інтелект - 20%. '
        cl = int(r.hget(message.from_user.id, 'class'))
        if cl == 2 or cl == 12 or cl == 22:
            s221 = s221 * 3
            s222 = s222 * 3
            if cl == 12 or cl == 22:
                s11 = s11 / 2
                s22 = s22 / 2

        up1 = ' Для покращення цієї здібності треба випити \u2622 ' + str(int(s11 * 100)) + ' горілки.'
        up2 = 'Покращення цієї здібності збільшить матеріальну та моральну користь від шахт та коштує 100 грн. ' \
              'Також необхідно набрати \n\U0001F3C6 ' + str(int(s22 * 250)) + ' перемог. За повне покращення ' \
                                                                              'інтелект русака збільшиться на 2.'
        up3 = 'Етапи будівництва:\n' \
              '1. Купівля другої утепленої будки (30 грн)\n' \
              '2. Купівля будівельних матеріалів (750 грн)\n' \
              '3. Будівництво (твій русак втратить 25% сили). ' \
              'На цьому етапі можна отримати додаткового русака (годувати одного в день)\n' \
              '4. Купівля припасів (1500 грн). Можна годувати і відправляти в шахти обох русаків.\n'
        if s1 >= 10:
            up1 = ''
        if s2 >= 5:
            up2 = ''
        if s3 >= 5:
            up3 = ''
        msg = '\u2622 Алкоголізм:\n\nГорілка додає від ' + str(10 * s1) + ' до ' + str(70 * s1) + \
              ' бойового духу.' + up1 + '\n'
        for a in range(10):
            if s1 <= 0:
                msg = msg + '\u2B1C'
            else:
                msg = msg + '\U0001f7e7'
                s1 = s1 - 1

        msg = msg + '\n\n\u26CF Майстерність:\n\nЗараз русак в шахті може заробити від ' + str(s221) + ' до ' + \
                    str(s222) + intel + up2 + '\n'

        for a in range(5):
            if s2 <= 0:
                msg = msg + '\u2B1C'
            else:
                msg = msg + '\U0001f7e5'
                s2 = s2 - 1

        msg = msg + '\n\n\U0001F3DA Велике будівництво\n\nПідвал для додаткового русака. \n' + up3
        for a in range(5):
            if s3 <= 0:
                msg = msg + '\u2B1C'
            else:
                msg = msg + '\U0001f7eb'
                s3 = s3 - 1
        await bot.send_message(message.from_user.id, msg, reply_markup=skill_set())
        if message.chat.type != 'private':
            await message.reply('Надіслано в пп.')
    except:
        pass


@dp.message_handler(commands=['swap'])
async def swap(message):
    try:
        if int(r.hget(message.from_user.id, 's3')) >= 4:
            if r.hexists(message.from_user.id, 'name') == 1:
                a = r.hmget(message.from_user.id, 'name', 'strength', 'intellect', 'spirit',
                            'weapon', 's_weapon', 'defense', 's_defense', 'mushrooms', 'class', 'photo', 'injure', 'hp',
                            'support', 's_support', 'sch', 'buff', 'head', 's_head')
                b = r.hmget(message.from_user.id, 'name2', 'strength2', 'intellect2', 'spirit2', 'weapon2', 's_weapon2',
                            'defense2', 's_defense2', 'mushrooms2', 'class2', 'photo2', 'injure2', 'hp2',
                            'support2', 's_support2', 'sch2', 'buff2', 'head2', 's_head2')
                r.hset(message.from_user.id, 'name2', a[0], {'strength2': a[1], 'intellect2': a[2], 'spirit2': a[3],
                                                             'weapon2': a[4], 's_weapon2': a[5], 'defense2': a[6],
                                                             's_defense2': a[7], 'mushrooms2': a[8], 'class2': a[9],
                                                             'photo2': a[10], 'injure2': a[11], 'hp2': a[12],
                                                             'support2': a[13], 's_support2': a[14], 'sch2': a[15],
                                                             'buff2': a[16], 'head2': a[17], 's_head2': a[18]})
                r.hset(message.from_user.id, 'name', b[0], {'strength': b[1], 'intellect': b[2], 'spirit': b[3],
                                                            'weapon': b[4], 's_weapon': b[5], 'defense': b[6],
                                                            's_defense': b[7], 'mushrooms': b[8], 'class': b[9],
                                                            'photo': b[10], 'injure': b[11], 'hp': b[12],
                                                            'support': b[13], 's_support': b[14], 'sch': b[15],
                                                            'buff': b[16], 'head': b[17], 's_head': b[18]})
                if r.hexists(message.from_user.id, 'time22') == 1:
                    a1 = r.hget(message.from_user.id, 'time')
                    b1 = r.hget(message.from_user.id, 'time22')
                    a2 = r.hget(message.from_user.id, 'time1')
                    b2 = r.hget(message.from_user.id, 'time23')
                    r.hset(message.from_user.id, 'time', b1)
                    r.hset(message.from_user.id, 'time22', a1)
                    r.hset(message.from_user.id, 'time1', b2)
                    r.hset(message.from_user.id, 'time23', a2)
                await message.reply('Бойового русака змінено.')
            else:
                await message.reply('\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на \n/donbass')
    except:
        pass


@dp.message_handler(commands=['clan'])
async def clan(message):
    cid = str(message.chat.id)
    c = 'c' + cid
    prefix = ['', 'Банда', 'Клан', 'Гільдія', 'Угруповання',
              'Комуна', 'Коаліція', 'Асоціація', 'Організація',
              'Союз', 'Орден', 'Ліга', 'Корпорація']
    chats = [-1001211933154]  # -1001733230634
    if message.chat.type == 'supergroup' and message.chat.id not in chats:
        if r.hexists(c, 'base') == 0:
            await message.reply('\U0001F3D7 В чаті нема клану.\n\nАдміністратор може заснувати банду за \U0001F4B5'
                                ' 250 гривень або \U0001F31F 1 погон російського генерала і стати лідером.',
                                reply_markup=create_clan())
        else:
            if str(message.from_user.id).encode() in r.smembers('cl' + cid) or message.from_user.id in sudoers:
                base = int(r.hget(c, 'base'))
                title = r.hget(c, 'title').decode()
                leader = r.hget(int(r.hget(c, 'leader')), 'firstname').decode()
                if r.scard('cl2' + cid) == 1:
                    leader += f"\nЗаступник: {r.hget(r.srandmember('cl2' + cid), 'firstname').decode()}"
                elif r.scard('cl2' + cid) == 2:
                    ran = r.srandmember('cl2' + cid, 2)
                    leader += f"\nЗаступники: {r.hget(ran[0], 'firstname').decode()}, " \
                              f"{r.hget(ran[1], 'firstname').decode()}"
                if base == 1:
                    await message.answer(f"<i>Банда</i> {title}\n\nЛідер: {leader}"
                                         f"\nКількість учасників: {r.scard('cl' + cid)} / 25\n\n\U0001f6d6 Барак\n"
                                         f"Можливість обирати фашиста дня та зберігати деякі ресурси.\n\nРесурси:"
                                         f"\n\U0001F4B5 Гривні: {r.hget(c, 'money').decode()}"
                                         f"\n\U0001F333 Деревина: {r.hget(c, 'wood').decode()} / 15000"
                                         f"\n\U0001faa8 Камінь: {r.hget(c, 'stone').decode()} / 10000",
                                         parse_mode='HTML')
                elif base >= 2:
                    building, wins, num = '', '', 25
                    if r.hexists(222, cid) == 1:
                        wins = '\nКількість перемог: ' + r.hget(222, cid).decode()
                    if base == 2:
                        building = '\U0001F3E0 Притулок\n\U0001F4B5 +6 \U0001F47E +1 за перемоги в міжчатових боях, ' \
                                   'якщо серед учасників всі з клану.\n'
                    elif base == 3:
                        building = '\U0001F3E1 Апартаменти\n\U0001F4B5 +34% за роботу на шахтах Соледару.\n'
                    elif base == 4:
                        building = '\U0001F3D8 Штаб\n\U0001F4B5 Шанс подвоїти грошову нагороду за перемогу в дуелях, ' \
                                   'але клан стає ціллю для рейдерів.\n'
                    building += '\U0001F3ED Інфраструктура:'
                    resources = f"\n\nРесурси:\n\U0001F4B5 Гривні: {r.hget(c, 'money').decode()}" \
                                f"\n\U0001F333 Деревина: {r.hget(c, 'wood').decode()} / 15000" \
                                f"\n\U0001faa8 Камінь: {r.hget(c, 'stone').decode()} / 10000"
                    if int(r.hget(c, 'sawmill')) == 1:
                        building += ' пилорама'
                    if int(r.hget(c, 'mine')) == 1:
                        building += ', шахта'
                    if int(r.hget(c, 'craft')) == 1:
                        building += ', цех'
                    if int(r.hget(c, 'storage')) == 1:
                        building += ', склад'
                        resources += f"\n\U0001F9F6 Тканина: {r.hget(c, 'cloth').decode()} / 5000"
                        if base >= 3:
                            resources += f"\n\U0001F9F1 Цегла: {r.hget(c, 'brick').decode()} / 3000"
                            if int(r.hget(c, 'technics')) > 0:
                                resources += '\n\U0001F4FB Радіотехніка: ' + r.hget(c, 'technics').decode()
                        if base > 4:
                            if int(r.hget(c, 'codes')) > 0:
                                resources += '\n\U0001F916 Секретні коди: ' + r.hget(c, 'codes').decode()
                        resources += '\n\U0001F47E Рускій дух: ' + r.hget(c, 'r_spirit').decode()

                    if int(r.hget(c, 'silicate')) == 1:
                        building += ', силікатний завод'
                    if int(r.hget(c, 'complex')) == 1:
                        building += ', житловий комплекс'
                        num += 25
                        if int(r.hget(c, 'build5')) == 3:
                            num += 10
                    if int(r.hget(c, 'shop')) == 1:
                        building += ', їдальня'
                    if int(r.hget(c, 'monument')) == 1:
                        building += ', монумент'
                    if int(r.hget(c, 'post')) == 1:
                        building += ', блокпост'
                    if int(r.hget(c, 'camp')) == 1:
                        building += ', концтабір'
                    if int(r.hget(c, 'morgue')) == 1:
                        building += ', морг'
                    if int(r.hget(c, 'new_post')) == 1:
                        building += ', відділення НП'
                    await message.answer(f"<i>{prefix[base]}</i> {title}\n\nЛідер: {leader}\nКількість учасників: "
                                         f"{r.scard('cl' + cid)} / {num}{wins}\n\n{building}{resources}",
                                         parse_mode='HTML')
            elif r.hexists(message.from_user.id, 'class') and int(r.hget(message.from_user.id, 'class')) == 27 and \
                    int(r.hget(c, 'money')) >= 20:
                if int(r.hget(message.from_user.id, 'fsb')) != datetime.now().day:
                    r.hset(message.from_user.id, 'fsb', datetime.now().day)
                    ran = choice([2, 1, 1, 1, 0])
                    if ran == 2:
                        await bot.send_message(message.from_user.id, 'Агент втервся в довіру до керівництва і випросив '
                                                                     'трохи грошей.\n\U0001F4B5 +20')
                        r.hincrby(message.from_user.id, 'money', 20)
                        r.hincrby(c, 'money', -20)
                    elif ran == 1:
                        await bot.send_message(message.from_user.id, 'Агент непомітно забрав собі кілька гривень.'
                                                                     '\n\U0001F4B5 +10')
                        r.hincrby(message.from_user.id, 'money', 10)
                        r.hincrby(c, 'money', -10)
                    else:
                        await message.reply('Агент ФСБ хотів вкрасти гроші з кланової скрабниці, але його помітили...'
                                            '\n\U0001fac0 -100')
                        r.hset(message.from_user.id, 'hp', 0)
    elif message.chat.id == -1001211933154:
        try:
            await bot.delete_message(message.chat.id, int(r.hget('soledar', 'clan')))
        except:
            pass
        msg = '\U0001F530 Тут можна знайти собі клан'
        for mem in r.smembers('recruitment'):
            c = 'c' + mem.decode()
            num1 = r.scard('cl' + mem.decode())
            num2 = 25
            cl = r.hmget(c, 'base', 'link', 'complex', 'build5', 'title')
            link = cl[1].decode()
            if int(cl[2]) == 1:
                num2 += 25
            if int(cl[3]) == 3:
                num2 += 10
            msg += f'\n\n<i>{prefix[int(cl[0])]}</i> <a href="{link}">{cl[4].decode()}</a>\nУчасники: {num1} / {num2}'
        if r.scard('recruitment') == 0:
            msg = '\U0001F530 На даний момент ніхто не шукає учасників в клан.'
        a = await bot.send_message(message.chat.id, msg, disable_web_page_preview=True, parse_mode='HTML')
        r.hset('soledar', 'clan', a.message_id)


@dp.message_handler(commands=['upgrade'])
async def upgrade(message):
    try:
        if str(message.from_user.id).encode() in r.smembers('cl' + str(message.chat.id)):
            c = 'c' + str(message.chat.id)
            base = int(r.hget(c, 'base'))
            if base == 1:
                await message.answer('\U0001F3D7 Покращення Банди до Клану коштує \U0001F333 100, '
                                     '\U0001faa8 20 і \U0001F4B5 120.')
                admins = []
                admins2 = await bot.get_chat_administrators(message.chat.id)
                for admin in admins2:
                    admins.append(admin.user.id)
                if int(r.hget(c, 'wood')) >= 100 and int(r.hget(c, 'stone')) >= 20 and int(r.hget(c, 'money')) >= 120 \
                        and message.from_user.id not in sudoers and message.from_user.id not in admins:
                    await message.answer('\U0001F3D7 Достатньо ресурсів для покращення, кличте адмінів.')
                elif int(r.hget(c, 'wood')) >= 100 and int(r.hget(c, 'stone')) >= 20 and \
                        int(r.hget(c, 'money')) >= 120:
                    if message.from_user.id in admins or message.from_user.id in sudoers:
                        r.hincrby(c, 'money', -120)
                        r.hincrby(c, 'wood', -100)
                        r.hincrby(c, 'stone', -20)
                        r.hset(c, 'base', 2)
                        await message.answer('\U0001F3D7 Покращено Банду до Клану.')
            elif base == 2:
                await message.answer('\U0001F3D7 Покращення Клану до Гільдії коштує \U0001F333 1000, '
                                     '\U0001faa8 600, \U0001F9F6 300, \U0001F47E 20 і \U0001F4B5 1500.')
                admins = []
                admins2 = await bot.get_chat_administrators(message.chat.id)
                for admin in admins2:
                    admins.append(admin.user.id)
                if int(r.hget(c, 'wood')) >= 1000 and int(r.hget(c, 'stone')) >= 600 \
                        and int(r.hget(c, 'cloth')) >= 300 and int(r.hget(c, 'money')) >= 1500 \
                        and int(r.hget(c, 'r_spirit')) >= 20 and message.from_user.id not in admins:
                    await message.answer('\U0001F3D7 Достатньо ресурсів для покращення, кличте адмінів.')
                if int(r.hget(c, 'wood')) >= 1000 and int(r.hget(c, 'stone')) >= 600 \
                        and int(r.hget(c, 'cloth')) >= 300 and int(r.hget(c, 'money')) >= 1500 \
                        and int(r.hget(c, 'r_spirit')) >= 20:
                    if message.from_user.id in admins:
                        r.hincrby(c, 'money', -1500)
                        r.hincrby(c, 'wood', -1000)
                        r.hincrby(c, 'stone', -600)
                        r.hincrby(c, 'cloth', -300)
                        r.hincrby(c, 'r_spirit', -20)
                        r.hset(c, 'base', 3)
                        await message.answer('\U0001F3D7 Покращено Клан до Гільдії.')
            elif base == 3:
                await message.answer('\U0001F3D7 Покращення Гільдії до Угруповання коштує '
                                     '\U0001F333 3000, \U0001faa8 1500, \U0001F9F6 800, \U0001F9F1 400, '
                                     '\U0001F47E 50 і \U0001F4B5 3000.')
                admins = []
                admins2 = await bot.get_chat_administrators(message.chat.id)
                for admin in admins2:
                    admins.append(admin.user.id)
                if int(r.hget(c, 'wood')) >= 3000 and int(r.hget(c, 'stone')) >= 1500 \
                        and int(r.hget(c, 'cloth')) >= 800 and int(r.hget(c, 'brick')) >= 400 \
                        and int(r.hget(c, 'money')) >= 3000 and int(r.hget(c, 'r_spirit')) >= 50 and \
                        message.from_user.id not in admins:
                    await message.answer('\U0001F3D7 Достатньо ресурсів для покращення, кличте адмінів.')
                if int(r.hget(c, 'wood')) >= 3000 and int(r.hget(c, 'stone')) >= 1500 \
                        and int(r.hget(c, 'cloth')) >= 800 and int(r.hget(c, 'brick')) >= 400 \
                        and int(r.hget(c, 'money')) >= 3000 and int(r.hget(c, 'r_spirit')) >= 50:
                    if message.from_user.id in admins:
                        r.hincrby(c, 'money', -3000)
                        r.hincrby(c, 'wood', -3000)
                        r.hincrby(c, 'stone', -1500)
                        r.hincrby(c, 'cloth', -800)
                        r.hincrby(c, 'brick', -400)
                        r.hincrby(c, 'r_spirit', -50)
                        r.hset(c, 'base', 4)
                        r.sadd('groupings', message.chat.id)
                        await message.answer('\U0001F3D7 Покращено Гільдію до Угруповання.')
            elif base == 4:
                msg = '\U0001F3D7 Покращення Угруповання до нового рівня коштує\n\U0001F333 6000, \U0001faa8 3000, ' \
                      '\U0001F9F6 1500, \U0001F9F1 1000, \U0001F4FB 100, \U0001F47E 100 і \U0001F4B5 5000.\n\nВам ' \
                      'доведеться зробити важливий вибір - обрати один з 4 варіантів розвитку.'
                markup = InlineKeyboardMarkup()
                if int(r.hget(c, 'wood')) >= 6000 and int(r.hget(c, 'stone')) >= 3000 \
                        and int(r.hget(c, 'cloth')) >= 1500 and int(r.hget(c, 'brick')) >= 1000 \
                        and int(r.hget(c, 'technics')) >= 100\
                        and int(r.hget(c, 'money')) >= 5000 and int(r.hget(c, 'r_spirit')) >= 100:
                    msg += '\n\nДостатньо ресурсів для покращення. Який шлях розвитку ви обираєте?\n\nНа даний' \
                           ' момент не можна вибрати організацію.'
                    markup.add(InlineKeyboardButton(text='Комуна', callback_data='clan_side_1'),
                               InlineKeyboardButton(text='Коаліція', callback_data='clan_side_2'))
                    markup.add(InlineKeyboardButton(text='Асоціація', callback_data='clan_side_3'),
                               InlineKeyboardButton(text='Організація', callback_data='clan_side_4'))
                await message.answer(msg, reply_markup=markup)
            elif 4 < base < 9:
                side1 = ['', 'Комуни', 'Коаліції', 'Асоціації', 'Організації']
                side2 = ['', 'Союзу', 'Ордену', 'Ліги', 'Корпорації']
                side3 = ['', 'Комуну', 'Коаліцію', 'Асоціацію', 'Організацію']
                side = int(r.hget(c, 'side'))

                await message.answer(f'\U0001F3D7 Покращення {side1[side]} до {side2[side]} коштує '
                                     f'\U0001F333 10000, \U0001faa8 5000, \U0001F9F6 3000, \U0001F9F1 2000, '
                                     f'\U0001F4FB 200, \U0001F47E 200, \U0001F916 5 і \U0001F4B5 5000.')
                admins = []
                admins2 = await bot.get_chat_administrators(message.chat.id)
                for admin in admins2:
                    admins.append(admin.user.id)
                if int(r.hget(c, 'wood')) >= 10000 and int(r.hget(c, 'stone')) >= 5000 \
                        and int(r.hget(c, 'cloth')) >= 3000 and int(r.hget(c, 'brick')) >= 2000 \
                        and int(r.hget(c, 'money')) >= 5000 and int(r.hget(c, 'r_spirit')) >= 200 and \
                        int(r.hget(c, 'technics')) >= 200 and int(r.hget(c, 'codes')) >= 5 and\
                        message.from_user.id not in admins:
                    await message.answer('\U0001F3D7 Достатньо ресурсів для покращення, кличте адмінів.')
                if int(r.hget(c, 'wood')) >= 10000 and int(r.hget(c, 'stone')) >= 5000 \
                        and int(r.hget(c, 'cloth')) >= 3000 and int(r.hget(c, 'brick')) >= 2000 \
                        and int(r.hget(c, 'money')) >= 5000 and int(r.hget(c, 'r_spirit')) >= 200 and \
                        int(r.hget(c, 'technics')) >= 200 and int(r.hget(c, 'codes')) >= 5:
                    if message.from_user.id in admins:
                        r.hincrby(c, 'money', -5000)
                        r.hincrby(c, 'wood', -10000)
                        r.hincrby(c, 'stone', -5000)
                        r.hincrby(c, 'cloth', -3000)
                        r.hincrby(c, 'brick', -2000)
                        r.hincrby(c, 'r_spirit', -200)
                        r.hincrby(c, 'technics', -200)
                        r.hincrby(c, 'codes', -5)

                        if side == 1:
                            r.hset(c, 'base', 9)
                        elif side == 2:
                            r.hset(c, 'base', 10)
                        elif side == 3:
                            r.hset(c, 'base', 11)
                        elif side == 4:
                            r.hset(c, 'base', 12)
                        await message.answer(f'\U0001F3D7 Покращено {side3[side]} до {side2[side]}.')
    except:
        pass


@dp.message_handler(commands=['build'])
async def build(message):
    try:
        admins = []
        admins2 = await bot.get_chat_administrators(message.chat.id)
        for admin in admins2:
            admins.append(admin.user.id)
        if message.from_user.id in admins:
            if str(message.from_user.id).encode() in r.smembers('cl' + str(message.chat.id)):
                c = 'c' + str(message.chat.id)
                if int(r.hget(c, 'base')) >= 2:
                    msg = '\U0001F3D7 Для подальшого розвитку клану потрібно збудувати:\n'
                    markup = InlineKeyboardMarkup()
                    if int(r.hget(c, 'sawmill')) == 0:
                        markup.add(
                            InlineKeyboardButton(text='Побудувати пилораму', callback_data='build_sawmill'))
                        msg += '\nПилорама (\U0001F4B5 200) - \U0001F333 5-15 від роботи.'
                    if int(r.hget(c, 'mine')) == 0:
                        markup.add(InlineKeyboardButton(text='Побудувати шахту', callback_data='build_mine'))
                        msg += '\nШахта (\U0001F4B5 300) - \U0001faa8 2-10 від роботи.'
                    if int(r.hget(c, 'craft')) == 0:
                        markup.add(InlineKeyboardButton(text='Побудувати цех', callback_data='build_craft'))
                        msg += '\nЦех (\U0001F333 300, \U0001faa8 200, \U0001F4B5 100) - \U0001F9F6 2-5 від роботи.'
                    if int(r.hget(c, 'storage')) == 0:
                        markup.add(InlineKeyboardButton(text='Побудувати склад', callback_data='build_storage'))
                        msg += '\nСклад (\U0001F333 200, \U0001faa8 100) - доступ до всіх видів ресурсів.'
                    if int(r.hget(c, 'base')) >= 3:
                        if int(r.hget(c, 'silicate')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати силікатний завод',
                                                            callback_data='build_silicate'))
                            msg += '\nСилікатний завод (\U0001F333 1050, \U0001faa8 750, \U0001F9F6 200, ' \
                                   '\U0001F4B5 2000) - \U0001F9F1 1-3 від роботи.'
                        if int(r.hget(c, 'complex')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати житловий комплекс',
                                                            callback_data='build_complex'))
                            msg += '\nЖитловий комплекс (\U0001F333 500, \U0001faa8 500, \U0001F9F6 500, ' \
                                   '\U0001F9F1 50, \U0001F4B5 500) - розширення максимальної кількості учасників ' \
                                   'з 25 до 50.'
                        if int(r.hget(c, 'shop')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати магазин',
                                                            callback_data='build_shop'))
                            msg += '\nЇдальня (\U0001F333 1000, \U0001faa8 200, \U0001F9F6 400, ' \
                                   '\U0001F9F1 40, \U0001F4B5 300) - доступ до команди /clan_shop. Кілька товарів, ' \
                                   'що збільшують бойовий дух русаків.'
                        if int(r.hget(c, 'monument')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати монумент',
                                                            callback_data='build_monument'))
                            msg += '\nМонумент (\U0001F333 100, \U0001faa8 1000, \U0001F9F6 50, ' \
                                   '\U0001F9F1 100, \U0001F4B5 2000, \U0001F47E 50) - можливість для лідера у \n' \
                                   '/clan_shop витрачати \U0001F47E.'
                    if int(r.hget(c, 'base')) >= 4:
                        if int(r.hget(c, 'post')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати блокпост',
                                                            callback_data='build_post'))
                            msg += '\nБлокпост (\U0001F333 200, \U0001faa8 200, \U0001F9F6 200, ' \
                                   '\U0001F9F1 200, \U0001F4B5 200) - можливість захищатись від рейдів.'
                        if int(r.hget(c, 'camp')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати концтабір',
                                                            callback_data='build_camp'))
                            msg += '\nКонцтабір (\U0001F333 3000, \U0001faa8 1000, \U0001F9F6 1000, ' \
                                   '\U0001F9F1 400, \U0001F4B5 3000, \U0001F47E 100) - вдвічі більше ресурсів від ' \
                                   'роботи, якщо є другий русак.'
                        if int(r.hget(c, 'morgue')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати морг',
                                                            callback_data='build_morgue'))
                            msg += '\nМорг (\U0001F333 1000, \U0001faa8 2000, \U0001F9F6 800, ' \
                                   '\U0001F9F1 500, \U0001F4B5 5000, \U0001F47E 100) - +0.2% сили в міжчатовій битві ' \
                                   'за кожного вбитого русака (максимум 20%). \U0001F47E +1 за кожне жертвоприношення.'
                        if int(r.hget(c, 'new_post')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати відділення НП',
                                                            callback_data='build_new_post'))
                            msg += '\nВідділення НП (\U0001F333 800, \U0001faa8 500, \U0001F9F6 500, ' \
                                   '\U0001F9F1 200, \U0001F4B5 2000, \U0001F47E 30) - можливість отримувати ' \
                                   '\U0001F4FB радіотехніку з пакунків. При включеній зарплаті, за роботу ' \
                                   'видаватиметься \U0001F4E6 пакунок (але +2грн податку).'
                    if int(r.hget(c, 'base')) in (5, 9):
                        if int(r.hget(c, 'build1')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати тракторний завод',
                                                            callback_data='build1'))
                            msg += '\nТракторний завод (\U0001F333 4000, \U0001faa8 2000, \U0001F9F6 750, ' \
                                   '\U0001F9F1 500, \U0001F4B5 4000 \U0001F4FB 50, \U0001F47E 50) - можливість ' \
                                   'купувати уламки бронетехніки та зміцнювати ними захист до 50.'
                        if int(r.hget(c, 'build2')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати пивний ларьок',
                                                            callback_data='build2'))
                            msg += '\nПивний ларьок (\U0001F333 3000, \U0001faa8 500, \U0001F9F6 500, ' \
                                   '\U0001F9F1 300, \U0001F4B5 1000, \U0001F47E 50) - вдвічі більше ресурсів від ' \
                                   'роботи для роботяг.'
                        if int(r.hget(c, 'build3')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати падік',
                                                            callback_data='build3'))
                            msg += '\nПадік (\U0001F333 1000, \U0001faa8 1000, \U0001F9F6 500, ' \
                                   '\U0001F9F1 400, \U0001F4B5 2000) - здібність гопніка буде працювати, якщо на ' \
                                   'рахунку менше 200 гривень.'
                        if int(r.hget(c, 'build4')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати тюрму',
                                                            callback_data='build4'))
                            msg += '\nТюрма (\U0001F333 2000, \U0001faa8 1000, \U0001F9F6 500, ' \
                                   '\U0001F9F1 400, \U0001F4B5 2000, \U0001F4FB 200) - бонус сили для мусорів при ' \
                                   'захисті від рейдів збільшується до 100%.'
                    if int(r.hget(c, 'base')) in (6, 10):
                        if int(r.hget(c, 'build1')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати штаб тероборони',
                                                            callback_data='build1'))
                            msg += '\nШтаб тероборони (\U0001F333 4000, \U0001faa8 2000, \U0001F9F6 750, ' \
                                   '\U0001F9F1 500, \U0001F4B5 4000 \U0001F4FB 50, \U0001F47E 50) - можливість ' \
                                   'купувати шоломи та міни, зберігає 33% ресурсів від ворожих рейдерів.'
                        if int(r.hget(c, 'build2')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати березову рощу',
                                                            callback_data='build2'))
                            msg += '\nБерезова роща (\U0001F333 3000, \U0001faa8 500, \U0001F9F6 500, ' \
                                   '\U0001F9F1 300, \U0001F4B5 1000, \U0001F47E 50) - якщо язичник застосує сокиру ' \
                                   'Перуна проти язичника - обидва отримають 10000 бойового духу.'
                        if int(r.hget(c, 'build3')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати генеральську дачу',
                                                            callback_data='build3'))
                            msg += '\nГенеральська дача (\U0001F333 1000, \U0001faa8 1000, \U0001F9F6 500, ' \
                                   '\U0001F9F1 400, \U0001F4B5 2000) - присутність генерала в міжчатовій битві ' \
                                   'додатково принесе 1 рускій дух за перемогу.'
                        if int(r.hget(c, 'build4')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати казарму',
                                                            callback_data='build4'))
                            msg += '\nКазарма (\U0001F333 2000, \U0001faa8 1000, \U0001F9F6 500, ' \
                                   '\U0001F9F1 400, \U0001F4B5 2000, \U0001F4FB 200) - +20% сили гарматному м`ясу в ' \
                                   'міжчатових битвах.'
                    if int(r.hget(c, 'base')) in (7, 11):
                        if int(r.hget(c, 'build1')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати dungeon',
                                                            callback_data='build1'))
                            msg += '\nDungeon (\U0001F333 4000, \U0001faa8 2000, \U0001F9F6 750, ' \
                                   '\U0001F9F1 500, \U0001F4B5 4000 \U0001F4FB 50, \U0001F47E 50) - можливість ' \
                                   'купувати батіг.'
                        if int(r.hget(c, 'build2')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати бійцівський клуб',
                                                            callback_data='build2'))
                            msg += '\nБійцівський клуб (\U0001F333 3000, \U0001faa8 500, \U0001F9F6 500, ' \
                                   '\U0001F9F1 300, \U0001F4B5 1000, \U0001F47E 50) - втричі більший шанс кинути ' \
                                   'прогином хачам.'
                        if int(r.hget(c, 'build3')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати циганський табір',
                                                            callback_data='build3'))
                            msg += '\nЦиганський табір (\U0001F333 1000, \U0001faa8 1000, \U0001F9F6 500, ' \
                                   '\U0001F9F1 400, \U0001F4B5 2000) - 20% шанс фокусникам вкрасти нагороду ворога в ' \
                                   'дуелях.'
                        if int(r.hget(c, 'build4')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати радіовежу',
                                                            callback_data='build4'))
                            msg += '\nРадіовежа (\U0001F333 2000, \U0001faa8 1000, \U0001F9F6 500, ' \
                                   '\U0001F9F1 400, \U0001F4B5 2000, \U0001F4FB 200) - малорос в міжчатовій битві ' \
                                   'надсилає 3 шизофренії випадковому ворогу.'
                    if int(r.hget(c, 'base')) in (8, 12):
                        if int(r.hget(c, 'build1')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати біолабораторію',
                                                            callback_data='build1'))
                            msg += '\nБіолабораторія (\U0001F333 4000, \U0001faa8 2000, \U0001F9F6 750, ' \
                                   '\U0001F9F1 500, \U0001F4B5 4000 \U0001F4FB 50, \U0001F47E 50) - можливість ' \
                                   'купувати королівські мухомори (тим, в кого русак має до 20 інтелекту).'
                        if int(r.hget(c, 'build2')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати аптеку',
                                                            callback_data='build2'))
                            msg += '\nАптека (\U0001F333 3000, \U0001faa8 500, \U0001F9F6 500, ' \
                                   '\U0001F9F1 300, \U0001F4B5 1000, \U0001F47E 50) - патологоанатом з аптечкою ' \
                                   'отримуватиме по 10 гривень за воскрешання русаків.'
                        if int(r.hget(c, 'build3')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати АЗС',
                                                            callback_data='build3'))
                            msg += '\nАЗС (\U0001F333 1000, \U0001faa8 1000, \U0001F9F6 500, ' \
                                   '\U0001F9F1 400, \U0001F4B5 2000) - дизель в клановому магазині для таксистів.'
                        if int(r.hget(c, 'build4')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати дата-центр',
                                                            callback_data='build4'))
                            msg += '\nДата-центр (\U0001F333 2000, \U0001faa8 1000, \U0001F9F6 500, ' \
                                   '\U0001F9F1 400, \U0001F4B5 2000, \U0001F4FB 200) - здібність хакера надсилатиме ' \
                                   'стільки ж грошей в скарбницю клану.'
                    if int(r.hget(c, 'base')) == 9:
                        if int(r.hget(c, 'build5')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати воєнкомат',
                                                            callback_data='build5'))
                            msg += '\nВоєнкомат (\U0001F333 2000, \U0001faa8 1000, \U0001F9F6 800, ' \
                                   '\U0001F9F1 500, \U0001F4B5 6000 \U0001F4FB 100) - можливість ' \
                                   'купувати АК-47 та вушанки, або отримати їх безплатно за охорону.'
                        if int(r.hget(c, 'build6')) == 0 and int(r.hget(c, 'build1')) > 0 \
                                and int(r.hget(c, 'build2')) > 0 and int(r.hget(c, 'build3')) > 0 \
                                and int(r.hget(c, 'build4')) > 0 and int(r.hget(c, 'build5')) > 0:
                            markup.add(InlineKeyboardButton(text='Побудувати гулаг',
                                                            callback_data='build6'))
                            msg += '\nГулаг (\U0001F333 15000, \U0001faa8 10000, \U0001F9F6 5000, ' \
                                   '\U0001F9F1 3000, \U0001F4B5 10000, \U0001F4FB 300, \U0001F47E 300, \U0001F916 10)' \
                                   ' - якщо хтось покидає клан - його русаки втрачають по 20% сили. Шанс отримати ' \
                                   'додаткове годування після відпрацювання зміни - 1% за кожну тисячу деревини, ' \
                                   'каменю, тканини і цегли на складі.'
                    if int(r.hget(c, 'base')) == 10:
                        if int(r.hget(c, 'build5')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати ферму',
                                                            callback_data='build5'))
                            msg += '\nФерма (\U0001F333 2000, \U0001faa8 1000, \U0001F9F6 800, ' \
                                   '\U0001F9F1 500, \U0001F4B5 6000 \U0001F4FB 100) - годування русака лікує до ' \
                                   '30 поранень. Можливість зберегти кавун ще на 1 годування.'
                        if int(r.hget(c, 'build6')) == 0 and int(r.hget(c, 'build1')) > 0 \
                                and int(r.hget(c, 'build2')) > 0 and int(r.hget(c, 'build3')) > 0 \
                                and int(r.hget(c, 'build4')) > 0 and int(r.hget(c, 'build5')) > 0:
                            markup.add(InlineKeyboardButton(text='Побудувати ядерний бункер',
                                                            callback_data='build6'))
                            msg += '\nЯдерний бункер (\U0001F333 15000, \U0001faa8 10000, \U0001F9F6 5000, ' \
                                   '\U0001F9F1 3000, \U0001F4B5 10000, \U0001F4FB 300, \U0001F47E 300, \U0001F916 10)' \
                                   ' - Шизофренія не впливатиме негативно на міжчатові битви та рейди, а навпаки - ' \
                                   'додаватиме 5 інтелекту. Можливість купляти шапочки з фольги.'
                    if int(r.hget(c, 'base')) == 11:
                        if int(r.hget(c, 'build5')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати готель',
                                                            callback_data='build5'))
                            msg += '\nГотель (\U0001F333 2000, \U0001faa8 1000, \U0001F9F6 800, ' \
                                   '\U0001F9F1 500, \U0001F4B5 6000 \U0001F4FB 100) - максимальна кількість ' \
                                   'учасників збільшується на 10. Можливість вступити в клан без обмежень в часі.'
                        if int(r.hget(c, 'build6')) == 0 and int(r.hget(c, 'build1')) > 0 \
                                and int(r.hget(c, 'build2')) > 0 and int(r.hget(c, 'build3')) > 0 \
                                and int(r.hget(c, 'build4')) > 0 and int(r.hget(c, 'build5')) > 0:
                            markup.add(InlineKeyboardButton(text='Побудувати офіс Червоного Хреста',
                                                            callback_data='build6'))
                            msg += '\nОфіс Червоного Хреста (\U0001F333 15000, \U0001faa8 10000, \U0001F9F6 5000, ' \
                                   '\U0001F9F1 3000, \U0001F4B5 10000, \U0001F4FB 300, \U0001F47E 300, \U0001F916 10)' \
                                   ' - можливість лікувати весь клан, та проводити перерозподіл багатств - за 500 ' \
                                   'гривень з скарбниці по 100 гривень 5 найбіднішим учасникам.'
                    if int(r.hget(c, 'base')) == 12:
                        if int(r.hget(c, 'build5')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати торговий центр',
                                                            callback_data='build5'))
                            msg += '\nТорговий центр (\U0001F333 2000, \U0001faa8 1000, \U0001F9F6 800, ' \
                                   '\U0001F9F1 500, \U0001F4B5 6000 \U0001F4FB 100) - можливість ' \
                                   'купувати Цукор (при годуванні збільшує силу, або зменшує шанс її зменшення) та ' \
                                   'Кавун базований для всього клану (+5 сили за годування і +5 гривень за роботу ' \
                                   'на соляній шахті, зникне, якщо сила зменшиться).'
                        if int(r.hget(c, 'build6')) == 0 and int(r.hget(c, 'build1')) > 0 \
                                and int(r.hget(c, 'build2')) > 0 and int(r.hget(c, 'build3')) > 0 \
                                and int(r.hget(c, 'build4')) > 0 and int(r.hget(c, 'build5')) > 0:
                            markup.add(InlineKeyboardButton(text='Побудувати невільничий ринок',
                                                            callback_data='build6'))
                            msg += '\nНевільничий ринок (\U0001F333 15000, \U0001faa8 10000, \U0001F9F6 5000, ' \
                                   '\U0001F9F1 3000, \U0001F4B5 10000, \U0001F4FB 300, \U0001F47E 300, \U0001F916 10)' \
                                   ' - можливість купувати російських немовлят. Нові русаки з`являтимуться з 500+ сили.'
                    if len(markup.inline_keyboard) == 0:
                        msg = '\U0001F3D7 Більше нічого будувати...'
                    await message.reply(msg, reply_markup=markup)
    except:
        pass


@dp.message_handler(commands=['clan_shop'])
async def clan_shop(message):
    try:
        if str(message.from_user.id).encode() in r.smembers('cl' + str(message.chat.id)):
            c = 'c' + str(message.chat.id)
            if int(r.hget(c, 'shop')) == 1:
                msg, markup = c_shop(c, 1)
                await message.answer(msg, reply_markup=markup)
    except:
        pass


@dp.message_handler(commands=['clan_settings'])
async def clan_settings(message):
    try:
        c = 'c' + r.hget(message.from_user.id, 'clan').decode()
        msg = 'Які налаштування бажаєте змінити?\n\nНазва: ' + r.hget(c, 'title').decode()
        if message.chat.type != 'private':
            try:
                await bot.delete_message(message.chat.id, message.message_id)
            except:
                pass
        if checkLeader(message.from_user.id, int(r.hget(message.from_user.id, 'clan'))) or \
                message.from_user.id in sudoers:
            if int(r.hget(c, 'allow')) == 0:
                msg += '\n\nВ клан може приєднатись кожен бажаючий.'
            else:
                msg += '\n\nВ клан можна приєднатись тільки з дозволу адміністраторів.'
            if int(r.hget(c, 'war_allow')) == 0:
                msg += '\n\nВ міжчатову битву може зайти кожен бажаючий.'
            else:
                msg += '\n\nВ міжчатову битву в перші 5 хвилин може зайти тільки учасник клану.'
            if int(r.hget(c, 'salary')) == 0:
                msg += '\n\nЗа роботу не видається зарплата з кланових ресурсів.'
            else:
                msg += '\n\nЗа роботу з рахунку клану зніматиметься 8 гривень: 5 гривень робітнику, 3 - податок.'
            if int(r.hget(c, 'recruitment')) == 0:
                msg += '\n\nВ Соледарі не відкрито набір в клан.'
            else:
                msg += '\n\nВ Соледарі відкрито набір в клан.'
            await bot.send_message(message.from_user.id, msg, reply_markup=clan_set())
    except:
        pass


@dp.message_handler(commands=['join'])
async def join(message):
    c = 'c' + str(message.chat.id)
    num = 25
    ts = 604800
    cid = message.chat.id
    if r.hexists(message.from_user.id, 'clan_ts') == 0:
        r.hset(message.from_user.id, 'clan_ts', 0)
    try:
        if int(r.hget(c, 'base')) > 0 and len(str(r.hget(message.from_user.id, 'clan'))) < 5:
            if int(r.hget(c, 'complex')) >= 1:
                num += 25
            if int(r.hget(c, 'build5')) == 3:
                num += 10
                ts = 0
            if int(datetime.now().timestamp()) - int(r.hget(message.from_user.id, 'clan_ts')) > ts or \
                    message.from_user.id in sudoers:
                if r.scard('cl' + str(message.chat.id)) < num:
                    if int(r.hget(c, 'allow')) == 0 or message.from_user.id in sudoers:
                        r.hset(message.from_user.id, 'clan', cid, {'clan_ts': int(datetime.now().timestamp())})
                        if r.hexists(message.from_user.id, 'clan_time') == 0:
                            r.hset(message.from_user.id, 'clan_time', 0)
                        r.sadd('cl' + str(message.chat.id), message.from_user.id)
                        r.hset(message.from_user.id, 'firstname', message.from_user.first_name)
                        await message.reply('\U0001F4E5 Ти вступив в клан ' +
                                            r.hget('c' + str(message.chat.id), 'title').decode() + '.')
                    elif int(r.hget(c, 'allow')) == 1:
                        await message.reply('\U0001F4E5 Прийняти в клан ' + message.from_user.first_name + '?',
                                            reply_markup=invite())
                else:
                    await message.reply('\U0001F4E5 Неможливо вступити в клан, оскільки він переповнений.')
            else:
                await message.reply('\U0001F4E5 Вступати в клан можна лише раз в тиждень.')
    except Exception as e:
        print(e)


@dp.message_handler(commands=['invest'])
async def invest(message):
    try:
        if str(message.from_user.id).encode() in r.smembers('cl' + str(message.chat.id)):
            c = 'c' + str(message.chat.id)
            if message.text == '/invest':
                await message.reply('\U0001F4B5 Щоб інвестувати гроші в клан напиши після команди кількість.\n'
                                    'Наприклад: /invest 50')
            else:
                m = int(message.text.split(' ')[1])
                if m > 0:
                    if m <= int(r.hget(message.from_user.id, 'money')):
                        r.hincrby(c, 'money', m)
                        r.hincrby(message.from_user.id, 'money', -m)
                        msg = f'\U0001F4B5 Клановий рахунок поповнено на {m} гривень.'
                        if m >= 500:
                            if r.hexists(message.from_user.id, 'ac15') == 0:
                                r.hset(message.from_user.id, 'ac15', 1)
                        if m >= 1000 and int(r.hget(c, 'base')) == 12:
                            p = int(m / 20)
                            r.hincrby(message.from_user.id, 'packs', p)
                            msg += f'\n\U0001F4E6 +{p}'
                        await message.reply(msg)
                    else:
                        await message.reply('Недостатньо коштів на рахунку.')

    except:
        pass


@dp.message_handler(commands=['kick'])
async def kick(message):
    try:
        if checkLeader(message.from_user.id, message.chat.id):
            if message.chat.id == int(r.hget(message.from_user.id, 'clan')) or message.chat.type == 'private':
                uid = int(message.text.split(' ')[1])
                if str(uid).encode() in r.smembers('cl' + str(message.chat.id)) \
                        and not checkLeader(uid, message.chat.id):
                    r.hset(uid, 'clan', 0)
                    r.srem('cl' + str(message.chat.id), uid)
                    await message.reply('\u2705')
    except:
        pass


@dp.message_handler(commands=['promote'])
async def promote(message):
    try:
        cid = str(message.chat.id)
        if message.from_user.id == int(r.hget('c' + cid, 'leader')):
            if message.chat.id == int(r.hget(message.from_user.id, 'clan')):
                uid = str(message.reply_to_message.from_user.id).encode()
                if uid in r.smembers('cl' + cid) and uid not in r.smembers('cl2' + cid) and \
                        message.reply_to_message.from_user.id != int(r.hget('c' + cid, 'leader')):
                    r.sadd('cl2' + cid, uid)
                    await message.reply('\u2705')
    except:
        pass


@dp.message_handler(commands=['demote'])
async def demote(message):
    try:
        cid = str(message.chat.id)
        if message.from_user.id == int(r.hget('c' + cid, 'leader')):
            if message.chat.id == int(r.hget(message.from_user.id, 'clan')):
                uid = str(message.reply_to_message.from_user.id).encode()
                if uid in r.smembers('cl2' + cid):
                    r.srem('cl2' + cid, uid)
                    await message.reply('\u2705')
    except:
        pass


@dp.message_handler(commands=['leave'])
async def leave(message):
    if checkClan(message.from_user.id):
        if message.chat.id == int(r.hget(message.from_user.id, 'clan')) or message.chat.type == 'private':
            markup = InlineKeyboardMarkup()
            await message.reply('\U0001F4E4 Покинути клан?', reply_markup=markup.add(InlineKeyboardButton(
                text='Так', callback_data='leave_from_clan')))


@dp.message_handler(commands=['work'])
async def work(message):
    try:
        c = 'c' + str(message.chat.id)
        name = names[int(r.hget(message.from_user.id, 'name'))]
        if int(r.hget(message.from_user.id, 'clan')) == message.chat.id:
            if int(r.hget(message.from_user.id, 'clan_time')) != datetime.now().day:
                resources = ''
                base = int(r.hget(c, 'base'))
                if base == 1:
                    if int(r.hget(message.from_user.id, 'support')) != 3 and \
                            int(r.hget(message.from_user.id, 'support')) != 4:
                        await message.reply('\u26CF Банді потрібна деревина і камінь.\nЗбігати в магазин за '
                                            'інструментами?\n\nСокира [Допомога, міцність=3, ціна=5]  1-10 дере'
                                            'вини в день.\nКайло [Допомога, міцність=3, ціна=10] 1-5 каміння в день.',
                                            reply_markup=buy_tools())
                    elif int(r.hget(message.from_user.id, 'support')) == 3 or \
                            int(r.hget(message.from_user.id, 'support')) == 4:
                        r.hset(message.from_user.id, 'clan_time', datetime.now().day)
                        if int(r.hget(message.from_user.id, 'support')) == 3:
                            ran = randint(1, 5)
                            resources += '\U0001F333 +' + str(ran)
                            wood(c, ran)
                        elif int(r.hget(message.from_user.id, 'support')) == 4:
                            ran = randint(1, 5)
                            resources += '\U0001faa8 +' + str(ran)
                            stone(c, ran)
                        if int(r.hget(c, 'salary')) == 1 and int(r.hget(c, 'money')) >= 8:
                            resources += ' \U0001F4B5 +5'
                            r.hincrby(c, 'money', -8)
                            r.hincrby(message.from_user.id, 'money', 5)
                            r.hincrby('soledar', 'money', 3)
                        damage_support(message.from_user.id)
                        await message.reply(name + ' попрацював на благо громади.\n' + resources)
                elif base >= 2:
                    if int(r.hget(c, 'sawmill')) == 0 and int(r.hget(c, 'mine')) == 0 and int(r.hget(c, 'craft')) == 0:
                        await message.reply('Зберіть гроші, щоб побудувати пилораму і шахту.\n\n/build')
                    else:
                        r.hset(message.from_user.id, 'clan_time', datetime.now().day)
                        camp = 0
                        packs = int(r.hget(message.from_user.id, 'packs'))
                        side = int(r.hget(c, 'side'))
                        cl = int(r.hget(message.from_user.id, 'class'))
                        worker = 2 if cl in (2, 12, 22) and int(r.hget(c, 'build2')) == 1 else 1
                        trucker = 1
                        if cl in (32, 33) and packs > 0:
                            if packs > 40:
                                packs = 40
                            trucker += packs * 0.03
                        if int(r.hget(c, 'camp')) == 1:
                            if r.hexists(message.from_user.id, 'name2') == 1:
                                camp = 1
                        if int(r.hget(c, 'sawmill')) == 1:
                            ran = 15 if side == 1 else randint(5, 15)
                            if camp == 1:
                                ran *= 2
                            ran = int(ran * trucker) * worker
                            resources += '\U0001F333 +' + str(ran)
                            wood(c, ran)
                        if int(r.hget(c, 'mine')) == 1:
                            ran = 10 if side == 1 else randint(2, 10)
                            if camp == 1:
                                ran *= 2
                            ran = int(ran * trucker) * worker
                            resources += ' \U0001faa8 +' + str(ran)
                            stone(c, ran)
                        if int(r.hget(c, 'craft')) == 1:
                            ran = 5 if side == 1 else randint(2, 5)
                            if camp == 1:
                                ran *= 2
                            ran = int(ran * trucker) * worker
                            resources += ' \U0001F9F6 +' + str(ran)
                            cloth(c, ran)
                        if int(r.hget(c, 'silicate')) == 1:
                            ran = 3 if side == 1 else randint(1, 3)
                            if camp == 1:
                                ran *= 2
                            ran = int(ran * trucker) * worker
                            resources += ' \U0001F9F1 +' + str(ran)
                            brick(c, ran)
                        if int(r.hget(c, 'salary')) == 1 and int(r.hget(c, 'money')) >= 10:
                            if side == 4:
                                if int(r.hget(c, 'new_post')) == 0:
                                    resources += ' \n\U0001F4B5 +8'
                                    r.hincrby(message.from_user.id, 'money', 8)
                                    r.hincrby(c, 'money', -8)
                                else:
                                    r.hincrby(message.from_user.id, 'money', 10)
                                    r.hincrby(c, 'money', -10)
                                    resources += ' \n\U0001F4B5 +10 \U0001F4E6 +1'
                                    r.hincrby(message.from_user.id, 'packs', 1)
                            else:
                                resources += ' \n\U0001F4B5 +5'
                                r.hincrby(message.from_user.id, 'money', 5)
                                if int(r.hget(c, 'new_post')) == 0:
                                    r.hincrby(c, 'money', -8)
                                    r.hincrby('soledar', 'money', 3)
                                else:
                                    r.hincrby(c, 'money', -10)
                                    r.hincrby('soledar', 'money', 5)
                                    resources += ' \U0001F4E6 +1'
                                    r.hincrby(message.from_user.id, 'packs', 1)
                        if int(r.hget(c, 'build6')) == 1:
                            ch = int(r.hget(c, 'wood')) + int(r.hget(c, 'stone')) + \
                                 int(r.hget(c, 'cloth')) + int(r.hget(c, 'brick'))
                            if choices([1, 0], [int(ch / 1000), 100 - int(ch / 1000)]) == [1]:
                                r.hset(message.from_user.id, 'time', 0)
                                resources += ' \U0001F372 +1'
                        if cl == 36 and side == 1 and choices([1, 0], [20, 80]) == [1]:
                            resources += '\n\U0001F916 +1'
                            r.hincrby(c, 'codes', 1)
                            
                        await message.reply(name + ' попрацював на благо громади.\n' + resources)
            else:
                await message.reply('Твій русак сьогодні вже своє відпрацював.')
    except:
        pass


@dp.message_handler(commands=['guard'])
async def guard(message):
    try:
        mid = message.from_user.id
        c = 'c' + str(message.chat.id)
        g = 'guard' + str(message.chat.id)
        if int(r.hget(c, 'day')) != datetime.now().day:
            r.hset(c, 'day', datetime.now().day)
            r.hset(c, 'power', 0)
            for m in r.smembers(g):
                r.srem(g, m)
        if checkClan(mid, base=4, building='post') and r.hexists(mid, 'name') == 1 and \
                int(r.hget(message.from_user.id, 'clan')) == message.chat.id:
            if int(r.hget(mid, 'clan_time')) != datetime.now().day and r.scard(g) < 5:
                r.hset(mid, 'clan_time', datetime.now().day)
                if int(r.hget(c, 'build5')) == 1:
                    if int(r.hget(mid, 'weapon')) == 0:
                        r.hset(mid, 'weapon', 15, {'s_weapon': 30})
                    if int(r.hget(mid, 'head')) == 0:
                        r.hset(mid, 'head', 4, {'s_head': 20})
                st = await guard_power(mid)
                if int(r.hget(c, 'base')) == 12:
                    st = int(st * (1 + 0.01 * int(int(r.hget(c, 'money')) / 1000)))
                r.hincrby(c, 'power', st)
                r.sadd(g, mid)
                name = names[int(r.hget(mid, 'name'))]
                msg = name + ' сьогодні охоронятиме територію від злодіїв.\n\n\U0001F4AA +' + str(st)
                if int(r.hget(c, 'salary')) == 1 and int(r.hget(c, 'money')) >= 10:
                    if int(r.hget(c, 'side')) == 4:
                        if int(r.hget(c, 'new_post')) == 0:
                            msg += ' \U0001F4B5 +8'
                            r.hincrby(message.from_user.id, 'money', 8)
                            r.hincrby(c, 'money', -8)
                        else:
                            msg += ' \U0001F4B5 +10'
                            r.hincrby(message.from_user.id, 'money', 10)
                            r.hincrby(c, 'money', -10)
                            msg += ' \U0001F4E6 +1'
                            r.hincrby(message.from_user.id, 'packs', 1)
                    else:
                        msg += ' \U0001F4B5 +5'
                        r.hincrby(message.from_user.id, 'money', 5)
                        if int(r.hget(c, 'new_post')) == 0:
                            r.hincrby(c, 'money', -8)
                            r.hincrby('soledar', 'money', 3)
                        else:
                            r.hincrby(c, 'money', -10)
                            r.hincrby('soledar', 'money', 5)
                            msg += ' \U0001F4E6 +1'
                            r.hincrby(message.from_user.id, 'packs', 1)
                if int(r.hget(mid, 'class')) == 36 and int(r.hget(c, 'side')) == 3:
                    if int(r.hget('convoy', 'day')) != datetime.now().day:
                        r.hset('convoy', 'power', 2000000)
                        r.hset('convoy', 'day', datetime.now().day)
                    r.hincrby('convoy', 'power', 500000)
                    msg += '\n\U0001F396 Генерал викликав додатковий гумконвой.'
                await message.reply(msg + '\n\U0001F4AA Загальна сила: ' + r.hget(c, 'power').decode() +
                                    '\n\U0001F5E1 Кількість сторожів: ' + str(r.scard(g)) + '/5')
            else:
                await message.reply('Твій русак сьогодні вже своє відпрацював.'
                                    '\n\n\U0001F4AA Загальна сила: ' + r.hget(c, 'power').decode() +
                                    '\n\U0001F5E1 Кількість сторожів: ' + str(r.scard(g)) + '/5')
    except:
        pass


@dp.message_handler(commands=['raid'])
async def raid(message):
    try:
        c = 'c' + str(message.chat.id)
        if int(r.hget(message.from_user.id, 'clan')) == message.chat.id:
            if message.chat.id == -100:
                await message.reply('Хватить на сьогодні рейдів.')
            elif 0 <= datetime.now().hour < 8:
                await message.reply('Комендантська година, рейди недоступні.')
            elif r.hexists(c, 'start') == 0:
                if r.hexists(c, 'raid_ts') == 0:
                    r.hset(c, 'raid_ts', 0)
                if r.hexists(c, 'raid_ts2') == 0:
                    r.hset(c, 'raid_ts2', 0)
                if int(datetime.now().timestamp()) - int(r.hget(c, 'raid_ts')) > 5:
                    r.hset(c, 'raid_ts', int(datetime.now().timestamp()))
                    if int(datetime.now().timestamp()) - int(r.hget(c, 'raid_ts2')) > 3600:
                        try:
                            try:
                                await bot.delete_message(message.chat.id, message.message_id)
                            except:
                                pass
                            a = await bot.send_message(message.chat.id, '\U0001F4B0 Починається рейд...\n\n',
                                                       reply_markup=battle_button_4())
                            r.hset(c, 'start', a.message_id)
                            r.hset(c, 'starter', message.from_user.id)
                            try:
                                await bot.pin_chat_message(a.chat.id, a.message_id, disable_notification=True)
                                r.hset(c, 'pin', a.message_id)
                            except:
                                pass
                        except:
                            pass
                    else:
                        t = str(int((3600 - int(datetime.now().timestamp()) + int(r.hget(c, 'raid_ts2'))) / 60))
                        await message.reply('Рейди можна проводити один раз в годину.\nЗалишилось ' + t + 'хв.')
            else:
                try:
                    await bot.send_message(message.chat.id, '\U0001F4B0 Підготовка до рейду тут\n\nКількість бійців: ' +
                                           str(r.scard('fighters_3' + str(message.chat.id))),
                                           reply_to_message_id=int(r.hget(c, 'start')))
                    try:
                        await bot.delete_message(message.chat.id, message.message_id)
                    except:
                        pass
                except:
                    try:
                        await bot.delete_message(message.chat.id, int(r.hget(c, 'start')))
                    except:
                        pass
                    r.hdel(c, 'start')
                    for mem in r.smembers('fighters_3' + str(message.chat.id)):
                        r.srem('fighters_3' + str(message.chat.id), mem)
                    try:
                        await bot.delete_message(message.chat.id, message.message_id)
                    except:
                        pass
    except:
        pass


@dp.message_handler(commands=['commands'])
async def commands(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Інформація', callback_data='full_list_1'))
    markup.add(InlineKeyboardButton(text='Гра в русаків', callback_data='full_list_2'))
    markup.add(InlineKeyboardButton(text='Топ', callback_data='full_list_3'),
               InlineKeyboardButton(text='Клани', callback_data='full_list_4'))
    markup.add(InlineKeyboardButton(text='Адміністраторські команди', callback_data='full_list_5'))
    await message.reply('/links - реклама, головний чат, творець\n'
                        '/wiki - інформація щодо гри\n'
                        '/feed - погодувати русака\n'
                        '/mine - заробити гривні (доступно тільки в '
                        '<a href="https://t.me/+cClR7rA-sZAyY2Uy">@soledar1</a>)\n'
                        '/woman - провідати жінку\n'
                        '/clan - інформація про клан\n'
                        '/achieve - досягнення\n'
                        '/skills - вміння\n'
                        '/i - інвентар\n'
                        '/battle - чатова битва (5-10 русаків)\n'
                        '/war - міжчатова битва 5х5\n'
                        '...', reply_markup=markup,
                        parse_mode='HTML', disable_web_page_preview=True)


@dp.message_handler(commands=['wiki'])
async def wiki(message):
    try:
        msg = '\U0001F1FA\U0001F1E6 @Random_UAbot - бот, який перенесе тебе в альтернативну реальність, у якій ти ' \
               'потрапляєш на Донбас і ловиш русаків.\nЇх можна розвивати, відправляти в бої проти інших ' \
               'русаків, об`єднувати в клани, а також - вбивати.\nТут можна знайти майже всю інформацію щодо гри.'
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='\U0001F5E1 Бої', callback_data='wiki_duel'),
                   InlineKeyboardButton(text='\U0001F4C8 Розвиток', callback_data='wiki_grow_feed'))
        markup.add(InlineKeyboardButton(text='\U0001F530 Клан', callback_data='wiki_clan'),
                   InlineKeyboardButton(text='\U0001F4DC Паспорт', callback_data='wiki_passport'))
        await bot.send_message(message.from_user.id, msg, reply_markup=markup)
        if message.chat.type != 'private':
            await message.reply('Надіслано в пп.')
    except:
        pass


@dp.callback_query_handler(lambda call: True)
async def handle_query(call):
    if call.data.startswith('getrusak') and call.from_user.id == call.message.reply_to_message.from_user.id:
        try:
            if r.hexists(call.from_user.id, 'name') == 1:
                await bot.edit_message_text(text='\U0001F98D У тебе вже є русак!',
                                            chat_id=call.message.chat.id, message_id=call.message.message_id)
            else:
                raise Exception
        except:
            cid = call.from_user.id
            n, s, i = get_rusak()
            if checkClan(cid, building='build6', level=4):
                s += 400
            r.hset(cid, 'name', n, {'strength': s, 'intellect': i, 'spirit': 0, 'class': 0, 'weapon': 0, 's_weapon': 0,
                                    'defense': 0, 's_defense': 0, 'support': 0, 's_support': 0, 'mushrooms': 0,
                                    'hp': 100, 'injure': 0, 'sch': 0, 'buff': 0, 'head': 0, 's_head': 0,
                                    'photo': choice(default), 'firstname': call.from_user.first_name})
            r.sadd('everyone', call.from_user.id)
            try:
                r.hset(call.from_user.id, 'username', call.from_user.username)
                if call.message.chat.type != 'private':
                    r.sadd(call.message.chat.id, call.from_user.id)
                    r.sadd(111, call.from_user.id)
            except:
                pass
            if r.hexists(call.from_user.id, 'time') == 0:
                r.hset(call.from_user.id, 'time', 0)
            if r.hexists(call.from_user.id, 'packs') == 0:
                r.hset(call.from_user.id, 'packs', 5)
            if r.hexists(call.from_user.id, 'money') == 0:
                r.hset(call.from_user.id, 'money', 20)
            if r.hexists(call.from_user.id, 'strap') == 0:
                r.hset(call.from_user.id, 'strap', 0)
            if r.hexists(call.from_user.id, 'opened') == 0:
                r.hset(call.from_user.id, 'opened', 0)
            if r.hexists(call.from_user.id, 'childs') == 0:
                r.hset(call.from_user.id, 'childs', 0)
            if r.hexists(call.from_user.id, 'deaths') == 0:
                r.hset(call.from_user.id, 'deaths', 0)
            if r.hexists(call.from_user.id, 'wins') == 0:
                r.hset(call.from_user.id, 'wins', 0)
            if r.hexists(call.from_user.id, 'trophy') == 0:
                r.hset(call.from_user.id, 'trophy', 0)
            if r.hexists(call.from_user.id, 'vodka') == 0:
                r.hset(call.from_user.id, 'vodka', 0)
            if r.hexists(call.from_user.id, 'eat') == 0:
                r.hset(call.from_user.id, 'eat', 0)
            if r.hexists(call.from_user.id, 's1') == 0:
                r.hset(call.from_user.id, 's1', 1)
            if r.hexists(call.from_user.id, 's2') == 0:
                r.hset(call.from_user.id, 's2', 1)
            if r.hexists(call.from_user.id, 's3') == 0:
                r.hset(call.from_user.id, 's3', 1)
            await bot.edit_message_text(text='\U0001F3DA Ти приходиш на Донбас - чудове місце для полювання на'
                                             ' русаків\n\n\U0001F412 Русака взято в полон...',
                                        chat_id=call.message.chat.id, message_id=call.message.message_id)

    elif call.data.startswith('fight') and r.hexists(call.from_user.id, 'name') == 1:
        cdata = call.data[5:].split(',', 3)
        uid1 = cdata[0]
        uid2 = call.from_user.id
        try:
            un1 = r.hget(uid1, 'firstname').decode()
        except:
            un1 = '...'
        timestamp = datetime.now().timestamp()
        if r.hexists(uid1, 'timestamp') == 0:
            r.hset(uid1, 'timestamp', 0)
        if timestamp - float(r.hget(uid1, 'timestamp')) < 0.5:
            pass
        else:
            r.hset(uid1, 'timestamp', timestamp)
            try:
                if r.hexists(uid1, 'name') == 1 and int(uid2) != int(uid1):
                    if int(r.hget(uid2, 'hp')) > 0:
                        if int(r.hget(uid1, 'hp')) > 0:
                            q = cdata[1].split()
                            diff = int(q[1])
                            if int(r.hget(uid1, 'strength')) - diff <= int(r.hget(uid2, 'strength')) <= \
                                    int(r.hget(uid1, 'strength')) + diff:
                                un2 = call.from_user.first_name
                                fi = await fight(uid1, uid2, un1, un2, 1, call.inline_message_id)
                                await bot.edit_message_text(text=fi,
                                                            inline_message_id=call.inline_message_id)
                            else:
                                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                text='Твій русак не підходить по силі для цього бою.')
                        else:
                            if int(r.hget(uid2, 'class')) == 29:
                                if int(r.hget(uid2, 'support')) == 1 and checkClan(uid2, building='build2', level=4):
                                    money = 10
                                else:
                                    money = 5
                                await bot.edit_message_text(
                                    text=f'\u26D1 {call.from_user.first_name} відправив свого русака надати медичну '
                                         f'допомогу пораненому.\n\U0001fac0 +20 \U0001F4B5 +{money}',
                                    inline_message_id=call.inline_message_id)
                                hp(20, uid1)
                                r.hincrby(call.from_user.id, 'money', money)
                            elif int(r.hget(call.from_user.id, 'class')) == 23:
                                await bot.edit_message_text(
                                    text='\U0001F52E ' + ' Некромант проводить дивні ритуали над напівживим русаком...'
                                                         '\n\U0001fac0 +10 \U0001F44A +5',
                                    inline_message_id=call.inline_message_id)
                                hp(10, uid1)
                                increase_trance(5, call.from_user.id)
                            else:
                                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                text='\U0001fac0 Зараз цей русак не може битись.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='\U0001fac0 Русак лежить весь в крові.\nВін не може '
                                                             'битись поки не поїсть, або не полікується.')
                elif r.hexists(uid1, 'name') == 0:
                    pass
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ти хочеш атакувати свого русака, але розумієш, що він зараз '
                                                         'має битись з іншими русаками.')
            except:
                try:
                    uid2 = call.from_user.id
                    un2 = call.from_user.first_name
                    if cdata[1] == 'tr':
                        if r.hexists(uid1, 't_ts') == 0:
                            r.hset(uid1, 't_ts', 0)
                        if timestamp - float(r.hget(uid1, 't_ts')) < 15:
                            pass
                        else:
                            r.hset(uid1, 't_ts', timestamp)
                            try:
                                q = cdata[2].split()
                                if q[1][1:].lower() == call.from_user.username.lower():
                                    await fight(uid1, uid2, un1, un2, 5, call.inline_message_id)
                                else:
                                    await bot.answer_callback_query(callback_query_id=call.id,
                                                                    show_alert=True, text='Цей бій не для тебе.')
                            except:
                                await fight(uid1, uid2, un1, un2, 5, call.inline_message_id)
                    elif cdata[1] == 'pr':
                        try:
                            q = cdata[2].split()
                            if q[1][1:].lower() == call.from_user.username.lower():
                                fi = await fight(uid1, uid2, un1, un2, 1, call.inline_message_id)
                                await bot.edit_message_text(text=fi, inline_message_id=call.inline_message_id)
                            else:
                                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                text='Цей бій не для тебе.')
                        except:
                            raise Exception
                    else:
                        raise Exception
                except:
                    uid2 = call.from_user.id
                    un2 = call.from_user.first_name
                    fi = await fight(uid1, uid2, un1, un2, 1, call.inline_message_id)
                    await bot.edit_message_text(text=fi, inline_message_id=call.inline_message_id)

    elif call.data.startswith('join') and r.hexists('battle' + str(call.message.chat.id), 'start') == 1:
        if str(call.from_user.id).encode() not in r.smembers('fighters' + str(call.message.chat.id)) and \
                r.hexists(call.from_user.id, 'name') == 1 and \
                call.message.message_id == int(r.hget('battle' + str(call.message.chat.id), 'start')):
            r.hset(call.from_user.id, 'firstname', call.from_user.first_name)
            r.sadd('fighters' + str(call.message.chat.id), call.from_user.id)
            fighters = r.scard('fighters' + str(call.message.chat.id))
            if fighters == 1:
                await bot.edit_message_text(
                    text=call.message.text + '\n\nБійці: ' + call.from_user.first_name, chat_id=call.message.chat.id,
                    message_id=call.message.message_id, reply_markup=battle_button())
            elif 5 <= fighters <= 9:
                await bot.edit_message_text(
                    text=call.message.text + ', ' + call.from_user.first_name, chat_id=call.message.chat.id,
                    message_id=call.message.message_id, reply_markup=battle_button_2())
            elif fighters >= 10:
                await bot.edit_message_text(
                    text=call.message.text + ', ' + call.from_user.first_name + '\n\nБій почався...',
                    chat_id=call.message.chat.id, message_id=call.message.message_id)
                ran = choice(['Битва в Соледарі', 'Битва на овечій фермі', 'Битва на покинутому заводі',
                              'Битва в темному лісі', 'Битва біля старого дуба', 'Битва в житловому районі',
                              'Битва біля поліцейського відділку', 'Битва в офісі ОПЗЖ',
                              'Битва в серверній кімнаті', 'Штурм Горлівки', 'Штурм ДАП', 'Битва в психлікарні',
                              'Висадка в Чорнобаївці', 'Битва в темному провулку', 'Битва біля розбитої колони',
                              'Розгром командного пункту'])
                big_battle = True
                try:
                    await bot.unpin_chat_message(chat_id=call.message.chat.id,
                                                 message_id=int(r.hget('battle' + str(call.message.chat.id), 'pin')))
                except:
                    pass
                await war(call.message.chat.id, ran, big_battle)
            else:
                await bot.edit_message_text(
                    text=call.message.text + ', ' + call.from_user.first_name, chat_id=call.message.chat.id,
                    message_id=call.message.message_id, reply_markup=battle_button())
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ти або вже в битві, або в тебе відсутній русак')

    elif call.data.startswith('start_battle') and r.hexists('battle' + str(call.message.chat.id), 'start') == 1:
        if call.from_user.id == int(r.hget('battle' + str(call.message.chat.id), 'starter')):
            await bot.edit_message_text(text=call.message.text + '\n\nБій почався...',
                                        chat_id=call.message.chat.id, message_id=call.message.message_id)
            ran = choice(['Битва в Соледарі', 'Штурм Горлівки', 'Штурм ДАП'])
            big_battle = False
            try:
                await bot.unpin_chat_message(chat_id=call.message.chat.id,
                                             message_id=int(r.hget('battle' + str(call.message.chat.id), 'pin')))
            except:
                pass
            await war(call.message.chat.id, ran, big_battle)
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Почати битву може тільки'
                                                                                             ' той, хто почав набір.')

    elif call.data.startswith('war_join') and r.hexists('war_battle' + str(call.message.chat.id), 'start') == 1:
        if str(call.from_user.id).encode() not in r.smembers('fighters_2' + str(call.message.chat.id)) and \
                r.hexists(call.from_user.id, 'name') == 1 and r.hexists(call.from_user.id, 'in_war') == 0 and \
                call.message.message_id == int(r.hget('war_battle' + str(call.message.chat.id), 'start')):
            allow = True
            if r.hexists('c' + str(call.message.chat.id), 'war_allow'):
                if int(r.hget('c' + str(call.message.chat.id), 'war_allow')) == 1:
                    if str(call.from_user.id).encode() not in r.smembers('cl' + str(call.message.chat.id)) and \
                            int(datetime.now().timestamp()) - \
                            int(r.hget('war_battle' + str(call.message.chat.id), 'war_ts')) < 300:
                        allow = False
            if allow:
                r.sadd('fighters_2' + str(call.message.chat.id), call.from_user.id)
                r.hset(call.from_user.id, 'firstname', call.from_user.first_name)
                r.hset(call.from_user.id, 'in_war', call.message.chat.id)
                r.hset(call.from_user.id, 'w_ts', int(datetime.now().timestamp()))
                r.sadd('in_war', call.from_user.id)
                fighters = r.scard('fighters_2' + str(call.message.chat.id))
                n = ''
                try:
                    if int(r.hget(222, call.message.chat.id)) > 100:
                        n = '2'
                except:
                    pass
                if fighters == 1:
                    await bot.edit_message_text(
                        text=call.message.text + '\n\nБійці: ' + call.from_user.first_name,
                        chat_id=call.message.chat.id, message_id=call.message.message_id,
                        reply_markup=battle_button_3())
                elif fighters >= 5 and r.scard('battles' + n) == 0:
                    await call.message.reply('\u2694 Пошук ворогів...')
                    await bot.edit_message_text(text=call.message.text + ', ' + call.from_user.first_name,
                                                chat_id=call.message.chat.id, message_id=call.message.message_id)
                    r.sadd('battles' + n, call.message.chat.id)
                elif fighters >= 5 and r.scard('battles' + n) >= 1:
                    if str(call.message.chat.id).encode() in r.smembers('battles' + n):
                        pass
                    else:
                        enemy = r.spop('battles' + n)
                        await bot.edit_message_text(text=call.message.text + ', ' + call.from_user.first_name +
                                                                             '\n\nБій почався...',
                                                    chat_id=call.message.chat.id, message_id=call.message.message_id)
                        a = list(r.smembers('fighters_2' + str(call.message.chat.id)))[0:5]
                        b = list(r.smembers('fighters_2' + enemy.decode()))[0:5]
                        msg = 'Починається сутичка між двома бандами русаків!\n\n' + \
                              r.hget('war_battle' + str(call.message.chat.id), 'title').decode() + ' | ' + \
                              r.hget('war_battle' + enemy.decode(), 'title').decode() + \
                              '\n1. ' + r.hget(a[0], 'firstname').decode() + ' | ' + \
                              r.hget(b[0], 'firstname').decode() + \
                              '\n2. ' + r.hget(a[1], 'firstname').decode() + ' | ' + \
                              r.hget(b[1], 'firstname').decode() + \
                              '\n3. ' + r.hget(a[2], 'firstname').decode() + ' | ' + \
                              r.hget(b[2], 'firstname').decode() + \
                              '\n4. ' + r.hget(a[3], 'firstname').decode() + ' | ' + \
                              r.hget(b[3], 'firstname').decode() + \
                              '\n5. ' + r.hget(a[4], 'firstname').decode() + ' | ' + \
                              r.hget(b[4], 'firstname').decode()
                        await bot.send_message(int(call.message.chat.id), msg)
                        await bot.send_message(int(enemy), msg)
                        await great_war(call.message.chat.id, int(enemy), a, b)
                        try:
                            await bot.unpin_chat_message(chat_id=call.message.chat.id,
                                                         message_id=int(r.hget('war_battle' +
                                                                               str(call.message.chat.id), 'pin')))
                        except:
                            pass
                        try:
                            await bot.unpin_chat_message(chat_id=int(enemy),
                                                         message_id=int(r.hget('war_battle' + enemy.decode(), 'pin')))
                        except:
                            pass
                else:
                    await bot.edit_message_text(
                        text=call.message.text + ', ' + call.from_user.first_name, chat_id=call.message.chat.id,
                        message_id=call.message.message_id, reply_markup=battle_button_3())
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ти не в цьому клані, тому зайти зможеш через 5 хвилин після'
                                                     ' початку набору.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ти або вже в битві, або в тебе відсутній русак')

    elif call.data.startswith('raid_join') and r.hexists('c' + str(call.message.chat.id), 'start') == 1:
        if str(call.from_user.id).encode() not in r.smembers('fighters_3' + str(call.message.chat.id)) and \
                r.hexists(call.from_user.id, 'name') == 1 and \
                call.message.message_id == int(r.hget('c' + str(call.message.chat.id), 'start')) and\
                str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if 0 <= datetime.now().hour < 8:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Комендантська година, рейди недоступні.')
            else:
                r.sadd('fighters_3' + str(call.message.chat.id), call.from_user.id)
                r.hset(call.from_user.id, 'firstname', call.from_user.first_name)
                fighters = r.scard('fighters_3' + str(call.message.chat.id))
                if fighters == 1:
                    await bot.edit_message_text(text=call.message.text + '\n\nБійці: ' + call.from_user.first_name,
                                                chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                reply_markup=battle_button_4())
                elif fighters >= 5:
                    await bot.edit_message_text(text=call.message.text + ', ' + call.from_user.first_name +
                                                                         '\n\nРейд почався...',
                                                chat_id=call.message.chat.id, message_id=call.message.message_id)
                    await call.message.reply('\u2694 Русаки вирушили в рейд...')
                    await start_raid(call.message.chat.id)
                else:
                    await bot.edit_message_text(
                        text=call.message.text + ', ' + call.from_user.first_name, chat_id=call.message.chat.id,
                        message_id=call.message.message_id, reply_markup=battle_button_4())
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ти або вже в битві, або в тебе відсутній русак.\n\n'
                                                 'В рейді можуть брати участь тільки учасники клану')

    elif call.data.startswith('captcha_true') and \
            call.from_user.id == call.message.reply_to_message.new_chat_members[0].id:
        try:
            await bot.restrict_chat_member(call.message.chat.id, call.from_user.id,
                                           can_send_messages=True, can_send_media_messages=True,
                                           can_send_other_messages=True, can_add_web_page_previews=True)
            await bot.edit_message_text(text=f'\u2705 Вітаю в чаті, {call.from_user.first_name}.',
                                        chat_id=call.message.chat.id, message_id=call.message.message_id)
        except:
            pass

    elif call.data.startswith('captcha_false') and \
            call.from_user.id == call.message.reply_to_message.new_chat_members[0].id:
        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Неправильна відповідь.')

    elif call.data.startswith('create_'):
        if r.hexists('c' + str(call.message.chat.id), 'base') == 0:
            if len(str(r.hget(call.from_user.id, 'clan'))) < 5:
                admins = []
                admins2 = await bot.get_chat_administrators(call.message.chat.id)
                for admin in admins2:
                    admins.append(admin.user.id)
                if call.from_user.id in admins or call.from_user.id in sudoers:
                    money = 0
                    if call.data == 'create_hrn':
                        if int(r.hget(call.from_user.id, 'money')) >= 250:
                            money = 1
                    else:
                        if r.hexists(call.from_user.id, 'strap') == 0:
                            r.hset(call.from_user.id, 'strap', 0)
                        if int(r.hget(call.from_user.id, 'strap')) >= 1:
                            money = 1
                    if money == 1:
                        r.hset('c' + str(call.message.chat.id), 'base', 1,
                               {'money': 0, 'wood': 0, 'stone': 0, 'cloth': 0, 'brick': 0, 'technics': 0, 'codes': 0,
                                'r_spirit': 0, 'storage': 0, 'sawmill': 0, 'mine': 0, 'craft': 0, 'silicate': 0,
                                'shop': 0, 'complex': 0, 'monument': 0, 'camp': 0, 'morgue': 0, 'post': 0, 'day': 0,
                                'power': 0, 'new_post': 0, 'salary': 0, 'war_allow': 0, 'recruitment': 0,
                                'leader': call.from_user.id, 'allow': 0, 'title': call.message.chat.title,
                                'side': 0, 'build1': 0, 'build2': 0, 'build3': 0, 'build4': 0,
                                'build5': 0, 'build6': 0})
                        r.sadd('cl' + str(call.message.chat.id), call.from_user.id)
                        r.sadd('clans', call.message.chat.id)
                        r.hset(call.from_user.id, 'clan', call.message.chat.id,
                               {'clan_ts': int(datetime.now().timestamp()), 'clan_time': 0})
                        if call.data == 'create_hrn':
                            r.hincrby(call.from_user.id, 'money', -250)
                        else:
                            r.hincrby(call.from_user.id, 'strap', -1)
                        await bot.edit_message_text('\U0001F3D7 Засновано банду ' + call.message.chat.title + '!',
                                                    call.message.chat.id, call.message.message_id)
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ти не адміністратор.')

    elif call.data.startswith('clan_side'):
        c = 'c' + str(call.message.chat.id)
        if call.data.startswith('clan_side_4'):
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Організацій забагато, виберіть щось інше.')
        elif int(r.hget(c, 'side')) == 0:
            if call.from_user.id == int(r.hget(c, 'leader')):
                if int(r.hget(c, 'wood')) >= 6000 and int(r.hget(c, 'stone')) >= 3000 \
                        and int(r.hget(c, 'cloth')) >= 1500 and int(r.hget(c, 'brick')) >= 1000 \
                        and int(r.hget(c, 'technics')) >= 100 \
                        and int(r.hget(c, 'money')) >= 5000 and int(r.hget(c, 'r_spirit')) >= 100:
                    r.hincrby(c, 'money', -5000)
                    r.hincrby(c, 'wood', -6000)
                    r.hincrby(c, 'stone', -3000)
                    r.hincrby(c, 'cloth', -1500)
                    r.hincrby(c, 'brick', -1000)
                    r.hincrby(c, 'technics', -100)
                    r.hincrby(c, 'r_spirit', -100)
                    if call.data.startswith('clan_side_1'):
                        r.hset(c, 'base', 5)
                        r.hset(c, 'side', 1)
                        await bot.send_message(call.message.chat.id, '\U0001F3D7 Покращено Угруповання до Комуни.')
                    elif call.data.startswith('clan_side_2'):
                        r.hset(c, 'base', 6)
                        r.hset(c, 'side', 2)
                        await bot.send_message(call.message.chat.id, '\U0001F3D7 Покращено Угруповання до Коаліції.')
                    elif call.data.startswith('clan_side_3'):
                        r.hset(c, 'base', 7)
                        r.hset(c, 'side', 3)
                        await bot.send_message(call.message.chat.id, '\U0001F3D7 Покращено Угруповання до Асоціації.')
                    elif call.data.startswith('clan_side_4'):
                        r.hset(c, 'base', 8)
                        r.hset(c, 'side', 4)
                        await bot.send_message(call.message.chat.id, '\U0001F3D7 Покращено Угруповання до Організації.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо ресурсів.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Це має зробити лідер.')

    elif call.data.startswith('invite'):
        admins = []
        uid = call.message.reply_to_message.from_user.id
        num = 25
        ts = 604800
        admins2 = await bot.get_chat_administrators(call.message.chat.id)
        for admin in admins2:
            admins.append(admin.user.id)
        if int(r.hget('c' + str(call.message.chat.id), 'complex')) >= 1:
            num += 25
        if int(r.hget('c' + str(call.message.chat.id), 'build5')) == 3:
            num += 10
            ts = 0
        if call.from_user.id in admins and \
                str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)) and \
                r.scard('cl' + str(call.message.chat.id)) < num:
            if int(datetime.now().timestamp()) - int(r.hget(uid, 'clan_ts')) > ts or uid in sudoers:
                r.hset(uid, 'clan', call.message.chat.id, {'clan_ts': int(datetime.now().timestamp()),
                                                           'firstname': call.from_user.first_name})
                if r.hexists(uid, 'clan_time') == 0:
                    r.hset(uid, 'clan_time', 0)
                r.sadd('cl' + str(call.message.chat.id), uid)
                await bot.edit_message_text('\U0001F4E5 Ти вступив в клан ' +
                                            r.hget('c' + str(call.message.chat.id), 'title').decode() + '.',
                                            call.message.chat.id, call.message.message_id)
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='\U0001F4E5 Вступати в клан можна лише раз в тиждень.')

    elif call.data.startswith('buy_axe'):
        if int(r.hget(call.from_user.id, 'support')) == 0:
            if int(r.hget(call.from_user.id, 'money')) >= 5:
                r.hincrby(call.from_user.id, 'money', -5)
                r.hset(call.from_user.id, 'support', 3)
                r.hset(call.from_user.id, 's_support', 3)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви успішно купили сокиру')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='У вас вже є допоміжне спорядження')

    elif call.data.startswith('buy_pickaxe'):
        if int(r.hget(call.from_user.id, 'support')) == 0:
            if int(r.hget(call.from_user.id, 'money')) >= 10:
                r.hincrby(call.from_user.id, 'money', -10)
                r.hset(call.from_user.id, 'support', 4)
                r.hset(call.from_user.id, 's_support', 3)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви успішно купили кайло')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='У вас вже є допоміжне спорядження')

    elif call.data.startswith('leave_from_clan'):
        try:
            if call.from_user.id == call.message.reply_to_message.from_user.id:
                if checkClan(call.from_user.id):
                    if checkClan(call.from_user.id, building='build6', level=1):
                        r.hincrby(call.from_user.id, 'strength', -int(int(r.hget(call.from_user.id, 'strength')) * 0.2))
                        if r.hexists(call.from_user.id, 'strength2'):
                            r.hincrby(call.from_user.id, 'strength2',
                                      -int(int(r.hget(call.from_user.id, 'strength2')) * 0.2))
                    r.srem('cl' + r.hget(call.from_user.id, 'clan').decode(), call.from_user.id)
                    r.hset(call.from_user.id, 'clan', 0)
                    await bot.edit_message_text('\U0001F4E4 Ти покинув клан', call.message.chat.id,
                                                call.message.message_id)
        except:
            pass

    elif call.data.startswith('change_title'):
        c = int(r.hget(call.from_user.id, 'clan'))
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, c):
            t = await bot.get_chat(c)
            r.hset('c' + str(c), 'title', t.title)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Назву клану оновлено.')

    elif call.data.startswith('toggle_allow'):
        c = int(r.hget(call.from_user.id, 'clan'))
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, c):
            if int(r.hget('c' + str(c), 'allow')) == 0:
                r.hset('c' + str(c), 'allow', 1)
            else:
                r.hset('c' + str(c), 'allow', 0)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Режим набору змінено.')

    elif call.data.startswith('toggle_war'):
        c = int(r.hget(call.from_user.id, 'clan'))
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, c):
            if int(r.hget('c' + str(c), 'war_allow')) == 0:
                r.hset('c' + str(c), 'war_allow', 1)
            else:
                r.hset('c' + str(c), 'war_allow', 0)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Режим входу в міжчатові битви змінено.')

    elif call.data.startswith('salary'):
        c = int(r.hget(call.from_user.id, 'clan'))
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, c):
            if int(r.hget('c' + str(c), 'salary')) == 0:
                r.hset('c' + str(c), 'salary', 1)
            else:
                r.hset('c' + str(c), 'salary', 0)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Режим видачі зарплати за роботу змінено.')

    elif call.data.startswith('recruitment'):
        c = int(r.hget(call.from_user.id, 'clan'))
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, c) \
                and str(call.chat.id).encode() not in r.smembers('banned'):
            try:
                if int(r.hget('c' + str(c), 'recruitment')) == 0:
                    try:
                        await bot.revoke_chat_invite_link(c, r.hget('c' + str(c), 'link').decode())
                    except:
                        pass
                    a = await bot.create_chat_invite_link(c, creates_join_request=True)
                    r.hset('c' + str(c), 'recruitment', 1, {'link': a.invite_link})
                    r.sadd('recruitment', c)
                else:
                    try:
                        await bot.revoke_chat_invite_link(c, r.hget('c' + str(c), 'link').decode())
                    except:
                        pass
                    r.hset('c' + str(c), 'recruitment', 0)
                    r.srem('recruitment', c)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Режим набору змінено.')
            except:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Схоже в бота нема прав додавати користувачів.')

    elif call.data.startswith('get_members'):
        uid = call.from_user.id
        if checkClan(uid) and checkLeader(uid, int(r.hget(uid, 'clan'))) or \
                call.from_user.id in sudoers:
            msg = ''
            for mem in r.smembers('cl' + r.hget(call.from_user.id, 'clan').decode()):
                if int(r.hget(mem, 'clan_time')) == datetime.now().day:
                    msg += '\U0001f7e9 '
                else:
                    msg += '\U0001f7e5 '
                name = r.hget(mem, 'firstname').decode()
                msg += f'<a href="tg://user?id={int(mem)}">{name}</a>\n'
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Отримати список з user id', callback_data='get_id_members'))
            await bot.send_message(call.message.chat.id, msg, parse_mode='HTML', reply_markup=markup)

    elif call.data.startswith('get_id_members'):
        uid = call.from_user.id
        if checkClan(uid) and checkLeader(uid, int(r.hget(uid, 'clan'))) or \
                call.from_user.id in sudoers:
            msg = ''
            for mem in r.smembers('cl' + r.hget(call.from_user.id, 'clan').decode()):
                if int(r.hget(mem, 'clan_time')) == datetime.now().day:
                    msg += '\U0001f7e9 '
                else:
                    msg += '\U0001f7e5 '
                name = r.hget(mem, 'firstname').decode()
                msg += f'<a href="tg://user?id={int(mem)}">{name}</a> {mem.decode()}\n'
            await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, parse_mode='HTML')

    elif call.data.startswith('build_sawmill') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        if int(r.hget(c, 'sawmill')) == 0:
            if int(r.hget(c, 'money')) >= 200:
                r.hincrby(c, 'money', -200)
                r.hset(c, 'sawmill', 1)
                await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано пилораму.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build_mine') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        if int(r.hget(c, 'mine')) == 0:
            if int(r.hget(c, 'money')) >= 300:
                r.hincrby(c, 'money', -300)
                r.hset(c, 'mine', 1)
                await bot.send_message(call.message.chat.id, 'На території вашого клану відкрито шахту!'
                                                             ' Русаки можуть приступати до роботи.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build_craft') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        if int(r.hget(c, 'craft')) == 0:
            if int(r.hget(c, 'storage')) != 0:
                if int(r.hget(c, 'money')) >= 100 and int(r.hget(c, 'wood')) >= 300 and int(r.hget(c, 'stone')) >= 200:
                    r.hincrby(c, 'money', -100)
                    r.hincrby(c, 'wood', -300)
                    r.hincrby(c, 'stone', -200)
                    r.hset(c, 'craft', 1)
                    await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано цех.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо ресурсів.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Потрібен склад')

    elif call.data.startswith('build_storage') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        if int(r.hget(c, 'storage')) == 0:
            if int(r.hget(c, 'wood')) >= 200 and int(r.hget(c, 'stone')) >= 100:
                r.hincrby(c, 'wood', -200)
                r.hincrby(c, 'stone', -100)
                r.hset(c, 'storage', 1)
                await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано склад.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build_complex') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        if int(r.hget(c, 'complex')) == 0:
            if int(r.hget(c, 'wood')) >= 500 and int(r.hget(c, 'stone')) >= 500 and int(r.hget(c, 'cloth')) >= 500 \
                    and int(r.hget(c, 'brick')) >= 50 and int(r.hget(c, 'money')) >= 500:
                r.hincrby(c, 'wood', -500)
                r.hincrby(c, 'stone', -500)
                r.hincrby(c, 'cloth', -500)
                r.hincrby(c, 'brick', -50)
                r.hincrby(c, 'money', -500)
                r.hset(c, 'complex', 1)
                await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано житловий комплекс.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build_silicate') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        if int(r.hget(c, 'silicate')) == 0:
            if int(r.hget(c, 'wood')) >= 1050 and int(r.hget(c, 'stone')) >= 750 \
                    and int(r.hget(c, 'cloth')) >= 200 and int(r.hget(c, 'money')) >= 2000:
                r.hincrby(c, 'wood', -1050)
                r.hincrby(c, 'stone', -750)
                r.hincrby(c, 'cloth', -200)
                r.hincrby(c, 'money', -2000)
                r.hset(c, 'silicate', 1)
                await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано силікатний завод.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build_shop') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        if int(r.hget(c, 'shop')) == 0:
            if int(r.hget(c, 'wood')) >= 1000 and int(r.hget(c, 'stone')) >= 200 and int(r.hget(c, 'cloth')) >= 400 \
                    and int(r.hget(c, 'brick')) >= 40 and int(r.hget(c, 'money')) >= 300:
                r.hincrby(c, 'wood', -1000)
                r.hincrby(c, 'stone', -200)
                r.hincrby(c, 'cloth', -400)
                r.hincrby(c, 'brick', -40)
                r.hincrby(c, 'money', -300)
                r.hset(c, 'shop', 1)
                await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано їдальню.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build_monument') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        if int(r.hget(c, 'monument')) == 0:
            if int(r.hget(c, 'wood')) >= 100 and int(r.hget(c, 'stone')) >= 1000 and int(r.hget(c, 'cloth')) >= 50 \
                    and int(r.hget(c, 'brick')) >= 100 and int(r.hget(c, 'money')) >= 2000 \
                    and int(r.hget(c, 'r_spirit')) >= 50:
                r.hincrby(c, 'wood', -100)
                r.hincrby(c, 'stone', -1000)
                r.hincrby(c, 'cloth', -50)
                r.hincrby(c, 'brick', -100)
                r.hincrby(c, 'money', -2000)
                r.hincrby(c, 'r_spirit', -50)
                r.hset(c, 'monument', 1)
                await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано монумент.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build_post') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        if int(r.hget(c, 'post')) == 0:
            if int(r.hget(c, 'wood')) >= 200 and int(r.hget(c, 'stone')) >= 200 and int(r.hget(c, 'cloth')) >= 200 \
                    and int(r.hget(c, 'brick')) >= 200 and int(r.hget(c, 'money')) >= 200:
                r.hincrby(c, 'wood', -200)
                r.hincrby(c, 'stone', -200)
                r.hincrby(c, 'cloth', -200)
                r.hincrby(c, 'brick', -200)
                r.hincrby(c, 'money', -200)
                r.hset(c, 'post', 1)
                await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано блокпост.\n\nМожна '
                                                             'туди відправити русака замість роботи командою /guard')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build_camp') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        if int(r.hget(c, 'camp')) == 0:
            if int(r.hget(c, 'wood')) >= 3000 and int(r.hget(c, 'stone')) >= 1000 and int(r.hget(c, 'cloth')) >= 1000 \
                    and int(r.hget(c, 'brick')) >= 400 and int(r.hget(c, 'money')) >= 3000 \
                    and int(r.hget(c, 'r_spirit')) >= 100:
                r.hincrby(c, 'wood', -3000)
                r.hincrby(c, 'stone', -1000)
                r.hincrby(c, 'cloth', -100)
                r.hincrby(c, 'brick', -400)
                r.hincrby(c, 'money', -3000)
                r.hincrby(c, 'r_spirit', -100)
                r.hset(c, 'camp', 1)
                await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано концтабір.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build_morgue') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        if int(r.hget(c, 'morgue')) == 0:
            if int(r.hget(c, 'wood')) >= 1000 and int(r.hget(c, 'stone')) >= 2000 and int(r.hget(c, 'cloth')) >= 800 \
                    and int(r.hget(c, 'brick')) >= 500 and int(r.hget(c, 'money')) >= 5000 \
                    and int(r.hget(c, 'r_spirit')) >= 100:
                r.hincrby(c, 'wood', -1000)
                r.hincrby(c, 'stone', -2000)
                r.hincrby(c, 'cloth', -800)
                r.hincrby(c, 'brick', -500)
                r.hincrby(c, 'money', -5000)
                r.hincrby(c, 'r_spirit', -100)
                r.hset(c, 'morgue', 1)
                await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано морг.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build_new_post') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        if int(r.hget(c, 'new_post')) == 0:
            if int(r.hget(c, 'wood')) >= 800 and int(r.hget(c, 'stone')) >= 500 and int(r.hget(c, 'cloth')) >= 500 \
                    and int(r.hget(c, 'brick')) >= 200 and int(r.hget(c, 'money')) >= 2000 \
                    and int(r.hget(c, 'r_spirit')) >= 30:
                r.hincrby(c, 'wood', -800)
                r.hincrby(c, 'stone', -500)
                r.hincrby(c, 'cloth', -500)
                r.hincrby(c, 'brick', -200)
                r.hincrby(c, 'money', -2000)
                r.hincrby(c, 'r_spirit', -30)
                r.hset(c, 'new_post', 1)
                await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано '
                                                             'відділення Нової пошти.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build1') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        s = int(r.hget(c, 'side'))
        if int(r.hget(c, 'build1')) == 0 and s != 0:
            if int(r.hget(c, 'wood')) >= 4000 and int(r.hget(c, 'stone')) >= 2000 and int(r.hget(c, 'cloth')) >= 750 \
                    and int(r.hget(c, 'brick')) >= 500 and int(r.hget(c, 'money')) >= 4000 \
                    and int(r.hget(c, 'r_spirit')) >= 50 and int(r.hget(c, 'technics')) >= 50:
                r.hincrby(c, 'wood', -4000)
                r.hincrby(c, 'stone', -2000)
                r.hincrby(c, 'cloth', -750)
                r.hincrby(c, 'brick', -500)
                r.hincrby(c, 'money', -4000)
                r.hincrby(c, 'r_spirit', -50)
                r.hincrby(c, 'technics', -50)
                r.hset(c, 'build1', s)
                b = ['', 'тракторний завод', 'штаб тероборони', 'dungeon', 'біолабораторію']
                await bot.send_message(call.message.chat.id, f'На території вашого клану побудовано {b[s]}.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build2') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        s = int(r.hget(c, 'side'))
        if int(r.hget(c, 'build2')) == 0 and s != 0:
            if int(r.hget(c, 'wood')) >= 3000 and int(r.hget(c, 'stone')) >= 500 and int(r.hget(c, 'cloth')) >= 500 \
                    and int(r.hget(c, 'brick')) >= 300 and int(r.hget(c, 'money')) >= 1000 \
                    and int(r.hget(c, 'r_spirit')) >= 50:
                r.hincrby(c, 'wood', -3000)
                r.hincrby(c, 'stone', -500)
                r.hincrby(c, 'cloth', -500)
                r.hincrby(c, 'brick', -300)
                r.hincrby(c, 'money', -1000)
                r.hincrby(c, 'r_spirit', -50)
                r.hset(c, 'build2', s)
                b = ['', 'пивний ларьок', 'березову рощу', 'бійцівський клуб', 'аптеку']
                await bot.send_message(call.message.chat.id, f'На території вашого клану побудовано {b[s]}.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build3') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        s = int(r.hget(c, 'side'))
        if int(r.hget(c, 'build3')) == 0 and s != 0:
            if int(r.hget(c, 'wood')) >= 1000 and int(r.hget(c, 'stone')) >= 1000 and int(r.hget(c, 'cloth')) >= 500 \
                    and int(r.hget(c, 'brick')) >= 400 and int(r.hget(c, 'money')) >= 2000:
                r.hincrby(c, 'wood', -1000)
                r.hincrby(c, 'stone', -1000)
                r.hincrby(c, 'cloth', -500)
                r.hincrby(c, 'brick', -400)
                r.hincrby(c, 'money', -2000)
                r.hset(c, 'build3', s)
                b = ['', 'падік', 'генеральську дачу', 'циганський табір', 'АЗС']
                await bot.send_message(call.message.chat.id, f'На території вашого клану побудовано {b[s]}.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build4') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        s = int(r.hget(c, 'side'))
        if int(r.hget(c, 'build4')) == 0 and s != 0:
            if int(r.hget(c, 'wood')) >= 2000 and int(r.hget(c, 'stone')) >= 1000 and int(r.hget(c, 'cloth')) >= 500 \
                    and int(r.hget(c, 'brick')) >= 400 and int(r.hget(c, 'money')) >= 2000 \
                    and int(r.hget(c, 'technics')) >= 200:
                r.hincrby(c, 'wood', -2000)
                r.hincrby(c, 'stone', -1000)
                r.hincrby(c, 'cloth', -500)
                r.hincrby(c, 'brick', -400)
                r.hincrby(c, 'money', -2000)
                r.hincrby(c, 'technics', -200)
                r.hset(c, 'build4', s)
                b = ['', 'тюрму', 'казарму', 'радіовежу', 'дата-центр']
                await bot.send_message(call.message.chat.id, f'На території вашого клану побудовано {b[s]}.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build5') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        s = int(r.hget(c, 'side'))
        if int(r.hget(c, 'build5')) == 0 and s != 0:
            if int(r.hget(c, 'wood')) >= 2000 and int(r.hget(c, 'stone')) >= 1000 and int(r.hget(c, 'cloth')) >= 800 \
                    and int(r.hget(c, 'brick')) >= 500 and int(r.hget(c, 'money')) >= 6000 \
                    and int(r.hget(c, 'technics')) >= 100:
                r.hincrby(c, 'wood', -2000)
                r.hincrby(c, 'stone', -1000)
                r.hincrby(c, 'cloth', -800)
                r.hincrby(c, 'brick', -500)
                r.hincrby(c, 'money', -6000)
                r.hincrby(c, 'technics', -100)
                r.hset(c, 'build5', s)
                b = ['', 'воєнкомат', 'ферму', 'готель', 'торговий центр']
                await bot.send_message(call.message.chat.id, f'На території вашого клану побудовано {b[s]}.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('build6') and call.from_user.id == call.message.reply_to_message.from_user.id:
        c = 'c' + str(call.message.chat.id)
        s = int(r.hget(c, 'side'))
        if int(r.hget(c, 'build6')) == 0 and s != 0:
            if int(r.hget(c, 'wood')) >= 15000 and int(r.hget(c, 'stone')) >= 10000 and int(r.hget(c, 'cloth')) >= 5000\
                    and int(r.hget(c, 'brick')) >= 3000 and int(r.hget(c, 'money')) >= 10000 \
                    and int(r.hget(c, 'technics')) >= 300 and int(r.hget(c, 'r_spirit')) >= 300 \
                    and int(r.hget(c, 'codes')) >= 10:
                r.hincrby(c, 'wood', -15000)
                r.hincrby(c, 'stone', -10000)
                r.hincrby(c, 'cloth', -5000)
                r.hincrby(c, 'brick', -3000)
                r.hincrby(c, 'money', -10000)
                r.hincrby(c, 'technics', -300)
                r.hincrby(c, 'r_spirit', -300)
                r.hincrby(c, 'codes', -10)
                r.hset(c, 'build6', s)
                b = ['', 'гулаг', 'ядерний бункер', 'офіс Червоного Хреста', 'невільничий ринок']
                await bot.send_message(call.message.chat.id, f'На території вашого клану побудовано {b[s]}.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')

    elif call.data.startswith('sacrifice') and call.from_user.id == call.message.reply_to_message.from_user.id and \
            int(r.hget(call.from_user.id, 'time2')) != datetime.now().day:
        r.hset(call.from_user.id, 'time2', datetime.now().day)
        try:
            cl = int(r.hget(call.from_user.id, 'class'))
            for member in r.smembers(call.message.chat.id):
                try:
                    mem = int(member)
                    try:
                        st = await bot.get_chat_member(call.message.chat.id, mem)
                        if st.status == 'left' or st.status == 'kicked' or st.status == 'banned':
                            r.srem(call.message.chat.id, mem)
                            continue
                    except:
                        r.srem(call.message.chat.id, mem)
                    i1 = int(r.hget(mem, 'spirit'))
                    i = int(i1 / 10)
                    r.hincrby(mem, 'spirit', -i)
                    if cl == 7 or cl == 17 or cl == 27:
                        mush = int(r.hget(mem, 'mushrooms'))
                        if mush > 0:
                            r.hset(mem, 'mushrooms', 0)
                            intellect(-mush, mem)
                        else:
                            r.hset(mem, 'spirit', i)
                    if int(r.hget(mem, 'head')) == 1:
                        r.hset(mem, 'spirit', i1)
                        damage_head(mem)
                except:
                    pass
        except:
            pass
        name = int(r.hget(call.from_user.id, 'name'))
        clm = int(r.hget(call.from_user.id, 'class'))
        r.srem('class-' + str(clm), call.from_user.id)
        r.hdel(call.from_user.id, 'name')
        r.hset(call.from_user.id, 'photo', 0, {'strength': 0, 'intellect': 0, 'spirit': 0,
                                               'class': 0, 'weapon': 0, 's_weapon': 0, 'defense': 0, 's_defense': 0,
                                               'support': 0, 's_support': 0, 'mushrooms': 0})
        r.hincrby(call.from_user.id, 'deaths', 1)
        r.hincrby('all_deaths', 'deaths', 1)
        msg = '\u2620\uFE0F ' + names[name] + ' був убитий. \nОдним кацапом менше, а вторий насрав в штани.'
        if checkClan(call.from_user.id, base=4, building='morgue'):
            r.hincrby('c' + r.hget(call.from_user.id, 'clan').decode(), 'r_spirit', 1)
            msg += '\n\U0001F47E +1'
        if clm == 36:
            r.hincrby(call.from_user.id, 'strap', 1)
            msg += '\n\U0001F31F +1'
        if call.message.chat.type != 'private':
            msg += '\n' + str(len(r.smembers(call.message.chat.id)) - 1) + ' русаків втратили бойовий дух.'
        await bot.edit_message_text(text=msg, chat_id=call.message.chat.id, message_id=call.message.message_id)

    elif call.data.startswith('full_list'):
        msg, markup = com(call.data)
        try:
            await bot.edit_message_text(text=msg, chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        parse_mode='HTML', reply_markup=markup, disable_web_page_preview=True)
        except:
            pass

    elif call.data.startswith('wiki'):
        msg, markup = wiki_text(call.data)
        try:
            await bot.edit_message_text(text=msg, reply_markup=markup,
                                        chat_id=call.message.chat.id, message_id=call.message.message_id)
        except:
            pass

    elif call.data.startswith('alcohol'):
        s1 = int(r.hget(call.from_user.id, 's1'))
        if s1 < 10:
            cl = int(r.hget(call.from_user.id, 'class'))
            s11 = s1
            if cl == 12 or cl == 22:
                s11 = s1 / 2
            if int(r.hget(call.from_user.id, 'vodka')) >= s11 * 100:
                r.hincrby(call.from_user.id, 's1', 1)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='\u2622 Ви підняли рівень алкоголізму до ' + str(s1 + 1) + '.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ще рано переходити на наступний етап алкоголізму.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Немає сенсу ставати ще більшим алкоголіком.')

    elif call.data.startswith('master'):
        s2 = int(r.hget(call.from_user.id, 's2'))
        if s2 < 5:
            cl = int(r.hget(call.from_user.id, 'class'))
            s22 = s2
            if cl == 12 or cl == 22:
                s22 = s2 / 2
            if int(r.hget(call.from_user.id, 'wins')) >= s22 * 250:
                if int(r.hget(call.from_user.id, 'money')) >= 100:
                    r.hincrby(call.from_user.id, 'money', -100)
                    r.hincrby(call.from_user.id, 's2', 1)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='\u26CF Ви підняли рівень майстерності до ' + str(
                                                        s2 + 1) + '.')
                    if s2 + 1 == 5:
                        intellect(2, call.from_user.id)
                        await bot.send_message(call.message.chat.id, 'За досягнення найвищого рівня майстерності твій'
                                                                     ' русак отримує \U0001F9E0 +2 інтелекту.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ще рано переходити на наступний етап майтерності.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Немає сенсу ставати ще кращим майстром.')

    elif call.data.startswith('cellar'):
        s3 = int(r.hget(call.from_user.id, 's3'))
        if s3 == 1:
            if int(r.hget(call.from_user.id, 'money')) >= 30:
                r.hincrby(call.from_user.id, 'money', -30)
                r.hincrby(call.from_user.id, 's3', 1)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви купили другу утеплену будку.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        elif s3 == 2:
            if int(r.hget(call.from_user.id, 'money')) >= 750:
                r.hincrby(call.from_user.id, 'money', -750)
                r.hincrby(call.from_user.id, 's3', 1)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви купили будівельні матеріали.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        elif s3 == 3:
            if r.hexists(call.from_user.id, 'name') == 1:
                st = int(int(r.hget(call.from_user.id, 'strength')) * 0.75)
                r.hset(call.from_user.id, 'strength', st)
                r.hincrby(call.from_user.id, 's3', 1)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви розширили місце в підвалі для додаткового русака.')
                await bot.send_message(call.message.chat.id, '\U0001F412 У вас з`явився другий русак.\n'
                                                             'Змінити бойового русака можна командою /swap.')
                r.hset(call.from_user.id, 'name2', randint(0, len(names) - 1),
                       {'strength2': randint(10, 50),
                        'intellect2': int(choice(['1', '1', '1', '1', '2'])),
                        'spirit2': 0, 'weapon2': 0, 's_weapon2': 0, 'defense2': 0, 's_defense2': 0,
                        'mushrooms2': 0, 'class2': 0, 'photo2': choice(default), 'injure2': 0, 'hp2': 100,
                        'support2': 0, 's_support2': 0, 'sch2': 0, 'buff2': 0, 'head2': 0, 's_head2': 0})
                r.sadd('swappers', call.from_user.id)
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас немає русака.')
        elif s3 == 4:
            if int(r.hget(call.from_user.id, 'money')) >= 1500:
                r.hincrby(call.from_user.id, 'money', -1500)
                r.hincrby(call.from_user.id, 's3', 1)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви купили припаси.')
                await bot.send_message(call.message.chat.id,
                                       'Тепер можна по одному годувати двох русаків. Змінити бойового'
                                       ' русака можна командою /swap.')
                r.hset(call.from_user.id, 'time22', 0)
                r.hset(call.from_user.id, 'time23', 0)
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        elif s3 == 5:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='У вас вже нічого будувати.')

    elif call.data.startswith('vodka'):
        if int(r.hget(call.from_user.id, 'money')) >= 2:
            r.hincrby(call.from_user.id, 'money', -2)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно купили горілку "Козаки"\n\U0001F54A + ' +
                                                 vodka(call.from_user.id))
        else:
            cl = int(r.hget(call.from_user.id, 'class'))
            if cl == 17 or cl == 27:
                if int(r.hget(call.from_user.id, 'wins')) >= 2:
                    r.hincrby(call.from_user.id, 'wins', -2)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили горілку "Козаки" за перемоги'
                                                         '\n\U0001F54A + ' + vodka(call.from_user.id))
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку')

    elif call.data.startswith('weapon'):
        if int(r.hget(call.from_user.id, 'weapon')) == 0:
            if int(r.hget(call.from_user.id, 'money')) >= 4:
                r.hincrby(call.from_user.id, 'money', -4)
                msg = 'Ви успішно купили колючий дрин'
                if int(r.hget(call.from_user.id, 'class')) == 14 or int(r.hget(call.from_user.id, 'class')) == 24:
                    r.hset(call.from_user.id, 'weapon', 4)
                    r.hset(call.from_user.id, 's_weapon', 3)
                    msg = 'Ви успішно купили биту'
                else:
                    r.hset(call.from_user.id, 'weapon', 1)
                    r.hset(call.from_user.id, 's_weapon', 1)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text=msg)
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='У вас вже є зброя')

    elif call.data.startswith('defense'):
        if int(r.hget(call.from_user.id, 'defense')) == 0:
            if int(r.hget(call.from_user.id, 'money')) >= 5:
                r.hincrby(call.from_user.id, 'money', -5)
                r.hset(call.from_user.id, 'defense', 1)
                r.hset(call.from_user.id, 's_defense', 1)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви успішно купили колючий щит')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='У вас вже є захисне спорядження')

    elif call.data.startswith('aid_kit'):
        if r.hexists(call.from_user.id, 's_support') == 0:
            r.hset(call.from_user.id, 's_support', 0)
        if int(r.hget(call.from_user.id, 'support')) == 0:
            if int(r.hget(call.from_user.id, 'money')) >= 4:
                r.hincrby(call.from_user.id, 'money', -4)
                hp(5, call.from_user.id)
                r.hset(call.from_user.id, 'support', 1)
                r.hset(call.from_user.id, 's_support', 5)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви успішно купили аптечку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='У вас вже є допоміжне спорядження')

    elif call.data.startswith('passport'):
        if int(r.hget(call.from_user.id, 'money')) >= 10:
            ran = randint(0, len(names) - 1)
            r.hincrby(call.from_user.id, 'money', -10)
            r.hset(call.from_user.id, 'name', ran)
            if r.hexists(call.from_user.id, 'ac3') == 0:
                r.hset(call.from_user.id, 'ac3', 1)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно купили трофейний паспорт')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо коштів на рахунку')

    elif call.data.startswith('cabin'):
        if r.hexists(call.from_user.id, 'cabin') == 0:
            r.hset(call.from_user.id, 'cabin', 0)
        if int(r.hget(call.from_user.id, 'cabin')) == 0:
            if int(r.hget(call.from_user.id, 'money')) >= 30:
                r.hincrby(call.from_user.id, 'money', -30)
                r.hset(call.from_user.id, 'cabin', 1)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви успішно купили утеплену будку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='У вас вже є утееплена будка')

    elif call.data.startswith('woman'):
        if r.hexists(call.from_user.id, 'woman') == 0:
            r.hset(call.from_user.id, 'woman', 0)
        price = 150
        if r.hexists(call.from_user.id, 'name') == 1 and int(r.hget(call.from_user.id, 'class')) in (32, 33):
            price = 100
        if int(r.hget(call.from_user.id, 'woman')) == 0:
            if int(r.hget(call.from_user.id, 'money')) >= price:
                r.hincrby(call.from_user.id, 'money', -price)
                r.hset(call.from_user.id, 'woman', 1)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви успішно купили жінку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='У вас вже є жінка')

    elif call.data.startswith('pipe'):
        if r.hexists(call.from_user.id, 'woman') and int(r.hget(call.from_user.id, 'woman')) == 1:
            r.hset(call.from_user.id, 'woman', 0)
            r.hset(call.from_user.id, 'time5', 0)
            spirit(5000, call.from_user.id, 0)
            r.hincrby(call.from_user.id, 'deaths', 5)
            r.hincrby('all_deaths', 'deaths', 5)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно проміняли жінку на тютюн та люльку.\nНеобачний.')
            await bot.send_message(call.message.chat.id, 'Ви успішно проміняли жінку на тютюн та люльку.\nНеобачний.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо жінок на рахунку')

    elif call.data.startswith('fragment'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            if int(r.hget(call.from_user.id, 'defense')) == 0:
                if int(r.hget(call.from_user.id, 'money')) >= 10:
                    r.hincrby(call.from_user.id, 'money', -10)
                    r.hset(call.from_user.id, 'defense', 9)
                    r.hset(call.from_user.id, 's_defense', 7)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили уламок бронетехніки')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас вже є захисне спорядження')
        else:
            await bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id,
                                        call.message.message_id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('uav'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            if int(r.hget(call.from_user.id, 'weapon')) == 0:
                if int(r.hget(call.from_user.id, 'money')) >= 90:
                    r.hincrby(call.from_user.id, 'money', -90)
                    r.hset(call.from_user.id, 'weapon', 5)
                    r.hset(call.from_user.id, 's_weapon', 1)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили БпЛА')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас вже є зброя')
        else:
            await bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id,
                                        call.message.message_id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('bombs'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            if int(r.hget(call.from_user.id, 'defense')) == 0:
                if int(r.hget(call.from_user.id, 'money')) >= 30:
                    r.hincrby(call.from_user.id, 'money', -30)
                    r.hset(call.from_user.id, 'defense', 3)
                    r.hset(call.from_user.id, 's_defense', 3)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили міни')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас вже є захисне спорядження')
        else:
            await bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id,
                                        call.message.message_id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('mushroom'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            if int(r.hget(call.from_user.id, 'support')) == 0:
                mushroom = int(r.hget(call.from_user.id, 'mushrooms'))
                if int(r.hget(call.from_user.id, 'class')) == 18 or int(r.hget(call.from_user.id, 'class')) == 28:
                    mushroom = 0
                if mushroom < 3:
                    if int(r.hget(call.from_user.id, 'intellect')) < 20:
                        if int(r.hget(call.from_user.id, 'money')) >= 60:
                            r.hincrby(call.from_user.id, 'money', -60)
                            r.hset(call.from_user.id, 'support', 6)
                            r.hset(call.from_user.id, 's_support', 1)
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Ви успішно купили мухомор королівський')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Недостатньо коштів на рахунку')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ваш русак вже занадто розумний')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Для вашого русака не передбачено більше трьох мухоморів')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас вже є допоміжне спорядження')
        else:
            await bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id,
                                        call.message.message_id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('sugar'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            if int(r.hget(call.from_user.id, 'support')) == 0:
                if int(r.hget(call.from_user.id, 'money')) >= 150:
                    r.hincrby(call.from_user.id, 'money', -150)
                    r.hset(call.from_user.id, 'support', 7)
                    r.hset(call.from_user.id, 's_support', 2)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили цукор')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас вже є допоміжне спорядження')
        else:
            await bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id,
                                        call.message.message_id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('kvs'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            if int(r.hget(call.from_user.id, 'support')) == 0:
                if int(r.hget(call.from_user.id, 'money')) >= 35:
                    r.hincrby(call.from_user.id, 'money', -35)
                    r.hset(call.from_user.id, 'support', 8)
                    r.hset(call.from_user.id, 's_support', 5)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили квас')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас вже є допоміжне спорядження')
        else:
            await bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id,
                                        call.message.message_id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('foil'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            if int(r.hget(call.from_user.id, 'head')) == 0:
                if int(r.hget(call.from_user.id, 'money')) >= 30:
                    r.hincrby(call.from_user.id, 'money', -30)
                    r.hincrby(call.from_user.id, 'sch', 30)
                    r.hset(call.from_user.id, 'head', 1)
                    r.hset(call.from_user.id, 's_head', 10)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили шапочку з фольги')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас вже є шапка')
        else:
            await bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id,
                                        call.message.message_id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('ear'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            if int(r.hget(call.from_user.id, 'head')) == 0:
                if int(r.hget(call.from_user.id, 'money')) >= 30:
                    r.hincrby(call.from_user.id, 'money', -30)
                    r.hset(call.from_user.id, 'head', 4)
                    r.hset(call.from_user.id, 's_head', 20)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили вушанку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас вже є шапка')
        else:
            await bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id,
                                        call.message.message_id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('watermelon'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            if int(r.hget(call.from_user.id, 'head')) == 0:
                if int(r.hget(call.from_user.id, 'money')) >= 333:
                    r.hincrby(call.from_user.id, 'money', -333)
                    r.hset(call.from_user.id, 'head', 3)
                    r.hset(call.from_user.id, 's_head', 1)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили кавун базований')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас вже є шапка')
        else:
            await bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id,
                                        call.message.message_id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('equipment'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            cl = int(r.hget(call.from_user.id, 'class'))
            if cl == 1 or cl == 11 or cl == 21:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 6:
                        r.hincrby(call.from_user.id, 'money', -6)
                        r.hset(call.from_user.id, 'weapon', 11)
                        r.hset(call.from_user.id, 's_weapon', 5)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили травмат')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя')

            elif cl == 2 or cl == 12 or cl == 22:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 15:
                        r.hincrby(call.from_user.id, 'money', -15)
                        r.hset(call.from_user.id, 'weapon', 12)
                        r.hset(call.from_user.id, 's_weapon', 25)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили діамантове кайло')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя')

            elif cl == 3 or cl == 13 or cl == 23:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 5:
                        r.hincrby(call.from_user.id, 'money', -5)
                        r.hset(call.from_user.id, 'weapon', 13)
                        r.hset(call.from_user.id, 's_weapon', 3)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили колоду з кіоску')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя')

            elif cl == 4 or cl == 14 or cl == 24:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 7:
                        r.hincrby(call.from_user.id, 'money', -7)
                        r.hset(call.from_user.id, 'weapon', 14)
                        r.hset(call.from_user.id, 's_weapon', 1)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили сокиру Перуна')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя')

            elif cl == 5 or cl == 15 or cl == 25:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 20:
                        r.hincrby(call.from_user.id, 'money', -20)
                        r.hset(call.from_user.id, 'weapon', 15)
                        r.hset(call.from_user.id, 's_weapon', 30)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили АК-47')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя')

            elif cl == 6 or cl == 16 or cl == 26:
                if int(r.hget(call.from_user.id, 'defense')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 10:
                        r.hincrby(call.from_user.id, 'money', -10)
                        r.hset(call.from_user.id, 'defense', 16)
                        r.hset(call.from_user.id, 's_defense', 10)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили поліцейський щит')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є захисне спорядження')

            elif cl == 7 or cl == 17 or cl == 27:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 5:
                        r.hincrby(call.from_user.id, 'money', -5)
                        r.hset(call.from_user.id, 'weapon', 17)
                        r.hset(call.from_user.id, 's_weapon', 8)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили прапор новоросії')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя')

            elif cl == 8 or cl == 18 or cl == 28:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 9:
                        r.hincrby(call.from_user.id, 'money', -9)
                        r.hset(call.from_user.id, 'weapon', 18)
                        r.hset(call.from_user.id, 's_weapon', 2)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили експлойт')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя')

            elif cl == 9 or cl == 19 or cl == 29:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 10:
                        r.hincrby(call.from_user.id, 'money', -10)
                        r.hset(call.from_user.id, 'weapon', 19)
                        r.hset(call.from_user.id, 's_weapon', 8)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили медичну пилку')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя')
            elif cl == 10 or cl == 20 or cl == 30:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 5:
                        r.hincrby(call.from_user.id, 'money', -5)
                        r.hset(call.from_user.id, 'weapon', 20)
                        r.hset(call.from_user.id, 's_weapon', 10)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили скляну пляшку')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя')

            elif cl == 31 or cl == 32 or cl == 33:
                if int(r.hget(call.from_user.id, 'support')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 15:
                        r.hincrby(call.from_user.id, 'money', -15)
                        r.hset(call.from_user.id, 'support', 2)
                        r.hset(call.from_user.id, 's_support', 5)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили дизель')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є допоміжне спорядження')

            elif cl == 34 or cl == 35 or cl == 36:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    if int(r.hget(call.from_user.id, 'money')) >= 10:
                        r.hincrby(call.from_user.id, 'money', -10)
                        r.hset(call.from_user.id, 'weapon', 21)
                        r.hset(call.from_user.id, 's_weapon', 15)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили палаш')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя')

        else:
            await bot.edit_message_text('Мандрівний торговець повернеться завтра.', call.message.chat.id,
                                        call.message.message_id)
            r.hset('soledar', 'merchant_hour_now', 26)

    elif call.data.startswith('donate'):
        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                        text='Один погон коштує 30 гривень. Для отримання погонів скиньте на карту '
                                             'потрібну суму і введіть боту в пп \n/donated <будь-яке повідомлення>'
                                             '\nНарахування погонів триватиме до 24 годин.')

    elif call.data.startswith('40_packs'):
        if int(r.hget(call.from_user.id, 'strap')) >= 1:
            r.hincrby(call.from_user.id, 'strap', -1)
            r.hincrby(call.from_user.id, 'packs', 40)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно замовили 40 донбаських пакунків')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо погонів на рахунку')

    elif call.data.startswith('buy_resources'):
        if checkClan(call.from_user.id):
            if int(r.hget(call.from_user.id, 'strap')) >= 2:
                r.hincrby(call.from_user.id, 'strap', -2)
                c = 'c' + r.hget(call.from_user.id, 'clan').decode()
                r.hincrby(c, 'r_spirit', 33)
                wood(c, 2222)
                stone(c, 1111)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви успішно замовили ресурси для свого клану')
                try:
                    msg = 'Ваше замовлення прибуло.\n\U0001F333 2222 \U0001faa8 1111 \U0001F47E 33'
                    await bot.send_message(int(r.hget(call.from_user.id, 'clan')), msg)
                except:
                    pass
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо погонів на рахунку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Ти не в клані')

    elif call.data.startswith('premium1'):
        if int(r.hget(call.from_user.id, 'strap')) >= 1 and int(r.hget(call.from_user.id, 'class')) > 0:
            r.hincrby(call.from_user.id, 'strap', -1)
            cl = int(r.hget(call.from_user.id, 'class'))
            if cl == 1 or cl == 11 or cl == 21:
                r.hset(call.from_user.id, 'photo', premium[0])
            elif cl == 2 or cl == 12 or cl == 22:
                r.hset(call.from_user.id, 'photo', premium[1])
            elif cl == 3 or cl == 13 or cl == 23:
                r.hset(call.from_user.id, 'photo', premium[2])
            elif cl == 4 or cl == 14 or cl == 24:
                r.hset(call.from_user.id, 'photo', premium[3])
            elif cl == 5 or cl == 15 or cl == 25:
                r.hset(call.from_user.id, 'photo', premium[4])
            elif cl == 6 or cl == 16 or cl == 26:
                r.hset(call.from_user.id, 'photo', premium[5])
            elif cl == 7 or cl == 17 or cl == 27:
                r.hset(call.from_user.id, 'photo', premium[6])
            elif cl == 8 or cl == 18 or cl == 28:
                r.hset(call.from_user.id, 'photo', premium[7])
            elif cl == 9 or cl == 19 or cl == 29:
                r.hset(call.from_user.id, 'photo', premium[8])
            elif cl == 10 or cl == 20 or cl == 30:
                r.hset(call.from_user.id, 'photo', premium[9])
            elif cl == 31 or cl == 32 or cl == 33:
                r.hset(call.from_user.id, 'photo', premium[10])
            elif cl == 34 or cl == 35 or cl == 36:
                r.hset(call.from_user.id, 'photo', premium[11])
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно змінили фото русаку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо погонів на рахунку, або русак без класу')

    elif call.data.startswith('premium2'):
        if int(r.hget(call.from_user.id, 'strap')) >= 1 and r.hexists(call.from_user.id, 'name'):
            r.hincrby(call.from_user.id, 'strap', -1)
            cl = int(r.hget(call.from_user.id, 'class'))
            if cl == 0:
                r.hset(call.from_user.id, 'photo', default[4])
            elif cl == 1 or cl == 11 or cl == 21:
                r.hset(call.from_user.id, 'photo', chm[0])
            elif cl == 2 or cl == 12 or cl == 22:
                r.hset(call.from_user.id, 'photo', chm[1])
            elif cl == 3 or cl == 13 or cl == 23:
                r.hset(call.from_user.id, 'photo', chm[2])
            elif cl == 4 or cl == 14 or cl == 24:
                r.hset(call.from_user.id, 'photo', chm[3])
            elif cl == 5 or cl == 15 or cl == 25:
                r.hset(call.from_user.id, 'photo', chm[4])
            elif cl == 6 or cl == 16 or cl == 26:
                r.hset(call.from_user.id, 'photo', chm[5])
            elif cl == 7 or cl == 17 or cl == 27:
                r.hset(call.from_user.id, 'photo', chm[6])
            elif cl == 8 or cl == 18 or cl == 28:
                r.hset(call.from_user.id, 'photo', chm[7])
            elif cl == 9 or cl == 19 or cl == 29:
                r.hset(call.from_user.id, 'photo', chm[8])
            elif cl == 10 or cl == 20 or cl == 30:
                r.hset(call.from_user.id, 'photo', chm[9])
            elif cl == 31 or cl == 32 or cl == 33:
                r.hset(call.from_user.id, 'photo', chm[10])
            elif cl == 34 or cl == 35 or cl == 36:
                r.hset(call.from_user.id, 'photo', chm[11])
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно змінили фото русаку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо погонів на рахунку, або русак без класу')

    elif call.data.startswith('premium3'):
        if int(r.hget(call.from_user.id, 'strap')) >= 1 and int(r.hget(call.from_user.id, 'class')) > 0:
            r.hincrby(call.from_user.id, 'strap', -1)
            cl = int(r.hget(call.from_user.id, 'class'))
            if cl == 1 or cl == 11 or cl == 21:
                r.hset(call.from_user.id, 'photo', premium2[0])
            elif cl == 2 or cl == 12 or cl == 22:
                r.hset(call.from_user.id, 'photo', premium2[1])
            elif cl == 3 or cl == 13 or cl == 23:
                r.hset(call.from_user.id, 'photo', premium2[2])
            elif cl == 4 or cl == 14 or cl == 24:
                r.hset(call.from_user.id, 'photo', premium2[3])
            elif cl == 5 or cl == 15 or cl == 25:
                r.hset(call.from_user.id, 'photo', premium2[4])
            elif cl == 6 or cl == 16 or cl == 26:
                r.hset(call.from_user.id, 'photo', premium2[5])
            elif cl == 7 or cl == 17 or cl == 27:
                r.hset(call.from_user.id, 'photo', premium2[6])
            elif cl == 8 or cl == 18 or cl == 28:
                r.hset(call.from_user.id, 'photo', premium2[7])
            elif cl == 9 or cl == 19 or cl == 29:
                r.hset(call.from_user.id, 'photo', premium2[8])
            elif cl == 10 or cl == 20 or cl == 30:
                r.hset(call.from_user.id, 'photo', premium2[9])
            elif cl == 31 or cl == 32 or cl == 33:
                r.hset(call.from_user.id, 'photo', premium2[10])
            elif cl == 34 or cl == 35 or cl == 36:
                r.hset(call.from_user.id, 'photo', premium2[11])
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно змінили фото русаку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо погонів на рахунку, або русак без класу')

    elif call.data.startswith('hawthorn'):
        if int(r.hget(call.from_user.id, 'strength')) < 1000 and int(r.hget(call.from_user.id, 'intellect')) < 5:
            if int(r.hget(call.from_user.id, 'strap')) >= 1 and r.hexists(call.from_user.id, 'name') == 1:
                r.hincrby(call.from_user.id, 'strap', -1)
                r.hincrby(call.from_user.id, 'strength', 400)
                r.hincrby(call.from_user.id, 'intellect', 4)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви успішно купили настоянку глоду')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо погонів на рахунку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Твій русак не отримає жодного ефекту від цього товару')
    elif call.data.startswith('course'):
        cl = int(r.hget(call.from_user.id, 'class'))
        if int(r.hget(call.from_user.id, 'strap')) >= 2 and cl > 0:
            r.hincrby(call.from_user.id, 'strap', -2)
            if cl == 21:
                r.hincrby(call.from_user.id, 'strength', -200)
            r.srem('class-' + str(cl), call.from_user.id)
            r.hset(call.from_user.id, 'class', 0)
            if int(r.hget(call.from_user.id, 'intellect')) < 5:
                r.hset(call.from_user.id, 'intellect', 5)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно купили курс перекваліфікаації русаку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо погонів на рахунку, або русак без класу')

    elif call.data.startswith('fast_cellar'):
        if int(r.hget(call.from_user.id, 's3')) <= 2:
            if int(r.hget(call.from_user.id, 'strap')) >= 3:
                r.hincrby(call.from_user.id, 'strap', -3)
                r.hset(call.from_user.id, 's3', 5)
                r.hset(call.from_user.id, 'name2', randint(0, len(names) - 1),
                       {'strength2': randint(10, 50),
                        'intellect2': int(choice(['1', '1', '1', '1', '2'])),
                        'spirit2': 0, 'weapon2': 0, 's_weapon2': 0, 'defense2': 0, 's_defense2': 0,
                        'mushrooms2': 0, 'class2': 0, 'photo2': choice(default), 'injure2': 0, 'hp2': 100,
                        'support2': 0, 's_support2': 0, 'sch2': 0, 'buff2': 0, 'head2': 0, 's_head2': 0})
                r.hset(call.from_user.id, 'time22', 0)
                r.hset(call.from_user.id, 'time23', 0)
                r.sadd('swappers', call.from_user.id)
                await bot.send_message(call.message.chat.id, '\U0001F412 У вас з`явився другий русак.\n'
                                                             'Змінити бойового русака можна командою /swap.')
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви успішно побудували підвал максимального рівня')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо погонів на рахунку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Пізно пришвидшувати будівництво')

    elif call.data.startswith('drop_w') and call.from_user.id == call.message.reply_to_message.from_user.id:
        if int(r.hget(call.from_user.id, 'weapon')) != 0:
            if int(r.hget(call.from_user.id, 'weapon')) == 16:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Зброю мусора неможливо викинути')
            else:
                r.hset(call.from_user.id, 'weapon', 0)
                r.hset(call.from_user.id, 's_weapon', 0)
                cl = int(r.hget(call.from_user.id, 'class'))
                if cl == 6 or cl == 16 or cl == 26:
                    r.hset(call.from_user.id, 'weapon', 16)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Русак викинув зброю')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='В твого русака нема зброї')

    elif call.data.startswith('drop_d') and call.from_user.id == call.message.reply_to_message.from_user.id:
        if int(r.hget(call.from_user.id, 'defense')) != 0:
            r.hset(call.from_user.id, 'defense', 0)
            r.hset(call.from_user.id, 's_defense', 0)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Русак викинув захисне спорядження')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='В твого русака нема захисного спорядження')

    elif call.data.startswith('drop_s') and call.from_user.id == call.message.reply_to_message.from_user.id:
        if int(r.hget(call.from_user.id, 'support')) != 0:
            r.hset(call.from_user.id, 'support', 0)
            r.hset(call.from_user.id, 's_support', 0)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Русак викинув допоміжне спорядження')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='В твого русака нема допоміжного спорядження')

    elif call.data.startswith('drop_h') and call.from_user.id == call.message.reply_to_message.from_user.id:
        if int(r.hget(call.from_user.id, 'head')) != 0:
            r.hset(call.from_user.id, 'head', 0)
            r.hset(call.from_user.id, 's_head', 0)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Русак викинув шапку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='В твого русака нема шапки')

    elif call.data.startswith('unpack') and call.from_user.id == call.message.reply_to_message.from_user.id:
        uid = call.from_user.id
        cl = int(r.hget(uid, 'class'))

        if int(r.hget(uid, 'money')) >= 20 or int(r.hget(uid, 'packs')) > 0:
            if int(r.hget(uid, 'packs')) > 0:
                r.hincrby(uid, 'packs', -1)
            else:
                r.hincrby(uid, 'money', -20)
            r.hincrby(uid, 'opened', 1)
            r.hincrby('all_opened', 'packs', 1)

            ran = choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                          weights=[20, 18, 15, 12, 10, 7, 6, 5, 3, 2, 1, 0.45, 0.45, 0.1])
            if ran == [1]:
                if checkClan(uid, base=4, building='new_post') and choice([0, 1]) == 1:
                    await bot.edit_message_text('\u26AA В пакунку знайдено робочу радіотехніку.\n\U0001F4FB +1',
                                                call.message.chat.id, call.message.message_id)
                    r.hincrby('c' + r.hget(uid, 'clan').decode(), 'technics', 1)
                else:
                    await bot.edit_message_text('\u26AA В пакунку знайдено лише пил і гнилі недоїдки.',
                                                call.message.chat.id, call.message.message_id)
            elif ran == [2]:
                await bot.edit_message_text('\u26AA В цьому пакунку лежить якраз те, що потрібно твоєму русаку '
                                            '(класове спорядження)! ' + icons[cl], call.message.chat.id,
                                            call.message.message_id)
                if cl == 1 or cl == 11 or cl == 21:
                    if int(r.hget(uid, 'weapon')) in (11, 22):
                        r.hincrby(uid, 's_weapon', 5)
                        if int(r.hget(uid, 's_weapon')) >= 50:
                            r.hset(uid, 'weapon', 22)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 11)
                        r.hset(uid, 's_weapon', 5)
                elif cl == 2 or cl == 12 or cl == 22:
                    if int(r.hget(uid, 'weapon')) in (12, 23):
                        r.hincrby(uid, 's_weapon', 25)
                        if int(r.hget(uid, 's_weapon')) >= 250:
                            r.hset(uid, 'weapon', 23)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 12)
                        r.hset(uid, 's_weapon', 25)
                elif cl == 3 or cl == 13 or cl == 23:
                    if int(r.hget(uid, 'weapon')) in (13, 24):
                        r.hincrby(uid, 's_weapon', 3)
                        if int(r.hget(uid, 's_weapon')) >= 30:
                            r.hset(uid, 'weapon', 24)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 13)
                        r.hset(uid, 's_weapon', 3)
                elif cl == 4 or cl == 14 or cl == 24:
                    if int(r.hget(uid, 'weapon')) in (14, 25):
                        r.hincrby(uid, 's_weapon', 1)
                        if int(r.hget(uid, 's_weapon')) >= 10:
                            r.hset(uid, 'weapon', 25)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 14)
                        r.hset(uid, 's_weapon', 1)
                elif cl == 5 or cl == 15 or cl == 25:
                    if int(r.hget(uid, 'weapon')) in (15, 26):
                        r.hincrby(uid, 's_weapon', 30)
                        if int(r.hget(uid, 's_weapon')) >= 300:
                            r.hset(uid, 'weapon', 26)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 15)
                        r.hset(uid, 's_weapon', 30)
                elif cl == 6 or cl == 16 or cl == 26:
                    if int(r.hget(uid, 'defense')) in (16, 17):
                        r.hincrby(uid, 's_defense', 10)
                        if int(r.hget(uid, 's_defense')) >= 100:
                            r.hset(uid, 'defense', 17)
                    elif int(r.hget(uid, 'defense')) != 2:
                        r.hset(uid, 'defense', 16)
                        r.hset(uid, 's_defense', 10)
                elif cl == 7 or cl == 17 or cl == 27:
                    if int(r.hget(uid, 'weapon')) in (17, 28):
                        r.hincrby(uid, 's_weapon', 8)
                        if int(r.hget(uid, 's_weapon')) >= 80:
                            r.hset(uid, 'weapon', 28)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 17)
                        r.hset(uid, 's_weapon', 8)
                elif cl == 8 or cl == 18 or cl == 28:
                    if int(r.hget(uid, 'weapon')) in (18, 29):
                        r.hincrby(uid, 's_weapon', 2)
                        if int(r.hget(uid, 's_weapon')) >= 20:
                            r.hset(uid, 'weapon', 29)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 18)
                        r.hset(uid, 's_weapon', 2)
                elif cl == 9 or cl == 19 or cl == 29:
                    if int(r.hget(uid, 'weapon')) in (19, 30):
                        r.hincrby(uid, 's_weapon', 8)
                        if int(r.hget(uid, 's_weapon')) >= 80:
                            r.hset(uid, 'weapon', 30)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 19)
                        r.hset(uid, 's_weapon', 8)
                elif cl == 10 or cl == 20 or cl == 30:
                    if int(r.hget(uid, 'weapon')) in (20, 31):
                        r.hincrby(uid, 's_weapon', 10)
                        if int(r.hget(uid, 's_weapon')) >= 100:
                            r.hset(uid, 'weapon', 31)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 20)
                        r.hset(uid, 's_weapon', 10)
                elif cl == 31 or cl == 32 or cl == 33:
                    if int(r.hget(uid, 'support')) in (2, 9):
                        r.hincrby(uid, 's_support', 5)
                        if int(r.hget(uid, 's_support')) >= 50:
                            r.hset(uid, 'support', 9)
                    elif int(r.hget(uid, 'support')) not in (6, 7):
                        r.hset(uid, 'support', 2)
                        r.hset(uid, 's_support', 5)
                elif cl == 34 or cl == 35 or cl == 36:
                    if int(r.hget(uid, 'weapon')) in (21, 32):
                        r.hincrby(uid, 's_weapon', 15)
                        if int(r.hget(uid, 's_weapon')) >= 150:
                            r.hset(uid, 'weapon', 32)
                    elif int(r.hget(uid, 'weapon')) != 2:
                        r.hset(uid, 'weapon', 21)
                        r.hset(uid, 's_weapon', 15)
                else:
                    await bot.edit_message_text('\u26AA В цьому пакунку лежать дивні речі, якими '
                                                'русак не вміє користуватись...', call.message.chat.id,
                                                call.message.message_id)
            elif ran == [3]:
                await bot.edit_message_text('\u26AA Знайдено: \U0001F6E1\U0001F5E1 Колючий комплект (дрин і щит).',
                                            call.message.chat.id, call.message.message_id)
                if int(r.hget(uid, 'weapon')) == 0:
                    r.hset(uid, 'weapon', 1)
                    r.hset(uid, 's_weapon', 1)
                elif int(r.hget(uid, 'weapon')) == 1:
                    r.hincrby(uid, 's_weapon', 1)
                if int(r.hget(uid, 'defense')) == 0:
                    r.hset(uid, 'defense', 1)
                    r.hset(uid, 's_defense', 1)
                elif int(r.hget(uid, 'defense')) == 1:
                    r.hincrby(uid, 's_defense', 1)
            elif ran == [4]:
                await bot.edit_message_text('\u26AA Знайдено: пошкоджений уламок бронетехніки (здати на металобрухт).'
                                            '\n\U0001F4B5 + 4', call.message.chat.id, call.message.message_id)
                r.hincrby(uid, 'money', 4)
            elif ran == [5]:
                await bot.edit_message_text('\u26AA Знайдено: \U0001F6E1 Уламок бронетехніки.\n\U0001F6E1 +7',
                                            call.message.chat.id, call.message.message_id)
                if int(r.hget(uid, 'defense')) == 0 or int(r.hget(uid, 'defense')) == 1 or \
                        int(r.hget(uid, 'defense')) == 3:
                    r.hset(uid, 'defense', 9)
                    r.hset(uid, 's_defense', 7)
                else:
                    r.hincrby(uid, 's_defense', 7)
            elif ran == [6]:
                await bot.edit_message_text('\U0001f535 Знайдено: \U0001F4B5 50 гривень.',
                                            call.message.chat.id, call.message.message_id)
                r.hincrby(uid, 'money', 50)
            elif ran == [7]:
                vo = 0
                for v in range(20):
                    vo += int(vodka(uid))
                await bot.edit_message_text('\U0001f535 Цей пакунок виявився ящиком горілки.\n\u2622 +20 \U0001F54A +' +
                                            str(vo), call.message.chat.id, call.message.message_id)
            elif ran == [8]:
                await bot.edit_message_text('\U0001f535 В цьому пакунку лежить мертвий русак...\n\u2620\uFE0F +1',
                                            call.message.chat.id, call.message.message_id)
                r.hincrby(uid, 'deaths', 1)
                r.hincrby('all_deaths', 'deaths', 1)
            elif ran == [9]:
                if int(r.hget(uid, 'intellect')) < 20:
                    await bot.edit_message_text('\U0001f7e3 Знайдено: \U0001F6E1 Мухомор королівський.',
                                                call.message.chat.id, call.message.message_id)
                    if int(r.hget(uid, 'support')) != 6:
                        r.hset(uid, 'support', 6)
                        r.hset(uid, 's_support', 1)
                    elif int(r.hget(uid, 'support')) == 6:
                        r.hincrby(uid, 's_support', 1)
                else:
                    await bot.edit_message_text('\u26AA В пакунку знайдено лише пил і гнилі недоїдки.',
                                                call.message.chat.id, call.message.message_id)
            elif ran == [10]:
                msg = '\U0001f7e3 В пакунку знайдено кілька упаковок фольги. З неї можна зробити непогану шапку ' \
                      'для русака.\n'
                if int(r.hget(uid, 'head')) == 1:
                    r.hincrby(uid, 'sch', 30)
                    r.hincrby(uid, 's_head', 20)
                    msg += '\U0001F464 +30'
                elif int(r.hget(uid, 'head')) not in (2, 3, 4):
                    r.hset(uid, 'sch', 30)
                    r.hset(uid, 'head', 1)
                    r.hset(uid, 's_head', 20)
                    msg += '\U0001F464 +30'
                else:
                    msg += 'Але в цьому немає потреби.\n\U0001F464 +10'
                    r.hincrby(uid, 'sch', 10)
                await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id)
            elif ran == [11]:
                emoji = choice(['\U0001F35C', '\U0001F35D', '\U0001F35B', '\U0001F957', '\U0001F32D'])
                await bot.edit_message_text('\U0001f7e3 Крім гаманця з грошима, в цьому пакунку лежить багато гнилої'
                                            ' бараболі і закруток з помідорами (можна згодувати русаку).'
                                            '\n\u2B50 +1 \U0001F4B5 +300 ' + emoji + ' +1',
                                            call.message.chat.id, call.message.message_id)
                r.hincrby(uid, 'money', 300)
                r.hset(uid, 'time', 0)
                if r.hexists(uid, 'ac13') == 0:
                    r.hset(uid, 'ac13', 1)
            elif ran == [12]:
                await bot.edit_message_text(
                    '\U0001f7e1 В цьому пакунку знайдено неушкоджений Бронежилет вагнерівця [Захист, '
                    'міцність=50] - зменшує силу ворога на бій на 75% та захищає від РПГ-7.',
                    call.message.chat.id, call.message.message_id)
                if int(r.hget(uid, 'defense')) == 2:
                    r.hincrby(uid, 's_defense', 50)
                else:
                    r.hset(uid, 'defense', 2)
                    r.hset(uid, 's_defense', 50)
            elif ran == [13]:
                await bot.edit_message_text('\U0001f7e1 В цьому пакунку знайдено 40-мм ручний протитанковий гранатомет '
                                            'РПГ-7 і одну гранату до нього [Атака, міцність=1] - завдає ворогу важке по'
                                            'ранення (віднімає бойовий дух, здоров`я і все спорядження, на 300 боїв '
                                            'бойовий дух впаде вдвічі а сила втричі).',
                                            call.message.chat.id, call.message.message_id)
                if int(r.hget(uid, 'weapon')) == 2:
                    r.hincrby(uid, 's_weapon', 1)
                else:
                    r.hset(uid, 'weapon', 2)
                    r.hset(uid, 's_weapon', 1)
            elif ran == [14]:
                await bot.edit_message_text(
                    '\U0001f7e1 В пакунку лежить дорога парадна форма якогось російського генерала.'
                    '\n\U0001F31F +1',
                    call.message.chat.id, call.message.message_id)
                r.hincrby(uid, 'strap', 1)
        else:
            try:
                await bot.edit_message_text('Недостатньо коштів на рахунку.', call.message.chat.id,
                                            call.message.message_id)
            except:
                pass

    elif call.data.startswith('clan_shop_1'):
        msg, markup = c_shop('c' + str(call.message.chat.id), 1)
        await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data.startswith('clan_shop_2'):
        msg, markup = c_shop('c' + str(call.message.chat.id), 2)
        await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data.startswith('clan_shop_3'):
        msg, markup = c_shop('c' + str(call.message.chat.id), 3)
        await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data.startswith('ration'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            price = 4 if int(r.hget('c' + str(call.message.chat.id), 'side')) == 1 else 10
            if int(r.hget(call.from_user.id, 'money')) >= price:
                r.hincrby(call.from_user.id, 'money', -price)
                ran = randint(1, 3)
                if ran == 1:
                    spirit(1000, call.from_user.id, 0)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Русак їсть пломбір, і думає про те, як '
                                                         'класно жилось при Сталінє...\n\U0001F54A +1000')
                elif ran == 2:
                    spirit(1000, call.from_user.id, 0)
                    if randint(1, 2) == 1:
                        msg = '\U0001F464 +5'
                        r.hincrby(call.from_user.id, 'sch', 5)
                    else:
                        increase_trance(5, call.from_user.id)
                        msg = '\U0001F44A +5'
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Русак їсть ковбасу і згадує про воювавших '
                                                         'дідів...\n\U0001F54A 1000 ' + msg)
                elif ran == 3:
                    if int(r.hget(call.from_user.id, 'support')) > 0:
                        spirit(3000, call.from_user.id, 0)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Русак їсть хліб, і сумує через розпад совка...'
                                                             '\n\U0001F54A +3000')
                    else:
                        r.hset(call.from_user.id, 'support', 5)
                        r.hset(call.from_user.id, 's_support', 1)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Русак понадкушував хліб і залишив на потім...')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_fragment'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'money')) >= 15:
                if int(r.hget(call.from_user.id, 'defense')) == 0 or int(r.hget(call.from_user.id, 'defense')) == 1:
                    r.hset(call.from_user.id, 'defense', 9)
                    r.hset(call.from_user.id, 's_defense', 7)
                    r.hincrby(call.from_user.id, 'money', -15)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили уламок бронетехніки')
                elif int(r.hget(call.from_user.id, 's_defense')) < 50:
                    r.hincrby(call.from_user.id, 's_defense', 7)
                    r.hincrby(call.from_user.id, 'money', -15)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили уламок бронетехніки')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ваша броня вже достатньо міцна')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_helmet'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'money')) >= 50:
                if int(r.hget(call.from_user.id, 'head')) == 0:
                    r.hset(call.from_user.id, 'head', 2)
                    r.hset(call.from_user.id, 's_head', 40)
                    r.hincrby(call.from_user.id, 'money', -50)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили тактичний шолом')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є шапка.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_bombs'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'money')) >= 20:
                if int(r.hget(call.from_user.id, 'defense')) == 0:
                    r.hset(call.from_user.id, 'defense', 3)
                    r.hset(call.from_user.id, 's_defense', 3)
                    r.hincrby(call.from_user.id, 'money', -20)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили міни')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є захисне спорядження.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_lash'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'money')) >= 60:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    r.hset(call.from_user.id, 'weapon', 3)
                    r.hset(call.from_user.id, 's_weapon', 3)
                    r.hincrby(call.from_user.id, 'money', -60)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили батіг')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_mushroom'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'money')) >= 100:
                if int(r.hget(call.from_user.id, 'support')) == 0:
                    if int(r.hget(call.from_user.id, 'intellect')) < 20:
                        r.hset(call.from_user.id, 'support', 6)
                        r.hset(call.from_user.id, 's_support', 1)
                        r.hincrby(call.from_user.id, 'money', -100)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили мухомор королівський.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ваш русак вже занадто розумний.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є допоміжне спорядження.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_diesel'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'class')) in (31, 32, 33):
                if int(r.hget(call.from_user.id, 'money')) >= 20:
                    if int(r.hget(call.from_user.id, 'support')) == 0:
                        r.hset(call.from_user.id, 'support', 2)
                        r.hset(call.from_user.id, 's_support', 5)
                        r.hincrby(call.from_user.id, 'money', -20)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили дизель.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='У вас вже є допоміжне спорядження.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Дизель можна купити тільки таксистам.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_ak'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'money')) >= 15:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    r.hset(call.from_user.id, 'weapon', 15)
                    r.hset(call.from_user.id, 's_weapon', 30)
                    r.hincrby(call.from_user.id, 'money', -15)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили АК-47.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_ear'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'money')) >= 20:
                if int(r.hget(call.from_user.id, 'head')) == 0:
                    r.hset(call.from_user.id, 'head', 4)
                    r.hset(call.from_user.id, 's_head', 20)
                    r.hincrby(call.from_user.id, 'money', -20)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили вушанку.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є шапка.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_sugar'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'money')) >= 55:
                if int(r.hget(call.from_user.id, 'support')) == 0:
                    r.hset(call.from_user.id, 'support', 7)
                    r.hset(call.from_user.id, 's_support', 1)
                    r.hincrby(call.from_user.id, 'money', -55)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили цукор.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є допоміжне спорядження.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_kvs'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'money')) >= 15:
                if int(r.hget(call.from_user.id, 'support')) == 0:
                    r.hset(call.from_user.id, 'support', 8)
                    r.hset(call.from_user.id, 's_support', 5)
                    r.hincrby(call.from_user.id, 'money', -15)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили квас.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є допоміжне спорядження.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_foil'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'money')) >= 50:
                if int(r.hget(call.from_user.id, 'head')) == 0:
                    r.hset(call.from_user.id, 'head', 1)
                    r.hset(call.from_user.id, 's_head', 10)
                    r.hincrby(call.from_user.id, 'sch', 30)
                    r.hincrby(call.from_user.id, 'money', -50)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили шапочку з фольги')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є шапка.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_children'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'money')) >= 100:
                r.hincrby(call.from_user.id, 'money', -100)
                r.hincrby(call.from_user.id, 'childs', 1)
                r.hincrby('all_children', 'children', 1)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви успішно купили російське немовля.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('clan_uav'):
        if str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            if int(r.hget(call.from_user.id, 'money')) >= 50:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    r.hset(call.from_user.id, 'weapon', 5)
                    r.hset(call.from_user.id, 's_weapon', 1)
                    r.hincrby(call.from_user.id, 'money', -50)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили БпЛА.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Клановий магазин тільки для учасників клану.')

    elif call.data.startswith('monument'):
        c = 'c' + str(call.message.chat.id)
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, call.message.chat.id):
            if int(r.hget(c, 'r_spirit')) >= 10:
                r.hincrby(c, 'r_spirit', -10)
                s = 1 if int(r.hget(c, 'side')) == 2 else 0
                for mem in r.smembers('cl' + str(call.message.chat.id)):
                    increase_trance(5, mem)
                    if s == 1:
                        spirit(int(int(r.hget(mem, 'spirit')) * 0.5), mem, 0)
                await bot.send_message(call.message.chat.id, '\U0001F44A Клан готовий йти в бій.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Це може зробити тільки лідер чи заступник.')

    elif call.data.startswith('clan_spike'):
        c = 'c' + str(call.message.chat.id)
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, call.message.chat.id):
            if int(r.hget(c, 'wood')) >= 200 and int(r.hget(c, 'stone')) >= 100:
                r.hincrby(c, 'wood', -200)
                r.hincrby(c, 'stone', -100)
                for mem in r.smembers('cl' + str(call.message.chat.id)):
                    if int(r.hget(mem, 'weapon')) == 0:
                        r.hset(mem, 'weapon', 1)
                        r.hset(mem, 's_weapon', 1)
                    if int(r.hget(mem, 'defense')) == 0:
                        r.hset(mem, 'defense', 1)
                        r.hset(mem, 's_defense', 1)
                await bot.send_message(call.message.chat.id, '\U0001F5E1\U0001F6E1 Клан готовий йти в бій.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Це може зробити тільки лідер чи заступник.')

    elif call.data.startswith('clan_vodka'):
        c = 'c' + str(call.message.chat.id)
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, call.message.chat.id):
            if int(r.hget(c, 'money')) >= 300:
                r.hincrby(c, 'money', -300)
                for mem in r.smembers('cl' + str(call.message.chat.id)):
                    if int(r.hget(mem, 'clan_time')) == datetime.now().day:
                        r.hincrby(mem, 'vodka', 9)
                        r.hincrby('all_vodka', 'vodka', 9)
                        spirit(int(vodka(mem)) * 9, mem, 0)
                await bot.send_message(call.message.chat.id, '\u2622 Клан святкує відпрацьовану зміну.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Це може зробити тільки лідер чи заступник.')

    elif call.data.startswith('clan_rpg'):
        c = 'c' + str(call.message.chat.id)
        if checkClan(call.from_user.id) and call.from_user.id == int(r.hget(c, 'leader')):
            if int(r.hget(c, 'money')) >= 2000 and int(r.hget(c, 'r_spirit')) >= 200:
                if int(r.hget(call.from_user.id, 'weapon')) == 0:
                    r.hset(call.from_user.id, 'weapon', 2)
                    r.hset(call.from_user.id, 's_weapon', 1)
                    r.hincrby(c, 'money', -2000)
                    r.hincrby(c, 'r_spirit', -200)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили РПГ-7.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є зброя.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Це може зробити тільки лідер.')

    elif call.data.startswith('clan_armor'):
        c = 'c' + str(call.message.chat.id)
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, call.message.chat.id):
            if int(r.hget(c, 'money')) >= 1000 and int(r.hget(c, 'r_spirit')) >= 50:
                if int(r.hget(call.from_user.id, 'defense')) == 0:
                    r.hset(call.from_user.id, 'defense', 2)
                    r.hset(call.from_user.id, 's_defense', 50)
                    r.hincrby(c, 'money', -1000)
                    r.hincrby(c, 'r_spirit', -50)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили бронежилет вагнерівця.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас вже є захисне спорядження.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Це може зробити тільки лідер чи заступник.')

    elif call.data.startswith('clan_watermelon'):
        c = 'c' + str(call.message.chat.id)
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, call.message.chat.id):
            if int(r.hget(c, 'money')) >= 200 and int(r.hget(c, 'r_spirit')) >= 50:
                r.hincrby(c, 'money', -200)
                r.hincrby(c, 'r_spirit', -50)
                for mem in r.smembers('cl' + str(call.message.chat.id)):
                    if int(r.hget(mem, 'head')) == 0:
                        r.hset(mem, 'head', 3)
                        r.hset(mem, 's_head', 1)
                await bot.send_message(call.message.chat.id, '\U0001F349 Клан очманів від бази.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Це може зробити тільки лідер чи заступник.')

    elif call.data.startswith('clan_heal'):
        c = 'c' + str(call.message.chat.id)
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, call.message.chat.id):
            if int(r.hget(c, 'money')) >= 10:
                r.hincrby(c, 'money', -10)
                for mem in r.smembers('cl' + str(call.message.chat.id)):
                    hp(100, mem)
                await bot.send_message(call.message.chat.id, '\U0001fac0 Клан вилікувано.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Це може зробити тільки лідер чи заступник.')

    elif call.data.startswith('clan_money'):
        c = 'c' + str(call.message.chat.id)
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, call.message.chat.id):
            if int(r.hget(c, 'money')) >= 500 and int(r.hget(c, 'r_spirit')) >= 10:
                r.hincrby(c, 'money', -500)
                r.hincrby(c, 'r_spirit', -10)
                rating = {}
                for mem in r.smembers('cl' + str(call.message.chat.id)):
                    rating.update({mem: int(r.hget(mem, 'money'))})
                s_rating = sorted(rating, key=rating.get, reverse=False)
                n = 0
                for i in s_rating:
                    n += 1
                    if n == 6:
                        break
                    r.hincrby(i, 'money', 100)
                await bot.send_message(call.message.chat.id, '\U0001F4B5 Деякі учасники отримали соціальні виплати.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Це може зробити тільки лідер чи заступник.')

    elif call.data.startswith('clan_sell_'):
        c = 'c' + str(call.message.chat.id)
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, call.message.chat.id):
            if call.data.startswith('clan_sell_wood') and int(r.hget(c, 'wood')) >= 7500:
                r.hincrby(c, 'money', 500)
                r.hincrby(c, 'wood', -1500)
                r.hincrby('resources', 'wood', 1500)
                await bot.send_message(call.message.chat.id, '\U0001F333 Продано 1500 деревини.')
            elif call.data.startswith('clan_sell_stone') and int(r.hget(c, 'stone')) >= 5000:
                r.hincrby(c, 'money', 500)
                r.hincrby(c, 'stone', -1000)
                r.hincrby('resources', 'stone', 1000)
                await bot.send_message(call.message.chat.id, '\U0001faa8 Продано 1000 каміння.')
            elif call.data.startswith('clan_sell_cloth') and int(r.hget(c, 'cloth')) >= 2500:
                r.hincrby(c, 'money', 500)
                r.hincrby(c, 'cloth', -500)
                r.hincrby('resources', 'cloth', 500)
                await bot.send_message(call.message.chat.id, '\U0001F9F6 Продано 500 тканини.')
            elif call.data.startswith('clan_sell_brick') and int(r.hget(c, 'brick')) >= 1500:
                r.hincrby(c, 'money', 500)
                r.hincrby(c, 'brick', -300)
                r.hincrby('resources', 'brick', 300)
                await bot.send_message(call.message.chat.id, '\U0001F9F1 Продано 300 цегли.')
            elif call.data.startswith('clan_sell_radio') and int(r.hget(c, 'technics')) >= 50:
                r.hincrby(c, 'money', 500)
                r.hincrby(c, 'technics', -50)
                r.hincrby('resources', 'technics', 50)
                await bot.send_message(call.message.chat.id, '\U0001F4FB Продано 50 радіотехніки.')
            elif call.data.startswith('clan_sell_code') and int(r.hget(c, 'codes')) >= 1:
                r.hincrby(c, 'money', 500)
                r.hincrby(c, 'r_spirit', 50)
                r.hincrby(c, 'codes', -1)
                r.hincrby('resources', 'codes', 1)
                await bot.send_message(call.message.chat.id, '\U0001F916 Продано секретний код.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо ресурсів.')
            try:
                msg, markup = c_shop(c, 3)
                await bot.edit_message_text(text=msg, chat_id=call.message.chat.id,
                                            message_id=call.message.message_id, reply_markup=markup)
            except:
                pass
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Це може зробити тільки лідер чи заступник.')

    elif call.data.startswith('clan_buy_'):
        c = 'c' + str(call.message.chat.id)
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, call.message.chat.id):
            if int(r.hget(c, 'money')) >= 2000:
                if call.data.startswith('clan_buy_wood') and int(r.hget('resources', 'wood')) >= 1500:
                    r.hincrby(c, 'money', -2000)
                    r.hincrby(c, 'wood', 1500)
                    r.hincrby('resources', 'wood', -1500)
                    await bot.send_message(call.message.chat.id, '\U0001F333 Придбано 1500 деревини.')
                elif call.data.startswith('clan_buy_stone') and int(r.hget('resources', 'stone')) >= 1000:
                    r.hincrby(c, 'money', -2000)
                    r.hincrby(c, 'stone', 1000)
                    r.hincrby('resources', 'stone', -1000)
                    await bot.send_message(call.message.chat.id, '\U0001faa8 Придбано 1000 каміння.')
                elif call.data.startswith('clan_buy_cloth') and int(r.hget('resources', 'cloth')) >= 500:
                    r.hincrby(c, 'money', -2000)
                    r.hincrby(c, 'cloth', 500)
                    r.hincrby('resources', 'cloth', -500)
                    await bot.send_message(call.message.chat.id, '\U0001F9F6 Придбано 500 тканини.')
                elif call.data.startswith('clan_buy_brick') and int(r.hget('resources', 'brick')) >= 300:
                    r.hincrby(c, 'money', -2000)
                    r.hincrby(c, 'brick', 300)
                    r.hincrby('resources', 'brick', -300)
                    await bot.send_message(call.message.chat.id, '\U0001F9F1 Придбано 300 цегли.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо ресурсів.')
                try:
                    msg, markup = c_shop(c, 3)
                    await bot.edit_message_text(text=msg, chat_id=call.message.chat.id,
                                                message_id=call.message.message_id, reply_markup=markup)
                except:
                    pass
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Це може зробити тільки лідер чи заступник.')


@dp.message_handler()
async def echo(message):
    try:
        try:
            if message.text.startswith('@') and message.text[1:].encode() in r.smembers('run'):
                await message.reply('\u26A0\uFE0F УВАГА! \u26A0\uFE0F\n\nЦей канал розповсюджує фейки.')
            elif str(message.forward_from_chat.id).encode() in r.smembers('rid') or \
                    str(message.from_user.id).encode() in r.smembers('rid'):
                await message.reply('\u26A0\uFE0F УВАГА! \u26A0\uFE0F\n\nЦей канал розповсюджує фейки.')
        except:
            pass
        if 'Кубик' in message.text or 'кубик' in message.text:
            await bot.send_dice(chat_id=message.chat.id, reply_to_message_id=message.message_id)

        elif 'казино' in message.text.lower():
            await bot.send_sticker(message.chat.id,
                                   'CAACAgIAAxkBAAEIjuhhS6oNEVDkBDkBUokJJLjTBRloBAACCQADT9w1GxCgVEna0OwQIQQ',
                                   reply_to_message_id=message.message_id)
        elif 'мавпа' in message.text.lower():
            await bot.send_sticker(message.chat.id,
                                   'CAACAgIAAxkBAAEMZfVim53LeR6F2ivPdG-_GmEUXcigIQACDAgAAnTPIUglz-b_Qh_CJCQE',
                                   reply_to_message_id=message.message_id)
        elif message.text.lower() == 'карта' or message.text.lower() == 'мапа':
            await message.reply('https://deepstatemap.live')

        elif message.text == '\U0001F346':
            await bot.send_sticker(message.chat.id,
                                   'CAACAgEAAxkBAAEJbHxho8TpMNv1z5ilwsnv5-ls4prPZQACowgAAuN4BAABejm_DcUkS2oiBA',
                                   reply_to_message_id=message.message_id)

        elif message.text == '\U0001F351':
            await bot.send_sticker(message.chat.id,
                                   'CAACAgEAAxkBAAEJbIlho8a1VzFNc2lFs2mvQpIDruqNxQAChwgAAuN4BAABd8eOV12a0r4iBA',
                                   reply_to_message_id=message.message_id)

        elif message.text == 'Чат хуйня':
            await message.reply('+')

        elif message.text == 'N':
            await message.answer('I')

        elif message.chat.type == 'private':
            if r.hexists(message.from_user.id, 'intellect') == 1:
                if int(r.hget(message.from_user.id, 'intellect')) >= 5 and \
                        int(r.hget(message.from_user.id, 'class')) == 0:
                    if message.text.startswith('Обираю клас '):
                        if 'Хач' in message.text or 'хач' in message.text:
                            ran = choice(p1)
                            r.hset(message.from_user.id, 'photo', ran)
                            await message.reply_photo(photo=ran, caption='Ти вибрав клас Хач.')
                            r.hset(message.from_user.id, 'class', 1)
                            r.sadd('class-1', message.from_user.id)
                        elif 'Роботяга' in message.text or 'роботяга' in message.text:
                            ran = choice(p2)
                            r.hset(message.from_user.id, 'photo', ran)
                            await message.reply_photo(photo=ran, caption='Ти вибрав клас Роботяга.')
                            r.hset(message.from_user.id, 'class', 2)
                            r.sadd('class-2', message.from_user.id)
                        elif 'Фокусник' in message.text or 'фокусник' in message.text:
                            ran = choice(p3)
                            r.hset(message.from_user.id, 'photo', ran)
                            await message.reply_photo(photo=ran, caption='Ти вибрав клас Фокусник.')
                            r.hset(message.from_user.id, 'class', 3)
                            r.hincrby(message.from_user.id, 'intellect', 1)
                            intellect(1, message.from_user.id)
                            r.sadd('class-3', message.from_user.id)
                        elif 'Язичник' in message.text or 'язичник' in message.text:
                            ran = choice(p4)
                            r.hset(message.from_user.id, 'photo', ran)
                            await message.reply_photo(photo=ran, caption='Ти вибрав клас Язичник.')
                            r.hset(message.from_user.id, 'class', 4)
                            r.sadd('class-4', message.from_user.id)
                        elif 'Гарматне' in message.text or 'гарматне' in message.text:
                            ran = choice(p5)
                            r.hset(message.from_user.id, 'photo', ran)
                            await message.reply_photo(photo=ran, caption='Ти вибрав клас Гарматне м`ясо.')
                            r.hset(message.from_user.id, 'class', 5)
                            r.sadd('class-5', message.from_user.id)
                        elif 'Мусор' in message.text or 'мусор' in message.text:
                            ran = choice(p6)
                            r.hset(message.from_user.id, 'photo', ran)
                            await message.reply_photo(photo=ran, caption='Ти вибрав клас Мусор.')
                            r.hset(message.from_user.id, 'class', 6)
                            r.hset(message.from_user.id, 'weapon', 16)
                            r.sadd('class-6', message.from_user.id)
                        elif 'Малорос' in message.text or 'малорос' in message.text:
                            ran = choice(p7)
                            r.hset(message.from_user.id, 'photo', ran)
                            await message.reply_photo(photo=ran, caption='Ти вибрав клас Малорос.')
                            r.hset(message.from_user.id, 'class', 7)
                            intellect(-2, message.from_user.id)
                            r.sadd('class-7', message.from_user.id)
                        elif 'Хакер' in message.text or 'хакер' in message.text:
                            ran = choice(p8)
                            r.hset(message.from_user.id, 'photo', ran)
                            await message.reply_photo(photo=ran, caption='Ти вибрав клас Хакер.')
                            r.hset(message.from_user.id, 'class', 8)
                            r.sadd('class-8', message.from_user.id)
                        elif 'Медик' in message.text or 'медик' in message.text:
                            ran = choice(p9)
                            r.hset(message.from_user.id, 'photo', ran)
                            await message.reply_photo(photo=ran, caption='Ти вибрав клас Медик.')
                            r.hset(message.from_user.id, 'class', 9)
                            r.sadd('class-9', message.from_user.id)
                        elif 'Гопнік' in message.text or 'гопнік' in message.text:
                            ran = choice(p10)
                            r.hset(message.from_user.id, 'photo', ran)
                            await message.reply_photo(photo=ran, caption='Ти вибрав клас Гопнік.')
                            r.hset(message.from_user.id, 'class', 10)
                            r.sadd('class-10', message.from_user.id)
                        elif 'Таксист' in message.text or 'таксист' in message.text:
                            ran = choice(p11)
                            r.hset(message.from_user.id, 'photo', ran)
                            await message.reply_photo(photo=ran, caption='Ти вибрав клас Таксист.')
                            r.hset(message.from_user.id, 'class', 31)
                            r.sadd('class-31', message.from_user.id)
                        elif 'Офіцер' in message.text or 'офіцер' in message.text:
                            if int(r.hget(message.from_user.id, 'money')) >= 500:
                                r.hincrby(message.from_user.id, 'money', -500)
                                ran = choice(p12)
                                r.hset(message.from_user.id, 'photo', ran)
                                await message.reply_photo(photo=ran, caption='Ти вибрав клас Офіцер.')
                                r.hset(message.from_user.id, 'class', 34)
                                r.sadd('class-34', message.from_user.id)
            if int(r.hget(message.from_user.id, 'intellect')) >= 12:
                if message.text == 'Покращити русака':
                    cl = int(r.hget(message.from_user.id, 'class'))
                    if cl == 1:
                        await message.reply('Ти покращив хача до Борцухи.')
                        r.hset(message.from_user.id, 'class', 11)
                        r.srem('class-1', message.from_user.id)
                        r.sadd('class-11', message.from_user.id)
                    if cl == 2:
                        await message.reply('Ти покращив роботягу до Почесного алкаша.')
                        r.hset(message.from_user.id, 'class', 12)
                        r.srem('class-2', message.from_user.id)
                        r.sadd('class-12', message.from_user.id)
                    if cl == 3:
                        await message.reply('Ти покращив фокусника до Злого генія.')
                        r.hset(message.from_user.id, 'class', 13)
                        intellect(2, message.from_user.id)
                        r.srem('class-3', message.from_user.id)
                        r.sadd('class-13', message.from_user.id)
                    if cl == 4:
                        await message.reply('Ти покращив язичника до Скінхеда.')
                        r.hset(message.from_user.id, 'class', 14)
                        r.srem('class-4', message.from_user.id)
                        r.sadd('class-14', message.from_user.id)
                    if cl == 5:
                        await message.reply('Ти покращив гарматне м`ясо до Орка.')
                        r.hset(message.from_user.id, 'class', 15)
                        r.srem('class-5', message.from_user.id)
                        r.sadd('class-15', message.from_user.id)
                    if cl == 6:
                        await message.reply('Ти покращив мусора до Силовика.')
                        r.hset(message.from_user.id, 'class', 16)
                        r.srem('class-6', message.from_user.id)
                        r.sadd('class-16', message.from_user.id)
                    if cl == 7:
                        await message.reply('Ти покращив малороса до Кремлебота.')
                        r.hset(message.from_user.id, 'class', 17)
                        r.hincrby(message.from_user.id, 'money', 200)
                        r.hset(message.from_user.id, 'mushrooms', 0)
                        r.srem('class-7', message.from_user.id)
                        r.sadd('class-17', message.from_user.id)
                    if cl == 8:
                        await message.reply('Ти покращив хакера до Кіберзлочинця.')
                        r.hset(message.from_user.id, 'class', 18)
                        r.srem('class-8', message.from_user.id)
                        r.sadd('class-18', message.from_user.id)
                    if cl == 9:
                        await message.reply('Ти покращив медика до Нарколога.')
                        r.hset(message.from_user.id, 'class', 19)
                        r.srem('class-9', message.from_user.id)
                        r.sadd('class-19', message.from_user.id)
                    if cl == 10:
                        await message.reply('Ти покращив гопніка до Зека.')
                        r.hset(message.from_user.id, 'class', 20)
                        r.srem('class-10', message.from_user.id)
                        r.sadd('class-20', message.from_user.id)
                    if cl == 31:
                        await message.reply('Ти покращив таксиста до Далекобійника.')
                        r.hset(message.from_user.id, 'class', 32)
                        r.srem('class-31', message.from_user.id)
                        r.sadd('class-32', message.from_user.id)
                    if cl == 34:
                        if int(r.hget(message.from_user.id, 'trophy')) >= 50:
                            r.hincrby(message.from_user.id, 'trophy', -50)
                            await message.reply('Ти покращив офіцера до Воєнного злочинця.')
                            r.hset(message.from_user.id, 'class', 35)
                            r.srem('class-34', message.from_user.id)
                            r.sadd('class-35', message.from_user.id)
            if int(r.hget(message.from_user.id, 'intellect')) >= 20:
                if message.text == 'Вдосконалити русака':
                    cl = int(r.hget(message.from_user.id, 'class'))
                    if cl == 11:
                        await message.reply('Ти покращив борцуху до Грози Кавказу.')
                        r.hset(message.from_user.id, 'class', 21)
                        r.hset(message.from_user.id, 'hach_time2', 0)
                        r.hincrby(message.from_user.id, 'strength', 200)
                        r.srem('class-11', message.from_user.id)
                        r.sadd('class-21', message.from_user.id)
                    if cl == 12:
                        await message.reply('Ти покращив почесного алкаша до П`яного майстра.')
                        r.hset(message.from_user.id, 'class', 22)
                        r.hset(message.from_user.id, 'worker', 0)
                        r.srem('class-12', message.from_user.id)
                        r.sadd('class-22', message.from_user.id)
                    if cl == 13:
                        await message.reply('Ти покращив злого генія до Некроманта.')
                        r.hset(message.from_user.id, 'class', 23)
                        r.srem('class-13', message.from_user.id)
                        r.sadd('class-23', message.from_user.id)
                    if cl == 14:
                        await message.reply('Ти покращив скінхеда до Білого вождя.')
                        r.hset(message.from_user.id, 'class', 24)
                        r.srem('class-14', message.from_user.id)
                        r.sadd('class-24', message.from_user.id)
                    if cl == 15:
                        await message.reply('Ти покращив орка до Героя Новоросії.')
                        r.hset(message.from_user.id, 'class', 25)
                        r.srem('class-15', message.from_user.id)
                        r.sadd('class-25', message.from_user.id)
                    if cl == 16:
                        await message.reply('Ти покращив силовика до Товариша майора.')
                        r.hset(message.from_user.id, 'class', 26)
                        r.srem('class-16', message.from_user.id)
                        r.sadd('class-26', message.from_user.id)
                    if cl == 17:
                        await message.reply('Ти покращив кремлебота до Агента ФСБ.')
                        r.hset(message.from_user.id, 'class', 27)
                        r.hset(message.from_user.id, 'fsb', 0)
                        r.hincrby(message.from_user.id, 'money', 300)
                        r.srem('class-17', message.from_user.id)
                        r.sadd('class-27', message.from_user.id)
                    if cl == 18:
                        await message.reply('Ти покращив кіберзлочинця до Black Hat.')
                        r.hset(message.from_user.id, 'class', 28)
                        r.srem('class-18', message.from_user.id)
                        r.sadd('class-28', message.from_user.id)
                    if cl == 19:
                        await message.reply('Ти покращив нарколога до Патологоанатома')
                        r.hset(message.from_user.id, 'class', 29)
                        r.srem('class-19', message.from_user.id)
                        r.sadd('class-29', message.from_user.id)
                    if cl == 20:
                        await message.reply('Ти покращив зека до Мародера')
                        r.hset(message.from_user.id, 'class', 30)
                        r.srem('class-20', message.from_user.id)
                        r.sadd('class-30', message.from_user.id)
                    if cl == 32:
                        await message.reply('Ти покращив далекобійника до Танкіста')
                        r.hset(message.from_user.id, 'class', 33)
                        r.srem('class-32', message.from_user.id)
                        r.sadd('class-33', message.from_user.id)
                    if cl == 35:
                        if int(r.hget(message.from_user.id, 'strap')) >= 1:
                            r.hincrby(message.from_user.id, 'strap', -1)
                            await message.reply('Ти покращив воєнного злочинця до Генерала.')
                            r.hset(message.from_user.id, 'class', 36)
                            r.srem('class-35', message.from_user.id)
                            r.sadd('class-36', message.from_user.id)

    except:
        pass


@dp.inline_handler(lambda query: len(query.query) == 0)
async def inline_echo(inline_query):
    try:
        markup = InlineKeyboardMarkup()
        call = 'fight' + str(inline_query.from_user.id)
        r1 = InlineQueryResultArticle(
            id='1',
            title='Бій русаків',
            input_message_content=InputTextMessageContent(str(prepare_to_fight(inline_query.from_user.id,
                                                                               inline_query.from_user.first_name,
                                                                               inline_query.query))),
            reply_markup=markup.add(InlineKeyboardButton(text='Атакувати!', callback_data=call)),
            thumb_url='https://i.ibb.co/0nFNwSH/rusak.png',
            description='надери комусь дупу\nнапиши & щоб відкрити інші режими')
        r2 = InlineQueryResultArticle(
            id='2',
            title='Ким ти був в минулому житті?',
            input_message_content=InputTextMessageContent(str('Ким ти був в минулому житті?\n\n' + pastLife())),
            thumb_url='https://i.ibb.co/mJ0SXzL/Past-lives-2-56a6ede63df78cf772910470.jpg',
            description='можливо, воно було не таке нікчемне як зараз')
        r3 = InlineQueryResultArticle(
            id='3',
            title='Куди ти поїдеш на заробітки?',
            input_message_content=InputTextMessageContent(str('Куди ти поїдеш на заробітки?\n\n' + earnings())),
            thumb_url='https://i.ibb.co/ypDcLNc/Polunytsya-e1538080073461.jpg',
            description='добре там є, де нас нема')
        r4 = InlineQueryResultArticle(
            id='4',
            title='Визнач свої політичні координати?',
            input_message_content=InputTextMessageContent(str('Мої політичні координати\n\n' + political())),
            thumb_url='https://i.ibb.co/XbGNVSS/maxresdefault.jpg',
            description='правачок чи лібераха?')
        r5 = InlineQueryResultArticle(
            id='5',
            title='Наскільки ви підходите один одному?',
            input_message_content=InputTextMessageContent('*звук мовчання*'),
            thumb_url='https://i.ibb.co/QDkHD0b/telltaale.jpg',
            description='вибирай дівку і залицяйся')
        r6 = InlineQueryResultArticle(
            id='6',
            title='Питай, що турбує',
            input_message_content=InputTextMessageContent('*звук мовчання*'),
            thumb_url='https://i.ibb.co/qkjYFDF/im610x343-Zelensky-notebook.jpg',
            description='ну тобто треба щось написати')
        r7 = InlineQueryResultArticle(
            id='7',
            title='Зрадометр',
            input_message_content=InputTextMessageContent(str(zradoMoga())),
            thumb_url='https://i.ibb.co/7GJzmc4/Ea-PHB6-EWs-AAVER4.jpg',
            description='допоможе визначитись з певною подією')
        r8 = InlineQueryResultArticle(
            id='8',
            title='Якого розміру в тебе пісюн?',
            input_message_content=InputTextMessageContent(str(penis())),
            thumb_url='https://i.ibb.co/3FQYpgB/photo-2020-08-27-14-49-33.jpg',
            description='роздягайся')
        r9 = InlineQueryResultArticle(
            id='9',
            title='Вибір з кількох варіантів',
            input_message_content=InputTextMessageContent('*звук мовчання*'),
            thumb_url='https://i.ibb.co/HtK6FTR/o-1ej2111rn189p9qrabv1au81o1o1k.jpg',
            description='наприклад, "Бути чи/або не бути?"')
        r10 = InlineQueryResultArticle(
            id='10',
            title='Вибери для себе пиво',
            input_message_content=InputTextMessageContent('Бот радить тобі...\n\n' + beer()),
            thumb_url='https://i.ibb.co/rZbG1fD/image.jpg',
            description='або для когось іншого')
        r11 = InlineQueryResultArticle(
            id='11',
            title='Генератор випадкових чисел',
            input_message_content=InputTextMessageContent(generator(inline_query.query)),
            thumb_url='https://i.ibb.co/3TZsnyj/randomn.png',
            description='введи від 1 до 3 чисел (перші два проміжок, третє кількість)')
        r12 = InlineQueryResultArticle(
            id='12',
            title='Визнач своє походження',
            input_message_content=InputTextMessageContent('Моє походження:\n\n' + race()),
            thumb_url='https://i.ibb.co/7V4QmDL/nations.png',
            description='зараз бот проаналізує твої ДНК...')
        r13 = InlineQueryResultArticle(
            id='13',
            title='Який в тебе гендер?',
            input_message_content=InputTextMessageContent(gender()),
            thumb_url='https://i.ibb.co/LrH2D0W/gender.jpg',
            description='все дуже серйозно')
        r14 = InlineQueryResultArticle(
            id='14',
            title='Віджимайся!',
            input_message_content=InputTextMessageContent('\U0001F4AA Роби ' + roll_push_ups()),
            thumb_url='https://i.ibb.co/xjQ56rR/billy.png',
            description='ти ж цього не зробиш, чи не так?')
        await bot.answer_inline_query(inline_query.id, results=[r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12,
                                                                r13, r14], cache_time=0)
    except:
        pass


@dp.inline_handler(lambda query: query.query.startswith('&'))
async def default_query(inline_query):
    try:
        markup = InlineKeyboardMarkup()
        markup2 = InlineKeyboardMarkup()
        markup3 = InlineKeyboardMarkup()
        call = 'fight' + str(inline_query.from_user.id) + ',' + str(inline_query.query)
        call1 = 'fight' + str(inline_query.from_user.id) + ',' + 'pr,' + str(inline_query.query)
        call2 = 'fight' + str(inline_query.from_user.id) + ',' + 'tr,' + str(inline_query.query)
        r1 = InlineQueryResultArticle(
            id='1',
            title='Пошук суперника по силі',
            input_message_content=InputTextMessageContent(str(prepare_to_fight(inline_query.from_user.id,
                                                                               inline_query.from_user.first_name,
                                                                               inline_query.query))),
            reply_markup=markup.add(InlineKeyboardButton(text='Атакувати!', callback_data=call)),
            thumb_url='https://i.ibb.co/0nFNwSH/rusak.png',
            description='введи різницю сили (мінімум 1)')
        r2 = InlineQueryResultArticle(
            id='2',
            title='Особисте запрошення',
            input_message_content=InputTextMessageContent(str(prepare_to_fight(inline_query.from_user.id,
                                                                               inline_query.from_user.first_name,
                                                                               'pr' + inline_query.query))),
            reply_markup=markup2.add(InlineKeyboardButton(text='Атакувати!', callback_data=call1)),
            thumb_url='https://i.ibb.co/0nFNwSH/rusak.png',
            description='введи @username')
        r3 = InlineQueryResultArticle(
            id='3',
            title='Турнірний режим',
            input_message_content=InputTextMessageContent(str(prepare_to_fight(inline_query.from_user.id,
                                                                               inline_query.from_user.first_name,
                                                                               'tr' + inline_query.query))),
            reply_markup=markup3.add(InlineKeyboardButton(text='Атакувати!', callback_data=call2)),
            thumb_url='https://i.ibb.co/0nFNwSH/rusak.png',
            description='Режим Best of 5. Можна ввести @username. Без нагород.')
        await bot.answer_inline_query(inline_query.id, results=[r1, r2, r3], cache_time=0)
    except:
        pass


@dp.inline_handler(lambda query: len(query.query) > 0)
async def inline_echo(inline_query):
    try:
        r1 = InlineQueryResultArticle(
            id='1',
            title='Ким ' + inline_query.query + ' був в минулому житті?',
            input_message_content=InputTextMessageContent(str('Ким ' + inline_query.query +
                                                              ' був в минулому житті?\n\n' + pastLife())),
            thumb_url='https://i.ibb.co/mJ0SXzL/Past-lives-2-56a6ede63df78cf772910470.jpg',
            description='можливо, воно було не таке нікчемне як зараз')
        r2 = InlineQueryResultArticle(
            id='2',
            title='Куди ' + inline_query.query + ' поїде на заробітки?',
            input_message_content=InputTextMessageContent(str('Куди ' + inline_query.query +
                                                              ' поїде на заробітки?\n\n' + earnings())),
            thumb_url='https://i.ibb.co/ypDcLNc/Polunytsya-e1538080073461.jpg',
            description='добре там є, де нас нема')
        r3 = InlineQueryResultArticle(
            id='3',
            title='Визнач ' + inline_query.query + ' політичні координати',
            input_message_content=InputTextMessageContent(str(inline_query.query + ' політичні координати\n\n' +
                                                              political())),
            thumb_url='https://i.ibb.co/XbGNVSS/maxresdefault.jpg',
            description='правачок чи лібераха?')
        r4 = InlineQueryResultArticle(
            id='4',
            title='Наскільки ви з ' + inline_query.query + ' підходите один одному?',
            input_message_content=InputTextMessageContent(str('Ви з ' + inline_query.query +
                                                              ' підходите один одному на ' + love())),
            thumb_url='https://i.ibb.co/QDkHD0b/telltaale.jpg',
            description='вибирай дівку і залицяйся')
        r5 = InlineQueryResultArticle(
            id='5',
            title='Питай, що турбує',
            input_message_content=InputTextMessageContent(str('\u2753 ' + inline_query.query + '\n\n' + question())),
            thumb_url='https://i.ibb.co/qkjYFDF/im610x343-Zelensky-notebook.jpg',
            description='ну тобто треба щось написати')
        r6 = InlineQueryResultArticle(
            id='6',
            title='Зрадометр',
            input_message_content=InputTextMessageContent(str(inline_query.query + '\n\n' + zradoMoga())),
            thumb_url='https://i.ibb.co/7GJzmc4/Ea-PHB6-EWs-AAVER4.jpg',
            description='допоможе визначитись з певною подією')
        r7 = InlineQueryResultArticle(
            id='7',
            title='Якого розміру в тебе пісюн?',
            input_message_content=InputTextMessageContent(str(penis())),
            thumb_url='https://i.ibb.co/3FQYpgB/photo-2020-08-27-14-49-33.jpg',
            description='роздягайся')
        r8 = InlineQueryResultArticle(
            id='8',
            title='Вибір з кількох варіантів',
            input_message_content=InputTextMessageContent('\u2753' + inline_query.query +
                                                          '\n\n' + choose(inline_query.query)),
            thumb_url='https://i.ibb.co/HtK6FTR/o-1ej2111rn189p9qrabv1au81o1o1k.jpg',
            description='наприклад, "Бути чи/або не бути?"')
        r9 = InlineQueryResultArticle(
            id='9',
            title='Вибери для ' + inline_query.query + ' пиво',
            input_message_content=InputTextMessageContent(inline_query.query + ', я рекомендую тобі тобі...\n\n' +
                                                          beer()),
            thumb_url='https://i.ibb.co/rZbG1fD/image.jpg',
            description='або для когось іншого')
        r10 = InlineQueryResultArticle(
            id='10',
            title='Генератор випадкових чисел',
            input_message_content=InputTextMessageContent(generator(inline_query.query)),
            thumb_url='https://i.ibb.co/3TZsnyj/randomn.png',
            description='введи від 1 до 3 чисел (перші два проміжок, третє кількість)')
        r11 = InlineQueryResultArticle(
            id='11',
            title='Визнач ' + inline_query.query + ' походження',
            input_message_content=InputTextMessageContent('Походження ' + inline_query.query + ':\n\n' + race()),
            thumb_url='https://i.ibb.co/7V4QmDL/nations.png',
            description='зараз бот проаналізує твої ДНК...')
        r12 = InlineQueryResultArticle(
            id='12',
            title='Який в тебе гендер?',
            input_message_content=InputTextMessageContent(gender()),
            thumb_url='https://i.ibb.co/LrH2D0W/gender.jpg',
            description='все дуже серйозно')
        r13 = InlineQueryResultArticle(
            id='13',
            title='Віджимайся!',
            input_message_content=InputTextMessageContent('\U0001F4AA ' + inline_query.query + ', роби ' +
                                                          roll_push_ups()),
            thumb_url='https://i.ibb.co/xjQ56rR/billy.png',
            description='ти ж цього не зробиш, чи не так?')
        await bot.answer_inline_query(inline_query.id, results=[r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12,
                                                                r13], cache_time=0)
    except:
        pass


async def on_startup(dp):
    await bot.set_webhook(environ.get('APP_URL') + TOKEN)
    print(dp.get_current())


async def on_shutdown(dp):
    print(dp.get_current())
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path='/' + TOKEN,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=int(environ.get('PORT', 3001)))
