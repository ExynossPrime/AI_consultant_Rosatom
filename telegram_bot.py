from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
import telebot
from telebot import types

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials='ZWNhNjg5MDEtOGIxYS00Nzg1LWFiOTAtMjQ4ZjhmYjViZGIzOjZkNjk3ZWEyLTkwYTgtNDNmNC04YTIzLTMwODljY2QyZDA2OQ==', verify_ssl_certs=False)
bot = telebot.TeleBot('6837296858:AAHJtUPKsPSIUjDyXFrydQkKIslBROq1Fx0')

# messages = [
#     SystemMessage(
#         content="Ты эмпатичный бот-консультант, который помогает пользователю решить его проблемы."
#     )
# ]

# messages = [
#     SystemMessage(
#         content="Ты бот ищущий ответы в нормативно-правовых актах Российской Федерации"
#     )
# ]

messages = [
    SystemMessage(
        content="Ты работаешь в отделе закупок государственной организации и ищешь ответы в нормативно-правовых актах Российской Федерации"
    )
]

# messages = [
#     SystemMessage(
#         content="Ты работаешь в отделе закупок государственной организации Росатом и ищешь ответы в нормативно-правовых актах Росатома и ЕОСЗ"
#     )
# ]

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник Росатом!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота

    text = message.text
    messages.append(HumanMessage(content=text))
    res = chat(messages)
    messages.append(res)
    # messages.append('и в каком нормативно-правовом акте это указано')
    print(res.content)
    bot.send_message(message.chat.id, res.content)

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть

# while (True):
#     user_input = input("User: ")
#     messages.append(HumanMessage(content=user_input))
#     res = chat(messages)
#     messages.append(res)
#     print("Bot: ", res.content)