from config import token, bot_token
import openai
import telebot

bot = telebot.TeleBot(bot_token)
openai.api_key = token


@bot.message_handler(commands=["start"])
def handle_message(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}! Я помогу тебе чем смогу! Напиши вопрос и я пришлю на него ответ. Желательно пиши вопрос на английском языке. Так ответ будет наиболее точным. Удачи!")


@bot.message_handler(content_types=["text"])
def handle_message(message): # Название функции не играет никакой роли
    try:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        )
        bot.send_message(message.chat.id, response["choices"][0]['text'])
    except IndexError:
        bot.send_message(message.chat.id, "Не получилось, попробуйте еще")


if __name__ == '__main__':
     bot.infinity_polling()