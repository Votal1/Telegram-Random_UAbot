from random import randint, choice, choices
from datetime import datetime, timedelta
from os import environ
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputTextMessageContent, \
    InlineQueryResultArticle, ChatPermissions
from aiogram.utils.executor import start_webhook
from asyncio import sleep

from config import r, TOKEN, bot, dp
from inline import prepare_to_fight, pastLife, earnings, political, love, \
    question, zradoMoga, penis, choose, beer, generator, race, gender, roll_push_ups, donate_to_zsu
from parameters import spirit, vodka, intellect, hp, damage_weapon, damage_defense, damage_support, damage_head, \
    increase_trance
from fight import fight, war, great_war, start_raid, guard_power
from methods import feed_rusak, mine_salt, checkClan, checkLeader, com, c_shop, top, itop, ctop, \
    wood, stone, cloth, brick, auto_clan_settings, q_points, anti_clicker, msg_fmt


from constants.names import names, names_case
from constants.classes import class_name, icons, icons_simple
from constants.photos import p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, premium, premium2, premium3, default
from content.buttons import battle_button, battle_button_2, battle_button_3, \
    battle_button_4, unpack, gift_unpack, create_clan, clan_set, invite, buy_tools
from content.inventory import show_inventory, drop_item, change_item, upgrade_item, check_set, empty_backpack
from content.merchant import merchant_msg
from content.shop import shop_msg, salt_shop
from content.packs import open_pack, open_pack2, check_slot, open_gift3
from content.quests import quests, quest, re_roll
from content.wiki import wiki_text

from cloudscraper import create_scraper
from bs4 import BeautifulSoup

from PIL import Image
import requests
import logging
import sentry_sdk

sentry_sdk.init(environ.get('SENTRY'), traces_sample_rate=0.1)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['gruz200', 'orki', 'z', 'poter_net', 'fertilizer', 'ruskie_idut_nahuy'])
async def gruz200(message):
    try:
        quest(message.from_user.id, 1, 5)
        scraper = create_scraper(delay=10, browser='chrome')
        url = 'https://index.minfin.com.ua/ua/russian-invading/casualties/'
        page = scraper.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        title = '\U0001F437\U0001F436 Втрати росії на ' + soup.find('span', 'black').text
        d = soup.find('div', 'casualties').find_all('li')
        msg = f'\n\n\u2620\uFE0F Вбито: {d[12].text.split()[4]} {d[12].text.split()[6]}' \
              f'\n\U0001F690 ББМ: {d[1].text.split(maxsplit=2)[2]}' \
              f'\n\U0001F69C Танки: {d[0].text.split(maxsplit=2)[2]}' \
              f'\n\U0001F525 Артилерія: {d[2].text.split(maxsplit=2)[2]}' \
              f'\n\u2708\uFE0F Літаки: {d[5].text.split(maxsplit=2)[2]}' \
              f'\n\U0001F681 Гелікоптери: {d[6].text.split(maxsplit=2)[2]}' \
              f'\n\U0001F6A2 Кораблі та катери: {d[9].text.split(maxsplit=3)[3]}'
        await message.reply(title + msg)
    except:
        await message.reply('index.minfin.com.ua/ua/russian-invading/casualties', disable_web_page_preview=True)


@dp.message_handler(commands=['start'])
async def send_welcome(message):
    if message.chat.type == 'private':
        uid = message.from_user.id
        r.sadd('everyone_3', uid)
        msg = '👋 Вітаю.\n\n' \
              '🐒 Щоб взяти русака напиши команду /donbass\n\n' \
              '📃 Для кращого ознайомлення з грою, переглянь список команд (/commands), особливо ті, які ' \
              'показані в /status\n\n' \
              '⛏ Обов\'язково заходь в <a href="https://t.me/+cClR7rA-sZAyY2Uy">Соледар</a>, ' \
              'особливо коли не маєш з ким грати. Там легко можна знайти собі клан\n\n' \
              '🖲 Введи <code>@RandomUA3bot</code>, щоб почати битву русаків або обрати одну з функцій рандому\n\n' \
              '📚 У /wiki зібрана вся актуальна інфа по грі, а на @randomuanews можна слідкувати за оновленнями\n\n' \
              '🚨 Слід зазначити, що бот може надати карту тривог. Для цього напиши <code>Тривога</code> або /alert'
        await message.reply(msg, disable_web_page_preview=True, parse_mode='HTML')
        '''
        if str(uid).encode() not in r.smembers('sudoers'):
            await message.reply('Почнемо.\n\nЩоб взяти русака напиши команду \n/donbass\n/wiki - вся інфа по грі\n'
                                '/commands - всі команди\n@randomuanews - новини', disable_web_page_preview=True)
        else:
            language_code = message.from_user.language_code
            if not r.hexists(uid, 'language_code'):
                if language_code not in ('uk', 'en'):
                    language_code = 'uk'
                r.hset(uid, 'language_code', language_code)
            else:
                language_code = r.hget(uid, 'language_code').decode()
            msg = get_message(message.from_user.id, 'start', language_code=language_code)
            await message.reply(msg, disable_web_page_preview=True, reply_markup=choose_lang())
        '''


@dp.message_handler(commands=['help'])
async def get_help(message):
    msg = '🐒 Щоб взяти русака напиши команду /donbass\n\n' \
          '📃 Для кращого ознайомлення з грою, переглянь список команд (/commands), особливо ті, які ' \
          'показані в /status\n\n' \
          '⛏ Обов\'язково заходь в <a href="https://t.me/+cClR7rA-sZAyY2Uy">Соледар</a>, ' \
          'особливо коли не маєш з ким грати. Там легко можна знайти собі клан\n\n' \
          '🖲 Введи <code>@RandomUA3bot</code>, щоб почати битву русаків або обрати одну з функцій рандому\n\n' \
          '📚 У /wiki зібрана вся актуальна інфа по грі, а на @randomuanews можна слідкувати за оновленнями\n\n' \
          '🚨 Слід зазначити, що бот може надати карту тривог. Для цього напиши <code>Тривога</code> або /alert'
    await message.reply(msg, disable_web_page_preview=True, parse_mode='HTML')


@dp.message_handler(commands=['links'])
async def handle_links(message):
    await message.reply('<a href="https://t.me/+cClR7rA-sZAyY2Uy">@soledar1</a> - місце, де збираються люди з усіх '
                        'куточків України, щоб похизуватись своїми бойовими русаками!\n'
                        '<a href="https://telegra.ph/Pravila-Soledaru-01-11">Правила</a> чату\n'
                        '@randomuanews - новини, патчноути, опитування\n\n'
                        '@borykva - осередок цебулізму\n'
                        '@ukrnastup - осередок сучасного українського націоналізму\n'
                        '@gatilnia - гумор з однокласників\n'
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
        mute_permissions = ChatPermissions(
            can_send_messages=False
        )
        un_mute_permissions = ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True
        )
        if int(r.hget('f' + str(message.chat.id), 'admin')) == 1:
            if st.status == 'creator' or st.can_restrict_members is True:
                msg = message.reply_to_message.from_user.first_name
                if message.text.startswith('/unmute'):
                    await bot.restrict_chat_member(message.chat.id, uid, permissions=un_mute_permissions)
                    await message.answer('З ' + message.reply_to_message.from_user.first_name + ' знято всі обмеження.')
                else:
                    try:
                        a = message.text.split(' ')
                        if a[1].endswith('m'):
                            await bot.restrict_chat_member(message.chat.id, uid,
                                                           until_date=datetime.now() + timedelta(
                                                               minutes=int(a[1][:-1])), permissions=mute_permissions)
                            msg += ' посидить ' + a[1][:-1] + ' хвилин без права голосу.'
                            await message.answer(msg)
                        elif a[1].endswith('h'):
                            await bot.restrict_chat_member(message.chat.id, uid,
                                                           until_date=datetime.now() + timedelta(hours=int(a[1][:-1])),
                                                           permissions=mute_permissions)
                            msg += ' посидить ' + a[1][:-1] + ' годин без права голосу.'
                            await message.answer(msg)
                        elif a[1].endswith('d'):
                            await bot.restrict_chat_member(message.chat.id, uid,
                                                           until_date=datetime.now() + timedelta(days=int(a[1][:-1])),
                                                           permissions=mute_permissions)
                            msg += ' посидить ' + a[1][:-1] + ' днів без права голосу.'
                            await message.answer(msg)
                        elif a[1].endswith('f'):
                            await bot.restrict_chat_member(message.chat.id, uid, permissions=mute_permissions)
                            msg += ' назавжди залишається без права голосу.'
                            await message.answer(msg)
                        else:
                            raise Exception
                    except:
                        await bot.restrict_chat_member(message.chat.id, uid,
                                                       until_date=datetime.now() + timedelta(hours=12),
                                                       permissions=mute_permissions)
                        msg += ' посидить 12 годин без права голосу.'
                        await message.answer(msg)
    except:
        pass


@dp.message_handler(commands=['moxir'])
async def moxir(message):
    try:
        uid = message.reply_to_message.from_user.id
        st = await bot.get_chat_member(message.chat.id, message.from_user.id)
        moxir_permissions = ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False
        )
        if int(r.hget('f' + str(message.chat.id), 'admin')) == 1:
            if st.status == 'creator' or st.can_restrict_members is True:
                msg = 'У ' + message.reply_to_message.from_user.first_name + ' забрали стікери і медіа'
                try:
                    a = message.text.split(' ')
                    if a[1].endswith('m'):
                        await bot.restrict_chat_member(message.chat.id, uid,
                                                       until_date=datetime.now() + timedelta(minutes=int(a[1][:-1])),
                                                       permissions=moxir_permissions)
                        await message.answer(msg + ' на ' + a[1][:-1] + ' хвилин.')
                    elif a[1].endswith('h'):
                        await bot.restrict_chat_member(message.chat.id, uid,
                                                       until_date=datetime.now() + timedelta(hours=int(a[1][:-1])),
                                                       permissions=moxir_permissions)
                        await message.answer(msg + ' на ' + a[1][:-1] + ' годин.')
                    elif a[1].endswith('d'):
                        await bot.restrict_chat_member(message.chat.id, uid,
                                                       until_date=datetime.now() + timedelta(days=int(a[1][:-1])),
                                                       permissions=moxir_permissions)
                        await message.answer(msg + ' на ' + a[1][:-1] + ' днів.')
                    else:
                        raise Exception
                except:
                    await bot.restrict_chat_member(message.chat.id, uid, permissions=moxir_permissions)
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
            await bot.restrict_chat_member(message.chat.id, message.new_chat_members[0].id,
                                           permissions=ChatPermissions(can_send_messages=False))
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
        pass
        # await bot.send_message(456514639, f'{e}\n{mid}\n{r.hget(mid, "photo").decode()}')


@dp.message_handler(commands=['feed'])
async def feed(message):
    try:
        uid = message.from_user.id
        try:
            r.hset(uid, 'username', message.from_user.username)
            if message.chat.type != 'private':
                r.sadd(message.chat.id, uid)
                r.sadd(111, uid)
            if message.chat.type == 'supergroup':
                r.hset('f' + str(message.chat.id), 'title', message.chat.title)
        except:
            pass
        if not datetime.now().day == int(r.hget(uid, 'time')):
            r.hset(uid, 'time', datetime.now().day)
            quest(uid, 3, 2, 2)
            r.hset(uid, 'hp', 100)
            if checkClan(uid, building='build5', level=2) and\
                    int(r.hget(uid, 'injure')) > 0:
                r.hincrby(uid, 'injure', -30)
                if int(r.hget(uid, 'injure')) < 0:
                    r.hset(uid, 'injure', 0)
            stats = r.hmget(uid, 'strength', 'intellect')
            r_name = names[int(r.hget(uid, 'name'))]
            fr = feed_rusak(int(stats[1]))
            r.hincrby(uid, 'eat', 1)
            success = fr[0]
            cl = int(r.hget(uid, 'class'))
            if cl in (2, 12, 22) or int(r.hget(uid, 'support')) == 10:
                success = 1
            if success == 1:
                if r.hexists(uid, 'cabin') and int(r.hget(uid, 'cabin')) == 1 and int(stats[0]) <= 5000:
                    ran = fr[1] + 15
                    if cl == 20 or cl == 30:
                        ran += 15
                else:
                    ran = fr[1]
                if ran <= 10 and int(r.hget(uid, 's5')) >= 5:
                    ran = 10
                bd = fr[3]
                if int(r.hget(uid, 'support')) == 5:
                    bd = 2
                    damage_support(uid)
                emoji = choice(['\U0001F35C', '\U0001F35D', '\U0001F35B', '\U0001F957', '\U0001F32D'])
                word = 'зросла'
                h = int(r.hget(uid, 'head'))
                ran += 5 if h in (3, 5) else 0
                if h == 5:
                    r.hset(uid, 'head', 0, {'s_head': 0})

                sugar = 0
                if int(r.hget(uid, 'support')) in (7, 12):
                    sugar = 1
                    damage_support(uid)
                elif r.hexists(uid, 'support2') and int(r.hget(uid, 'support2')) == 12:
                    sugar = 1
                    damage_support(uid, second=True)

                if int(stats[0]) > 5000:
                    if int(stats[0]) > 8000:
                        if sugar:
                            decrease = choices([1, 0], [75, 25])
                            increase_trance(5, uid)
                        else:
                            decrease = choices([1, 0], [60, 40])
                    else:
                        if sugar:
                            decrease = choices([1, 0], [95, 5])
                            increase_trance(5, uid)
                        else:
                            decrease = choices([1, 0], [80, 20])
                    if decrease == [0]:
                        word = 'зменшилась'
                        ran = -ran
                        if int(r.hget(uid, 'head')) == 3:
                            if checkClan(uid, building='build5', level=2):
                                r.hset(uid, 'head', 5, {'s_head': 1})
                            else:
                                r.hset(uid, 'head', 0, {'s_head': 0})
                else:
                    if sugar:
                        ran += 15
                        increase_trance(5, uid)

                r.hincrby(uid, 'strength', ran)
                ran = abs(ran)

                msg = f"{emoji} Твій {r_name} смачно поїв.\n\nСила {word} на {ran}.\n"
                if fr[2] == 1:
                    msg += 'Інтелект збільшився на 1.\n'
                    intellect(1, uid)
                if bd == 2:
                    msg += 'Русак сьогодні в гарному настрої. Бойовий дух збільшився на 10000.'
                    spirit(10000, uid, 0)
                    await message.reply_photo('https://i.ibb.co/bK2LrSD/feed.jpg', caption=msg)
                else:
                    if bd == 1:
                        msg += 'Русак сьогодні в гарному настрої. Бойовий дух збільшився на 1000.'
                        spirit(1000, uid, 0)

                    if word == 'зросла':
                        if int(r.hget(uid, 'support')) == 10 and choices([1, 0], [2, 8]) == [1]:
                            if int(r.hget(uid, 'injure')) > 0 \
                                    or int(r.hget(uid, 'sch')) > 0 \
                                    or int(r.hget(uid, 'mushrooms')) > 0:
                                damage_support(uid)
                                r.hset(uid, 'injure', 0)
                                r.hset(uid, 'sch', 0)
                                r.hset(uid, 'mushrooms', 0)
                                msg += '\n\n\U0001F43D\U0001F41F Швайнокарась зняв з русака негативні ефекти.'

                    await message.reply(msg)
            else:
                await message.reply(f'\U0001F9A0 Твій {r_name} сьогодні захворів. Сили від їжі не прибавилось.')
        elif datetime.now().day == int(r.hget(uid, 'time')):
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
                head = int(r.hget(message.from_user.id, 'head'))
                ms = mine_salt(int(r.hget(message.from_user.id, 's2')), head, datetime.today().weekday())
                r_name = names[int(r.hget(message.from_user.id, 'name'))]
                r.hset(message.from_user.id, 'time1', datetime.now().day)
                quest(message.from_user.id, 1, 4)
                if message.text.startswith('/minecraft'):
                    if r.hexists(message.from_user.id, 'ac1') == 0:
                        r.hset(message.from_user.id, 'ac1', 1)
                success = ms[0]
                cl = int(r.hget(message.from_user.id, 'class'))
                if cl == 2 or cl == 12 or cl == 22:
                    success = choice([0, 0, 1, 1, 1])
                support = int(r.hget(message.from_user.id, 'support'))
                if support in (8, 13):
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
                    msg = f'\u26CF Твій {r_name} успішно відпрацював зміну на соляній шахті.\n\n' \
                          f'\U0001F4B5 Зароблено гривень: {money}.'
                    if ms[2] == 1:
                        msg += '\nРусак сьогодні працював з новітніми технологіями.\n'
                        if int(r.hget(message.from_user.id, 'intellect')) < 20:
                            msg += '\U0001F9E0 +1'
                            intellect(1, message.from_user.id)
                        else:
                            msg += '\U0001F4B5 +20'
                            r.hincrby(message.from_user.id, 'money', 20)
                    if choices([1, 0], [25, 75]) == [1] or head == 6:
                        msg += '\n\U0001F9C2 +1'
                        r.hincrby(message.from_user.id, 'salt', 1)
                    await message.reply(msg)
                else:
                    fish = 0
                    if support == 10:
                        fish = choices([1, 0], [1, 4])[0]
                    if cl in (2, 12, 22) and fish == 0:
                        msg = f'\U0001F37A Твій роботяга {r_name} втік з-під нагляду. ' \
                              f'Його знайшли п`яним біля шахти.\n\u2622 +5'
                        if cl == 12 or cl == 22:
                            msg = msg + ' \U0001F4B5 +8'
                            r.hincrby(message.from_user.id, 'money', 8)
                        r.hincrby(message.from_user.id, 'vodka', 5)
                        r.hincrby('all_vodka', 'vodka', 5)
                        await message.reply(msg)
                    elif fish == 1:
                        damage_support(message.from_user.id)
                        await message.reply(f'\U0001F37A Твій {r_name} втік з-під нагляду. Його знайшли п`яним біля '
                                            f'шахти разом з швайнокарасем.\n\u2622 +100 \U0001F4B5 +100')
                        r.hincrby(message.from_user.id, 'money', 100)
                        r.hincrby(message.from_user.id, 'vodka', 100)
                        r.hincrby('all_vodka', 'vodka', 100)
                    else:
                        await message.reply(f'\U0001F37A Твій {r_name} втік з-під нагляду. '
                                            f'Його знайшли п`яним біля шахти.\n\u2622 +1')
                        r.hincrby(message.from_user.id, 'vodka', 1)
                        r.hincrby('all_vodka', 'vodka', 1)
                        if cl in (18, 28):
                            r.hset(message.from_user.id, 'time1', 0)
                            if int(r.hget(message.from_user.id, 'weapon')) == 39 \
                                    and int(r.hget('soledar', 'merchant_day')) != datetime.now().day:
                                damage_weapon(message.from_user.id, cl)
                                msg = f'📟 Хакер дізнався, що торговець прийде о ' \
                                      f'{int(r.hget("soledar", "merchant_hour"))} годині.'
                                await bot.send_message(message.from_user.id, msg)
            elif datetime.now().day == int(r.hget(message.from_user.id, 'time1')):
                await message.reply('Твій русак сьогодні відпрацював зміну.')
        except:
            await message.reply('\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на \n/donbass')
    else:
        msg = 'Соляні шахти тут -> <a href="https://t.me/+cClR7rA-sZAyY2Uy">@soledar1</a>.'
        await message.answer(msg, disable_web_page_preview=True, parse_mode='HTML')


@dp.message_handler(commands=['stat'])
async def stat(message):
    if message.chat.type == 'private':
        try:
            ran = randint(1, 20)
            msg = ''
            if ran == 1:
                msg = '\U0001F465 Кількість користувачів: ' + str(r.scard('everyone')) + '\n\n' + \
                      r.hget('promo_code', 'stat_promo_code').decode()
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
            cl = int(r.hget(message.from_user.id, 'class'))
            if cl in (7, 17, 27):
                percent = 90
            else:
                percent = 10
            await message.reply(f'\U0001F52A Вбити свого русака?\n\n🦇 У всіх русаків в цьому чаті зменшиться '
                                f'бойовий дух на {percent}%.',
                                reply_markup=markup.add(InlineKeyboardButton(text='Принести в жертву русака',
                                                                             callback_data='sacrifice1')))
        else:
            await message.reply('Робити жертвоприношення русаків можна раз в день, і якщо є живий русак.')
    except:
        pass


@dp.message_handler(commands=['fascist'])
async def fascist(message):
    try:
        if message.chat.id == -1001211933154 or int(r.hget('c' + str(message.chat.id), 'base')) > 0:
            if r.scard(message.chat.id) >= 14:
                if r.hexists('f' + str(message.chat.id), 'time3') == 0:
                    r.hset('f' + str(message.chat.id), 'time3', 0)
                if int(r.hget('f' + str(message.chat.id), 'time3')) != int(datetime.now().day):
                    r.hset('f' + str(message.chat.id), 'time3', datetime.now().day)

                    for i in range(100):
                        mem = r.srandmember(message.chat.id)
                        st = await bot.get_chat_member(message.chat.id, int(mem))
                        if st.status not in ('banned', 'left', 'kicked'):
                            break
                        else:
                            r.srem(message.chat.id, mem)
                    else:
                        raise Exception

                    ran = int(mem)
                    r.hset('f' + str(message.chat.id), 'username', r.hget(ran, 'username').decode())
                    username = r.hget('f' + str(message.chat.id), 'username').decode()
                    if message.chat.id == -1001211933154:
                        msg = f'\U0001F468\U0001F3FB\u200D\u2708\uFE0F @{username} сьогодні займає посаду Фашист дня!' \
                              f' Йому видано один \U0001F31F погон російського генерала!'
                        r.hincrby(ran, 'strap', 1)

                    else:
                        msg = f'\U0001F468\U0001F3FB\u200D\u2708\uFE0F @{username} сьогодні займає посаду Фашист дня!' \
                              f' Йому видано одне \U0001F476 російське немовля!'
                        r.hincrby(ran, 'childs', 1)
                        r.hincrby('all_children', 'children', 1)

                    pin = await message.reply(msg)

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
                await message.reply('Фашиста дня можна обирати раз в добу і в чатах,'
                                    ' де є від 14 власників русаків (з юзернеймами) та заснований клан.')
        else:
            await message.reply('Фашиста дня можна обирати раз в добу і в чатах,'
                                ' де є від 14 власників русаків (з юзернеймами) та заснований клан.')
    except:
        await message.reply('Фашиста дня можна обирати раз в добу і в чатах,'
                            ' де є від 14 власників русаків (з юзернеймами) та заснований клан.')


@dp.message_handler(commands=['shop'])
async def shop(message):
    try:
        if r.hexists(message.from_user.id, 'money') == 0:
            await message.reply('У тебе ще не було русаків.\n\nРусака можна отримати, сходивши на /donbass')
        else:
            msg, markup = shop_msg(message.from_user.id, 1)
            await bot.send_message(message.from_user.id, msg, reply_markup=markup)
            if message.chat.type != 'private':
                await message.reply('Надіслано в пп.')
    except:
        pass


@dp.message_handler(commands=['account'])
async def account(message):
    try:
        if r.hexists(message.from_user.id, 'money') == 0:
            await message.reply('У тебе ще не було русаків.\n\nРусака можна отримати, сходивши на /donbass')
        else:
            m = r.hget(message.from_user.id, 'money').decode()
            p = r.hget(message.from_user.id, 'packs').decode()
            s = r.hget(message.from_user.id, 'strap').decode()
            salt = r.hget(message.from_user.id, 'salt').decode()
            tape = 0
            if r.hexists(message.from_user.id, 'tape'):
                tape = int(r.hget(message.from_user.id, 'tape'))
            msg = f'\U0001F4B5 Гривні: {m}\n' \
                  f'\U0001F4E6 Пакунки: {p}\n' \
                  f'\U0001F9C2 Сіль: {salt}\n' \
                  f'🌀 Ізострічка: {tape}\n' \
                  f'\U0001F31F Погони: {s}'
            await message.reply(msg)
    except:
        pass


