import telebot
from game import Game
from telebot import types

TOKEN = '6485833209:AAFDlRcOX-4kp8CoJOAFGNnEWtq5w3gTGAs'
bot = telebot.TeleBot(TOKEN)
game = Game()
player_location = {}
def send_location(chat_id, location):
    location_text = game.get_location_text(location)
    options = game.get_location_options(location)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)

    for option in options.values():
        btn = types.KeyboardButton(option)
        markup.add(btn)

    bot.send_message(chat_id, location_text, reply_markup=markup)
    player_location[chat_id] = location  # Update the player's current location

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Добро пожаловать в игру!")
    player_location[message.chat.id] = 'corridor'
    send_location(message.chat.id, 'corridor')

# ... (send_location function remains the same)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_choice = message.text
    chat_id = message.chat.id

    current_location = player_location.get(chat_id)

    if current_location:
        next_location, next_text = game.next_location(current_location, user_choice)
        print(next_location, '-', next_text)
        if next_location:
            if next_location != "game_over":
                send_location(chat_id, next_location)
                player_location[chat_id] = next_location
                if "победа" in next_text.lower():
                    bot.send_message(chat_id, "Правильный выбор,с победой!Если хотите,можете пройти еще раз и узнать другие исходы:/start")
                elif "поражение" in next_text.lower():
                    bot.send_message(chat_id, "Вы проиграли,но ничего страшного,попробуй пройти еще раз)/start")
            else:
                bot.send_message(chat_id, next_text)  # Send the game-over message
        else:
            bot.send_message(chat_id, "Что-то пошло не так, начните игру заново.")

bot.polling()
