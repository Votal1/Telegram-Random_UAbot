from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import r, bot


async def select_casino(message):
    try:
        uid = message.from_user.id
        mid = message.message_id

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='🎯', callback_data='selected_dice_1'),
                   InlineKeyboardButton(text='🎲', callback_data='selected_dice_2'),
                   InlineKeyboardButton(text='🎳', callback_data='selected_dice_3'))
        markup.add(InlineKeyboardButton(text='⚽', callback_data='selected_dice_4'),
                   InlineKeyboardButton(text='🏀', callback_data='selected_dice_5'),
                   InlineKeyboardButton(text='🎰', callback_data='selected_dice_6'))
        msg = '🌝 Вітаємо вас у RandomUAbotCasino!\n\n' \
              'Ціни за участь та суми виграшу:\n' \
              '🎯 - 💵 10 -> 50\n' \
              '🎲 - 💵 30 -> 150\n' \
              '🎳 - 💵 50 -> 250\n' \
              '⚽ - 💵 100 -> 150\n' \
              '🏀 - 💵 100 -> 200 \n' \
              '🎰 - 💵 25 -> 777 / 📦 / 🌀 / 🌟'
        await bot.send_message(uid, msg, reply_to_message_id=mid, reply_markup=markup)

        if message.chat.type != 'private':
            await message.reply('Надіслано в пп.')
    except:
        pass


async def dice(message):
    try:
        uid = message.from_user.id
        mid = message.message_id
        cid = message.chat.id
        selected_dice = r.hget(uid, 'selected_dice')
        money = int(r.hget(uid, 'money'))
        if selected_dice:
            selected_dice = selected_dice.decode()

            if selected_dice == '🎯':
                if money >= 10:
                    d = await bot.send_dice(cid, reply_to_message_id=mid, emoji=selected_dice)
                    value = d.dice.value
                    if value == 6:
                        r.hincrby(uid, 'money', 40)
                    else:
                        r.hincrby(uid, 'money', -10)
                else:
                    await message.reply('Недостатньо коштів на рахунку.')

            elif selected_dice == '🎲':
                text = message.text.split()
                if len(text) == 1 or int(text[1]) not in range(1, 7):
                    await message.reply('Виберіть число від 1 до 6')
                else:
                    if money >= 30:
                        d = await bot.send_dice(cid, reply_to_message_id=mid, emoji=selected_dice)
                        value = d.dice.value
                        if value == int(text[1]):
                            r.hincrby(uid, 'money', 120)
                        else:
                            r.hincrby(uid, 'money', -30)
                    else:
                        await message.reply('Недостатньо коштів на рахунку.')

            elif selected_dice == '🎳':
                if money >= 50:
                    d = await bot.send_dice(cid, reply_to_message_id=mid, emoji=selected_dice)
                    value = d.dice.value
                    if value == 6:
                        r.hincrby(uid, 'money', 200)
                    else:
                        r.hincrby(uid, 'money', -50)
                else:
                    await message.reply('Недостатньо коштів на рахунку.')

            elif selected_dice == '⚽':
                if money >= 100:
                    d = await bot.send_dice(cid, reply_to_message_id=mid, emoji=selected_dice)
                    value = d.dice.value
                    if value >= 3:
                        r.hincrby(uid, 'money', 50)
                    else:
                        r.hincrby(uid, 'money', -100)
                else:
                    await message.reply('Недостатньо коштів на рахунку.')

            elif selected_dice == '🏀':
                if money >= 50:
                    d = await bot.send_dice(cid, reply_to_message_id=mid, emoji=selected_dice)
                    value = d.dice.value
                    if value >= 4:
                        r.hincrby(uid, 'money', 100)
                    else:
                        r.hincrby(uid, 'money', -100)
                else:
                    await message.reply('Недостатньо коштів на рахунку.')

            elif selected_dice == '🎰':
                if money >= 25:
                    d = await bot.send_dice(cid, reply_to_message_id=mid, emoji=selected_dice)
                    value = d.dice.value
                    if value == 1:
                        r.hincrby(uid, 'packs', 1)
                    elif value == 22:
                        r.hincrby(uid, 'tape', 1)
                    elif value == 43:
                        r.hincrby(uid, 'strap', 1)
                    elif value == 64:
                        r.hincrby(uid, 'money', 777)
                    r.hincrby(uid, 'money', -25)
                else:
                    await message.reply('Недостатньо коштів на рахунку.')

        else:
            await message.reply('/casino - вибрати гру')
    except:
        pass


async def callback_dice(call):
    uid = call.from_user.id
    cdata = call.data
    msg = '123'
    if cdata == 'selected_dice_1':
        r.hset(uid, 'selected_dice', '🎯')
        msg = 'Вибрано дартс'
    if cdata == 'selected_dice_2':
        r.hset(uid, 'selected_dice', '🎲')
        msg = 'Вибрано кубик'
    if cdata == 'selected_dice_3':
        r.hset(uid, 'selected_dice', '🎳')
        msg = 'Вибрано булінг'
    if cdata == 'selected_dice_4':
        r.hset(uid, 'selected_dice', '⚽')
        msg = 'Вибрано ГОООООЛ'
    if cdata == 'selected_dice_5':
        r.hset(uid, 'selected_dice', '🏀')
        msg = 'Вибрано баскетбол'
    if cdata == 'selected_dice_6':
        r.hset(uid, 'selected_dice', '🎰')
        msg = 'Вибрано слоти'
    await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=msg)