@dp.message_handler(commands=['passport'])
async def passport(message):
    if r.hexists(message.from_user.id, 'wins') == 1:
        stats = r.hmget(message.from_user.id, 'wins', 'trophy', 'deaths', 'childs', 'vodka', 'opened', 'clan')
        sk = r.hmget(message.from_user.id, 's1', 's2', 's3', 's4', 's5', 'extra_slot')
        s6 = sk[5]
        if s6:
            s6 = int(s6) + 1
        else:
            s6 = 1
        skill = int((int(sk[0]) + int(sk[1]) + int(sk[2]) + int(sk[3]) + int(sk[4]) + s6) * 100 / 34)
        ac = 0
        acs = r.hmget(message.from_user.id, 'ac1', 'ac2', 'ac3', 'ac4', 'ac5',
                      'ac6', 'ac7', 'ac8', 'ac9', 'ac10', 'ac11', 'ac12', 'ac13', 'ac14', 'ac15', 'ac16')
        for a in acs:
            try:
                ac += int(a)
            except:
                pass
        wins = f'\U0001F3C6 Кількість перемог: {stats[0].decode()}\n\U0001F3C5 Кількість трофеїв: {stats[1].decode()}'
        deaths = f'\n\u2620\uFE0F Вбито русаків: {stats[2].decode()}\n\U0001F476 З`їдено немовлят: {stats[3].decode()}'
        try:
            if message.text.endswith(' -all'):
                wins = f'\U0001F3C6 Кількість перемог за всі сезони: ' \
                       f'{int(stats[0]) + int(r.hget(message.from_user.id, "wins_all"))}\n' \
                       f'\U0001F3C5 Кількість трофеїв за всі сезони: ' \
                       f'{int(stats[1]) + int(r.hget(message.from_user.id, "trophy_all"))}'
        except:
            pass
        try:
            if message.text.endswith(' -all'):
                deaths = f'\n\n\u2620\uFE0F Вбито русаків за всі сезони: ' \
                       f'{int(stats[2]) + int(r.hget(message.from_user.id, "deaths_all"))}\n' \
                       f'\U0001F476 З`їдено немовлят за всі сезони: ' \
                       f'{int(stats[3]) + int(r.hget(message.from_user.id, "childs_all"))}'
        except:
            pass
        clan1 = ''
        if checkClan(message.from_user.id):
            clan0 = msg_fmt(f'c{stats[6].decode()}', 'title')
            clan1 = f'\n\U0001F3E0 Клан: {clan0}'
        msg = f'\U0001F4DC {message.from_user.first_name.replace("@", "")}\n\n{wins}{deaths}' \
              f'\n\u2622 Випито горілки: {stats[4].decode()}' \
              f'\n\U0001F4E6 Відкрито пакунків: {stats[5].decode()}{clan1}' \
              f'\n\u26CF Скіли: {skill}%' \
              f'\n\u2B50 Досягнення: {int(ac * 100 / 32)}%'
        if message.from_user.id == 1897184980:
            msg += '\n\U0001F468\U0001F3FB\u200D\u2708\uFE0F Фашист року'
        await message.reply(msg, disable_web_page_preview=True)


@dp.message_handler(commands=['woman'])
async def woman(message):
    try:
        uid = message.from_user.id
        if r.hexists(uid, 'time4') == 0:
            r.hset(uid, 'time4', 0)
        if int(r.hget(uid, 'woman')) == 1:
            quest(uid, 1, -3)
            if int(r.hget(uid, 'time4')) != datetime.now().day:
                if r.hexists(uid, 'time5') == 0:
                    r.hset(uid, 'time5', 0)
                r.hset(uid, 'time4', datetime.now().day)
                r.hincrby(uid, 'time5', 1)
                if int(r.hget(uid, 'time5')) >= 9:
                    emoji = choice(['\U0001F35C', '\U0001F35D', '\U0001F35B', '\U0001F957', '\U0001F32D'])
                    msg = '\U0001F469\U0001F3FB Ти провідав жінку. Вона народила \U0001F476 немовля. ' \
                          'В тебе буде смачний сніданок!'
                    r.hincrby(uid, 'childs', 1)
                    r.hincrby('all_children', 'children', 1)
                    r.hset(uid, 'time5', 0)
                    if int(r.hget(uid, 's5')) >= 4:
                        if r.hexists(uid, 'time22') == 0:
                            msg += f'\n{emoji} +1'
                            r.hset(uid, 'time', 0)
                        else:
                            msg += f'\n{emoji} +2'
                            r.hset(uid, 'time', 0)
                            r.hset(uid, 'time22', 0)
                    await message.reply(msg)
                else:
                    await message.reply('\U0001F469\U0001F3FB Ти провідав жінку. Вона на ' +
                                        r.hget(uid, 'time5').decode() + ' місяці.')
            else:
                await message.reply('\U0001F469\U0001F3FB Ти знову провідав жінку. Вона на ' +
                                    r.hget(uid, 'time5').decode() + ' місяці.')
    except:
        pass


@dp.message_handler(commands=['ltop'])
async def l_top(message):
    try:
        if message.chat.id != -1001211933154:
            msg = await top(message.chat.id, message.from_user.id, message.text)
            await message.reply(msg)
        else:
            await message.reply('В Соледарі ця команда недоступна.')
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
        msg = await itop(message.from_user.id, message.chat.id, message.chat.type, message.text)
        await message.reply(msg)
    except:
        pass


@dp.message_handler(commands=['ctop'])
async def c_top(message):
    try:
        cid = message.chat.id
        if message.chat.type == 'private':
            cid = -1001211933154
        msg = await ctop(222, message.from_user.id, message.text, cid)
        await message.reply(msg, parse_mode='HTML')
    except:
        pass


@dp.message_handler(commands=['class'])
async def classes(message):
    msg = 'Класи русаків:\n\n\n' \
          '<code>Хач</code> \U0001F919 - якщо у ворога нема зброї - додає 30 бойового духу та збільшує свою ' \
          'силу на 20%.\n\n' \
          '<code>Роботяга</code> \U0001F9F0 - йому заборонено хворіти. В шахті заробляє втричі більше грошей,' \
          ' але вдвічі більший шанс забухати (п`є в 5 раз більше). \n\n' \
          '<code>Фокусник</code> \U0001F52E - моментально додає 1 інтелекту. 80% шанс ігнорувати дрин ворога ' \
          'і навести на нього шизофренію, перед початком бою показує випадкові характеристики.\n\n' \
          '<code>Язичник</code> \U0001F5FF - вдвічі збільшує бойовий дух в дуелях. При перемозі отримує' \
          ' втричі більше бойового духу.\n\n' \
          '<code>Гарматне м`ясо</code> \U0001fa96 - +50% сили в дуелі, якщо є АК-47 (зброя, яку можна придбати в ' \
          'мандрівного торговця). 1% шанс отримати 150 поранень в бою від АК-47 та втратити весь' \
          ' бойовий дух і здоров`я.\n\n' \
          '<code>Мусор</code> \U0001F46E - має постійну зброю, яка перед боєм ігнорує бойовий дух двох сторін.' \
          ' Якщо є поліцейський щит - ігнорує лише бойовий дух ворога.\n+30% сили при охороні клану від рейдерів.\n\n' \
          '<code>Малорос</code> \U0001F921 - моментально віднімає 2 інтелекту. При жертві віднімає у всіх' \
          ' русаків чату інтелект, який вони здобули від мухоморів (їх можна буде знову купити). ' \
          'Якщо інтелект не зняло, віднімає 90% бойового духу. Мінімальний шанс перемоги в дуелях збільшено ' \
          'до 20% (25%, якщо в малороса шизофренія).\n\n' \
          '<code>Хакер</code> \U0001F4DF - при поразці є 18% підняти собі бойовий дух, знизити ворогу' \
          ' і заробити гривню.\n\n' \
          '<code>Медик</code> \u26D1 -  якщо у ворога менше ніж 50 здоров`я, то медик лікує йому 5. В іншому' \
          ' випадку з шансом 20% завдає поранення на 2 бої. Наявність медика вдвічі збільшує ' \
          'загальну силу загону в міжчатових битвах.\n\n' \
          '<code>Гопнік</code> \U0001F6AC - лікується від поранення та шизофренії втричі швидше. Додаткові дві ' \
          'гривні за кожну перемогу, якщо на рахунку менше 100 гривень.\n+50% сили в рейдах\n\n' \
          '<code>Таксист</code> \U0001F695 - за перемогу в битві на 10 русаків отримує Донбаський пакунок.\n\n' \
          '<code>Офіцер</code> \U0001F396 - платний клас з платними покращеннями. Вибір офіцера коштує ' \
          '\U0001F4B5 500 грн. Збільшує силу у всіх боях на 30% (замість 10%), якщо більше ніж 90 здоров`я. 2% шанс ' \
          'збільшити інтелект на 1 у міжчатовій битві.\n\n\n'\
          'Щоб подивитись другий рівень класів натисни /class_2\n' \
          'Якщо твій русак вже набрав 5 інтелекту, можеш вибрати один з цих класів (один раз на ' \
          'одного русака), написавши сюди "<code>Обираю клас </code>" і назву класу.'
    try:
        await bot.send_message(message.from_user.id, msg, parse_mode='HTML')
        if message.chat.type != 'private':
            await message.reply('Надіслано в пп.')
    except:
        pass


@dp.message_handler(commands=['class_2'])
async def classes_2(message):
    msg = 'Класи русаків:\n\n\n' \
          '<code>Борцуха</code> \U0001F919\U0001F919 - якщо у ворога нема зброї' \
          ', є шанс активувати один з прийомів при перемозі. Чим більша сила ворога, тим більший ' \
          'цей шанс. Кидок через стегно: -50-100 бойового духу ворогу. Млин: +50-100 бойового духу.' \
          ' Кидок прогином: +2 гривні (10% шанс).\n\n' \
          '<code>Почесний алкаш</code> \U0001F9F0\U0001F9F0 - наполовину зменшує кількість потрібних перемог та' \
          ' горілки для прокачки майстерності та алкоголізму. Навіть якщо в шахті нап`ється, йому ' \
          'буде видано 8 гривень.\n\n' \
          '<code>Злий геній</code> \U0001F52E\U0001F52E - +2 інтелекту, колода з кіоску мінятиме лише ті ' \
          'характеристики, які у ворога більші.\n\n' \
          '<code>Скінхед</code> \U0001F5FF\U0001F5FF - збільшує силу на 20% якщо у ворога менше трофеїв. ' \
          'Подвоєний бойовий дух в боях з хачами. Замість купівлі дрина буде видана Бита [Зброя, міцність=3] - ' \
          'блокує зброю і захист ворога.\n\n' \
          '<code>Орк</code> \U0001fa96\U0001fa96 - додає +2.5% сили на дуель за кожне з`їдене немовля ' \
          '(максимум 50%).\n\n' \
          '<code>Силовик</code> \U0001F46E\U0001F46E - ігнорує інтелект, якщо він не менший. Якщо є щит, а інтелект і' \
          ' сила у ворога більші - ігнорує силу. Здібність не діє проти інших мусорів.\n\n' \
          '<code>Кремлебот</code> \U0001F921\U0001F921 - одноразова премія - 200 гривень. Онуляє рахунок мухоморів. ' \
          'Можливість купляти горілку за перемоги, якщо нема грошей.\n\n' \
          '<code>Кіберзлочинець</code> \U0001F4DF\U0001F4DF - отримує доступ до баз даних - якщо напився на ' \
          'роботі, то може працювати ще раз; можливість купляти мухомори без обмежень.\n\n' \
          '<code>Нарколог</code> \u26D1\u26D1 - якщо у ворога від 50 здоров`я - з шансом 20% додає на 1 ' \
          'поранення більше за кожен мухомор і зменшує здоров`я на рівень алкоголізму ворога.\n\n' \
          '<code>Зек</code> \U0001F6AC\U0001F6AC - подвоює бонус сили від утепленої будки. Зменшує бойовий дух ' \
          'ворога на 20%, а якщо в нього менше перемог - на 40%. Ця здібність не діє проти мусорів.\n\n' \
          '<code>Далекобійник</code> \U0001F695\U0001F695 - жінки на 50 гривень дешевші. +3% ресурсів за роботу' \
          ' в клані за кожен невідкритий пакунок (максимум 120%).\n\n' \
          '<code>Воєнний злочинець</code> \U0001F396\U0001F396 - \U0001F3C5 50 трофеїв. Якщо русак такого класу в ' \
          'міжчатовій битві один - збільшує свою силу на 50% за кожне гарматне м`ясо та зменшує бойовий дух ' \
          'ворогам на 5%.\n\n\n' \
          'Щоб подивитись третій рівень класів натисни /class_3\n' \
          'Якщо твій русак вже набрав 12 інтелекту і вибрав клас, можеш ' \
          'покращити клас, написавши сюди "<code>Покращити русака</code>".'
    try:
        await bot.send_message(message.from_user.id, msg, parse_mode='HTML')
        if message.chat.type != 'private':
            await message.reply('Надіслано в пп.')
    except:
        pass


