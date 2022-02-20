from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import json
import os

API_TOKEN = "5245769074:AAHpskqOMOfpqpkXbBCYNn4zZUagbJDKFew"
JSON_DATA = "data.json"

user = "@TreeOfLife_one" # Admin

if not os.path.exists(JSON_DATA):
    open("data.json", "w", encoding="utf8").write(r"{}")

bot = Bot(token=API_TOKEN, parse_mode="html")
dp  = Dispatcher(bot)

# Text and buttons, count of buttons must be equals to count of btns_text
start_text = "🚶 Добро пожаловать, используйте навигацию."
buttons    = ["ℹ️ Информация", "💲 Тарифы", "💳 Оформить доступ"]
btns_text  = ["""Информация о нашем закрытом криптовалютном клубе Rich Signals, и что в него входит: 

1⃣ Ежедневные сигналы спот и фьючерсы; 
2⃣ DeFi, NFT и GameFi; 
3⃣ Фарминг, пулы ликвидности, стейкинг; 
4⃣ Аирдропы, вайтлисты, халявные темы с майнингом и крипто игры; 
5⃣ Заходы в проекты на ранней стадии (Seed, Private стадии); 
6⃣ Амбассадорки,теснеты и ноды; 
7⃣ Полезные инструменты для работы; 
8⃣ Статьи и обучение; 
9⃣ Чат единомышленников и опытных специалистов, которые всегда помогут;
↗️ Моё личное кураторство.""", """💲 <b>Тарифы:</b>

👉 50$ 2 месяца 
👉 100$ 6 месяцев 
👉 150$ год 
👉 200$ навсегда""", f"<b>По всем вопросам:</b> {user}"]

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton(buttons[0]))
menu.add(KeyboardButton(buttons[1]), KeyboardButton(buttons[2]))


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, text=start_text, reply_markup=menu)
    # check user
    uid = message.chat.id
    users = json.load(open(JSON_DATA, "r", encoding="utf8"))
    if not uid in users:
        users[uid] = [message.chat.first_name, message.chat.last_name, message.chat.username]
        json.dump(users, open(JSON_DATA, "w", encoding="utf8"), indent=4)


@dp.message_handler()
async def handler(message: types.Message):
    chat_id = message.chat.id
    try:
        for i in range(0, len(buttons)):
            if message.text == buttons[i]:
                await bot.send_message(chat_id, btns_text[i], reply_markup=menu)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
