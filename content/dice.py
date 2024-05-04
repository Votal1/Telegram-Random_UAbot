from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import r, bot


async def select_casino(message, hour):
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
        if 8 < hour < 20:
            emoji = '🌝'
        else:
            emoji = '🌚'
        msg = f'{emoji} Вітаємо вас у RandomUAbotCasino!\n\n' \
              f'Ціни за участь та суми виграшу:\n' \
              f'🎯 - 💵 10 -> 50\n' \
              f'🎲 - 💵 30 -> 150\n' \
              f'🎳 - 💵 50 -> 250\n' \
              f'⚽ - 💵 100 -> 150\n' \
              f'🏀 - 💵 100 -> 200 \n' \
              f'🎰 - 💵 25 -> 777 / 📦 / 🌀 / 🌟'
        msg2 = False
        free_spins = '\n\nФріспіни:\n'
        for emoji in ['🎯', '🎲', '🎳', '⚽', '🏀', '🎰']:
            fs = r.hget(emoji, uid)
            if fs and int(fs) > 0:
                msg2 = True
                free_spins += f'{emoji} {int(fs)}, '
        if msg2:
            msg += free_spins[:-2]
        msg += '\n\n⬇ Виберіть гру та натискайте /dice'
        await bot.send_message(uid, msg, reply_to_message_id=mid, reply_markup=markup)

        if message.chat.type != 'private':
            await message.reply('Надіслано в пп.')
    except:
        pass


async def dice(message):
    try:
        prices = {'🎯': 10, '🎲': 30, '🎳': 50, '⚽': 100, '🏀': 100, '🎰': 25}
        uid = message.from_user.id
        mid = message.message_id
        cid = message.chat.id
        selected_dice = r.hget(uid, 'selected_dice')
        money = int(r.hget(uid, 'money'))
        if selected_dice:
            selected_dice = selected_dice.decode()
            if selected_dice == '🎲' and len(message.text.split()) == 1:
                await message.reply('Виберіть число від 1 до 6')
            else:
                free_spin = r.hget(selected_dice, uid)

                if free_spin and int(free_spin) > 0:
                    spin = True
                    r.hincrby(selected_dice, uid, -1)
                elif money >= prices[selected_dice]:
                    spin = True
                    r.hincrby(uid, 'money', -prices[selected_dice])
                else:
                    spin = False
                    await message.reply('Недостатньо коштів на рахунку.')

                if spin:
                    d = await bot.send_dice(cid, reply_to_message_id=mid, emoji=selected_dice)
                    value = d.dice.value

                    if selected_dice == '🎯':
                        if value == 6:
                            r.hincrby(uid, 'money', 50)
                    elif selected_dice == '🎲':
                        if value == int(message.text.split()[1]):
                            r.hincrby(uid, 'money', 50)
                    elif selected_dice == '🎳':
                        if value == 6:
                            r.hincrby(uid, 'money', 250)
                    elif selected_dice == '⚽':
                        if value >= 3:
                            r.hincrby(uid, 'money', 150)
                    elif selected_dice == '🏀':
                        if value >= 4:
                            r.hincrby(uid, 'money', 200)
                    elif selected_dice == '🎰':
                        if value == 1:
                            r.hincrby(uid, 'packs', 1)
                        elif value == 22:
                            r.hincrby(uid, 'tape', 1)
                        elif value == 43:
                            r.hincrby(uid, 'strap', 1)
                        elif value == 64:
                            r.hincrby(uid, 'money', 777)
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
