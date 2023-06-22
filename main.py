# 1. Приветствие
# 2. Инструкция игры
# 3. Генерация случайной карты
# 4. Вопрос игроку: масть красная или черная
# 5. Ответ игрока
# 6. Сравнение
# 6.1 Если игрок угадывает - программа его "хвалит"
# 6.2 Если игрок не угадывает - программа дает верный ответ
# from random import choice

# print("Добро пожаловать!") #1
# print("Угадай цвет масти, выбранной мной карты") #2

# random_card_number = choice(CARD_NUMBER)
# random_card_suit = choice(CARD_SUIT)

#  #3

# player_answer = input("Введите цвет масти: ").lower() #4-5

# # Если ответ игрока "черная", масть - пики или крести, то ответ верный
# # Если ответ игрока "красная", масть - буби или черви, то ответ верный
# # В любом другом варианте, ответ неверный

# if player_answer == 'черная' and random_card_suit in ['Пики','Крести']:
#   print("Ответ верный! Выбранной мной картой была: " + random_card)
# elif player_answer == 'красная' and random_card_suit in ['Буби','Черви']:
#   print("Ответ верный! Выбранной мной картой была: " + random_card)
# else:
#   print("Ответ неверный! Выбранной мной картой была: " + random_card)

import telebot
from random import choice

CARD_NUMBER = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']

CARD_SUIT = ['Черви', 'Буби', 'Пики', 'Крести']

SECRET_KEY = "D********************************************V"

bot = telebot.TeleBot(SECRET_KEY)

@bot.message_handler(commands=['start'])

def start(message):
  keyboard = telebot.types.ReplyKeyboardMarkup()
  red_button = telebot.types.KeyboardButton("🟥")
  black_button = telebot.types.KeyboardButton("⬛️")
  keyboard.row(red_button)
  keyboard.row(black_button)
  bot.send_message(message.chat.id, 
                   "Угадай цвет масти, выбранной мной карты: 🟥 или ⬛️",
                   reply_markup=keyboard)

  bot.register_next_step_handler(message, answer_card)

def answer_card(message):
  random_card_number, random_card_suit = generate_random_card()
  random_card = random_card_number + ' ' + random_card_suit
  if message.text == "🟥" and random_card_suit in ["Черви", "Буби"]: bot.send_message(message.chat.id, "Верно! Выбранной мной картой была: " + random_card)
  elif message.text == "⬛️" and random_card_suit in ["Пики", "Крести"]: bot.send_message(message.chat.id, "Верно! Выбранной мной картой была: " + random_card)
  else: bot.send_message (message.chat.id, "Неверно! Выбранной мной картой была: " + random_card)

  start(message)

def generate_random_card():
  random_card_number = choice(CARD_NUMBER)
  random_card_suit = choice(CARD_SUIT)
  return random_card_number, random_card_suit

bot.infinity_polling()