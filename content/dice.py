from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import r, bot


async def select_casino(message):
    try:
        uid = message.from_user.id
        mid = message.message_id

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='🎲', callback_data='selected_dice_2'))
        msg = '🌝 Вітаємо вас у RandomUAbotCasino!\n\n' \
              'Ціни за участь та суми виграшу:\n' \
              '🎲 - 💵 30 -> 150'
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
            if selected_dice == '🎲':
                text = message.text.split()
                input_number = int(text[1])
                if len(text) == 1 or input_number not in range(1, 7):
                    await message.reply('Виберіть число від 1 до 6')
                else:
                    if money >= 30:
                        d = await bot.send_dice(cid, reply_to_message_id=mid, emoji=selected_dice)
                        value = d.dice.value
                        if value == input_number:
                            r.hincrby(uid, 'money', 120)
                        else:
                            r.hincrby(uid, 'money', -30)
                    else:
                        await message.reply('Недостатньо коштів на рахунку.')

        else:
            await message.reply('/casino - вибрати гру')
    except:
        pass


async def callback_dice(call):
    uid = call.from_user.id
    cdata = call.data
    if cdata == 'selected_dice_2':
        r.hset(uid, 'selected_dice', '🎲')
        await bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Вибрано кубик')