from aiogram import Router, types, F
from aiogram.filters import Command, or_f
from aiogram.utils.markdown import hlink
from keyboards.for_navigate import keyboard

private_router = Router()

@private_router.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.reply("Привет, чем могу помочь?", reply_markup=keyboard)
    await message.answer_sticker(sticker="CAACAgIAAxkBAAPqZwK3kqfKSO9WEIlvTew3GaX-jhQAAiwVAAKwrFBIjVq8L92aYLA2BA")


@private_router.message(or_f(Command('birzhi'), F.text == 'Биржи'))
async def handle_birzhi(message: types.Message):
    binance_link = hlink('Binance💸',
                         'https://www.binance.com/activity/referral-entry/CPA/together-v4?hl=ru&ref=CPA_00S173EB0S')
    response_text = f"<b>‼️Все биржи на которых торгуем‼️</b>:\n{binance_link}"
    await message.reply(response_text, parse_mode="HTML")


@private_router.message(or_f(Command('reklama'), F.text == 'Реклама'))
async def handle_reklama(message: types.Message):
    await message.reply( "<b>💸НАШ ПРАЙС💸</b>\n"
                         "\n🔥3/48 <b>120$ <s>150$</s></b>\n"
                         "🔥2/24 <b>70$ <s>115$</s></b>\n"
                         "\n<b>‼️По рекламе писать менеджеру‼️</b>",
                         parse_mode = "HTML")


@private_router.message(or_f(Command('zakrytyy_kanal'), F.text == 'Закрытый канал'))
async def handle_zakrytyy_kanal(message: types.Message):
    await message.reply("<b>🔒Наши закрытые каналы🔒</b>\n"
                        "\n🔥Канал для новичков <b>10$ <s>30$</s></b>\n "
                        "🔥PRO канал <b>50$ <s>100$</s></b>\n"
                        "\n<b>‼️ПО ЗАКРЫТЫМ КАНАЛАМ ПИСАТЬ МЕНЕДЖЕРУ‼️</b>",
                        partse_mode = 'HTML')


@private_router.message(or_f(Command('menedzher'), F.text == 'Менеджер'))
async def handle_menedzher(message: types.Message):
    await message.reply("<b>👨‍💻По всем вопросам писать: @wexhr</b>\n"
                        "\n<b>‼️ВАЖНО У НАС ТОЛЬКО ОДИН МЕНЕДЖЕР,НЕ ВЕДИТЕСЬ НА МОШЕННИКОВ‼️</b>")


@private_router.message(Command('about'))
async def about(message: types.Message):
    about_text = """
<b>Наш канал предлагает:</b>
- Множество бесплатных материалов по криптовалютам и акциям.
- Первые новости о раздачах и других важных событиях.
- Активную торговлю вместе с нами и доступ к схемам и портфелю в наших приватных каналах.

<b>В боте вы найдете:</b>
- Ссылки на наши приватные каналы.
- Информацию для рекламодателей.
- Биржи, на которых мы торгуем.
"""
    await message.reply(about_text, parse_mode="HTML")