@dp.message_handler(commands=['class_3'])
async def classes_3(message):
    msg = 'Класи русаків:\n\n\n' \
          '<code>Гроза Кавказу</code> \U0001F919\U0001F919\U0001F919 - моментально збільшує силу на 200. ' \
          '+10 сили і +1000 бойового духу якщо вперше за день в бою зустрів хача.\n\n' \
          '<code>П`яний майстер</code> \U0001F9F0\U0001F9F0\U0001F9F0 - якщо русак вже їв, 0% шанс в бою ' \
          'отримати талон на їжу (додаткове годування). Шанс збільшується на 1% за кожні два рівня ' \
          'алкоголізму.\n\n' \
          '<code>Некромант</code> \U0001F52E\U0001F52E\U0001F52E - при захисті збільшує інтелект на 5% за кожну' \
          ' смерть (максимум 45%). При атаці збільшує силу на 3% за кожну смерть ворога ' \
          '(максимум 45%). Якщо у ворога 0 хп - лікує його на 10 і збільшує свій \U0001F44A ' \
          'бойовий транс на 5.\n\n' \
          '<code>Білий вождь</code> \U0001F5FF\U0001F5FF\U0001F5FF - збільшує бойовий дух на 1% за кожен трофей ' \
          '(максимум 50%). Якщо весь загін міжчатової битви з одного клану - збільшує загальну силу' \
          ' на 25% і додає кожному 250 бойового духу.\n\n' \
          '<code>Герой Новоросії</code> \U0001fa96\U0001fa96\U0001fa96 - обидва русаки можуть отримати 150 поранень' \
          ' (якщо в героя є АК-47). Також з шансом 10% в бою герой і ворог можуть отримати невелике поранення ' \
          '(герой: +1 \U0001fa78, ворог +5-10\U0001fa78).\n\n' \
          '<code>Товариш майор</code> \U0001F46E\U0001F46E\U0001F46E - якщо є поліцейський щит - 10% шанс вилучити' \
          ' в ворога зброю при захисті і захист при атаці (або зменшити міцність на 300) і збільшити міцність ' \
          'щита на 20 (не діє проти інших мусорів).\n\n' \
          '<code>Агент ФСБ</code> \U0001F921\U0001F921\U0001F921 - одноразова премія - 300 гривень. В бою проти ' \
          'русака без класу є 5% шанс перетворити його в малороса. За це агент отримує 50 гривень, а русак ' \
          '300 шизофренії. Можливість на території ворожого клану вкрасти до 50 гривень командою clan.\n\n' \
          '<code>Black Hat</code> \U0001F4DF\U0001F4DF\U0001F4DF - здібність хакера тепер додає по гривні за ' \
          'кожні 50 гривень на рахунку ворога (1-5 гривень).\n\n' \
          '<code>Патологоанатом</code> \u26D1\u26D1\u26D1 - якщо у ворога менше ніж 50 здоров`я - лікує ' \
          'поранення і шизофренію на 1, 50% шанс отримати за це 2 гривні і по одній гривні ' \
          'додатково за лікування цих захворювань. Якщо у ворога 0 здоров`я - лікує йому 20 і ' \
          'отримує 5 гривень.\n\n' \
          '<code>Мародер</code> \U0001F6AC\U0001F6AC\U0001F6AC - +10% шанс потрапити на рейдову локацію. ' \
          'Потрапивши на неї - грабує вдвічі більше. Якщо рейд проти клану - при програші зменшує силу ворожої ' \
          'охорони на 10% за кожного мародера в групі.\n\n' \
          '<code>Танкіст</code> \U0001F695\U0001F695\U0001F695 - під час пошуку цілі для рейду +20% шанс активувати ' \
          'Пограбування гумконвоїв (стакається).\n\n' \
          '<code>Генерал</code> \U0001F396\U0001F396\U0001F396 - \U0001F31F 1 погон. Здібність залежить від клану.\n' \
          'Комуна - збільшує власну силу в міжчатовій битві на 1% за кожен \U0001F916 (максимум 50%) та ' \
          'нагороду на 2 \U0001F4B5 або 2 \U0001F47E.\n' \
          'Коаліція - 15% шанс знайти \U0001F4E6 1 за перемогу в міжчатовій битві. ' \
          '\U0001F4E6 +1 за кожну 1000 перемог (максимум 3 за бій).\n' \
          'Асоціація - при охороні - збільшує силу гумконвою на 500000.\n' \
          'Організація - збільшує нагороду у міжчатових битвах на \U0001F4B5 4 та ще на 1 за кожен ' \
          'мільйон на рахунку клану.\n\n\n' \
          'Якщо твій русак вже набрав 20 інтелекту і покращив клас, можеш ще раз ' \
          'покращити клас, написавши сюди "<code>Вдосконалити русака</code>".'
    try:
        await bot.send_message(message.from_user.id, msg, parse_mode='HTML')
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
            slot, strap, tape = randint(1, 3), randint(1, 3), randint(20, 50)
            r.hset('soledar', 'merchant_slot', slot)
            r.hset('soledar', 'merchant_strap', strap)
            r.hset('soledar', 'merchant_tape', tape)
            msg, markup = merchant_msg(slot, strap, tape)
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
    try:
        markup = InlineKeyboardMarkup()
        url = f'https://randomuabot.diaka.ua/donate?name={message.from_user.id}&amount=20'
        markup.add(InlineKeyboardButton(text='\U0001F349 Задонатити', url=url))
        msg = 'Якщо хтось хоче підтримати автора, то може задонатити і отримати\n\U0001F31F погон російського ' \
              'генерала, який можна витратити в \n/donate_shop.\n\n\U0001F4B3 Акційна ціна одного погону — 20 грн!' \
              '\n\u274C Не міняйте ім`я (твій айді в тг) в формі оплати, якщо купляєте собі.'
        await bot.send_message(message.from_user.id, msg, reply_markup=markup, protect_content=True, parse_mode='HTML')
        if message.chat.type != 'private':
            await message.reply('Надіслано в пп.')
    except:
        pass


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
        msg, markup = shop_msg(message.from_user.id, 2)
        await bot.send_message(message.from_user.id, msg, reply_markup=markup)
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
                if msg.startswith('soledar_n') and uid not in r.smembers('first_code'):
                    r.sadd('first_code', message.from_user.id)

                    r.hincrby(message.from_user.id, 'packs', 20)
                    r.hincrby(message.from_user.id, 'money', 30)
                    r.hincrby(message.from_user.id, 'vodka', 50)
                    await message.reply('\u26CF Соледарський промокод активовано!'
                                        '\n\U0001F4E6 +20 \U0001F4B5 +30 \u2622 +50')
                elif msg.startswith('h') and uid not in r.smembers('second_code'):
                    msg = '\u26CF Хакерський промокод активовано!\n\U0001F4E6 +20 \u2622 +50 \U0001F4B5 +100'
                    r.sadd('second_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'packs', 20)
                    r.hincrby(message.from_user.id, 'money', 100)
                    r.hincrby(message.from_user.id, 'vodka', 50)
                    await message.reply(msg)
                elif msg.startswith('ne') and uid not in r.smembers('third_code'):
                    r.sadd('third_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'salt', 10)
                    r.hincrby(message.from_user.id, 'packs', 50)
                    if not r.hexists(message.from_user.id, 'weapon') or \
                            int(r.hget(message.from_user.id, 'weapon')) == 0:
                        r.hset(message.from_user.id, 'weapon', 23)
                        r.hset(message.from_user.id, 's_weapon', 300)
                    elif int(r.hget(message.from_user.id, 'weapon')) in (12, 23, 34):
                        r.hincrby(message.from_user.id, 's_weapon', 300)
                    await message.reply('\u26CF Промокод Майнкрафту активовано!\n🧂 +10 \U0001F4E6 +50 \U0001F5E1 +300')
                elif msg.startswith('kh') and uid not in r.smembers('fifth_code') \
                        and r.hget(message.from_user.id, 'clan') in r.smembers('fifth_code_allowed'):
                    r.sadd('fifth_code', message.from_user.id)
                    if int(r.hget(message.from_user.id, 'weapon')) == 0:
                        r.hset(message.from_user.id, 'weapon', 5)
                        r.hset(message.from_user.id, 's_weapon', 1)
                    if int(r.hget(message.from_user.id, 'strength')) >= 8000:
                        st = 10
                    elif int(r.hget(message.from_user.id, 'strength')) >= 4000:
                        st = 50
                    else:
                        st = 100
                    r.hincrby(message.from_user.id, 'strength', st)
                    r.hincrby(message.from_user.id, 'vodka', 100)
                    r.hincrby(message.from_user.id, 'money', 200)
                    await message.reply(f'\u26CF Промокод швайнокарасів активовано!\n\u2708\uFE0F +1 \U0001F4AA +{st} '
                                        f'\u2622 +100 \U0001F4B5 +200')
                elif msg.startswith('ran') and uid not in r.smembers('seventh_code'):
                    r.sadd('seventh_code', message.from_user.id)
                    if int(r.hget(message.from_user.id, 'weapon')) == 2:
                        weapon = 1
                    elif int(r.hget(message.from_user.id, 'weapon')) == 5:
                        weapon = 0
                    elif int(r.hget(message.from_user.id, 'weapon')) == 0:
                        weapon = 5
                        r.hset(message.from_user.id, 'weapon', 4)
                        r.hset(message.from_user.id, 's_weapon', 0)
                    else:
                        weapon = 5
                    r.hincrby(message.from_user.id, 's_weapon', weapon)

                    if int(r.hget(message.from_user.id, 'defense')) == 0:
                        defense = 5
                        r.hset(message.from_user.id, 'defense', 9)
                        r.hset(message.from_user.id, 's_defense', 0)
                    else:
                        defense = 5
                    r.hincrby(message.from_user.id, 's_defense', defense)

                    if int(r.hget(message.from_user.id, 'support')) == 6:
                        support = 1
                    elif int(r.hget(message.from_user.id, 'support')) == 5:
                        support = 0
                    elif int(r.hget(message.from_user.id, 'support')) == 0:
                        support = 5
                        r.hset(message.from_user.id, 'support', 7)
                        r.hset(message.from_user.id, 's_support', 0)
                    else:
                        support = 5
                    r.hincrby(message.from_user.id, 's_support', support)
                    if int(r.hget(message.from_user.id, 'support')) == 10:
                        r.hset(message.from_user.id, 's_support', 3)

                    if int(r.hget(message.from_user.id, 'head')) in (3, 5):
                        head = 0
                    elif int(r.hget(message.from_user.id, 'head')) == 0:
                        head = 5
                        r.hset(message.from_user.id, 'head', 4)
                        r.hset(message.from_user.id, 's_head', 0)
                    else:
                        head = 5
                    r.hincrby(message.from_user.id, 's_head', head)

                    await message.reply(f'\u26CF Промокод міцності активовано!\n'
                                        f'\U0001F5E1 +{weapon} \U0001F6E1 +{defense} '
                                        f'\U0001F9EA +{support} \U0001F3A9 +{head}')
                elif msg.startswith('ko') and uid not in r.smembers('ninth_code'):
                    msg = '\u26CF Промокод Козака активовано!\n\u2620\uFE0F +5 \U0001F476 +5 \u2622 +50'
                    r.sadd('ninth_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'deaths', 5)
                    r.hincrby(message.from_user.id, 'childs', 5)
                    r.hincrby(message.from_user.id, 'vodka', 50)
                    await message.reply(msg)

                elif msg.startswith('1') and uid not in r.smembers('fourteenth_code'):
                    msg = '\u26CF Промокод двохсот пятидесяти тисяч активовано!\n🧂 +25 ☠ +25 📦 +250'
                    r.sadd('fourteenth_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'deaths', 25)
                    r.hincrby(message.from_user.id, 'salt', 25)
                    r.hincrby(message.from_user.id, 'packs', 250)
                    if r.hexists(message.from_user.id, 'name') and not int(r.hget(message.from_user.id, 'support')):
                        r.hset(message.from_user.id, 'support', 11, {'s_support': 10})
                        msg += '\n🧾 +1'
                    await message.reply(msg)
                elif msg.startswith('25') and uid not in r.smembers('fifteenth_code'):
                    r.sadd('fifteenth_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'tape', 5)
                    r.hincrby(message.from_user.id, 'packs', 25)
                    r.hincrby(message.from_user.id, 'salt', 25)
                    await message.reply('\u26CF Промокод статистики активовано!\n'
                                        '🌀 +5 \U0001F9C2 +25 \U0001F4E6 +25')
                '''
                elif msg.startswith('bot') and uid not in r.smembers('twelfth_code'):
                    r.sadd('twelfth_code', message.from_user.id)
                    if not r.hexists(message.from_user.id, 'opened') \
                            or int(r.hget(message.from_user.id, 'opened')) < 500:
                        packs = 50
                    else:
                        packs = int(r.hget(message.from_user.id, 'opened')) // 10
                        if packs > 500:
                            packs = 500
                    r.hincrby(message.from_user.id, 'salt', 15)
                    r.hincrby(message.from_user.id, 'vodka', 50)
                    r.hincrby(message.from_user.id, 'packs', packs)
                    msg = f'\u26CF Промокод живого бота активовано!\n\U0001F9C2 +15 \u2622 +50 \U0001F4E6 +{packs}'
                    await message.reply(msg)
                elif msg.startswith('eas') and uid not in r.smembers('thirteenth_code'):
                    r.sadd('thirteenth_code', message.from_user.id)
                    if uid in r.smembers('easter_2023_top_20'):
                        packs = 20
                        salt = 10
                    else:
                        packs = 10
                        salt = 5
                    r.hincrby(message.from_user.id, 'salt', salt)
                    r.hincrby(message.from_user.id, 'packs_2023_2', packs)
                    r.hset(message.from_user.id, 'time', 0)
                    msg = f'\u26CF Великодній промокод активовано!\n🥓 +1 \U0001F9C2 +{salt} 🧺 {packs}'
                    await message.reply(msg)
                elif msg.startswith('soledar_2') and uid not in r.smembers('eleventh_code'):
                    msg = '\u26CF Ювілейний промокод активовано!\n\U0001F9C2 +22 \U0001F3C5 +22 \U0001F4E6 +100'
                    r.sadd('eleventh_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'trophy', 22)
                    r.hincrby(message.from_user.id, 'packs', 100)
                    r.hincrby(message.from_user.id, 'salt', 22)
                    await message.reply(msg)
                elif msg.startswith('100') and uid not in r.smembers('tenth_code'):
                    msg = '\u26CF Промокод ста тисяч активовано!\n\U0001F381 +10 \u2620\uFE0F +10 \U0001F4AA +100'
                    r.sadd('tenth_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'deaths', 10)
                    r.hincrby(message.from_user.id, 'packs_2023', 10)
                    r.hincrby(message.from_user.id, 'strength', 100)
                    if r.hexists(message.from_user.id, 'strength2'):
                        r.hincrby(message.from_user.id, 'strength2', 100)
                    await message.reply(msg)
                elif msg.startswith('pa') and uid not in r.smembers('eighth_code') \
                        and uid in r.smembers('premium_users'):
                    r.sadd('eighth_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'salt', 21)
                    r.hincrby(message.from_user.id, 'packs', 21)
                    if int(r.hget(message.from_user.id, 'support')) == 7:
                        r.hincrby(message.from_user.id, 's_support', 21)
                    else:
                        r.hset(message.from_user.id, 'support', 7, {'s_support': 21})
                    await message.reply('\u26CF Промокод донатера активовано!'
                                        '\n\U0001F9C2 +21 \U0001F9EA +21 \U0001F4E6 +21')
                elif msg.startswith('de') and uid not in r.smembers('fourth_code'):
                    r.sadd('fourth_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'packs', 10)
                    r.hincrby(message.from_user.id, 'money', 200)
                    r.hincrby(message.from_user.id, 'vodka', 100)
                    await message.reply('\u26CF Промокод активовано!\n\U0001F4E6 +10 \u2622 +100 \U0001F4B5 +200')
                elif msg.startswith('soledar_1') and uid not in r.smembers('sixth_code'):
                    r.sadd('sixth_code', message.from_user.id)
                    r.hincrby(message.from_user.id, 'strength', 33)
                    r.hincrby(message.from_user.id, 'packs', 22)
                    r.hincrby(message.from_user.id, 'salt', 11)
                    await message.reply('\u26CF Ювілейний Соледарський промокод активовано!\n'
                                        '\U0001F9C2 +11 \U0001F4E6 +22 \U0001F4AA +33')
                '''
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
                                               reply_markup=battle_button(), disable_web_page_preview=True)
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
    c = await bot.get_chat_members_count(message.chat.id)
    if message.chat.type != 'private' and c >= 10 and '@' not in message.chat.title and \
            str(message.chat.id).encode() not in r.smembers('war_banned') and \
            str(message.from_user.id).encode() not in r.smembers('war_banned'):
        if r.hexists('war_battle' + str(message.chat.id), 'start') == 0:
            try:
                await bot.delete_message(message.chat.id, message.message_id)
            except:
                pass
            emoji = choice(['\U0001F3DF', '\U0001F3AA', '\U0001F30E', '\U0001F30D', '\U0001F30F'])
            a = await bot.send_message(message.chat.id, emoji + ' Починається міжчатова битва...\n\n',
                                       reply_markup=battle_button_3(), disable_web_page_preview=True)
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
        if str(message.from_user.id).encode() in r.smembers('sudoers') \
                or st.status == 'creator' or st.can_restrict_members is True:
            r.hdel('war_battle' + str(message.chat.id), 'start')
            r.srem('battles', message.chat.id)
            r.srem('battles2', message.chat.id)
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
            r.hdel(message.from_user.id, 'in_war')
            '''
            cid = r.hget(message.from_user.id, 'in_war').decode()
            r.srem('fighters_2' + cid, message.from_user.id)
            '''
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
    if r.hexists(message.from_user.id, 'name'):
        msg1 = message.text.split()
        if len(msg1) > 1 and msg1[1] in ('e', 'empty', '-e', '--empty'):
            msg, markup = empty_backpack(False, message.from_user.id)
        else:
            msg, markup = show_inventory(message.from_user.id)
        await message.reply(msg, reply_markup=markup)
    else:
        await message.reply('\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на \n/donbass')


@dp.message_handler(commands=['pack'])
async def pack(message):
    if r.hexists(message.from_user.id, 'name') == 1:
        try:
            n = int(message.text.split()[1])
            if 0 < n < 2000:
                markup = InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton(text='Купити', callback_data=f'buy_pack_{n}'))
                await message.reply(f'\U0001F4E6 Купити {n} пакунків за \U0001F4B5 {n * 20} гривень?',
                                    reply_markup=markup)
        except:
            packs = int(r.hget(message.from_user.id, 'packs'))
            if packs != 0:
                await message.reply('\U0001F4E6 Донбаські пакунки: ' + str(packs) + '\n\nВідкрити?',
                                    reply_markup=unpack(message.from_user.id))
            else:
                await message.reply('\U0001F4E6 Донбаський пакунок коштує \U0001F4B5 20 гривень.'
                                    '\n\nКупити один і відкрити?', reply_markup=unpack(message.from_user.id))
    else:
        await message.reply('\U0001F3DA У тебе немає русака.\n\nРусака можна отримати, сходивши на \n/donbass')


@dp.message_handler(commands=['openpack'])
async def pack(message):
    try:
        packs = int(r.hget(message.from_user.id, 'packs'))
        if r.hexists('pack_ts2', message.from_user.id) == 0:
            r.hset('pack_ts2', message.from_user.id, 0)
        timestamp = int(datetime.now().timestamp())
        if timestamp - int(r.hget('pack_ts2', message.from_user.id)) < 0.2:
            pass
        elif packs > 0:
            r.hset('pack_ts2', message.from_user.id, timestamp)
            count = 1
            try:
                #if message.from_user.id in [456514639, 764407699, 1760585978, 1042645070,
                 #                           721627017, 1290022349, 354277131]:
                count = int(message.text.split()[1])
                if count > 20 or count < 1:
                    count = 1
            except:
                pass
            msg = open_pack2(message.from_user.id, f'pack_unpack_{message.from_user.id}', None, count)
            if msg:
                await message.reply(msg[0], reply_markup=msg[1])
        else:
            await message.reply('\U0001F4E6 Донбаський пакунок коштує \U0001F4B5 20 гривень.'
                                '\n\nКупити один і відкрити?', reply_markup=unpack(message.from_user.id))
    except Exception as e:
        #pass
        sentry_sdk.capture_exception(e)


@dp.message_handler(commands=['gift'])
async def pack(message):
    if r.hexists(message.from_user.id, 'name'):
        if r.hexists(message.from_user.id, 'packs_2023_3'):
            packs = int(r.hget(message.from_user.id, 'packs_2023_3'))
            if packs != 0:
                await message.reply('🧳 Валізи з бізнес-джета: ' + str(packs) + '\n\nВідкрити?',
                                    reply_markup=gift_unpack(message.from_user.id))


@dp.message_handler(commands=['skills'])
async def skills(message):
    try:
        markup = InlineKeyboardMarkup()
        s = r.hmget(message.from_user.id, 's1', 's2', 's3', 's4', 's5')
        pur = int(r.hget(message.from_user.id, 'purchase'))
        s1, s2, s3, s4, s5 = int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4])
        s6 = r.hget(message.from_user.id, 'extra_slot')

        if s6:
            s6 = int(s6) + 1
        else:
            s6 = 1

        if s1 < 10:
            markup.add(InlineKeyboardButton(text='Прокачати алкоголізм', callback_data='alcohol'))
        if s2 < 5:
            markup.add(InlineKeyboardButton(text='Прокачати майстерність', callback_data='master'))
        if s3 < 5:
            markup.add(InlineKeyboardButton(text='Продовжити будівництво', callback_data='cellar'))
        if s4 < 5:
            markup.add(InlineKeyboardButton(text='Прокачати наркозалежність', callback_data='addiction'))
        if s5 < 5:
            markup.add(InlineKeyboardButton(text='Прокачати психоз', callback_data='psycho'))

        s11, s22, s221, s222, s41 = s1, s2, 0, 0, s4 * 10
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
        up4 = f'Для покращення цієї здібності треба здійснити {s41} покупок в сольовому магазині.\n{pur}/{s41}\n' \
              f'Бонуси за кожен рівень:\n' \
              f'2. Зменшення шансу передозування з 10% до 5%\n' \
              f'3. Передозування даватиме 20 бойового трансу\n' \
              f'4. Кількість негативних ефектів вдвічі зменшується\n' \
              f'5. На 40% сили більше, купляючи її за сіль\n'
        up5 = f'Для покращення цієї здібності треба набрати {s5 * 20} вбитих русаків і з`їсти {s5 * 10} немовлят.\n' \
              f'Бонуси за кожен рівень:\n' \
              f'2. 33% шанс знайти 2-3 мертвих русаків в пакунку\n' \
              f'3. 50% шанс не зменшити бойовий транс в дуелях\n' \
              f'4. Русаки отримають порцію їжі, коли жінка народить немовля\n' \
              f'5. Мінімальна сила від годування - 10\n'
        up6 = f'Рюкзак можна купити в мандрівного торговця за ізострічку і 🌟 1-3 або в магазині за погони.\n'
        if s1 >= 10:
            up1 = ''
        if s2 >= 5:
            up2 = ''
        if s3 >= 5:
            up3 = ''
        if s4 >= 5:
            up4 = ''
        if s5 >= 5:
            up5 = ''
        if s6 >= 4:
            up6 = ''
        msg = '\u2622 Алкоголізм:\n\nГорілка додає від ' + str(10 * s1) + ' до ' + str(70 * s1) + \
              ' бойового духу.' + up1 + '\n'
        for a in range(10):
            if s1 <= 0:
                msg = msg + '⬜'
            else:
                msg = msg + '🟧'
                s1 = s1 - 1

        msg = msg + '\n\n\u26CF Майстерність:\n\nЗараз русак в шахті може заробити від ' + str(s221) + ' до ' + \
                    str(s222) + intel + up2 + '\n'

        for a in range(5):
            if s2 <= 0:
                msg = msg + '⬜'
            else:
                msg = msg + '🟥'
                s2 = s2 - 1

        msg = msg + '\n\n\U0001F3DA Велике будівництво\n\nПідвал для додаткового русака. \n' + up3
        for a in range(5):
            if s3 <= 0:
                msg = msg + '⬜'
            else:
                msg = msg + '🟫'
                s3 = s3 - 1

        msg = msg + '\n\n\U0001F9C2 Наркозалежність\n\nЗбільшує вигоду купівлі сили в сольовому магазині.\n' + up4
        for a in range(5):
            if s4 <= 0:
                msg = msg + '⬜'
            else:
                msg = msg + '🟦'
                s4 = s4 - 1

        msg = msg + '\n\n\u2620\uFE0F Психоз\n\nПокращує вміння різати русню.\n' + up5
        for a in range(5):
            if s5 <= 0:
                msg = msg + '⬜'
            else:
                msg = msg + '🟨'
                s5 = s5 - 1

        msg = msg + '\n\n🎒 Тактичний рюкзак\n\nЗбільшує кількість слотів спорядження та кількість можливої ' \
                    'ізострічки з пакунків.\n' + up6
        for a in range(4):
            if s6 <= 0:
                msg = msg + '⬜'
            else:
                msg = msg + '🟪'
                s6 = s6 - 1

        await bot.send_message(message.from_user.id, msg, reply_markup=markup)
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

                await message.reply(f'{icons_simple[int(b[9])]} Бойового русака змінено на {names_case[int(b[0])]}.')
            else:
                await message.reply('\U0001F3DA Візьми русака, щоб змінити його на другого'
                                    '.\n\nРусака можна отримати, сходивши на \n/donbass')
    except:
        pass


@dp.message_handler(commands=['clan'])
async def clan(message):
    cid = str(message.chat.id)
    c = 'c' + cid
    tier_emoji = ['', '\U0001F947', '\U0001F948', '\U0001F949']
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
            if str(message.from_user.id).encode() in r.smembers('cl' + cid) \
                    or str(message.from_user.id).encode() in r.smembers('sudoers'):
                base = int(r.hget(c, 'base'))
                title = r.hget(c, 'title').decode()
                leader = r.hget(int(r.hget(c, 'leader')), 'firstname').decode()
                if r.scard('cl2' + cid) == 1:
                    leader += f"\nЗаступник: {r.hget(r.srandmember('cl2' + cid), 'firstname').decode()}"
                elif r.scard('cl2' + cid) == 2:
                    ran = r.srandmember('cl2' + cid, 2)
                    leader += f"\nЗаступники: {r.hget(ran[0], 'firstname').decode()}, " \
                              f"{r.hget(ran[1], 'firstname').decode()}"
                leader = leader.replace('<', '').replace('>', '').replace('@', '')
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
                        wins = f'\nКількість перемог: {int(r.hget(222, cid))}\nТір-{int(r.hget(c, "tier"))} клан'
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
                        if int(r.hget(c, 'cloth')) > 0:
                            resources += f"\n\U0001F9F6 Тканина: {r.hget(c, 'cloth').decode()} / 5000"
                        if int(r.hget(c, 'brick')) > 0:
                            resources += f"\n\U0001F9F1 Цегла: {r.hget(c, 'brick').decode()} / 3000"
                        if int(r.hget(c, 'technics')) > 0:
                            resources += '\n\U0001F4FB Радіотехніка: ' + r.hget(c, 'technics').decode()
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
                    if int(r.hget(c, 'wall')) == 1:
                        building += ', стіна оголошень'
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
                    int(r.hget(c, 'money')) >= 50:
                if int(r.hget(message.from_user.id, 'fsb')) != datetime.now().day:
                    r.hset(message.from_user.id, 'fsb', datetime.now().day)
                    ran = choice([2, 1, 1, 1, 0])
                    if ran == 2:
                        await bot.send_message(message.from_user.id, 'Агент втерся в довіру до керівництва і випросив '
                                                                     'трохи грошей.\n\U0001F4B5 +50')
                        r.hincrby(message.from_user.id, 'money', 50)
                        r.hincrby(c, 'money', -50)
                    elif ran == 1:
                        await bot.send_message(message.from_user.id, 'Агент непомітно забрав собі кілька гривень.'
                                                                     '\n\U0001F4B5 +20')
                        r.hincrby(message.from_user.id, 'money', 20)
                        r.hincrby(c, 'money', -20)
                    else:
                        await message.reply('Агент ФСБ хотів вкрасти гроші з кланової скарбниці, але його помітили...'
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
            if int(r.hget(c, 'rec_time')) != datetime.now().day:
                if int(r.hget(c, 'technics')) >= 3:
                    r.hset(c, 'rec_time', datetime.now().day)
                    r.hincrby(c, 'technics', -3)
                else:
                    try:
                        await bot.revoke_chat_invite_link(int(mem), r.hget(c, 'link').decode())
                    except:
                        pass
                    r.hset(c, 'recruitment', 0)
                    r.srem('recruitment', mem)
                    continue
            num1 = r.scard('cl' + mem.decode())
            num2 = 25
            cl = r.hmget(c, 'base', 'link', 'complex', 'build5', 'title', 'tier')
            title = cl[4].decode().replace('<', '.').replace('>', '.')
            tier = int(cl[5])
            link = cl[1].decode()
            if int(cl[2]) == 1:
                num2 += 25
            if int(cl[3]) == 3:
                num2 += 10
            msg += f'\n\n{tier_emoji[tier]}<i>{prefix[int(cl[0])]}</i> <a href="{link}">{title}</a>\n' \
                   f'Учасники: {num1} / {num2}'
        if r.scard('recruitment') == 0:
            msg = '\U0001F530 На даний момент ніхто не шукає учасників в клан.'
        a = await bot.send_message(message.chat.id, msg, disable_web_page_preview=True, parse_mode='HTML')
        r.hset('soledar', 'clan', a.message_id)


@dp.message_handler(commands=['clan_war'])
async def clan_war(message):
    weekday = datetime.today().weekday()
    cid = message.chat.id
    c = f'c{cid}'
    tier_emoji = ['', '\U0001F947', '\U0001F948', '\U0001F949']

    if str(message.from_user.id).encode() in r.smembers(f'cl{cid}'):
        if not r.hexists('clan_wars', 'x'):
            r.hset('clan_wars', 'x', 0)

        if int(r.hget('clan_wars', 'x')) == 1:
            await sleep(5)

        if str(cid).encode() in r.smembers('clans'):
            if weekday in (5, 6):

                if int(r.hget(c, 'war')) == 1 and int(r.hget('clan_wars', 'x')) == 0:
                    r.hset('clan_wars', 'x', 1)
                    for mem in r.smembers('in_clan_war'):
                        try:
                            ct = 'c' + mem.decode()
                            r.hset(ct, 'war', 0, {'buff_1': 0, 'buff_2': 0, 'buff_3': 0, 'buff_4': 0, 'buff_5': 0})
                            r.srem('in_clan_war', mem)
                            enemy = r.hget(ct, 'enemy').decode()
                            tier = int(r.hget(ct, 'tier'))
                            points1 = int(r.hget(ct, 'points'))
                            q_points1 = int(r.hget(ct, 'q-points'))
                            points2 = int(r.hget('c' + enemy, 'points'))
                            if points1 > 0:
                                if points2 == 0:
                                    points2 = 0.1
                                if points1 / points2 >= 1.25:
                                    if tier == 3:
                                        r.hset(ct, 'tier', 2)
                                        r.sadd('tier2_clans', mem)
                                    elif tier == 2:
                                        if q_points1 >= 500:
                                            r.hset(ct, 'tier', 1)
                                            r.srem('tier2_clans', mem)
                                            r.sadd('tier1_clans', mem)
                                        else:
                                            r.sadd('tier2_clans', mem)
                                    elif tier == 1:
                                        if q_points1 >= 500:
                                            r.sadd('tier1_clans', mem)
                                        else:
                                            r.hset(ct, 'tier', 2)
                                            r.srem('tier1_clans', mem)
                                            r.sadd('tier2_clans', mem)
                                elif points1 / points2 <= 0.75:
                                    if tier == 2:
                                        r.hset(ct, 'tier', 3)
                                        r.srem('tier2_clans', mem)
                                    elif tier == 1:
                                        r.hset(ct, 'tier', 2)
                                        r.srem('tier1_clans', mem)
                                        r.sadd('tier2_clans', mem)
                                elif 0.75 < points1 / points2 < 1.25:
                                    if tier == 2:
                                        r.sadd('tier2_clans', mem)
                                    elif tier == 1:
                                        if q_points1 >= 500:
                                            r.sadd('tier1_clans', mem)
                                        else:
                                            r.hset(ct, 'tier', 2)
                                            r.srem('tier1_clans', mem)
                                            r.sadd('tier2_clans', mem)

                            else:
                                if tier == 2:
                                    r.hset(ct, 'tier', 3)
                                    r.srem('tier2_clans', mem)
                                elif tier == 1:
                                    r.hset(ct, 'tier', 2)
                                    r.srem('tier1_clans', mem)
                                    r.sadd('tier2_clans', mem)
                        except:
                            pass
                    r.hset('clan_wars', 'x', 0)

                if r.hexists(c, 'result'):
                    tier = int(r.hget(c, 'tier'))
                    c2 = f'c{r.hget(c, "enemy").decode()}'
                    points1 = int(r.hget(c, "points"))
                    points2 = int(r.hget(c2, "points"))
                    packs = points1 // 10
                    salt, codes = 0, 0
                    msg = f'\U0001f4ef Війна з кланом {r.hget(c2, "title").decode()} завершена.\n\n' \
                          f'\U0001fa99 Ваші очки: {points1}\n' \
                          f'\U0001fa99 Очки ворога: {points2}\n\n'
                    if points1 < points2:
                        msg += 'Ви програли...'
                    elif points1 > points2:
                        msg += 'Ви виграли!'
                        if tier == 3:
                            salt = 5
                        elif tier == 2:
                            salt = 10
                        elif tier == 1:
                            codes = 5
                            salt = 20
                        if int(r.hget(c, 'result')) == 2:
                            packs *= 2
                    else:
                        msg += 'На війні немає переможців, є тільки ті, хто залишився в живих.'
                    msg += f'\n\n{tier_emoji[tier]} Нагорода для Тір-{tier} клану:'

                    msg += f'\n\U0001F4E6 +{packs}'
                    if salt > 0:
                        msg += f' \U0001F9C2 +{salt}'
                    if codes > 0:
                        msg += f' \U0001F916 +{codes}'

                    r.hdel(c, 'result')

                    r.hincrby(c, 'codes', codes)
                    for mem in r.smembers(f'cl{cid}'):
                        if not r.hexists(mem, 'clan_war_ts'):
                            r.hset(mem, 'clan_war_ts', 0)
                        ts = int(datetime.now().timestamp())
                        if ts - int(r.hget(mem, 'clan_war_ts')) > 259200:
                            r.hset(mem, 'clan_war_ts', ts)
                            r.hincrby(mem, 'salt', salt)
                            r.hincrby(mem, 'packs', packs)

                    await message.answer(msg)

                elif int(r.hget(c, 'tier')) == 3:
                    if str(cid).encode() in r.smembers('registered'):
                        await message.answer('Ваш клан вже зареєстровано на війни кланів')
                    else:
                        markup = InlineKeyboardMarkup()
                        markup.add(InlineKeyboardButton(text='Зареєструватись', callback_data='enter_war'))
                        await message.answer('\U0001f4ef Відкрита реєстрація для тір-3 кланів на кланові війни!',
                                             reply_markup=markup)
                elif int(r.hget(c, 'tier')) == 2:
                    await message.answer('Ваш тір-2 клан автоматично бере участь в наступних кланових війнах')
                elif int(r.hget(c, 'tier')) == 1:
                    await message.answer('Ваш тір-1 клан автоматично бере участь в наступних кланових війнах')
            elif str(cid).encode() in r.smembers('registered'):
                if r.scard('registered') < 2:
                    r.srem('registered', cid)
                    await message.answer('Не вдалось знайти суперників, спробуйте ще раз через тиждень')
                else:
                    r.srem('registered', cid)
                    enemy = r.srandmember('registered')
                    c2 = f'c{enemy.decode()}'
                    r.srem('registered', enemy)
                    r.sadd('in_clan_war', cid, enemy)
                    r.hset(c, 'war', 1, {'enemy': enemy, 'result': 1, 'points': 0, 'q-points': 0})
                    r.hset(c2, 'war', 1, {'enemy': cid, 'result': 1, 'points': 0, 'q-points': 0})
                    await bot.send_message(cid, f'\U0001f4ef Кланові війни починаються!\n\n'
                                                f'Ваш противник:\n{r.hget(c2, "title").decode()}')
                    await bot.send_message(int(enemy), f'\U0001f4ef Кланові війни починаються!\n\n'
                                                       f'Ваш противник:\n{r.hget(c, "title").decode()}')
            elif str(cid).encode() in r.smembers('tier2_clans'):
                if r.scard('tier2_clans') < 2:
                    await message.answer('Не вдалось знайти суперників, спробуйте ще раз через тиждень')
                else:
                    r.srem('tier2_clans', cid)
                    enemy = r.srandmember('tier2_clans')
                    c2 = f'c{enemy.decode()}'
                    r.srem('tier2_clans', enemy)
                    r.sadd('in_clan_war', cid, enemy)
                    r.hset(c, 'war', 1, {'enemy': enemy, 'result': 1, 'points': 0, 'q-points': 0})
                    r.hset(c2, 'war', 1, {'enemy': cid, 'result': 1, 'points': 0, 'q-points': 0})
                    await bot.send_message(cid, f'\U0001f4ef Кланові війни починаються!\n\n'
                                                f'Ваш противник:\n{r.hget(c2, "title").decode()}')
                    await bot.send_message(int(enemy), f'\U0001f4ef Кланові війни починаються!\n\n'
                                                       f'Ваш противник:\n{r.hget(c, "title").decode()}')
            elif str(cid).encode() in r.smembers('tier1_clans'):
                if r.scard('tier1_clans') < 2:
                    await message.answer('Не вдалось знайти суперників, спробуйте ще раз через тиждень')
                else:
                    r.srem('tier1_clans', cid)
                    enemy = r.srandmember('tier1_clans')
                    c2 = f'c{enemy.decode()}'
                    r.srem('tier1_clans', enemy)
                    r.sadd('in_clan_war', cid, enemy)
                    r.hset(c, 'war', 1, {'enemy': enemy, 'result': 1, 'points': 0, 'q-points': 0})
                    r.hset(c2, 'war', 1, {'enemy': cid, 'result': 1, 'points': 0, 'q-points': 0})
                    await bot.send_message(cid, f'\U0001f4ef Кланові війни починаються!\n\n'
                                                f'Ваш противник:\n{r.hget(c2, "title").decode()}')
                    await bot.send_message(int(enemy), f'\U0001f4ef Кланові війни починаються!\n\n'
                                                       f'Ваш противник:\n{r.hget(c, "title").decode()}')
            elif int(r.hget(c, 'war')) == 1:
                enemy = r.hget(c, 'enemy').decode()
                title = msg_fmt(f'c{enemy}', 'title')
                msg = f'\U0001f4ef Триває війна з {title}\n\n' \
                      f'Ваш прогрес:\n' \
                      f'\U0001fa99 Очки: {int(r.hget(c, "points"))}\n' \
                      f'\U0001fa99 Квестові очки: {int(r.hget(c, "q-points"))}/500'
                if int(r.hget(c, 'buff_3')) == 1:
                    points2 = int(r.hget('c' + r.hget(c, 'enemy').decode(), 'points'))
                    msg += f'\n\U0001fa99 Очки ворога: {points2}'

                buffs = r.hmget(c, 'buff_1', 'buff_2', 'buff_3', 'buff_4', 'buff_5',)
                msg += '\n\n\U0001faac Бафи: ['
                if int(buffs[0]) == 0:
                    msg += '\u26AA'
                else:
                    msg += '\U0001f7e2'
                if int(buffs[1]) == 0:
                    msg += '\u26AA'
                else:
                    msg += '\U0001f7e0'
                if int(buffs[2]) == 0:
                    msg += '\u26AA'
                else:
                    msg += '\U0001f534'
                if int(buffs[3]) == 0:
                    msg += '\u26AA'
                else:
                    msg += '\U0001f7e3'
                if int(buffs[4]) == 0:
                    msg += '\u26AA]'
                else:
                    msg += '\U0001f7e1]'

                await bot.send_message(cid, msg)
            else:
                await message.answer('\U0001f4ef Зареєструватись на війни кланів можна у вихідні')


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
                        and message.from_user.id not in admins:
                    await message.answer('\U0001F3D7 Достатньо ресурсів для покращення, кличте адмінів.')
                elif int(r.hget(c, 'wood')) >= 100 and int(r.hget(c, 'stone')) >= 20 and \
                        int(r.hget(c, 'money')) >= 120:
                    if message.from_user.id in admins:
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
                    msg += '\n\nДостатньо ресурсів для покращення. Який шлях розвитку ви обираєте?'
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
                    if int(r.hget(c, 'new_post')) == 0:
                        markup.add(InlineKeyboardButton(text='Побудувати відділення НП',
                                                        callback_data='build_new_post'))
                        msg += '\nВідділення НП (\U0001F333 100, \U0001faa8 50, ' \
                               '\U0001F4B5 1000, \U0001F47E 1) - можливість отримувати ' \
                               '\U0001F4FB радіотехніку з пакунків. При включеній зарплаті, за роботу ' \
                               'видаватиметься \U0001F4E6 пакунок (але +2грн податку).'
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
                            markup.add(InlineKeyboardButton(text='Побудувати їдальню',
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
                        if int(r.hget(c, 'wall')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати стіну оголошень',
                                                            callback_data='build_wall'))
                            msg += '\nСтіна оголошень (\U0001F333 500, \U0001faa8 250, \U0001F9F6 150, ' \
                                   '\U0001F9F1 100, \U0001F4B5 1000, \U0001F47E 30) - додатковий щоденний' \
                                   ' квест (ще +1 через два апгрейди).'
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
                                   'отримуватиме по 10 гривень за піднімання русаків.'
                        if int(r.hget(c, 'build3')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати АЗС',
                                                            callback_data='build3'))
                            msg += '\nАЗС (\U0001F333 1000, \U0001faa8 1000, \U0001F9F6 500, ' \
                                   '\U0001F9F1 400, \U0001F4B5 2000) - +5 гривень за перемогу таксиста в масовій битві.'
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
                                   '\U0001F9F1 500, \U0001F4B5 6000 \U0001F4FB 100) - можливість отримати за ' \
                                   'роботу повістку у вільний слот допомоги. Якщо є повістка - за охорону може ' \
                                   'бути видано Мосінку, Кожух, Фронтові 100 грам і Вушанку (по 20 міцності).'
                        if int(r.hget(c, 'build6')) == 0 and int(r.hget(c, 'build1')) > 0 \
                                and int(r.hget(c, 'build2')) > 0 and int(r.hget(c, 'build3')) > 0 \
                                and int(r.hget(c, 'build4')) > 0 and int(r.hget(c, 'build5')) > 0:
                            markup.add(InlineKeyboardButton(text='Побудувати гулаг',
                                                            callback_data='build6'))
                            msg += '\nГулаг (\U0001F333 15000, \U0001faa8 10000, \U0001F9F6 5000, ' \
                                   '\U0001F9F1 3000, \U0001F4B5 10000, \U0001F4FB 300, \U0001F47E 300, \U0001F916 10)' \
                                   ' - якщо хтось покидає клан - його русаки втрачають по 20% сили. Шанс отримати ' \
                                   'додаткове годування після відпрацювання зміни - 3% за кожну тисячу деревини, ' \
                                   'каменю, тканини і цегли на складі. Можливість купувати вушанки.'
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
                                   ' - Шизофренія не впливатиме негативно на міжчатові битви та охорону, а ' \
                                   'навпаки - додаватиме 5 інтелекту. Можливість купляти шапочки з фольги.'
                    if int(r.hget(c, 'base')) == 11:
                        if int(r.hget(c, 'build5')) == 0:
                            markup.add(InlineKeyboardButton(text='Побудувати готель',
                                                            callback_data='build5'))
                            msg += '\nГотель (\U0001F333 2000, \U0001faa8 1000, \U0001F9F6 800, ' \
                                   '\U0001F9F1 500, \U0001F4B5 6000 \U0001F4FB 100) - максимальна кількість ' \
                                   'учасників збільшується на 10. Можливість вступити в клан майже без обмежень в часі.'
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
                                   '\U0001F9F1 500, \U0001F4B5 6000 \U0001F4FB 100) - можливість купувати Цукор ' \
                                   'і Квас (з подвоєною міцністю, якщо в клані більше мільйона гривень). ' \
                                   'Можливість закупити Кавун базований для всього клану.'
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
        uid = message.from_user.id
        if str(uid).encode() in r.smembers('cl' + str(message.chat.id)) or message.chat.type == 'private':
            if checkClan(uid, building='shop'):
                c = 'c' + str(int(r.hget(message.from_user.id, 'clan')))
                msg, markup = c_shop(c, 1)
                await message.answer(msg, reply_markup=markup)
    except:
        pass


@dp.message_handler(commands=['clan_settings'])
async def clan_settings(message):
    try:
        c = 'c' + r.hget(message.from_user.id, 'clan').decode()
        if message.chat.type != 'private':
            try:
                await bot.delete_message(message.chat.id, message.message_id)
            except:
                pass
        if checkLeader(message.from_user.id, int(r.hget(message.from_user.id, 'clan'))) or \
                str(message.from_user.id).encode() in r.smembers('sudoers'):
            await bot.send_message(message.from_user.id, auto_clan_settings(c), reply_markup=clan_set())
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
        if int(r.hget(c, 'base')) > 0 and len(str(r.hget(message.from_user.id, 'clan'))) < 5 \
                and r.hexists(message.from_user.id, 'name'):
            if int(r.hget(c, 'complex')) >= 1:
                num += 25
            if int(r.hget(c, 'build5')) == 3:
                num += 10
                ts = 10800
            diff = int(datetime.now().timestamp()) - int(r.hget(message.from_user.id, 'clan_ts'))
            if diff > ts:
                if r.scard('cl' + str(message.chat.id)) < num:
                    if int(r.hget(c, 'allow')) == 0 or message.from_user.id == int(r.hget(c, 'leader')) \
                            or str(message.from_user.id).encode() in r.smembers('sudoers'):
                        r.hset(message.from_user.id, 'clan', cid, {'clan_ts': int(datetime.now().timestamp())})
                        if r.hexists(message.from_user.id, 'clan_time') == 0:
                            r.hset(message.from_user.id, 'clan_time', 0)
                        r.sadd('cl' + str(message.chat.id), message.from_user.id)
                        r.hset(message.from_user.id, 'firstname', message.from_user.first_name)
                        if int(r.hget(c, 'buff_4')) == 32:
                            q_points(message.from_user.id, 10)
                        await message.reply('\U0001F4E5 Ти вступив в клан ' +
                                            r.hget('c' + str(message.chat.id), 'title').decode() + '.')
                    elif int(r.hget(c, 'allow')) == 1:
                        await message.reply('\U0001F4E5 Прийняти в клан ' + message.from_user.first_name + '?',
                                            reply_markup=invite())
                else:
                    await message.reply('\U0001F4E5 Неможливо вступити в клан, оскільки він переповнений.')
            else:
                markup = InlineKeyboardMarkup()
                td = timedelta(seconds=ts-diff)
                days, hours, minutes = td.days, td.seconds // 3600, (td.seconds // 60) % 60
                if days > 0:
                    msg = f'{days}д.'
                elif hours > 0:
                    msg = f'{hours}г.'
                elif minutes > 0:
                    msg = f'{minutes}хв.'
                else:
                    msg = 'менше хвилини.'

                if int(r.hget(message.from_user.id, 'strap')) > 0:
                    msg = f'\U0001F4E5 Вступати в клан можна лише раз в тиждень.\n\nЗалишилось часу: {msg}\n\n' \
                          f'\U0001F31F Онулити час очікування за погон?'
                    markup.add(InlineKeyboardButton(text='\U0001F31F 1 -> \u23F1', callback_data='zero_time'))
                else:
                    msg = f'\U0001F4E5 Вступати в клан можна лише раз в тиждень.\n\nЗалишилось часу: {msg}'
                await message.reply(msg, reply_markup=markup)
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
                        if m >= 50:
                            quest(message.from_user.id, 2, 3)
                        if m >= 500:
                            if r.hexists(message.from_user.id, 'ac15') == 0:
                                r.hset(message.from_user.id, 'ac15', 1)
                        if m >= 1000:
                            if int(r.hget(c, 'base')) == 12:
                                p = int(m / 20)
                                r.hincrby(message.from_user.id, 'packs', p)
                                msg += f'\n\U0001F4E6 +{p}'
                                quest(message.from_user.id, 3, -2, 4)
                            if int(r.hget(message.from_user.id, 'defense')) == 0:
                                r.hset(message.from_user.id, 'defense', 5, {'s_defense': 7})
                                msg += '\n✡ +7'
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
                if uid in r.smembers('cl' + cid) and uid not in r.smembers('cl2' + cid):
                    if message.reply_to_message.from_user.id != int(r.hget('c' + cid, 'leader')):
                        r.sadd('cl2' + cid, uid)
                        await message.reply('\u2705')
                else:
                    markup = InlineKeyboardMarkup()
                    uid = message.reply_to_message.from_user.id
                    markup.add(InlineKeyboardButton(text='Так', callback_data=f'promote_to_leader_{uid}'))
                    n = r.hget(message.reply_to_message.from_user.id, 'firstname').decode()
                    await message.reply(f'\U0001F530 Підвищити {n} до лідера?', reply_markup=markup)
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
                        quest(message.from_user.id, 3, 1, 1)
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
                            money, tax, packs = 5, 3, 0
                            if int(r.hget(c, 'new_post')):
                                money, tax, packs = 5, 5, 1
                            if side == 4:
                                money = money + tax
                                tax = 0
                            if int(r.hget(message.from_user.id, 'defense')) == 5 and int(r.hget(c, 'money')) >= 50:
                                if message.from_user.is_premium:
                                    money = money * 5
                                    tax = tax * 5
                                    packs = packs * 5
                                else:
                                    money = money * 3
                                    tax = tax * 3
                                    packs = packs * 3
                                damage_defense(message.from_user.id, 5)
                            r.hincrby(c, 'money', -(money + tax))
                            r.hincrby('soledar', 'money', tax)
                            if int(r.hget(c, 'buff_4')) == 5:
                                money = packs = 0
                                ran = randint(1, 3)
                                q_points(message.from_user.id, ran)
                                resources += f' \n\U0001fa99 {ran}'
                            if money:
                                r.hincrby(message.from_user.id, 'money', money)
                                resources += f' \n\U0001F4B5 +{money}'
                                if packs:
                                    r.hincrby(message.from_user.id, 'packs', packs)
                                    resources += f' \U0001F4E6 +{packs}'

                        if int(r.hget(c, 'build6')) == 1:
                            ch = 3 * (int(r.hget(c, 'wood')) + int(r.hget(c, 'stone')) +
                                      int(r.hget(c, 'cloth')) + int(r.hget(c, 'brick')))
                            if choices([1, 0], [int(ch / 1000), 100 - int(ch / 1000)]) == [1]:
                                r.hset(message.from_user.id, 'time', 0)
                                resources += ' \U0001F372 +1'
                        if int(r.hget(c, 'build5')) == 1:
                            if int(r.hget(message.from_user.id, 'support')) == 0:
                                r.hset(message.from_user.id, 'support', 11, {'s_support': 10})
                                resources += '\n🧾 Русаку вручили повістку!'

                        await message.reply(name + ' попрацював на благо громади.\n' + resources)
            else:
                await message.reply('Твій русак сьогодні вже своє відпрацював.')
    except:
        pass


@dp.message_handler(commands=['relax'])
async def relax(message):
    try:
        name = names[int(r.hget(message.from_user.id, 'name'))]
        if int(r.hget(message.from_user.id, 'clan')) == message.chat.id:
            if int(r.hget(message.from_user.id, 'clan_time')) == datetime.now().day:
                msg = '\U0001F319 ' + name + ' відпочиває і готується до завтрашньої роботи.'
                if int(r.hget(message.from_user.id, 'support')) == 10:
                    damage_support(message.from_user.id)
                    if int(r.hget(message.from_user.id, 'head')) == 0:
                        r.hset(message.from_user.id, 'head', 3)
                        r.hset(message.from_user.id, 's_head', 1)
                    spirit(10000, message.from_user.id, 0)
                    increase_trance(20, message.from_user.id)
                    hp(100, message.from_user.id)
                    msg += '\n\n\U0001F349 +1 \U0001F44A +20 \U0001fac0 +100 \U0001F54A +10000'
                quest(message.from_user.id, 2, -3)
                await message.reply(msg)
            else:
                await message.reply('Рано відпочивати...')
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
                    if int(r.hget(mid, 'support')) == 11:
                        r.hset(mid, 'support', 0, {'s_support': 0})

                        if int(r.hget(mid, 'weapon')) == 0:
                            r.hset(mid, 'weapon', 7, {'s_weapon': 20})
                        if int(r.hget(mid, 'defense')) == 0:
                            r.hset(mid, 'defense', 4, {'s_defense': 20})
                        if int(r.hget(mid, 'support')) == 0:
                            r.hset(mid, 'support', 13, {'s_support': 20})
                        if int(r.hget(mid, 'head')) == 0:
                            r.hset(mid, 'head', 4, {'s_head': 20})
                            quest(message.from_user.id, 3, 2, 1)

                st = await guard_power(mid)
                if int(r.hget(c, 'base')) == 12:
                    money = int(r.hget(c, 'money'))
                    if money > 200000:
                        money = 200000
                    st = int(st * (1 + 0.01 * int(money / 1000)))
                r.hincrby(c, 'power', st)
                r.sadd(g, mid)
                name = names[int(r.hget(mid, 'name'))]
                msg = name + ' сьогодні охоронятиме територію від злодіїв.\n\n\U0001F4AA +' + str(st)
                if int(r.hget(c, 'salary')) == 1 and int(r.hget(c, 'money')) >= 10:
                    money, tax, packs = 5, 3, 0
                    if int(r.hget(c, 'new_post')):
                        money, tax, packs = 5, 5, 1
                    if int(r.hget(c, 'side')) == 4:
                        money = money + tax
                        tax = 0
                    if int(r.hget(message.from_user.id, 'defense')) == 5 and int(r.hget(c, 'money')) >= 50:
                        if message.from_user.is_premium:
                            money = money * 5
                            tax = tax * 5
                            packs = packs * 5
                        else:
                            money = money * 3
                            tax = tax * 3
                            packs = packs * 3
                        damage_defense(message.from_user.id, 5)
                    r.hincrby(c, 'money', -(money + tax))
                    r.hincrby('soledar', 'money', tax)
                    if money:
                        r.hincrby(message.from_user.id, 'money', money)
                        msg += f' \n\U0001F4B5 +{money}'
                        if packs:
                            r.hincrby(message.from_user.id, 'packs', packs)
                            msg += f' \U0001F4E6 +{packs}'
                    if int(r.hget(c, 'buff_4')) == 22:
                        q_points(message.from_user.id, 12)
                        msg += ' \U0001fa99 +12'

                if int(r.hget(c, 'build6')) == 1:
                    ch = 3 * (int(r.hget(c, 'wood')) + int(r.hget(c, 'stone')) +
                              int(r.hget(c, 'cloth')) + int(r.hget(c, 'brick')))
                    if choices([1, 0], [int(ch / 1000), 100 - int(ch / 1000)]) == [1]:
                        r.hset(message.from_user.id, 'time', 0)
                        msg += '\n\U0001F372 +1'
                if int(r.hget('convoy', 'day')) != datetime.now().day:
                    r.hset('convoy', 'power', 5000000, {'day': datetime.now().day,
                                                        'hour': randint(8, 12), 'first': 1})
                if int(r.hget(mid, 'class')) == 36 and int(r.hget(c, 'side')) == 3:
                    value = 500000
                    r.hincrby('convoy', 'power', value)
                    for mem in r.smembers('followers'):
                        try:
                            c3 = 'c' + mem.decode()
                            if int(r.hget(c3, 'not_time')) != datetime.now().day:
                                if int(r.hget(c3, 'technics')) >= 3:
                                    r.hset(c3, 'not_time', datetime.now().day)
                                    r.hincrby(c3, 'technics', -3)
                                else:
                                    r.hset(c3, 'notification', 0)
                                    r.srem('followers', mem)
                                    continue
                            await bot.send_message(int(mem), '\U0001F69B Додатковий гумконвой вже в дорозі!')
                        except:
                            pass
                    msg += f'\n\U0001F396 Генерал викликав додатковий гумконвой.\n\U0001F69B +{value}'
                elif int(r.hget(mid, 'class')) in (8, 18, 28) and int(r.hget(mid, 'weapon')) == 39:
                    chance = int(r.hget(mid, 'intellect'))
                    if choices([1, 0], weights=[chance, 100 - chance])[0]:
                        damage_weapon(mid, 0)
                        ch = int(r.hget('convoy', 'hour'))
                        o = 'об' if ch == 11 else 'о'
                        if datetime.now().hour >= ch:
                            msg2 = f'📟 Хакер дізнався, що гумконвой приїжджав {o} {ch} годині.'
                        else:
                            msg2 = f'📟 Хакер дізнався, що гумконвой приїде {o} {ch} годині.'
                        await bot.send_message(mid, msg2)
                msg += f"\n\U0001F4AA Загальна сила: {r.hget(c, 'power').decode()}\n\U0001F5E1 Кількість сторожів: " \
                       f"{r.scard(g)}/5"
                mines = int(r.hget(c, 'mines'))
                if mines > 0:
                    msg += f'\n\U0001F6A7 Кількість мін: {mines}'
                await message.reply(msg)
            else:
                msg = f"Твій русак сьогодні вже своє відпрацював\n\n\U0001F4AA Загальна сила: " \
                      f"{r.hget(c, 'power').decode()}\n\U0001F5E1 Кількість сторожів: {r.scard(g)}/5"
                mines = int(r.hget(c, 'mines'))
                if mines > 0:
                    msg += f'\n\U0001F6A7 Кількість мін: {mines}'
                await message.reply(msg)
    except:
        pass


@dp.message_handler(commands=['quest'])
async def get_quest(message):
    try:
        msg = quests(message.from_user.id)
        await message.reply(msg)
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
                    if int(r.hget(c, 'buff_3')) == 1:
                        cooldown = 2700
                    else:
                        cooldown = 3600

                    if int(datetime.now().timestamp()) - int(r.hget(c, 'raid_ts2')) > cooldown:
                        try:
                            try:
                                await bot.delete_message(message.chat.id, message.message_id)
                            except:
                                pass
                            a = await bot.send_message(message.chat.id, '\U0001F4B0 Починається рейд...\n\n',
                                                       reply_markup=battle_button_4(), disable_web_page_preview=True)
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
                        seconds = cooldown - int(datetime.now().timestamp()) + int(r.hget(c, 'raid_ts2'))
                        minutes = seconds // 60
                        msg = f'Рейди можна проводити один раз в годину.\nЗалишилось {minutes}хв. {seconds % 60}с.'
                        if minutes == 0:
                            msg = f'Рейди можна проводити один раз в годину.\nЗалишилось {seconds}с.'
                        await message.reply(msg)
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


@dp.message_handler(commands=['status'])
async def status(message):
    uid = message.from_user.id
    day = datetime.now().day
    msg = ''
    markup = InlineKeyboardMarkup()

    if r.hexists(uid, 'time'):
        if int(r.hget(uid, 'time')) == day:
            if r.hexists(uid, 'time22') and int(r.hget(uid, 'time22')) == day:
                msg += '\U0001f7e9 /feed\n'
            elif r.hexists(uid, 'time22') and int(r.hget(uid, 'time22')) != day:
                msg += '\U0001f7e8 /feed\n'
            else:
                msg += '\U0001f7e9 /feed\n'
        else:
            if r.hexists(uid, 'time22') and int(r.hget(uid, 'time22')) == day:
                msg += '\U0001f7e8 /feed\n'
            else:
                msg += '\U0001f7e5 /feed\n'
    else:
        msg += '\U0001f7e5 /feed\n'

    if r.hexists(uid, 'time1'):
        if int(r.hget(uid, 'time1')) == day:
            if r.hexists(uid, 'time23') and int(r.hget(uid, 'time23')) == day:
                msg += '\U0001f7e9 /mine\n'
            elif r.hexists(uid, 'time23') and int(r.hget(uid, 'time23')) != day:
                msg += '\U0001f7e8 /mine\n'
            else:
                msg += '\U0001f7e9 /mine\n'
        else:
            if r.hexists(uid, 'time23') and int(r.hget(uid, 'time23')) == day:
                msg += '\U0001f7e8 /mine\n'
            else:
                msg += '\U0001f7e5 /mine\n'
    else:
        msg += '\U0001f7e5 /mine\n'

    if r.hexists(uid, 'time4') and r.hexists(uid, 'woman') and int(r.hget(uid, 'woman')) > 0:
        if int(r.hget(uid, 'time4')) == day:
            msg += '\U0001f7e9 /woman\n'
        else:
            msg += '\U0001f7e5 /woman\n'

    if r.hexists(uid, 'clan_time') and checkClan(uid):
        if int(r.hget(uid, 'clan_time')) == day:
            msg += '\U0001f7e9 /work\n'
        else:
            msg += '\U0001f7e5 /work\n'

    if r.hexists(uid, 'qt'):
        q = r.hmget(uid, 'qt', 'q1', 'q2', 'q3')
        if int(q[0]) == day:
            if int(q[1]) == 0 and int(q[2]) == 0 and int(q[3]) == 0:
                msg += '\U0001f7e9 /quest\n'
            elif int(q[1]) == 0 or int(q[2]) == 0 or int(q[3]) == 0:
                msg += '\U0001f7e8 /quest\n'
                markup.add(InlineKeyboardButton(text='\U0001F4F0 Змінити квести - \U0001F4B5 50',
                                                callback_data='re-roll'))
            else:
                msg += '\U0001f7e5 /quest\n'
                markup.add(InlineKeyboardButton(text='\U0001F4F0 Змінити квести - \U0001F4B5 50',
                                                callback_data='re-roll'))
        else:
            msg += '\U0001f7e5 /quest\n'

    if r.hexists(uid, 'wordle_time'):
        if int(r.hget(uid, 'wordle_time')) == day:
            msg += '\U0001f7e9 <a href="https://t.me/wordle1bot">/daily</a>\n'
        else:
            msg += '\U0001f7e5 <a href="https://t.me/wordle1bot">/daily</a>\n'
    else:
        msg += '\U0001f7e5 <a href="https://t.me/wordle1bot">/daily</a>\n'

    if r.hexists(uid, 'restriction'):
        ts1 = int(r.hget(uid, 'restriction_ts')) + 604800
        ts = datetime.fromtimestamp(ts1)

        if ts1 > int(datetime.now().timestamp()):
            msg += f'\n\u231B Дуелі: {int(r.hget(uid, "restriction"))}/10000'
            msg += f'\nОновлення ліміту:\n{ts.strftime("%H:%M %d.%m.%Y")}'
        else:
            msg += '\n\u231B Дуелі: 0/10000'

    await message.reply(msg, reply_markup=markup, parse_mode='HTML', disable_web_page_preview=True)


@dp.message_handler(commands=['commands'])
async def commands(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Інформація', callback_data='full_list_1'))
    markup.add(InlineKeyboardButton(text='Гра в русаків', callback_data='full_list_2'))
    markup.add(InlineKeyboardButton(text='Топ', callback_data='full_list_3'),
               InlineKeyboardButton(text='Клани', callback_data='full_list_4'))
    markup.add(InlineKeyboardButton(text='Адміністраторські команди', callback_data='full_list_5'))
    await message.reply('/help - основна інформація\n'
                        '/links - реклама, головний чат, творець\n'
                        '/wiki - інформація щодо гри\n'
                        '/feed - погодувати русака\n'
                        '/mine - заробити гривні (доступно тільки в '
                        '<a href="https://t.me/+cClR7rA-sZAyY2Uy">@soledar1</a>)\n'
                        '/woman - провідати жінку\n'
                        '/status - прогрес за день\n'
                        '/clan - інформація про клан\n'
                        '/achieve - досягнення\n'
                        '/skills - вміння\n'
                        '/i - інвентар\n'
                        '/battle - чатова битва (5-10 русаків)\n'
                        '/war - міжчатова битва 5х5\n'
                        '/quests - щоденні квести\n'
                        '...', reply_markup=markup,
                        parse_mode='HTML', disable_web_page_preview=True)


@dp.message_handler(commands=['wiki'])
async def wiki(message):
    try:
        msg, markup = wiki_text('wiki_menu')
        await bot.send_message(message.from_user.id, msg, reply_markup=markup)
        if message.chat.type != 'private':
            await message.reply('Надіслано в пп.')
    except:
        pass


@dp.callback_query_handler(lambda call: True)
async def handle_query(call):
    if call.data.startswith('getrusak') and call.from_user.id == call.message.reply_to_message.from_user.id:
        if r.hexists(call.from_user.id, 'name') == 1:
            await bot.edit_message_text(text='\U0001F98D У тебе вже є русак!',
                                        chat_id=call.message.chat.id, message_id=call.message.message_id)
        else:
            cid = call.from_user.id
            n, s, i = choice(list(names)), randint(100, 150), choices([1, 2], weights=[4, 1])[0]
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
            if r.hexists(call.from_user.id, 'time1') == 0:
                r.hset(call.from_user.id, 'time1', 0)
            if r.hexists(call.from_user.id, 'packs') == 0:
                r.hset(call.from_user.id, 'packs', 5)
            if r.hexists(call.from_user.id, 'money') == 0:
                r.hset(call.from_user.id, 'money', 20)
            if r.hexists(call.from_user.id, 'strap') == 0:
                r.hset(call.from_user.id, 'strap', 0)
            if r.hexists(call.from_user.id, 'salt') == 0:
                r.hset(call.from_user.id, 'salt', 0)
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
            if r.hexists(call.from_user.id, 's4') == 0:
                r.hset(call.from_user.id, 's4', 1)
            if r.hexists(call.from_user.id, 's5') == 0:
                r.hset(call.from_user.id, 's5', 1)
            if r.hexists(call.from_user.id, 'purchase') == 0:
                r.hset(call.from_user.id, 'purchase', 0)
            if r.hexists(call.from_user.id, 'q1') == 0:
                r.hset(call.from_user.id, 'q1', 0)
            if r.hexists(call.from_user.id, 'q2') == 0:
                r.hset(call.from_user.id, 'q2', 0)
            if r.hexists(call.from_user.id, 'q3') == 0:
                r.hset(call.from_user.id, 'q3', 0)
            if r.hexists(call.from_user.id, 'q1t') == 0:
                r.hset(call.from_user.id, 'q1t', 0)
            if r.hexists(call.from_user.id, 'q2t') == 0:
                r.hset(call.from_user.id, 'q2t', 0)
            if r.hexists(call.from_user.id, 'q3t') == 0:
                r.hset(call.from_user.id, 'q3t', 0)
            if r.hexists(call.from_user.id, 'qt') == 0:
                r.hset(call.from_user.id, 'qt', 0)
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
                                                            inline_message_id=call.inline_message_id,
                                                            disable_web_page_preview=True)
                            else:
                                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                text='Твій русак не підходить по силі для цього бою.')
                        else:
                            if int(r.hget(uid2, 'class')) == 29:
                                msg, money = '', 0
                                if anti_clicker(uid2):
                                    if int(r.hget(uid2, 'support')) == 1 and \
                                            checkClan(uid2, building='build2', level=4):
                                        money = 10
                                    else:
                                        money = 5
                                    msg = f'\U0001F4B5 +{money}'
                                await bot.edit_message_text(
                                    text=f'\u26D1 {call.from_user.first_name} відправив свого русака надати медичну '
                                         f'допомогу пораненому.\n\U0001fac0 +20 {msg}',
                                    inline_message_id=call.inline_message_id, disable_web_page_preview=True)
                                hp(20, uid1)
                                r.hincrby(call.from_user.id, 'money', money)
                            elif int(r.hget(call.from_user.id, 'class')) == 23:
                                await bot.edit_message_text(
                                    text='\U0001F52E ' + ' Некромант проводить дивні ритуали над напівживим русаком...'
                                                         '\n\U0001fac0 +10 \U0001F44A +5',
                                    inline_message_id=call.inline_message_id, disable_web_page_preview=True)
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
                                uname = q[1][1:].lower()
                                if call.from_user.username and uname == call.from_user.username.lower():
                                    await fight(uid1, uid2, un1, un2, 5, call.inline_message_id)
                                else:
                                    await bot.answer_callback_query(callback_query_id=call.id,
                                                                    show_alert=True, text='Цей бій не для тебе.')
                            except:
                                await fight(uid1, uid2, un1, un2, 5, call.inline_message_id)
                    elif cdata[1] == 'pr':
                        try:
                            q = cdata[2].split()
                            uname = q[1][1:].lower()
                            if call.from_user.username and uname == call.from_user.username.lower():
                                fi = await fight(uid1, uid2, un1, un2, 1, call.inline_message_id)
                                await bot.edit_message_text(text=fi, inline_message_id=call.inline_message_id,
                                                            disable_web_page_preview=True)
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
                    await bot.edit_message_text(text=fi, inline_message_id=call.inline_message_id,
                                                disable_web_page_preview=True)

    elif call.data.startswith('join') and r.hexists('battle' + str(call.message.chat.id), 'start'):
        if str(call.from_user.id).encode() not in r.smembers('fighters' + str(call.message.chat.id)) and \
                r.hexists(call.from_user.id, 'name') == 1 and \
                call.message.message_id == int(r.hget('battle' + str(call.message.chat.id), 'start')):
            r.hset(call.from_user.id, 'firstname', call.from_user.first_name)

            maximum = 10
            #  if call.message.chat.id == -1001211933154:
            #    maximum = 20

            if r.scard('fighters' + str(call.message.chat.id)) < maximum:
                r.sadd('fighters' + str(call.message.chat.id), call.from_user.id)

                fighters = r.smembers('fighters' + str(call.message.chat.id))
                fighters_num = r.scard('fighters' + str(call.message.chat.id))

                ts = int(datetime.now().timestamp())
                if not r.hexists('battle' + str(call.message.chat.id), 'edit_ts'):
                    r.hset('battle' + str(call.message.chat.id), 'edit_ts', ts)

                if ts - int(r.hget('battle' + str(call.message.chat.id), 'edit_ts')) > 2 or fighters_num >= maximum:
                    r.hset('battle' + str(call.message.chat.id), 'edit_ts', ts)

                    msg = '\u2694 Починається битва...\n\nБійці: '
                    i = 1
                    for mem in fighters:
                        msg += r.hget(mem, 'firstname').decode()
                        if fighters_num != i:
                            msg += ', '
                            i += 1
                    if fighters_num >= maximum:
                        msg += '\n\nБій почався...'

                    if 5 <= fighters_num < maximum and call.message.chat.id != -1001211933154:
                        markup = battle_button_2()
                    elif fighters_num >= maximum:
                        markup = None
                    else:
                        markup = battle_button()

                    await bot.edit_message_text(
                        text=msg.replace('@', ''),
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        reply_markup=markup,
                        disable_web_page_preview=True)

                if fighters_num >= maximum:
                    ran = choice(['Битва в Соледарі', 'Битва на овечій фермі', 'Битва на покинутому заводі',
                                  'Битва в темному лісі', 'Битва біля старого дуба', 'Битва в житловому районі',
                                  'Битва біля поліцейського відділку', 'Битва в офісі ОПЗЖ',
                                  'Битва в серверній кімнаті', 'Штурм Горлівки', 'Штурм ДАП', 'Битва в психлікарні',
                                  'Висадка в Чорнобаївці', 'Битва в темному провулку', 'Битва біля розбитої колони',
                                  'Розгром командного пункту'])
                    big_battle = True
                    try:
                        mid = int(r.hget('battle' + str(call.message.chat.id), 'pin'))
                        await bot.unpin_chat_message(chat_id=call.message.chat.id, message_id=mid)
                    except:
                        pass
                    await war(call.message.chat.id, ran, big_battle)
            await call.answer()
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
            allow, msg, n = True, '', ''
            if r.hexists('c' + str(call.message.chat.id), 'war_allow'):
                if int(r.hget('c' + str(call.message.chat.id), 'war_allow')) == 1:
                    if str(call.from_user.id).encode() not in r.smembers('cl' + str(call.message.chat.id)) and \
                            int(datetime.now().timestamp()) - \
                            int(r.hget('war_battle' + str(call.message.chat.id), 'war_ts')) < 600:
                        allow = False
                        msg = 'Ти не в цьому клані, тому зайти зможеш через 10 хвилин після початку набору.'
                elif int(r.hget('c' + str(call.message.chat.id), 'war_allow')) == 2:
                    if str(call.from_user.id).encode() not in r.smembers('cl' + str(call.message.chat.id)):
                        allow = False
                        msg = 'Ти не в цьому клані, тому ти не зможеш зайти в битву.'
                if int(r.hget('c' + str(call.message.chat.id), 'tier')) in (1, 2):
                    n = '2'
            if str(call.from_user.id).encode() in r.smembers('war_crime'):
                allow = False
                msg = 'Юзерботам заборонено заходити в міжчатові битви'
            if allow:
                if r.scard('fighters_2' + str(call.message.chat.id)) < 5:
                    r.sadd('fighters_2' + str(call.message.chat.id), call.from_user.id)
                    r.hset(call.from_user.id, 'firstname', call.from_user.first_name)
                    r.hset(call.from_user.id, 'in_war', call.message.chat.id)
                    r.hset(call.from_user.id, 'w_ts', int(datetime.now().timestamp()))
                    r.sadd('in_war', call.from_user.id)

                    fighters = r.smembers('fighters_2' + str(call.message.chat.id))
                    fighters_num = r.scard('fighters_2' + str(call.message.chat.id))

                    msg = f'{call.message.text.split()[0]} Починається міжчатова битва...\n\nБійці: '
                    i = 1
                    for mem in fighters:
                        msg += r.hget(mem, 'firstname').decode()
                        if fighters_num != i:
                            msg += ', '
                            i += 1
                    if fighters_num >= 5:
                        markup = None
                    else:
                        markup = battle_button_3()

                    await bot.edit_message_text(
                        text=msg.replace('@', ''),
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        reply_markup=markup,
                        disable_web_page_preview=True)

                    if r.hexists(222, call.message.chat.id) and int(r.hget(222, call.message.chat.id)) > 250:
                        n = '2'

                    if fighters_num >= 5:
                        if not r.scard('battles' + n):
                            await call.message.reply('\u2694 Пошук ворогів...')
                            r.sadd('battles' + n, call.message.chat.id)
                        else:
                            if str(call.message.chat.id).encode() in r.smembers('battles' + n):
                                pass
                            else:
                                enemy = r.spop('battles' + n)

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
                                await bot.send_message(int(call.message.chat.id), msg.replace('@', ''),
                                                       disable_web_page_preview=True)
                                await bot.send_message(int(enemy), msg.replace('@', ''), disable_web_page_preview=True)
                                await great_war(call.message.chat.id, int(enemy), a, b)
                                try:
                                    mid = int(r.hget('war_battle' + str(call.message.chat.id), 'pin'))
                                    await bot.unpin_chat_message(chat_id=call.message.chat.id, message_id=mid)
                                except:
                                    pass
                                try:
                                    mid = int(r.hget('war_battle' + enemy.decode(), 'pin'))
                                    await bot.unpin_chat_message(chat_id=int(enemy), message_id=mid)
                                except:
                                    pass
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text=msg)
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ти або вже в битві, або в тебе відсутній русак')

    elif call.data.startswith('raid_join') and r.hexists('c' + str(call.message.chat.id), 'start') == 1:
        if str(call.from_user.id).encode() not in r.smembers('fighters_3' + str(call.message.chat.id)) and \
                r.hexists(call.from_user.id, 'name') == 1 and \
                call.message.message_id == int(r.hget('c' + str(call.message.chat.id), 'start')) and\
                str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)):
            uname = call.from_user.first_name.replace('@', '')
            if 0 <= datetime.now().hour < 8:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Комендантська година, рейди недоступні.')
            else:
                r.hset(call.from_user.id, 'firstname', call.from_user.first_name)
                if r.scard('fighters_3' + str(call.message.chat.id)) < 5:
                    r.sadd('fighters_3' + str(call.message.chat.id), call.from_user.id)

                    fighters = r.smembers('fighters_3' + str(call.message.chat.id))
                    fighters_num = r.scard('fighters_3' + str(call.message.chat.id))

                    msg = f'\U0001F4B0 Починається рейд...\n\nБійці: '
                    i = 1
                    for mem in fighters:
                        msg += r.hget(mem, 'firstname').decode()
                        if fighters_num != i:
                            msg += ', '
                            i += 1
                    if fighters_num >= 5:
                        markup = None
                        msg += '\n\nРейд почався...'
                    else:
                        markup = battle_button_4()

                    await bot.edit_message_text(
                        text=msg.replace('@', ''),
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        reply_markup=markup,
                        disable_web_page_preview=True)

                    if fighters_num == 5:
                        await call.message.reply('\u2694 Русаки вирушили в рейд...')
                        await start_raid(call.message.chat.id)
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ти або вже в битві, або в тебе відсутній русак.\n\n'
                                                 'В рейді можуть брати участь тільки учасники клану')

    elif call.data.startswith('captcha_true') and \
            call.from_user.id == call.message.reply_to_message.new_chat_members[0].id:
        try:
            un_mute_permissions = ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_polls=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True
            )
            await bot.restrict_chat_member(call.message.chat.id, call.from_user.id, permissions=un_mute_permissions)
            await bot.edit_message_text(text=f'\u2705 Вітаю в чаті, {call.from_user.first_name}.',
                                        chat_id=call.message.chat.id, message_id=call.message.message_id)
        except:
            pass

    elif call.data.startswith('captcha_false') and \
            call.from_user.id == call.message.reply_to_message.new_chat_members[0].id:
        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Неправильна відповідь.')

    elif call.data.startswith('choose_lang'):
        if call.data.startswith('choose_lang_uk'):
            r.hset(call.from_user.id, 'language_code', 'uk')
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Вибрано українську мову.')
        if call.data.startswith('choose_lang_en'):
            r.hset(call.from_user.id, 'language_code', 'en')
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='English is selected.')

    elif call.data.startswith('create_'):
        if r.hexists('c' + str(call.message.chat.id), 'base') == 0:
            if len(str(r.hget(call.from_user.id, 'clan'))) < 5:
                admins = []
                admins2 = await bot.get_chat_administrators(call.message.chat.id)
                for admin in admins2:
                    admins.append(admin.user.id)
                if call.from_user.id in admins:
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
                                'notification': 0, 'hints': 0, 'mines': 0, 'wall': 0,
                                'leader': call.from_user.id, 'allow': 0, 'title': call.message.chat.title,
                                'side': 0, 'build1': 0, 'build2': 0, 'build3': 0, 'build4': 0,
                                'build5': 0, 'build6': 0, 'war': 0, 'tier': 3, 'war_wins': 0,
                                'buff_1': 0, 'buff_2': 0, 'buff_3': 0, 'buff_4': 0, 'buff_5': 0})
                        r.sadd('cl' + str(call.message.chat.id), call.from_user.id)
                        r.sadd('clans', call.message.chat.id)
                        r.hset(call.from_user.id, 'clan', call.message.chat.id,
                               {'clan_ts': int(datetime.now().timestamp())})
                        if r.hexists(call.from_user.id, 'clan_time') == 0:
                            r.hset(call.from_user.id, 'clan_time', 0)
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
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='В тебе є свій клан.')

    elif call.data.startswith('enter_war'):
        weekday = datetime.today().weekday()
        cid = call.message.chat.id
        uid = call.from_user.id
        c = f'c{cid}'
        if checkLeader(uid, cid):
            if weekday in (5, 6) and int(r.hget(c, 'tier')) == 3 and int(r.hget(c, 'base')) > 1:
                if r.scard(f'cl{cid}') >= 5:
                    r.sadd('registered', cid)
                    await bot.edit_message_text('Ваш клан зареєстровано на війни кланів.\nСамі війни повинні'
                                                ' відбудуться наступного тижня',
                                                call.message.chat.id, call.message.message_id)
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Знайдіть хоча б 5 учасників в клан')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Реєстрація тільки у вихідні, і тільки для тір-3 кланів')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Тільки лідер або заступники можуть натискати цю кнопку')

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
            ts = 10800
        if call.from_user.id in admins and \
                str(call.from_user.id).encode() in r.smembers('cl' + str(call.message.chat.id)) and \
                r.scard('cl' + str(call.message.chat.id)) < num:
            if r.hexists(call.from_user.id, 'name'):
                if int(datetime.now().timestamp()) - int(r.hget(uid, 'clan_ts')) > ts \
                        or str(uid).encode() in r.smembers('sudoers'):
                    r.hset(uid, 'clan', call.message.chat.id, {'clan_ts': int(datetime.now().timestamp()),
                                                               'firstname': call.from_user.first_name})
                    if r.hexists(uid, 'clan_time') == 0:
                        r.hset(uid, 'clan_time', 0)
                    r.sadd('cl' + str(call.message.chat.id), uid)
                    if int(r.hget('c' + str(call.message.chat.id), 'buff_4')) == 32:
                        q_points(call.from_user.id, 10)
                    await bot.edit_message_text('\U0001F4E5 Ти вступив в клан ' +
                                                r.hget('c' + str(call.message.chat.id), 'title').decode() + '.',
                                                call.message.chat.id, call.message.message_id)
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='\U0001F4E5 Вступати в клан можна лише раз в тиждень.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Цей користувач не має свого русака.')

    elif call.data.startswith('promote_to_leader'):
        try:
            uid1 = call.from_user.id
            uid2 = call.data.split('_')[3]
            uid2e = str(uid2).encode()
            c = 'c' + r.hget(uid1, 'clan').decode()
            cl = 'cl' + r.hget(uid1, 'clan').decode()
            cl2 = 'cl2' + r.hget(uid1, 'clan').decode()
            if call.message.chat.id == int(r.hget(uid1, 'clan')):
                if uid1 == int(r.hget(c, 'leader')):
                    if uid2e in r.smembers(cl) and uid2e in r.smembers(cl2):
                        r.hset(c, 'leader', uid2)
                        r.sadd(cl2, uid1)
                        r.srem(cl2, uid2)
                        await bot.edit_message_text('\U0001F530 Змінено лідера клану!',
                                                    call.message.chat.id, call.message.message_id)
        except:
            pass

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
            await bot.edit_message_text(auto_clan_settings('c' + str(c)), call.message.chat.id,
                                        call.message.message_id, reply_markup=clan_set())
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Режим набору змінено.')

    elif call.data.startswith('toggle_war'):
        c = int(r.hget(call.from_user.id, 'clan'))
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, c):
            if int(r.hget('c' + str(c), 'war_allow')) == 0:
                r.hset('c' + str(c), 'war_allow', 1)
            elif int(r.hget('c' + str(c), 'war_allow')) == 1:
                r.hset('c' + str(c), 'war_allow', 2)
            else:
                r.hset('c' + str(c), 'war_allow', 0)
            await bot.edit_message_text(auto_clan_settings('c' + str(c)), call.message.chat.id,
                                        call.message.message_id, reply_markup=clan_set())
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Режим входу в міжчатові битви змінено.')

    elif call.data.startswith('salary'):
        c = int(r.hget(call.from_user.id, 'clan'))
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, c):
            if int(r.hget('c' + str(c), 'salary')) == 0:
                r.hset('c' + str(c), 'salary', 1)
            else:
                r.hset('c' + str(c), 'salary', 0)
            await bot.edit_message_text(auto_clan_settings('c' + str(c)), call.message.chat.id,
                                        call.message.message_id, reply_markup=clan_set())
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Режим видачі зарплати за роботу змінено.')

    elif call.data.startswith('recruit'):
        c = int(r.hget(call.from_user.id, 'clan'))
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, c) \
                and str(c).encode() not in r.smembers('banned'):
            try:
                if int(r.hget('c' + str(c), 'recruitment')) == 0:
                    if int(r.hget('c' + str(c), 'technics')) >= 3:
                        try:
                            await bot.revoke_chat_invite_link(c, r.hget('c' + str(c), 'link').decode())
                        except:
                            pass
                        a = await bot.create_chat_invite_link(c, creates_join_request=True)
                        r.hset('c' + str(c), 'recruitment', 1, {'link': a.invite_link, 'rec_time': datetime.now().day})
                        r.sadd('recruitment', c)
                        r.hincrby('c' + str(c), 'technics', -3)
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо радіотехніки.')
                else:
                    try:
                        await bot.revoke_chat_invite_link(c, r.hget('c' + str(c), 'link').decode())
                    except:
                        pass
                    r.hset('c' + str(c), 'recruitment', 0)
                    r.srem('recruitment', c)
                await bot.edit_message_text(auto_clan_settings('c' + str(c)), call.message.chat.id,
                                            call.message.message_id, reply_markup=clan_set())
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Режим набору змінено.')
            except:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Схоже в бота нема прав додавати користувачів.')

    elif call.data.startswith('notification'):
        c = int(r.hget(call.from_user.id, 'clan'))
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, c):
            if int(r.hget('c' + str(c), 'notification')) == 0:
                if int(r.hget('c' + str(c), 'technics')) >= 3:
                    r.hset('c' + str(c), 'notification', 1)
                    r.sadd('followers', c)
                    r.hincrby('c' + str(c), 'technics', -3)
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо радіотехніки.')
            else:
                r.hset('c' + str(c), 'notification', 0, {'not_time': datetime.now().day})
                r.srem('followers', c)
            await bot.edit_message_text(auto_clan_settings('c' + str(c)), call.message.chat.id,
                                        call.message.message_id, reply_markup=clan_set())
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Сповіщення змінено.')

    elif call.data.startswith('hints'):
        c = int(r.hget(call.from_user.id, 'clan'))
        if checkClan(call.from_user.id) and checkLeader(call.from_user.id, c):
            if int(r.hget('c' + str(c), 'hints')) == 0:
                r.hset('c' + str(c), 'hints', 1)
            else:
                r.hset('c' + str(c), 'hints', 0)
            await bot.edit_message_text(auto_clan_settings('c' + str(c)), call.message.chat.id,
                                        call.message.message_id, reply_markup=clan_set())
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Налаштування підказок змінені.')

    elif call.data.startswith('get_members'):
        uid = call.from_user.id
        if checkClan(uid) and checkLeader(uid, int(r.hget(uid, 'clan'))) or \
                str(call.from_user.id).encode() in r.smembers('sudoers'):
            msg = ''
            for mem in r.smembers('cl' + r.hget(call.from_user.id, 'clan').decode()):
                if r.hexists(mem, 'clan_time') and int(r.hget(mem, 'clan_time')) == datetime.now().day:
                    msg += '\U0001f7e9 '
                else:
                    msg += '\U0001f7e5 '
                if r.hexists(mem, 'firstname'):
                    name = r.hget(mem, 'firstname').decode().replace('<', '.').replace('>', '.')
                else:
                    name = '?'
                msg += f'<a href="tg://user?id={int(mem)}">{name}</a>\n'
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Отримати список з id та силою', callback_data='get_id_members'))
            await bot.send_message(call.message.chat.id, msg, parse_mode='HTML', reply_markup=markup)

    elif call.data.startswith('get_id_members'):
        uid = call.from_user.id
        if checkClan(uid) and checkLeader(uid, int(r.hget(uid, 'clan'))) or \
                str(call.from_user.id).encode() in r.smembers('sudoers'):
            msg = ''
            today = datetime.now().day
            for mem in r.smembers('cl' + r.hget(call.from_user.id, 'clan').decode()):

                stats = r.hmget(mem, 'strength', 'strength2', 'class', 'class2',
                                'clan_time', 'firstname', 'qt', 'q1', 'q2', 'q3')

                if stats[4] and int(stats[4]) == today:
                    msg += '\U0001f7e9 '
                else:
                    msg += '\U0001f7e5 '
                if stats[5]:
                    name = stats[5].decode().replace('<', '.').replace('>', '.')
                else:
                    name = '?'
                msg += f'<a href="tg://user?id={int(mem)}">{name}</a> <code>{mem.decode()}</code>\n'

                if stats[0]:
                    msg += f'{icons_simple[int(stats[2])]} \U0001F4AA {int(stats[0])}'
                    if stats[1]:
                        msg += f' {icons_simple[int(stats[3])]} \U0001F4AA {int(stats[1])}'

                quests_done = 0
                if stats[6] and int(stats[6]) == today:
                    if int(stats[7]) == 0:
                        quests_done += 1
                    if int(stats[8]) == 0:
                        quests_done += 1
                    if int(stats[9]) == 0:
                        quests_done += 1
                msg += f' \U0001F4F0 {quests_done}/3'

                msg += '\n'
            await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, parse_mode='HTML')
    elif call.data.startswith('build'):
        if call.data.startswith('build_sawmill') and call.from_user.id == call.message.reply_to_message.from_user.id:
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
                    if int(r.hget(c, 'money')) >= 100 and int(r.hget(c, 'wood')) >= 300 \
                            and int(r.hget(c, 'stone')) >= 200:
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
                    await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано '
                                                                 'житловий комплекс.')
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
                    await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано '
                                                                 'силікатний завод.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо ресурсів.')

        elif call.data.startswith('build_shop') and call.from_user.id == call.message.reply_to_message.from_user.id:
            c = 'c' + str(call.message.chat.id)
            if int(r.hget(c, 'shop')) == 0:
                if int(r.hget(c, 'wood')) >= 1000 and int(r.hget(c, 'stone')) >= 200 \
                        and int(r.hget(c, 'cloth')) >= 400 \
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

        elif call.data.startswith('build_wall') and call.from_user.id == call.message.reply_to_message.from_user.id:
            c = 'c' + str(call.message.chat.id)
            if int(r.hget(c, 'wall')) == 0:
                if int(r.hget(c, 'wood')) >= 500 and int(r.hget(c, 'stone')) >= 250 and int(r.hget(c, 'cloth')) >= 150 \
                        and int(r.hget(c, 'brick')) >= 100 and int(r.hget(c, 'money')) >= 1000 \
                        and int(r.hget(c, 'r_spirit')) >= 30:
                    r.hincrby(c, 'wood', -500)
                    r.hincrby(c, 'stone', -250)
                    r.hincrby(c, 'cloth', -150)
                    r.hincrby(c, 'brick', -100)
                    r.hincrby(c, 'money', -1000)
                    r.hincrby(c, 'r_spirit', -30)
                    r.hset(c, 'wall', 1)
                    await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано '
                                                                 'стіну оголошень.')
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
                    await bot.send_message(call.message.chat.id, 'На території вашого клану побудовано блокпост.'
                                                                 '\n\nМожна туди відправити русака замість роботи'
                                                                 ' командою /guard')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо ресурсів.')

        elif call.data.startswith('build_camp') and call.from_user.id == call.message.reply_to_message.from_user.id:
            c = 'c' + str(call.message.chat.id)
            if int(r.hget(c, 'camp')) == 0:
                if int(r.hget(c, 'wood')) >= 3000 and int(r.hget(c, 'stone')) >= 1000 \
                        and int(r.hget(c, 'cloth')) >= 1000 and int(r.hget(c, 'brick')) >= 400 \
                        and int(r.hget(c, 'money')) >= 3000 and int(r.hget(c, 'r_spirit')) >= 100:
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
                if int(r.hget(c, 'wood')) >= 1000 and int(r.hget(c, 'stone')) >= 2000 \
                        and int(r.hget(c, 'cloth')) >= 800 and int(r.hget(c, 'brick')) >= 500 \
                        and int(r.hget(c, 'money')) >= 5000 and int(r.hget(c, 'r_spirit')) >= 100:
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
                if int(r.hget(c, 'wood')) >= 100 and int(r.hget(c, 'stone')) >= 50 and int(r.hget(c, 'money')) >= 1000 \
                        and int(r.hget(c, 'r_spirit')) >= 1:
                    r.hincrby(c, 'wood', -100)
                    r.hincrby(c, 'stone', -50)
                    r.hincrby(c, 'money', -1000)
                    r.hincrby(c, 'r_spirit', -1)
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
                if int(r.hget(c, 'wood')) >= 4000 and int(r.hget(c, 'stone')) >= 2000 \
                        and int(r.hget(c, 'cloth')) >= 750 \
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
                if int(r.hget(c, 'wood')) >= 3000 and int(r.hget(c, 'stone')) >= 500 \
                        and int(r.hget(c, 'cloth')) >= 500 and int(r.hget(c, 'brick')) >= 300 \
                        and int(r.hget(c, 'money')) >= 1000 and int(r.hget(c, 'r_spirit')) >= 50:
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
                if int(r.hget(c, 'wood')) >= 1000 and int(r.hget(c, 'stone')) >= 1000 \
                        and int(r.hget(c, 'cloth')) >= 500 \
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
                if int(r.hget(c, 'wood')) >= 2000 and int(r.hget(c, 'stone')) >= 1000 \
                        and int(r.hget(c, 'cloth')) >= 500 and int(r.hget(c, 'brick')) >= 400 \
                        and int(r.hget(c, 'money')) >= 2000 and int(r.hget(c, 'technics')) >= 200:
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
                if int(r.hget(c, 'wood')) >= 2000 and int(r.hget(c, 'stone')) >= 1000 \
                        and int(r.hget(c, 'cloth')) >= 800 and int(r.hget(c, 'brick')) >= 500 \
                        and int(r.hget(c, 'money')) >= 6000 and int(r.hget(c, 'technics')) >= 100:
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
                if int(r.hget(c, 'wood')) >= 15000 and int(r.hget(c, 'stone')) >= 10000 \
                        and int(r.hget(c, 'cloth')) >= 5000 and int(r.hget(c, 'brick')) >= 3000 \
                        and int(r.hget(c, 'money')) >= 10000 and int(r.hget(c, 'technics')) >= 300 \
                        and int(r.hget(c, 'r_spirit')) >= 300 and int(r.hget(c, 'codes')) >= 10:
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
        if call.data.startswith('sacrifice1'):
            msg = f'{call.message.text}\n\n⚰ Точно вбити русака?'
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Принести в жертву русака', callback_data='sacrifice2'))
            await bot.edit_message_text(text=msg, chat_id=call.message.chat.id,
                                        message_id=call.message.message_id, reply_markup=markup)
        elif call.data.startswith('sacrifice2'):
            str1 = int(r.hget(call.from_user.id, 'strength'))
            int1 = int(r.hget(call.from_user.id, 'intellect'))
            msg = f'{call.message.text}\n\n🕯 {str1} сили, {int1} інтелекту і все спорядження русака ' \
                  f'будуть назавжди втрачені.'
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text='Принести в жертву русака', callback_data='sacrifice3'))
            await bot.edit_message_text(text=msg, chat_id=call.message.chat.id,
                                        message_id=call.message.message_id, reply_markup=markup)
        elif call.data.startswith('sacrifice3'):
            r.hset(call.from_user.id, 'time2', datetime.now().day)
            name = int(r.hget(call.from_user.id, 'name'))
            r.hdel(call.from_user.id, 'name')
            try:
                cl = int(r.hget(call.from_user.id, 'class'))
                for member in r.smembers(call.message.chat.id):
                    try:
                        mem = int(member)
                        try:
                            st = await bot.get_chat_member(call.message.chat.id, mem)
                            if st.status in ('left', 'kicked', 'banned'):
                                r.srem(call.message.chat.id, mem)
                                continue
                        except:
                            r.srem(call.message.chat.id, mem)
                        i1 = int(r.hget(mem, 'spirit'))
                        i = int(i1 / 10)
                        r.hincrby(mem, 'spirit', -i)
                        if cl in (7, 17, 27):
                            mush = int(r.hget(mem, 'mushrooms'))
                            if mush > 0:
                                r.hset(mem, 'mushrooms', 0)
                                intellect(-mush, mem)
                            else:
                                r.hset(mem, 'spirit', i)
                        h = int(r.hget(mem, 'head'))
                        if h in (1, 7):
                            r.hset(mem, 'spirit', i1)
                            damage_head(mem)
                            if h == 7:
                                spirit(3000, mem, 0)
                    except:
                        pass
            except:
                pass
            clm = int(r.hget(call.from_user.id, 'class'))
            r.srem('class-' + str(clm), call.from_user.id)
            #r.hset(call.from_user.id, 'spirit', 0, {'strength': 100, 'intellect': 1, 'photo': choice(default),
            #                                        'class': 0, 'weapon': 0, 's_weapon': 0, 'defense': 0,
            #                                        's_defense': 0, 'support': 0, 's_support': 0, 'mushrooms': 0})
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
                r.hset(call.from_user.id, 'name2', choice(list(names)),
                       {'strength2': randint(100, 150),
                        'intellect2': choices([1, 2], weights=[4, 1])[0],
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

    elif call.data.startswith('addiction'):
        s4 = int(r.hget(call.from_user.id, 's4'))
        if s4 < 5:
            if int(r.hget(call.from_user.id, 'purchase')) >= s4 * 10:
                r.hincrby(call.from_user.id, 's4', 1)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text=f'\U0001F9C2 Ви підняли рівень наркозалежності до {s4+1}.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ще рано переходити на наступний етап наркозалежності.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Більше користі від солі не буде.')

    elif call.data.startswith('psycho'):
        s5 = int(r.hget(call.from_user.id, 's5'))
        if s5 < 5:
            if int(r.hget(call.from_user.id, 'childs')) >= s5 * 10 and \
                    int(r.hget(call.from_user.id, 'deaths')) >= s5 * 20:
                r.hincrby(call.from_user.id, 's5', 1)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text=f'\u2620\uFE0F Ви підняли рівень психозу до {s5+1}.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ще рано переходити на наступний рівень психозу.')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви вже достатньо псих.')

    elif call.data.startswith('re-roll') and call.from_user.id == call.message.reply_to_message.from_user.id:
        if int(r.hget(call.from_user.id, 'qt')) == datetime.now().day:
            q1 = int(r.hget(call.from_user.id, 'q1'))
            q2 = int(r.hget(call.from_user.id, 'q2'))
            q3 = int(r.hget(call.from_user.id, 'q3'))
            if q1 != 0 or q2 != 0 or q3 != 0:
                if int(r.hget(call.from_user.id, 'money')) >= 50:
                    r.hincrby(call.from_user.id, 'money', -50)
                    if q1 < 0 or q2 < 0 or q3 < 0:
                        jew = True
                    else:
                        jew = False
                    re_roll(call.from_user.id, q1, q2, q3, jew)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='У вас тепер нові квести')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Всі квести вже виконані')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Прострочені квести, візьми нові')

    elif call.data.startswith('20_vodka'):
        if int(r.hget(call.from_user.id, 'money')) >= 50:
            r.hincrby(call.from_user.id, 'money', -50)
            quest(call.from_user.id, 1, 2)
            quest(call.from_user.id, 3, -1, 1)
            if int(r.hget(call.from_user.id, 'spirit')) == 10000:
                quest(call.from_user.id, 3, 3, 2)
            vo = 0
            for v in range(20):
                vo += int(vodka(call.from_user.id))
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text=f'Ви успішно купили ящик горілки "Козаки"\n\U0001F54A +{vo}')
        else:
            cl = int(r.hget(call.from_user.id, 'class'))
            if cl == 17 or cl == 27:
                if int(r.hget(call.from_user.id, 'wins')) >= 50:
                    r.hincrby(call.from_user.id, 'wins', -50)
                    vo = 0
                    for v in range(20):
                        vo += int(vodka(call.from_user.id))
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text=f'Ви успішно купили ящик горілки "Козаки" за перемоги'
                                                         f'\n\U0001F54A +{vo}')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку')

    elif call.data.startswith('5_vodka'):
        if int(r.hget(call.from_user.id, 'money')) >= 12:
            r.hincrby(call.from_user.id, 'money', -12)
            quest(call.from_user.id, 1, 2)
            if int(r.hget(call.from_user.id, 'spirit')) == 10000:
                quest(call.from_user.id, 3, 3, 2)
            vo = 0
            for v in range(5):
                vo += int(vodka(call.from_user.id))
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text=f'Ви успішно купили упаковку горілки "Козаки"\n\U0001F54A +{vo}')
        else:
            cl = int(r.hget(call.from_user.id, 'class'))
            if cl == 17 or cl == 27:
                if int(r.hget(call.from_user.id, 'wins')) >= 12:
                    r.hincrby(call.from_user.id, 'wins', -12)
                    vo = 0
                    for v in range(5):
                        vo += int(vodka(call.from_user.id))
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text=f'Ви успішно купили упаковку горілки "Козаки" за перемоги'
                                                         f'\n\U0001F54A +{vo}')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо коштів на рахунку')

    elif call.data.startswith('vodka'):
        if int(r.hget(call.from_user.id, 'money')) >= 2:
            r.hincrby(call.from_user.id, 'money', -2)
            quest(call.from_user.id, 1, 2)
            if int(r.hget(call.from_user.id, 'spirit')) == 10000:
                quest(call.from_user.id, 3, 3, 2)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно купили горілку "Козаки"\n\U0001F54A +' +
                                                 vodka(call.from_user.id))
        else:
            cl = int(r.hget(call.from_user.id, 'class'))
            if cl == 17 or cl == 27:
                if int(r.hget(call.from_user.id, 'wins')) >= 2:
                    r.hincrby(call.from_user.id, 'wins', -2)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили горілку "Козаки" за перемоги'
                                                         '\n\U0001F54A +' + vodka(call.from_user.id))
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
        if int(r.hget(call.from_user.id, 'money')) >= 5:
            r.hincrby(call.from_user.id, 'money', -5)
            if int(r.hget(call.from_user.id, 'support')) == 0:
                hp(5, call.from_user.id)
                r.hset(call.from_user.id, 'support', 1)
                r.hset(call.from_user.id, 's_support', 10)
            else:
                hp(50, call.from_user.id)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно купили аптечку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо коштів на рахунку')

    elif call.data.startswith('passport'):
        if int(r.hget(call.from_user.id, 'money')) >= 10 and r.hexists(call.from_user.id, 'name'):
            current_name = int(r.hget(call.from_user.id, 'name'))
            ran = choice(list(names))
            while ran == current_name:
                ran = choice(list(names))
            r.hincrby(call.from_user.id, 'money', -10)
            r.hset(call.from_user.id, 'name', ran)
            if r.hexists(call.from_user.id, 'ac3') == 0:
                r.hset(call.from_user.id, 'ac3', 1)
            name = names[ran]
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text=f'Ви успішно купили трофейний паспорт\nНове ім`я - {name}')
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
                quest(call.from_user.id, 3, 1, 3)
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
            quest(call.from_user.id, 1, -4)
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
            if int(r.hget(call.from_user.id, 'weapon')) == 0:
                if int(r.hget(call.from_user.id, 'money')) >= 150:
                    r.hincrby(call.from_user.id, 'money', -150)
                    r.hset(call.from_user.id, 'weapon', 3)
                    r.hset(call.from_user.id, 's_weapon', 5)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили батіг')
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

    elif call.data.startswith('helmet'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            if int(r.hget(call.from_user.id, 'head')) == 0:
                if int(r.hget(call.from_user.id, 'money')) >= 70:
                    r.hincrby(call.from_user.id, 'money', -70)
                    r.hset(call.from_user.id, 'head', 2)
                    r.hset(call.from_user.id, 's_head', 40)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили тактичний шолом')
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
                    quest(call.from_user.id, 3, 2, 1)
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

    elif call.data.startswith('merchant_backpack'):
        if int(r.hget('soledar', 'merchant_hour_now')) == datetime.now().hour or \
                int(r.hget('soledar', 'merchant_hour_now')) + 1 == datetime.now().hour:
            slot = int(r.hget('soledar', 'merchant_slot'))
            strap = int(r.hget('soledar', 'merchant_strap'))
            tape = int(r.hget('soledar', 'merchant_tape'))
            extra = r.hget(call.from_user.id, 'extra_slot')
            if slot == 2:
                tape *= 2
            elif slot == 3:
                tape *= 4
            if extra:
                extra = int(extra)
            else:
                extra = 0
            if slot == extra + 1:
                if int(r.hget(call.from_user.id, 'strap')) >= strap and int(r.hget(call.from_user.id, 'tape')) >= tape:
                    r.hincrby(call.from_user.id, 'strap', -strap)
                    r.hincrby(call.from_user.id, 'tape', -tape)
                    r.hset(call.from_user.id, 'extra_slot', slot)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили тактичний рюкзак')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо коштів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас має бути рюкзак, який менший на один слот')
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
                                                        text='Ви успішно купили солярку')
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
            quest(call.from_user.id, 3, -2, 4)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно замовили 40 донбаських пакунків')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо погонів на рахунку')

    elif call.data.startswith('jew'):
        uid = call.from_user.id
        inv = r.hmget(uid, 'weapon', 'defense', 'support', 'head', 's_weapon', 's_defense', 's_support', 's_head')
        w, d, s, h = int(inv[0]), int(inv[1]), int(inv[2]), int(inv[3])
        s_w, s_d, s_s, s_h = int(inv[4]), int(inv[5]), int(inv[6]), int(inv[7])
        goy = 0
        if check_set(w, d, s, h) == 4:
            goy = 1
        if h == 0:
            if int(r.hget(uid, 'strap')) >= 1:
                r.hincrby(uid, 'strap', -1)
                r.hset(uid, 'head', 6)
                r.hset(uid, 's_head', 7)
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви успішно купили ярмулку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Недостатньо погонів на рахунку')
        elif goy:
            if s_w < 30 or s_d < 30 or s_s < 30 or s_h < 30:
                if int(r.hget(uid, 'strap')) >= 1:
                    r.hincrby(uid, 'strap', -1)
                    if s_w < 30:
                        r.hincrby(uid, 's_weapon', 7)
                    if s_d < 30:
                        r.hincrby(uid, 's_defense', 7)
                    if s_s < 30:
                        r.hincrby(uid, 's_support', 7)
                    if s_h < 30:
                        r.hincrby(uid, 's_head', 7)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно збільшили міцність свого гойського комплекту')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо погонів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Все ваше спорядження має більше 30 міцності')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='У вас вже є шапка')

    elif call.data.startswith('buy_resources'):
        if checkClan(call.from_user.id):
            if int(r.hget(call.from_user.id, 'strap')) >= 2:
                r.hincrby(call.from_user.id, 'strap', -2)
                c = 'c' + r.hget(call.from_user.id, 'clan').decode()
                r.hincrby(c, 'r_spirit', 33)
                wood(c, 2222)
                stone(c, 1111)
                if int(r.hget(c, 'buff_5')) > 1:
                    q_points(call.from_user.id, 40)
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

    elif call.data.startswith('premium4'):
        if int(r.hget(call.from_user.id, 'strap')) >= 1 and int(r.hget(call.from_user.id, 'class')) > 0:
            r.hincrby(call.from_user.id, 'strap', -1)
            cl = int(r.hget(call.from_user.id, 'class'))
            if cl == 1 or cl == 11 or cl == 21:
                r.hset(call.from_user.id, 'photo', premium3[0])
            elif cl == 2 or cl == 12 or cl == 22:
                r.hset(call.from_user.id, 'photo', premium3[1])
            elif cl == 3 or cl == 13 or cl == 23:
                r.hset(call.from_user.id, 'photo', premium3[2])
            elif cl == 4 or cl == 14 or cl == 24:
                r.hset(call.from_user.id, 'photo', premium3[3])
            elif cl == 5 or cl == 15 or cl == 25:
                r.hset(call.from_user.id, 'photo', premium3[4])
            elif cl == 6 or cl == 16 or cl == 26:
                r.hset(call.from_user.id, 'photo', premium3[5])
            elif cl == 7 or cl == 17 or cl == 27:
                r.hset(call.from_user.id, 'photo', premium3[6])
            elif cl == 8 or cl == 18 or cl == 28:
                r.hset(call.from_user.id, 'photo', premium3[7])
            elif cl == 9 or cl == 19 or cl == 29:
                r.hset(call.from_user.id, 'photo', premium3[8])
            elif cl == 10 or cl == 20 or cl == 30:
                r.hset(call.from_user.id, 'photo', premium3[9])
            elif cl == 31 or cl == 32 or cl == 33:
                r.hset(call.from_user.id, 'photo', premium3[10])
            elif cl == 34 or cl == 35 or cl == 36:
                r.hset(call.from_user.id, 'photo', premium3[11])
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

    elif call.data.startswith('prigozhin'):
        if int(r.hget(call.from_user.id, 'strap')) >= 1:
            r.hincrby(call.from_user.id, 'strap', -1)
            r.hset(call.from_user.id, 'photo', 'https://i.ibb.co/dMY198z/prig.jpg')
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно змінили фото русаку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо погонів на рахунку')

    elif call.data.startswith('copium'):
        if int(r.hget(call.from_user.id, 'strap')) >= 1 and r.hexists(call.from_user.id, 'name') == 1:
            r.hincrby(call.from_user.id, 'strap', -1)
            r.hset(call.from_user.id, 'mushrooms', 0)
            hp(100, call.from_user.id)
            if int(r.hget(call.from_user.id, 'injure')) < 300:
                r.hset(call.from_user.id, 'injure', 0)
            else:
                r.hincrby(call.from_user.id, 'injure', -300)

            if int(r.hget(call.from_user.id, 'sch')) < 300:
                r.hset(call.from_user.id, 'sch', 0)
            else:
                r.hincrby(call.from_user.id, 'sch', -300)

            if int(r.hget(call.from_user.id, 'strength')) < 5000:
                r.hset(call.from_user.id, 'time', 0)

            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно купили копіум')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо погонів на рахунку')

    elif call.data.startswith('hawthorn'):
        if int(r.hget(call.from_user.id, 'strength')) < 1000 and int(r.hget(call.from_user.id, 'intellect')) < 5:
            if int(r.hget(call.from_user.id, 'strap')) >= 1 and r.hexists(call.from_user.id, 'name') == 1:
                r.hincrby(call.from_user.id, 'strap', -1)
                r.hincrby(call.from_user.id, 'strength', 1000)
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
        if int(r.hget(call.from_user.id, 'strap')) >= 3 and cl > 0:
            r.hincrby(call.from_user.id, 'strap', -3)
            if cl == 21:
                r.hincrby(call.from_user.id, 'strength', -200)
            if cl in (6, 16, 26):
                r.hset(call.from_user.id, 'weapon', 0)
            r.srem('class-' + str(cl), call.from_user.id)
            r.hset(call.from_user.id, 'class', 0)
            if int(r.hget(call.from_user.id, 'intellect')) < 5:
                r.hset(call.from_user.id, 'intellect', 5)
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Ви успішно купили курс перекваліфікації русаку')
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо погонів на рахунку, або русак без класу')

    elif call.data.startswith('fast_cellar'):
        if int(r.hget(call.from_user.id, 's3')) <= 2:
            if int(r.hget(call.from_user.id, 'strap')) >= 3:
                r.hincrby(call.from_user.id, 'strap', -3)
                r.hset(call.from_user.id, 's3', 5)
                r.hset(call.from_user.id, 'name2', choice(list(names)),
                       {'strength2': randint(100, 150),
                        'intellect2': choices([1, 2], weights=[4, 1])[0],
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

    elif call.data.startswith('expand_backpack'):
        uid = call.from_user.id

        if not r.hexists(uid, 'backpack_1'):
            r.hset(uid, 'backpack_1', 0, {'backpack_1_s': 0, 'backpack_1_type': 'empty', 'extra_slot': 0,
                                          'backpack_2': 0, 'backpack_2_s': 0, 'backpack_2_type': 'empty'})

        if call.data.startswith('expand_backpack1'):
            if int(r.hget(uid, 'extra_slot')) == 0:
                if int(r.hget(uid, 'strap')) >= 5:
                    r.hincrby(uid, 'strap', -5)
                    r.hset(uid, 'extra_slot', 1)
                    r.sadd('backpackers', uid)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили тактичний рюкзак з другим слотом!')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо погонів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас вже є тактичний рюкзак з другим слотом')
        elif call.data.startswith('expand_backpack2'):
            if int(r.hget(uid, 'extra_slot')) == 1:
                if int(r.hget(uid, 'strap')) >= 10:
                    r.hincrby(uid, 'strap', -10)
                    r.hset(uid, 'extra_slot', 2)
                    r.sadd('backpackers', uid)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили тактичний рюкзак з третім слотом!')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо погонів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас вже є тактичний рюкзак з третім слотом')
        elif call.data.startswith('expand_backpack3'):
            if int(r.hget(uid, 'extra_slot')) == 2:
                if int(r.hget(uid, 'strap')) >= 20:
                    r.hincrby(uid, 'strap', -20)
                    r.hset(uid, 'extra_slot', 3)
                    r.sadd('backpackers', uid)
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви успішно купили тактичний рюкзак з четвертим слотом!')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Недостатньо погонів на рахунку')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='У вас вже є тактичний рюкзак з четвертим слотом')

    elif call.data.startswith('zero_time') and call.from_user.id == call.message.reply_to_message.from_user.id:
        if int(r.hget(call.from_user.id, 'strap')) >= 1:
            r.hincrby(call.from_user.id, 'strap', -1)
            r.hset(call.from_user.id, 'clan_ts', 0)
            await bot.edit_message_text('\u23F1 Час очікування онулений.',
                                        call.message.chat.id, call.message.message_id, reply_markup=None)
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо погонів на рахунку')

    elif call.data.startswith('drop_') and call.from_user.id == call.message.reply_to_message.from_user.id:
        msg, markup, edit, answer = drop_item(call.data, call.from_user.id)

        if edit:
            await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
        if answer:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=answer)

    elif call.data.startswith('backpack_') and call.from_user.id == call.message.reply_to_message.from_user.id:
        if call.data.startswith('backpack_empty'):
            msg, markup, edit, answer = empty_backpack(call.data, call.from_user.id)
        else:
            msg, markup, edit, answer = change_item(call.data, call.from_user.id)

        if edit:
            await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
        if answer:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=answer)

    elif call.data.startswith('tape') and call.from_user.id == call.message.reply_to_message.from_user.id:
        msg, markup, edit, answer = upgrade_item(call.data, call.from_user.id)

        if edit:
            await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
        if answer:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=answer)

    elif call.data.startswith('buy_pack') and call.from_user.id == call.message.reply_to_message.from_user.id:
        n = int(call.data.split('_')[2])
        if int(r.hget(call.from_user.id, 'money')) >= n * 20 and 0 < n < 2000:
            r.hincrby(call.from_user.id, 'money', -(n * 20))
            r.hincrby(call.from_user.id, 'packs', n)
            if n >= 10:
                quest(call.from_user.id, 3, -2, 4)
            await bot.edit_message_text('\U0001F4E6 Пакунки придбано.',
                                        call.message.chat.id, call.message.message_id, reply_markup=None)
        else:
            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                            text='Недостатньо коштів на рахунку')

    elif call.data.startswith('pack_'):
        try:
            if r.hexists('pack_ts', call.from_user.id) == 0:
                r.hset('pack_ts', call.from_user.id, 0)
            timestamp = int(datetime.now().timestamp())
            if not call.data.startswith('pack_unpack') and timestamp - int(r.hget('pack_ts', call.from_user.id)) < 2:
                pass
            else:
                r.hset('pack_ts', call.from_user.id, timestamp)
                if call.data.startswith('pack_unpack'):
                    msg = open_pack2(call.from_user.id, call.data, call.message.text, 1)
                    if msg:
                        await bot.edit_message_text(msg[0], call.message.chat.id, call.message.message_id,
                                                    reply_markup=msg[1])
                elif call.from_user.id == int(call.data.split('_')[2]):
                    if check_slot(call.from_user.id, call.data):
                        msg = call.message.text

                        markup = call.message.reply_markup
                        markup2 = InlineKeyboardMarkup()
                        for i in markup.inline_keyboard:
                            if i[0]['callback_data'] != call.data:
                                markup2.add(i[0])

                        if msg.endswith('#loot') and len(markup2.inline_keyboard) == 0:
                            msg = msg[:-5]
                        await bot.edit_message_text(msg, call.message.chat.id,
                                                    call.message.message_id, reply_markup=markup2)
                        open_pack2(call.from_user.id, call.data, call.message.text, 1)
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Неможливо взяти спорядження, '
                                                             'оскільки у вас вже є одне такого типу')
        except:
            pass

    elif call.data.startswith('gift_'):
        try:
            if r.hexists('pack_ts', call.from_user.id) == 0:
                r.hset('pack_ts', call.from_user.id, 0)
            timestamp = int(datetime.now().timestamp())
            if not call.data.startswith('gift_unpack') and timestamp - int(r.hget('pack_ts', call.from_user.id)) < 2:
                pass
            else:
                r.hset('pack_ts', call.from_user.id, timestamp)
                if call.data.startswith('gift_unpack'):
                    msg = open_gift3(call.from_user.id, call.data, call.message.text, call.message.chat.id)
                    if msg:
                        await bot.edit_message_text(msg[0], call.message.chat.id, call.message.message_id,
                                                    reply_markup=msg[1])
                elif call.from_user.id == int(call.data.split('_')[2]):
                    await bot.edit_message_text(call.message.text, call.message.chat.id,
                                                call.message.message_id, reply_markup=None)
                    open_gift3(call.from_user.id, call.data, call.message.text, call.message.chat.id)
        except:
            pass

    elif call.data.startswith('switch1'):
        msg, markup = shop_msg(call.from_user.id, 1)
        await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data.startswith('switch2'):
        msg, markup = shop_msg(call.from_user.id, 2)
        await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data.startswith('switch3'):
        msg, markup = shop_msg(call.from_user.id, 3)
        await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data.startswith('salt_'):
        msg = salt_shop(call.from_user.id, call.data)
        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=msg)
        if msg.startswith('Передозування'):
            s4 = int(r.hget(call.from_user.id, 's4'))
            ran1, ran2, tr = randint(50, 100), randint(50, 100), ''
            if s4 >= 4:
                ran1, ran2 = int(ran1 / 2), int(ran2 / 2)
            r.hincrby(call.from_user.id, 'injure', ran1)
            r.hincrby(call.from_user.id, 'sch', ran2)
            if s4 >= 3:
                increase_trance(20, call.from_user.id)
                tr = ' \U0001F44A +20'
            await bot.send_message(call.message.chat.id, f'Передозування!\n\U0001fa78 +{ran1} \U0001F464 +{ran2}{tr}')
        elif msg.startswith('Ви успішно купили ресурси для клану'):
            try:
                msg = 'Ваше замовлення прибуло.\n\U0001F4FB 22 \U0001F9F1 55 \U0001F9F6 111'
                await bot.send_message(int(r.hget(call.from_user.id, 'clan')), msg)
            except:
                pass
    elif call.data.startswith('clan_'):
        if call.data.startswith('clan_side'):
            c = 'c' + str(call.message.chat.id)
            if int(r.hget(c, 'side')) == 0:
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
                            await bot.send_message(call.message.chat.id, '\U0001F3D7 Покращено Угруповання до '
                                                                         'Комуни.')
                        elif call.data.startswith('clan_side_2'):
                            r.hset(c, 'base', 6)
                            r.hset(c, 'side', 2)
                            await bot.send_message(call.message.chat.id, '\U0001F3D7 Покращено Угруповання до '
                                                                         'Коаліції.')
                        elif call.data.startswith('clan_side_3'):
                            r.hset(c, 'base', 7)
                            r.hset(c, 'side', 3)
                            await bot.send_message(call.message.chat.id, '\U0001F3D7 Покращено Угруповання до '
                                                                         'Асоціації.')
                        elif call.data.startswith('clan_side_4'):
                            r.hset(c, 'base', 8)
                            r.hset(c, 'side', 4)
                            await bot.send_message(call.message.chat.id, '\U0001F3D7 Покращено Угруповання до '
                                                                         'Організації.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо ресурсів.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Це має зробити лідер.')
        elif call.data.startswith('clan_raid_loot'):
            c = 'c' + str(call.message.chat.id)
            cid = call.message.chat.id
            uid = call.from_user.id
            uid_enc = str(uid).encode()
            ts = int(datetime.now().timestamp())
            rl = r.hmget(c, 'raid_loot', 'raid_loot_n', 'raid_loot_mid', 'raid_loot_c', 'raid_loot_ts')
            data = rl[0].decode()
            item = int(rl[1])
            mid = int(rl[2])
            item_count = int(rl[3])
            ts2 = int(rl[4])
            items = ()
            markup = InlineKeyboardMarkup()
            if uid_enc in r.smembers(f'cl{cid}'):
                if uid_enc not in r.smembers(f'raid_loot{cid}'):
                    if item_count > 0 and call.message.message_id == mid:
                        if ts - ts2 > 300 or uid_enc in r.smembers(f'raiders{cid}'):
                            lt = -1
                            if int(r.hget(uid, 'weapon')) == 35 and int(r.hget(uid, 'class')) in (3, 13, 23):
                                il = int(r.hget(uid, 'intellect'))
                                damage_weapon(uid, 0)
                                if choices([1, 0], weights=[il, 100 - il])[0]:
                                    lt = 1
                            if data == 'food':
                                n = r.hincrby(c, 'raid_loot_c', lt)
                                r.sadd(f'raid_loot{cid}', uid)
                                r.hset(uid, 'time', 0)
                                if n > 0:
                                    markup.add(InlineKeyboardButton(text=f'Взяти лут. Залишилось {n}',
                                                                    callback_data='clan_raid_loot'))
                                await bot.edit_message_text(call.message.text, call.message.chat.id,
                                                            call.message.message_id, reply_markup=markup)

                            elif data == 'tape':
                                n = r.hincrby(c, 'raid_loot_c', lt)
                                r.sadd(f'raid_loot{cid}', uid)
                                r.hincrby(uid, 'tape', r.hget(c, 'raid_loot_s'))
                                if n > 0:
                                    markup.add(InlineKeyboardButton(text=f'Взяти лут. Залишилось {n}',
                                                                    callback_data='clan_raid_loot'))
                                await bot.edit_message_text(call.message.text, call.message.chat.id,
                                                            call.message.message_id, reply_markup=markup)

                            elif data == 'convoy':
                                if not r.hexists(uid, 'convoy_time'):
                                    r.hset(uid, 'convoy_time', datetime.now().day, {'convoy_c': 0})
                                if int(r.hget(uid, 'convoy_time')) != datetime.now().day:
                                    r.hset(uid, 'convoy_time', datetime.now().day, {'convoy_c': 0})
                                if int(r.hget(c, 'side')) == 3:
                                    tier = int(r.hget(c, 'tier'))
                                    if tier == 2:
                                        limit = 4
                                    elif tier == 1:
                                        limit = 5
                                    else:
                                        limit = 3
                                else:
                                    limit = 2
                                if int(r.hget(uid, 'convoy_c')) < limit:
                                    n = r.hincrby(c, 'raid_loot_c', lt)
                                    r.sadd(f'raid_loot{cid}', uid)
                                    r.hincrby(uid, 'convoy_c', 1)
                                    packs = int(r.hget(c, 'raid_loot_s'))
                                    r.hincrby(uid, 'packs', packs)
                                    if packs >= 10:
                                        quest(uid, 3, -2, 4)
                                    if n > 0:
                                        markup.add(InlineKeyboardButton(text=f'Взяти лут. Залишилось {n}',
                                                                        callback_data='clan_raid_loot'))
                                    await bot.edit_message_text(call.message.text, call.message.chat.id,
                                                                call.message.message_id, reply_markup=markup)
                                else:
                                    msg = f'Ви вже сьогодні достатньо взяли луту з конвоїв, залиште іншим!\n' \
                                          f'{limit}/{limit}'
                                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                    text=msg)

                            else:
                                if data == 'support':
                                    if item == 7:
                                        items = (7, 12)
                                    elif item == 8:
                                        items = (8, 13)
                                    elif item == 1:
                                        items = (1, 15)

                                if int(r.hget(uid, data)) == item or int(r.hget(uid, data)) in items:
                                    n = r.hincrby(c, 'raid_loot_c', lt)
                                    r.sadd(f'raid_loot{cid}', uid)
                                    r.hincrby(uid, f's_{data}', r.hget(c, 'raid_loot_s'))
                                    if n > 0:
                                        markup.add(InlineKeyboardButton(text=f'Взяти лут. Залишилось {n}',
                                                                        callback_data='clan_raid_loot'))
                                    await bot.edit_message_text(call.message.text, call.message.chat.id,
                                                                call.message.message_id, reply_markup=markup)
                                elif int(r.hget(uid, data)) == 0:
                                    n = r.hincrby(c, 'raid_loot_c', lt)
                                    r.sadd(f'raid_loot{cid}', uid)
                                    r.hset(uid, data, r.hget(c, 'raid_loot_n'),
                                           {f's_{data}': r.hget(c, 'raid_loot_s')})
                                    if n > 0:
                                        markup.add(InlineKeyboardButton(text=f'Взяти лут. Залишилось {n}',
                                                                        callback_data='clan_raid_loot'))
                                    await bot.edit_message_text(call.message.text, call.message.chat.id,
                                                                call.message.message_id, reply_markup=markup)
                                else:
                                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                    text='У вас вже є спорядження такого типу.')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='У рейдерів є 5 хвилин на те, щоб забрати лут.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Лут закінчився.')
                else:
                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                    text='Ви вже забрали свою частину.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Ви не з цього клану.')
        else:
            cid = call.data.split('_')[-1]
            if str(call.from_user.id).encode() in r.smembers('cl' + cid):
                if call.data.startswith('clan_shop_1'):
                    msg, markup = c_shop('c' + cid, 1)
                    await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
                elif call.data.startswith('clan_shop_2'):
                    msg, markup = c_shop('c' + cid, 2)
                    await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
                elif call.data.startswith('clan_shop_3'):
                    msg, markup = c_shop('c' + cid, 3)
                    await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)
                elif call.data.startswith('clan_shop_4'):
                    msg, markup = c_shop('c' + cid, 4)
                    await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)

                elif call.data.startswith('clan_fragment'):
                    if int(r.hget(call.from_user.id, 'money')) >= 15:
                        quest(call.from_user.id, 3, 3, 1)
                        if int(r.hget(call.from_user.id, 'defense')) == 0 or \
                                int(r.hget(call.from_user.id, 'defense')) == 1:
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

                elif call.data.startswith('clan_helmet'):
                    if int(r.hget(call.from_user.id, 'money')) >= 40:
                        if int(r.hget(call.from_user.id, 'head')) == 0:
                            r.hset(call.from_user.id, 'head', 2)
                            r.hset(call.from_user.id, 's_head', 40)
                            r.hincrby(call.from_user.id, 'money', -40)
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Ви успішно купили тактичний шолом')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='У вас вже є шапка.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку.')

                elif call.data.startswith('clan_bombs'):
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

                elif call.data.startswith('clan_lash'):
                    if int(r.hget(call.from_user.id, 'money')) >= 25:
                        if int(r.hget(call.from_user.id, 'weapon')) == 0:
                            r.hset(call.from_user.id, 'weapon', 3)
                            r.hset(call.from_user.id, 's_weapon', 3)
                            r.hincrby(call.from_user.id, 'money', -25)
                            quest(call.from_user.id, 3, 1, 3)
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Ви успішно купили батіг')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='У вас вже є зброя.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку.')

                elif call.data.startswith('clan_mushroom'):
                    if int(r.hget(call.from_user.id, 'money')) >= 100:
                        mushroom = int(r.hget(call.from_user.id, 'mushrooms'))
                        if int(r.hget(call.from_user.id, 'class')) in (18, 28):
                            mushroom = 0
                        if mushroom < 3:
                            if int(r.hget(call.from_user.id, 'support')) == 0:
                                if int(r.hget(call.from_user.id, 'intellect')) < 20:
                                    r.hset(call.from_user.id, 'support', 6)
                                    r.hset(call.from_user.id, 's_support', 1)
                                    r.hincrby(call.from_user.id, 'money', -100)
                                    quest(call.from_user.id, 3, 3, 4)
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
                                                            text='Для вашого русака не передбачено більше трьох мухоморів')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку.')

                elif call.data.startswith('clan_ear'):
                    if int(r.hget(call.from_user.id, 'money')) >= 20:
                        if int(r.hget(call.from_user.id, 'head')) == 0:
                            r.hset(call.from_user.id, 'head', 4)
                            r.hset(call.from_user.id, 's_head', 20)
                            r.hincrby(call.from_user.id, 'money', -20)
                            quest(call.from_user.id, 3, 2, 1)
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Ви успішно купили вушанку.')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='У вас вже є шапка.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку.')

                elif call.data.startswith('clan_sugar'):
                    if int(r.hget(call.from_user.id, 'money')) >= 55:
                        if int(r.hget(call.from_user.id, 'support')) == 0:
                            r.hset(call.from_user.id, 'support', 7)
                            s = 1
                            if int(r.hget(f'c{cid}', 'money')) >= 1000000:
                                s = 2
                            r.hset(call.from_user.id, 's_support', s)
                            r.hincrby(call.from_user.id, 'money', -55)
                            quest(call.from_user.id, 3, 3, 4)
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Ви успішно купили цукор.')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='У вас вже є допоміжне спорядження.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку.')

                elif call.data.startswith('clan_kvs'):
                    if int(r.hget(call.from_user.id, 'money')) >= 15:
                        if int(r.hget(call.from_user.id, 'support')) == 0:
                            r.hset(call.from_user.id, 'support', 8)
                            s = 5
                            if int(r.hget(f'c{cid}', 'money')) >= 1000000:
                                s = 10
                            r.hset(call.from_user.id, 's_support', 10)
                            r.hincrby(call.from_user.id, 'money', -15)
                            quest(call.from_user.id, 3, 3, 4)
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Ви успішно купили квас.')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='У вас вже є допоміжне спорядження.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку.')

                elif call.data.startswith('clan_foil'):
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

                elif call.data.startswith('clan_children'):
                    if int(r.hget(call.from_user.id, 'money')) >= 100:
                        r.hincrby(call.from_user.id, 'money', -100)
                        r.hincrby(call.from_user.id, 'childs', 1)
                        r.hincrby('all_children', 'children', 1)
                        quest(call.from_user.id, 3, 3, 4)
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Ви успішно купили російське немовля.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо коштів на рахунку.')

                elif call.data.startswith('clan_uav'):
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

                elif call.data.startswith('clan_ration'):
                    price = 4 if int(r.hget('c' + cid, 'side')) == 1 else 10
                    if int(r.hget(call.from_user.id, 'money')) >= price:
                        r.hincrby(call.from_user.id, 'money', -price)
                        ran = randint(1, 3)
                        quest(call.from_user.id, 2, -1)
                        quest(call.from_user.id, 3, 3, 4)
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

                elif call.data.startswith('clan_monument'):
                    c = 'c' + cid
                    if checkLeader(call.from_user.id, cid):
                        if int(r.hget(c, 'r_spirit')) >= 10:
                            r.hincrby(c, 'r_spirit', -10)
                            s = 1 if int(r.hget(c, 'side')) == 2 else 0
                            for mem in r.smembers('cl' + cid):
                                try:
                                    quest(mem, 2, -2)
                                    increase_trance(5, mem)
                                except:
                                    pass
                                if s == 1:
                                    spirit(int(int(r.hget(mem, 'spirit')) * 0.5), mem, 0)
                            await bot.send_message(cid, '\U0001F44A Клан готовий йти в бій.')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Недостатньо ресурсів.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Це може зробити тільки лідер чи заступник.')

                elif call.data.startswith('clan_spike'):
                    c = 'c' + cid
                    if checkLeader(call.from_user.id, cid):
                        if int(r.hget(c, 'wood')) >= 200 and int(r.hget(c, 'stone')) >= 100 \
                                and int(r.hget(c, 'cloth')) >= 50:
                            r.hincrby(c, 'wood', -200)
                            r.hincrby(c, 'stone', -100)
                            r.hincrby(c, 'cloth', -50)
                            for mem in r.smembers('cl' + cid):
                                try:
                                    stats = r.hmget(mem, 'weapon', 's_weapon', 'defense', 's_defense')
                                    if int(stats[0]) in (0, 7, 16):
                                        if int(stats[0]) == 7:
                                            if int(stats[1]) < 10:
                                                r.hset(mem, 's_weapon', 10)
                                        else:
                                            r.hset(mem, 'weapon', 7, {'s_weapon': 10})
                                    if int(stats[2]) in (0, 4):
                                        if int(stats[2]) == 4:
                                            if int(stats[3]) < 10:
                                                r.hset(mem, 's_defense', 10)
                                        else:
                                            r.hset(mem, 'defense', 4, {'s_defense': 10})
                                except:
                                    pass
                            await bot.send_message(cid, '\U0001F5E1 Клан готовий йти в бій.')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Недостатньо ресурсів.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Це може зробити тільки лідер чи заступник.')

                elif call.data.startswith('clan_vodka'):
                    c = 'c' + cid
                    if checkLeader(call.from_user.id, cid):
                        if int(r.hget(c, 'money')) >= 300:
                            r.hincrby(c, 'money', -300)
                            for mem in r.smembers('cl' + cid):
                                try:
                                    if int(r.hget(mem, 'clan_time')) == datetime.now().day:
                                        r.hincrby(mem, 'vodka', 9)
                                        r.hincrby('all_vodka', 'vodka', 9)
                                        spirit(int(vodka(mem)) * 9, mem, 0)
                                        if int(r.hget(mem, 'support')) == 0:
                                            r.hset(mem, 'support', 13)
                                            r.hset(mem, 's_support', randint(1, 5))
                                except:
                                    pass
                            await bot.send_message(cid, '\u2622 Клан святкує відпрацьовану зміну.')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Недостатньо ресурсів.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Це може зробити тільки лідер чи заступник.')

                elif call.data.startswith('clan_rpg'):
                    c = 'c' + cid
                    if int(r.hget(c, 'money')) >= 500 and int(r.hget(c, 'r_spirit')) >= 100:
                        if checkLeader(call.from_user.id, cid):
                            if not call.data.startswith('clan_rpg-'):
                                uid = call.from_user.id
                                if call.data.startswith('clan_rpg+'):
                                    uid = call.data.split('_')[1].split('+')[1]
                                if str(uid).encode() in r.smembers('cl' + cid):
                                    if int(r.hget(uid, 'weapon')) in (0, 16):
                                        r.hset(uid, 'weapon', 2)
                                        r.hset(uid, 's_weapon', 1)
                                        r.hincrby(c, 'money', -500)
                                        r.hincrby(c, 'r_spirit', -100)
                                        if call.data.startswith('clan_rpg+'):
                                            msg = call.message.text + '\n\n✅'
                                            await bot.edit_message_text(text=msg, chat_id=call.message.chat.id,
                                                                        message_id=call.message.message_id,
                                                                        reply_markup=None)
                                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                        text='Ви успішно купили РПГ-7.')
                                    else:
                                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                        text='У вас вже є зброя.')
                                else:
                                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                    text='Схоже, цей учасник не в клані.')
                            else:
                                msg = call.message.text + '\n\n❌'
                                await bot.edit_message_text(text=msg, chat_id=call.message.chat.id,
                                                            message_id=call.message.message_id, reply_markup=None)
                        elif not call.data.startswith('clan_rpg-') and not call.data.startswith('clan_rpg+'):
                            markup = InlineKeyboardMarkup()
                            markup.add(InlineKeyboardButton(text='РПГ-7 - \U0001F47E 100, \U0001F4B5 500',
                                                            callback_data=f'clan_rpg+{call.from_user.id}_{c[1:]}'))
                            markup.add(InlineKeyboardButton(text='❌', callback_data=f'clan_rpg-_{c[1:]}'))
                            msg = f'\U0001f7e1 {call.from_user.first_name} хоче купити РПГ-7.'
                            await bot.send_message(cid, msg, reply_markup=markup)
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Це може зробити тільки лідер чи заступник.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо ресурсів.')

                elif call.data.startswith('clan_armor'):
                    c = 'c' + cid
                    if int(r.hget(c, 'money')) >= 500 and int(r.hget(c, 'r_spirit')) >= 50:
                        if checkLeader(call.from_user.id, cid):
                            if not call.data.startswith('clan_armor-'):
                                uid = call.from_user.id
                                if call.data.startswith('clan_armor+'):
                                    uid = call.data.split('_')[1].split('+')[1]
                                if str(uid).encode() in r.smembers('cl' + cid):
                                    if int(r.hget(uid, 'defense')) == 0:
                                        r.hset(uid, 'defense', 2)
                                        r.hset(uid, 's_defense', 50)
                                        r.hincrby(c, 'money', -500)
                                        r.hincrby(c, 'r_spirit', -50)
                                        if call.data.startswith('clan_armor+'):
                                            msg = call.message.text + '\n\n✅'
                                            await bot.edit_message_text(text=msg, chat_id=call.message.chat.id,
                                                                        message_id=call.message.message_id,
                                                                        reply_markup=None)
                                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                        text='Ви успішно купили бронежилет вагнерівця.')
                                    else:
                                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                        text='У вас вже є захисне спорядження.')
                                else:
                                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                    text='Схоже, цей учасник не в клані.')
                            else:
                                msg = call.message.text + '\n\n❌'
                                await bot.edit_message_text(text=msg, chat_id=call.message.chat.id,
                                                            message_id=call.message.message_id, reply_markup=None)
                        elif not call.data.startswith('clan_armor-') and not call.data.startswith('clan_armor+'):
                            markup = InlineKeyboardMarkup()
                            markup.add(InlineKeyboardButton(text='Бронежилет - \U0001F47E 50, \U0001F4B5 500',
                                                            callback_data=f'clan_armor+{call.from_user.id}_{c[1:]}'))
                            markup.add(InlineKeyboardButton(text='❌', callback_data=f'clan_armor-_{c[1:]}'))
                            msg = f'\U0001f7e1 {call.from_user.first_name} хоче купити Бронежилет вагнерівця.'
                            await bot.send_message(cid, msg, reply_markup=markup)
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Це може зробити тільки лідер чи заступник.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Недостатньо ресурсів.')

                elif call.data.startswith('clan_watermelon'):
                    c = 'c' + cid
                    if checkLeader(call.from_user.id, cid):
                        if int(r.hget(c, 'money')) >= 200 and int(r.hget(c, 'r_spirit')) >= 50:
                            r.hincrby(c, 'money', -200)
                            r.hincrby(c, 'r_spirit', -50)
                            for mem in r.smembers('cl' + cid):
                                if int(r.hget(mem, 'head')) == 0:
                                    r.hset(mem, 'head', 3)
                                    r.hset(mem, 's_head', 1)
                                    quest(mem, 3, 3, 4)
                            await bot.send_message(cid, '\U0001F349 Клан очманів від бази.')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Недостатньо ресурсів.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Це може зробити тільки лідер чи заступник.')

                elif call.data.startswith('clan_heal'):
                    c = 'c' + cid
                    if checkLeader(call.from_user.id, cid):
                        if int(r.hget(c, 'money')) >= 10 and int(r.hget(c, 'r_spirit')) >= 1:
                            r.hincrby(c, 'money', -10)
                            r.hincrby(c, 'r_spirit', -1)
                            ran1 = randint(5, 10)
                            ran2 = randint(5, 10)
                            for mem in r.smembers('cl' + cid):
                                hp(100, mem)
                                r.hincrby(mem, 'injure', -ran1)
                                r.hincrby(mem, 'sch', -ran2)
                                if int(r.hget(mem, 'injure')) < 0:
                                    r.hset(mem, 'injure', 0)
                                if int(r.hget(mem, 'sch')) < 0:
                                    r.hset(mem, 'sch', 0)
                            await bot.send_message(cid, '\U0001fac0 Клан вилікувано.')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Недостатньо ресурсів.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Це може зробити тільки лідер чи заступник.')

                elif call.data.startswith('clan_money'):
                    c = 'c' + cid
                    if checkLeader(call.from_user.id, cid):
                        if int(r.hget(c, 'money')) >= 500 and int(r.hget(c, 'r_spirit')) >= 10:
                            r.hincrby(c, 'money', -500)
                            r.hincrby(c, 'r_spirit', -10)
                            rating = {}
                            for mem in r.smembers('cl' + cid):
                                rating.update({mem: int(r.hget(mem, 'money'))})
                            s_rating = sorted(rating, key=rating.get, reverse=False)
                            n = 0
                            for i in s_rating:
                                n += 1
                                if n == 6:
                                    break
                                r.hincrby(i, 'money', 100)
                            await bot.send_message(cid, '\U0001F4B5 Деякі учасники отримали соціальні виплати.')
                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Недостатньо ресурсів.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Це може зробити тільки лідер чи заступник.')

                elif call.data.startswith('clan_sell_'):
                    c = 'c' + cid
                    if checkLeader(call.from_user.id, cid):
                        if call.data.startswith('clan_sell_wood') and int(r.hget(c, 'wood')) >= 7500:
                            r.hincrby(c, 'money', 500)
                            r.hincrby(c, 'wood', -1500)
                            r.hincrby('resources', 'wood', 1500)
                            await bot.send_message(cid, '\U0001F333 Продано 1500 деревини.')
                        elif call.data.startswith('clan_sell_stone') and int(r.hget(c, 'stone')) >= 5000:
                            r.hincrby(c, 'money', 500)
                            r.hincrby(c, 'stone', -1000)
                            r.hincrby('resources', 'stone', 1000)
                            await bot.send_message(cid, '\U0001faa8 Продано 1000 каміння.')
                        elif call.data.startswith('clan_sell_cloth') and int(r.hget(c, 'cloth')) >= 2500:
                            r.hincrby(c, 'money', 500)
                            r.hincrby(c, 'cloth', -500)
                            r.hincrby('resources', 'cloth', 500)
                            await bot.send_message(cid, '\U0001F9F6 Продано 500 тканини.')
                        elif call.data.startswith('clan_sell_brick') and int(r.hget(c, 'brick')) >= 1500:
                            r.hincrby(c, 'money', 500)
                            r.hincrby(c, 'brick', -300)
                            r.hincrby('resources', 'brick', 300)
                            await bot.send_message(cid, '\U0001F9F1 Продано 300 цегли.')
                        elif call.data.startswith('clan_sell_radio') and int(r.hget(c, 'technics')) >= 50:
                            r.hincrby(c, 'money', 500)
                            r.hincrby(c, 'technics', -50)
                            r.hincrby('resources', 'technics', 50)
                            await bot.send_message(cid, '\U0001F4FB Продано 50 радіотехніки.')
                        elif call.data.startswith('clan_sell_code') and int(r.hget(c, 'codes')) >= 1:
                            r.hincrby(c, 'money', 500)
                            r.hincrby(c, 'r_spirit', 50)
                            r.hincrby(c, 'codes', -1)
                            r.hincrby('resources', 'codes', 1)
                            await bot.send_message(cid, '\U0001F916 Продано секретний код.')
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
                    c = 'c' + cid
                    if checkLeader(call.from_user.id, cid):
                        if int(r.hget(c, 'money')) >= 2000:
                            if call.data.startswith('clan_buy_wood') and int(r.hget('resources', 'wood')) >= 1500:
                                r.hincrby(c, 'money', -2000)
                                r.hincrby(c, 'wood', 1500)
                                r.hincrby('resources', 'wood', -1500)
                                await bot.send_message(cid, '\U0001F333 Придбано 1500 деревини.')
                            elif call.data.startswith('clan_buy_stone') and int(r.hget('resources', 'stone')) >= 1000:
                                r.hincrby(c, 'money', -2000)
                                r.hincrby(c, 'stone', 1000)
                                r.hincrby('resources', 'stone', -1000)
                                await bot.send_message(cid, '\U0001faa8 Придбано 1000 каміння.')
                            elif call.data.startswith('clan_buy_cloth') and int(r.hget('resources', 'cloth')) >= 500:
                                r.hincrby(c, 'money', -2000)
                                r.hincrby(c, 'cloth', 500)
                                r.hincrby('resources', 'cloth', -500)
                                await bot.send_message(cid, '\U0001F9F6 Придбано 500 тканини.')
                            elif call.data.startswith('clan_buy_brick') and int(r.hget('resources', 'brick')) >= 300:
                                r.hincrby(c, 'money', -2000)
                                r.hincrby(c, 'brick', 300)
                                r.hincrby('resources', 'brick', -300)
                                await bot.send_message(cid, '\U0001F9F1 Придбано 300 цегли.')
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
                elif call.data.startswith('clan_buff'):
                    c = 'c' + cid
                    if checkLeader(call.from_user.id, cid):
                        if int(r.hget(c, 'war')) == 1:
                            if call.data.startswith('clan_buff_1'):
                                if int(r.hget(c, 'buff_1')) == 0:
                                    if int(r.hget(c, 'wood')) >= 2000 and int(r.hget(c, 'stone')) >= 1000 \
                                            and int(r.hget(c, 'cloth')) >= 200 and int(r.hget(c, 'r_spirit')) >= 100:
                                        r.hincrby(c, 'wood', -2000)
                                        r.hincrby(c, 'stone', -1000)
                                        r.hincrby(c, 'cloth', -200)
                                        r.hincrby(c, 'r_spirit', -100)
                                        r.hset(c, 'buff_1', 1)
                                        await bot.send_message(cid, 'Отримано баф:\n\n\U0001f7e2 Додаткова нагорода '
                                                                    'за рейди на клани (залежить від його рівня).')
                                    else:
                                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                        text='Недостатньо ресурсів.')
                                else:
                                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                    text='У вас вже є цей баф.')

                            if call.data.startswith('clan_buff_2'):
                                if int(r.hget(c, 'buff_2')) == 0:
                                    if int(r.hget(c, 'money')) >= 10000:
                                        r.hincrby(c, 'money', -10000)
                                        r.hset(c, 'buff_2', 1)
                                        r.hset(c, 'result', 2)
                                        await bot.send_message(cid, 'Отримано баф:\n\n\U0001f7e0 Вдвічі більше очків'
                                                                    ' отримується за рейд на ворожий клан. Вдвічі '
                                                                    'більше пакунків за перемогу у війні.')
                                    else:
                                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                        text='Недостатньо ресурсів.')
                                else:
                                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                    text='У вас вже є цей баф.')

                            if call.data.startswith('clan_buff_3'):
                                if int(r.hget(c, 'buff_3')) == 0:
                                    if int(r.hget(c, 'codes')) >= 12 and int(r.hget(c, 'technics')) >= 100:
                                        r.hincrby(c, 'codes', -12)
                                        r.hincrby(c, 'technics', -100)
                                        r.hset(c, 'buff_3', 1)
                                        msg = 'Отримано баф:\n\n\U0001f534 Очки можна отримати з рейду на будь-який' \
                                              ' клан та рейдити раз в 45 хвилин. Можливість бачити очки ворога.'
                                        await bot.send_message(cid, msg)
                                    else:
                                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                        text='Недостатньо ресурсів.')
                                else:
                                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                    text='У вас вже є цей баф.')

                            if call.data.startswith('clan_buff_4'):
                                if int(r.hget(c, 'buff_4')) == 0:
                                    if call.data.startswith('clan_buff_4_0'):
                                        if int(r.hget(c, 'cloth')) >= 200 and int(r.hget(c, 'brick')) >= 200:
                                            r.hincrby(c, 'cloth', -200)
                                            r.hincrby(c, 'brick', -200)
                                            r.hset(c, 'buff_4', 5)
                                            msg = 'Отримано баф:\n\n\U0001f7e3 За роботу на благо громади ' \
                                                  'буде нараховано 1-3 квестових очків замість зарплати.'
                                            await bot.send_message(cid, msg)
                                        else:
                                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                            text='Недостатньо ресурсів.')
                                    if call.data.startswith('clan_buff_4_1_1'):
                                        if int(r.hget(c, 'cloth')) >= 600 and int(r.hget(c, 'brick')) >= 300 \
                                                and int(r.hget(c, 'wood')) >= 3000 and int(r.hget(c, 'stone')) >= 1500:
                                            r.hincrby(c, 'cloth', -600)
                                            r.hincrby(c, 'brick', -300)
                                            r.hincrby(c, 'wood', -3000)
                                            r.hincrby(c, 'stone', -1500)
                                            r.hset(c, 'buff_4', 11)
                                            msg = 'Отримано баф:\n\n\U0001f7e3\U0001f7e3 +2 очка за звичайні квести.'
                                            await bot.send_message(cid, msg)
                                        else:
                                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                            text='Недостатньо ресурсів.')
                                    if call.data.startswith('clan_buff_4_1_2'):
                                        if int(r.hget(c, 'codes')) >= 10:
                                            r.hincrby(c, 'codes', -10)
                                            r.hset(c, 'buff_4', 12)
                                            msg = 'Отримано баф:\n\n\U0001f7e3\U0001f7e3\U0001f7e3 ' \
                                                  '25% шанс отримати 3 квестові очки за перемогу в масовій битві.'
                                            await bot.send_message(cid, msg)
                                        else:
                                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                            text='Недостатньо ресурсів.')

                                    if call.data.startswith('clan_buff_4_2_1'):
                                        if int(r.hget(c, 'r_spirit')) >= 180:
                                            r.hincrby(c, 'r_spirit', -180)
                                            r.hset(c, 'buff_4', 21)
                                            msg = 'Отримано баф:\n\n\U0001f7e3\U0001f7e3 3% шанс непомітно отримати' \
                                                  ' квестове очко за перемогу в дуелі.'
                                            await bot.send_message(cid, msg)
                                        else:
                                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                            text='Недостатньо ресурсів.')
                                    if call.data.startswith('clan_buff_4_2_2'):
                                        if int(r.hget(c, 'codes')) >= 10:
                                            r.hincrby(c, 'codes', -10)
                                            r.hset(c, 'buff_4', 22)
                                            msg = 'Отримано баф:\n\n\U0001f7e3\U0001f7e3\U0001f7e3 +12 квестових очків'\
                                                  ' за охорону території, якщо увімкнена зарплата.'
                                            await bot.send_message(cid, msg)
                                        else:
                                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                            text='Недостатньо ресурсів.')

                                    if call.data.startswith('clan_buff_4_3_1'):
                                        if int(r.hget(c, 'technics')) >= 120 and int(r.hget(c, 'money')) >= 2500:
                                            r.hincrby(c, 'technics', -120)
                                            r.hincrby(c, 'money', -2500)
                                            r.hset(c, 'buff_4', 31)
                                            msg = 'Отримано баф:\n\n\U0001f7e3\U0001f7e3 +30 квестових очків ' \
                                                  'за пограбування гумконвою.'
                                            await bot.send_message(cid, msg)
                                        else:
                                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                            text='Недостатньо ресурсів.')
                                    if call.data.startswith('clan_buff_4_3_2'):
                                        if int(r.hget(c, 'codes')) >= 10:
                                            r.hincrby(c, 'codes', -10)
                                            r.hset(c, 'buff_4', 32)
                                            msg = 'Отримано баф:\n\n\U0001f7e3\U0001f7e3\U0001f7e3 +10 квестових ' \
                                                  'очків за приєднання учасника в клан.'
                                            await bot.send_message(cid, msg)
                                        else:
                                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                            text='Недостатньо ресурсів.')

                                    if call.data.startswith('clan_buff_4_4_1'):
                                        if int(r.hget(c, 'technics')) >= 50 and int(r.hget(c, 'money')) >= 10000:
                                            r.hincrby(c, 'technics', -50)
                                            r.hincrby(c, 'money', -10000)
                                            r.hset(c, 'buff_4', 41)
                                            msg = 'Отримано баф:\n\n\U0001f7e3\U0001f7e3 Шанс знайти квестове ' \
                                                  'очко в пакунку замість радіотехніки.'
                                            await bot.send_message(cid, msg)
                                        else:
                                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                            text='Недостатньо ресурсів.')
                                    if call.data.startswith('clan_buff_4_4_2'):
                                        if int(r.hget(c, 'codes')) >= 10:
                                            r.hincrby(c, 'codes', -10)
                                            r.hset(c, 'buff_4', 42)
                                            q_points(call.from_user.id, 250)
                                            msg = 'Отримано баф:\n\n\U0001f7e3\U0001f7e3\U0001f7e3 +250 квестових очків.'
                                            await bot.send_message(cid, msg)
                                        else:
                                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                            text='Недостатньо ресурсів.')
                                else:
                                    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                                    text='У вас вже є цей баф.')

                        else:
                            await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                            text='Вступіть в кланові війни, щоб купляти бафи.')
                    else:
                        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                        text='Це може зробити тільки лідер чи заступник.')
            else:
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                                text='Клановий магазин тільки для учасників клану.')

    #  await call.answer()


