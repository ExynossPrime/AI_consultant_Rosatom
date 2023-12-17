from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
import telebot
from telebot import types

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials='ZWNhNjg5MDEtOGIxYS00Nzg1LWFiOTAtMjQ4ZjhmYjViZGIzOjZkNjk3ZWEyLTkwYTgtNDNmNC04YTIzLTMwODljY2QyZDA2OQ==', verify_ssl_certs=False)
bot = telebot.TeleBot('6837296858:AAFSVSodG1VsO46BCA3x4fcQLBj1YUl8Qas')

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

# messages = [
#     SystemMessage(
#         content="Ты работаешь в отделе закупок государственной организации и ищешь ответы в нормативно-правовых актах Российской Федерации"
#     )
# ]

# messages = [
#     SystemMessage(
#         content="Ты работаешь в отделе закупок организации и ищешь ответы в нормативно-правовых актах Российской Федерации"
#     )
# ]

# messages = [
#     SystemMessage(
#         content="Ты работаешь в отделе закупок государственной организации Росатом и ищешь ответы в нормативно-правовых актах Росатома и ЕОСЗ"
#     )
# ]

# messages = [
#     SystemMessage(
#         content="Ты бот ищущий ответы для отдела закупок государственной организации Росатом согласно ЕДИНОМУ ОТРАСЛЕВОМУ СТАНДАРТУ ЗАКУПОК (ПОЛОЖЕНИЕ О ЗАКУПКЕ) ГОСУДАРСТВЕННОЙ КОРПОРАЦИИ ПО АТОМНОЙ ЭНЕРГИИ «РОСАТОМ» и в нормативно-правовых актах Российской Федерации и пишешь алгоритм и ссылки на законы"
#     )
# ]

messages = [
    SystemMessage(
        content="Ты бот ищущий ответы для отдела закупок государственной организации Росатом ссылаясь на Единый Отраслевой Стандарт Ззакупок (Положение о закупке) Государственной Корпорации По Атомной Энергии «РОСАТОМ» (ЕОСЗ) и нормативно-правовые актаы Российской Федерации и пишешь алгорит"
    )
]



@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник Росатом!", reply_markup=markup)
    if message.text == '👋 Поздороваться':
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=types.ReplyKeyboardRemove()) #ответ бота

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    text = message.text
    messages.append(HumanMessage(content=text))
    res = chat(messages)
    messages.append(res)
    print(res.content)
    bot.send_message(message.chat.id, res.content)

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
