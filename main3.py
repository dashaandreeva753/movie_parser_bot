import telebot
import movie_parser

TOKEN = '7357061420:AAEjTNJinBADrD0KcPXBLyu8oByL2vjl3GQ'
bot = telebot.TeleBot(TOKEN)


# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Добро пожаловать в справочный бот по фильмам!")


@bot.message_handler(func=lambda message: True)
def response(message):
    movie_title = message.text
    print(type(movie_title))
    movie_url = movie_parser.get_movie_url(movie_title)
    print(movie_url)

    if movie_url:
        # bot.send_message(message, f"url найденного фильма: {movie_url}")
        movie_info = movie_parser.get_movie_info(movie_url)
        print(movie_info)
        if movie_info:
            title, description = movie_info['title'], movie_info['description']
            print(title, description)
            response_text = f"Название: {title}\nОписание: {description}"
            bot.send_message(message.chat.id, response_text)
        else:
            response_text = "Не удалось получить информацию о фильме"
            bot.send_message(message.chat.id, response_text)
    else:
        response_text = "Ошибка. Попробуйте позже"
        bot.send_message(message.chat.id, response_text)


if __name__ == "__main__":
    bot.polling(non_stop=True)