@dp.message_handler()
async def echo(message):
    try:
        '''
        try:
            if message.text.startswith('@') and message.text[1:].encode() in r.smembers('run'):
                await message.reply('\u26A0\uFE0F УВАГА! \u26A0\uFE0F\n\nЦей канал розповсюджує фейки.')
            elif str(message.forward_from_chat.id).encode() in r.smembers('rid') or \
                    str(message.from_user.id).encode() in r.smembers('rid'):
                await message.reply('\u26A0\uFE0F УВАГА! \u26A0\uFE0F\n\nЦей канал розповсюджує фейки.')
        except:
            pass
        if message.chat.id != -1001211386939:
        '''
        if 'Кубик' in message.text or 'кубик' in message.text:
            await bot.send_dice(chat_id=message.chat.id, reply_to_message_id=message.message_id)

        elif 'казино' in message.text.lower():
            await bot.send_sticker(message.chat.id,
                                   'CAACAgIAAxkBAAEIjuhhS6oNEVDkBDkBUokJJLjTBRloBAACCQADT9w1GxCgVEna0OwQIQQ',
                                   reply_to_message_id=message.message_id)
        elif 'мавпа' in message.text.lower() or 'чурка' in message.text.lower():
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

        elif message.text.lower() in ('тривога', '/alert'):
            with open('pic.png', 'wb') as handle:
                response = requests.get('https://alerts.com.ua/map.png', stream=True)
                if not response.ok:
                    print(response)
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)

            webp = Image.open('pic.png')
            webp.save('pic.webp', format="webp")

            await bot.send_sticker(message.chat.id,
                                   open("pic.webp", "rb"),
                                   reply_to_message_id=message.message_id)
            r.hincrby('logs', 'alert_count', 1)

        elif message.text.lower() == '/fix':
            layout_en = "`~@#$%^&qwertyuiop[]QWERTYUIOP{}asdfghjkl;'\\ASDFGHJKL:\"|zxcvbnm,./ZXCVBNM<>?"
            layout_ua = "'₴\"№;%:?йцукенгшщзхїЙЦУКЕНГШЩЗХЇфівапролджє\\ФІВАПРОЛДЖЄ/ячсмитьбю.ЯЧСМИТЬБЮ,"

            msg1 = message.reply_to_message.text
            enl = 0
            msg2 = ''

            for letter in msg1:
                if letter in layout_en:
                    enl += 1

            if len(msg1) / 2 < enl:
                for letter in msg1:
                    if letter in layout_en:
                        msg2 += layout_ua[layout_en.index(letter)]
                    else:
                        msg2 += letter

                await message.answer(f'[Фікс розкладки]\n\n{msg2}')

        if message.chat.type == 'private':
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
                                                                               inline_query.query)),
                                                          disable_web_page_preview=True),
            reply_markup=markup.add(InlineKeyboardButton(text='Атакувати!', callback_data=call)),
            thumb_url='https://i.ibb.co/0nFNwSH/rusak.png',
            description='надери комусь дупу\nнапиши & щоб відкрити інші режими')
        r2 = InlineQueryResultArticle(
            id='2',
            title='Скільки задонатиш на ЗСУ?',
            input_message_content=InputTextMessageContent(donate_to_zsu()),
            thumb_url='https://i.ibb.co/WkpvSdd/zsu.png',
            description='прямо зараз')
        r3 = InlineQueryResultArticle(
            id='3',
            title='Ким ти був в минулому житті?',
            input_message_content=InputTextMessageContent(str('Ким ти був в минулому житті?\n\n' + pastLife())),
            thumb_url='https://i.ibb.co/mJ0SXzL/Past-lives-2-56a6ede63df78cf772910470.jpg',
            description='можливо, воно було не таке нікчемне як зараз')
        r4 = InlineQueryResultArticle(
            id='4',
            title='Куди ти поїдеш на заробітки?',
            input_message_content=InputTextMessageContent(str('Куди ти поїдеш на заробітки?\n\n' + earnings())),
            thumb_url='https://i.ibb.co/ypDcLNc/Polunytsya-e1538080073461.jpg',
            description='добре там є, де нас нема')
        r5 = InlineQueryResultArticle(
            id='5',
            title='Визнач свої політичні координати?',
            input_message_content=InputTextMessageContent(str('Мої політичні координати\n\n' + political())),
            thumb_url='https://i.ibb.co/XbGNVSS/maxresdefault.jpg',
            description='правачок чи лібераха?')
        r6 = InlineQueryResultArticle(
            id='6',
            title='Наскільки ви підходите один одному?',
            input_message_content=InputTextMessageContent('*звук мовчання*'),
            thumb_url='https://i.ibb.co/QDkHD0b/telltaale.jpg',
            description='вибирай дівку і залицяйся')
        r7 = InlineQueryResultArticle(
            id='7',
            title='Питай, що турбує',
            input_message_content=InputTextMessageContent('*звук мовчання*'),
            thumb_url='https://i.ibb.co/qkjYFDF/im610x343-Zelensky-notebook.jpg',
            description='ну тобто треба щось написати')
        r8 = InlineQueryResultArticle(
            id='8',
            title='Зрадометр',
            input_message_content=InputTextMessageContent(str(zradoMoga())),
            thumb_url='https://i.ibb.co/7GJzmc4/Ea-PHB6-EWs-AAVER4.jpg',
            description='допоможе визначитись з певною подією')
        r9 = InlineQueryResultArticle(
            id='9',
            title='Якого розміру в тебе пісюн?',
            input_message_content=InputTextMessageContent(str(penis())),
            thumb_url='https://i.ibb.co/3FQYpgB/photo-2020-08-27-14-49-33.jpg',
            description='роздягайся')
        r10 = InlineQueryResultArticle(
            id='10',
            title='Вибір з кількох варіантів',
            input_message_content=InputTextMessageContent('*звук мовчання*'),
            thumb_url='https://i.ibb.co/HtK6FTR/o-1ej2111rn189p9qrabv1au81o1o1k.jpg',
            description='наприклад, "Бути чи/або не бути?"')
        r11 = InlineQueryResultArticle(
            id='11',
            title='Вибери для себе пиво',
            input_message_content=InputTextMessageContent('Бот радить тобі...\n\n' + beer()),
            thumb_url='https://i.ibb.co/rZbG1fD/image.jpg',
            description='або для когось іншого')
        r12 = InlineQueryResultArticle(
            id='12',
            title='Генератор випадкових чисел',
            input_message_content=InputTextMessageContent(generator(inline_query.query)),
            thumb_url='https://i.ibb.co/3TZsnyj/randomn.png',
            description='введи від 1 до 3 чисел (перші два проміжок, третє кількість)')
        r13 = InlineQueryResultArticle(
            id='13',
            title='Визнач своє походження',
            input_message_content=InputTextMessageContent('Моє походження:\n\n' + race()),
            thumb_url='https://i.ibb.co/7V4QmDL/nations.png',
            description='зараз бот проаналізує твої ДНК...')
        r14 = InlineQueryResultArticle(
            id='14',
            title='Який в тебе гендер?',
            input_message_content=InputTextMessageContent(gender()),
            thumb_url='https://i.ibb.co/LrH2D0W/gender.jpg',
            description='все дуже серйозно')
        r15 = InlineQueryResultArticle(
            id='15',
            title='Віджимайся!',
            input_message_content=InputTextMessageContent('\U0001F4AA Роби ' + roll_push_ups()),
            thumb_url='https://i.ibb.co/xjQ56rR/billy.png',
            description='ти ж цього не зробиш, чи не так?')
        await bot.answer_inline_query(inline_query.id, results=[r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12,
                                                                r13, r14, r15], cache_time=0)
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
                                                                               inline_query.query)),
                                                          disable_web_page_preview=True),
            reply_markup=markup.add(InlineKeyboardButton(text='Атакувати!', callback_data=call)),
            thumb_url='https://i.ibb.co/0nFNwSH/rusak.png',
            description='введи різницю сили (мінімум 1)')
        r2 = InlineQueryResultArticle(
            id='2',
            title='Особисте запрошення',
            input_message_content=InputTextMessageContent(str(prepare_to_fight(inline_query.from_user.id,
                                                                               inline_query.from_user.first_name,
                                                                               'pr' + inline_query.query)),
                                                          disable_web_page_preview=True),
            reply_markup=markup2.add(InlineKeyboardButton(text='Атакувати!', callback_data=call1)),
            thumb_url='https://i.ibb.co/0nFNwSH/rusak.png',
            description='введи @username')
        r3 = InlineQueryResultArticle(
            id='3',
            title='Турнірний режим',
            input_message_content=InputTextMessageContent(str(prepare_to_fight(inline_query.from_user.id,
                                                                               inline_query.from_user.first_name,
                                                                               'tr' + inline_query.query)),
                                                          disable_web_page_preview=True),
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
            title='Скільки задонатиш на ЗСУ?',
            input_message_content=InputTextMessageContent(donate_to_zsu()),
            thumb_url='https://i.ibb.co/WkpvSdd/zsu.png',
            description='прямо зараз')
        r3 = InlineQueryResultArticle(
            id='3',
            title='Куди ' + inline_query.query + ' поїде на заробітки?',
            input_message_content=InputTextMessageContent(str('Куди ' + inline_query.query +
                                                              ' поїде на заробітки?\n\n' + earnings())),
            thumb_url='https://i.ibb.co/ypDcLNc/Polunytsya-e1538080073461.jpg',
            description='добре там є, де нас нема')
        r4 = InlineQueryResultArticle(
            id='4',
            title='Визнач ' + inline_query.query + ' політичні координати',
            input_message_content=InputTextMessageContent(str(inline_query.query + ' політичні координати\n\n' +
                                                              political())),
            thumb_url='https://i.ibb.co/XbGNVSS/maxresdefault.jpg',
            description='правачок чи лібераха?')
        r5 = InlineQueryResultArticle(
            id='5',
            title='Наскільки ви з ' + inline_query.query + ' підходите один одному?',
            input_message_content=InputTextMessageContent(str('Ви з ' + inline_query.query +
                                                              ' підходите один одному на ' + love())),
            thumb_url='https://i.ibb.co/QDkHD0b/telltaale.jpg',
            description='вибирай дівку і залицяйся')
        r6 = InlineQueryResultArticle(
            id='6',
            title='Питай, що турбує',
            input_message_content=InputTextMessageContent(str('\u2753 ' + inline_query.query + '\n\n' + question())),
            thumb_url='https://i.ibb.co/qkjYFDF/im610x343-Zelensky-notebook.jpg',
            description='ну тобто треба щось написати')
        r7 = InlineQueryResultArticle(
            id='7',
            title='Зрадометр',
            input_message_content=InputTextMessageContent(str(inline_query.query + '\n\n' + zradoMoga())),
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
            input_message_content=InputTextMessageContent('\u2753' + inline_query.query +
                                                          '\n\n' + choose(inline_query.query)),
            thumb_url='https://i.ibb.co/HtK6FTR/o-1ej2111rn189p9qrabv1au81o1o1k.jpg',
            description='наприклад, "Бути чи/або не бути?"')
        r10 = InlineQueryResultArticle(
            id='10',
            title='Вибери для ' + inline_query.query + ' пиво',
            input_message_content=InputTextMessageContent(inline_query.query + ', я рекомендую тобі тобі...\n\n' +
                                                          beer()),
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
            title='Визнач ' + inline_query.query + ' походження',
            input_message_content=InputTextMessageContent('Походження ' + inline_query.query + ':\n\n' + race()),
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
            input_message_content=InputTextMessageContent('\U0001F4AA ' + inline_query.query + ', роби ' +
                                                          roll_push_ups()),
            thumb_url='https://i.ibb.co/xjQ56rR/billy.png',
            description='ти ж цього не зробиш, чи не так?')
        await bot.answer_inline_query(inline_query.id, results=[r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12,
                                                                r13, r14], cache_time=0)
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
