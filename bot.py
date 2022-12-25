import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
from emoji import emojize
import config


winking_face_emoji = emojize(':winking_face:')
grinning_face_emoji = emojize(':grinning_face:')
smiling_tear_face_emoji = emojize(':smiling_face_with_tear:')

url1 = 'http://fapl.ru'
r1 = requests.get(url1)
soup1 = BeautifulSoup(r1.content, 'html.parser')
epl_table = soup1.find_all('div', class_='block table')[0].text
epl_matches = soup1.find_all('table', class_='positions matches')[1].text

url2 = 'https://www.sports.ru/la-liga/table/'
r2 = requests.get(url2)
soup2 = BeautifulSoup(r2.content, 'html.parser')
laliga_table = soup2.find_all('div', class_='stat mB6')[0].text

url3 = 'https://www.sports.ru/la-liga/calendar/'
r3 = requests.get(url3)
soup3 = BeautifulSoup(r3.content, 'html.parser')
laliga_matches = soup3.find_all('div', class_='stat mB15')[0].text

url4 = 'https://www.sports.ru/seria-a/table/'
r4 = requests.get(url4)
soup4 = BeautifulSoup(r4.content, 'html.parser')
seria_a_table = soup4.find_all('div', class_='stat mB6')[0].text

url5 = 'https://www.sports.ru/seria-a/calendar/'
r5 = requests.get(url5)
soup5 = BeautifulSoup(r5.content, 'html.parser')
seria_a_matches = soup5.find_all('div', class_='stat mB15')[0].text

url6 = 'https://www.sports.ru/bundesliga/table/'
r6 = requests.get(url6)
soup6 = BeautifulSoup(r6.content, 'html.parser')
bundesliga_table = soup6.find_all('div', class_='stat mB6')[0].text

url7 = 'https://www.sports.ru/bundesliga/calendar/'
r7 = requests.get(url7)
soup7 = BeautifulSoup(r7.content, 'html.parser')
bundesliga_matches = soup7.find_all('div', class_='stat mB15')[0].text

url8 = 'https://www.sports.ru/ligue-1/table/'
r8 = requests.get(url8)
soup8 = BeautifulSoup(r8.content, 'html.parser')
ligue_1_table = soup8.find_all('div', class_='stat mB6')[0].text

url9 = 'https://www.sports.ru/ligue-1/calendar/'
r9 = requests.get(url9)
soup9 = BeautifulSoup(r9.content, 'html.parser')
ligue_1_matches = soup9.find_all('div', class_='stat mB15')[0].text

url10 = 'https://terrikon.com/champions-league'
r10 = requests.get(url10)
soup10 = BeautifulSoup(r10.content, 'html.parser')
ucl = soup10.find_all('div', class_='groups-info')[0].text

url11 = 'https://terrikon.com/europa-league'
r11 = requests.get(url11)
soup11 = BeautifulSoup(r11.content, 'html.parser')
uel = soup11.find_all('div', class_='groups-info')[0].text

url12 = 'https://terrikon.com/conference-league'
r12 = requests.get(url12)
soup12 = BeautifulSoup(r12.content, 'html.parser')
conference_league = soup12.find_all('div', class_='groups-info')[0].text


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Лига Чемпионов')
    button2 = types.KeyboardButton('Лига Европы')
    button3 = types.KeyboardButton('Лига Конференций')
    button4 = types.KeyboardButton('АПЛ')
    button5 = types.KeyboardButton('ЛаЛига')
    button6 = types.KeyboardButton('Серия А')
    button7 = types.KeyboardButton('Бундеслига')
    button8 = types.KeyboardButton('Лига 1')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
    bot.send_message(message.chat.id, f'Привет! Выбери нужную тебе лигу {winking_face_emoji}', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lig_buttons(message):
    if message.text == 'Лига Чемпионов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Ближайшие матчи Лиги Чемпионов')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, 'Лига Чемпионов', reply_markup=markup)

    elif message.text == 'Ближайшие матчи Лиги Чемпионов':
        bot.send_message(message.chat.id, f'Ближайшие матчи: {ucl}')

    elif message.text == 'Лига Европы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Ближайшие матчи Лиги Европы')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, 'Лига Европы', reply_markup=markup)

    elif message.text == 'Ближайшие матчи Лиги Европы':
        bot.send_message(message.chat.id, f'Ближайшие матчи: {uel}')

    elif message.text == 'Лига Конференций':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Ближайшие матчи Лиги Конференций')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, 'Лига Конференций', reply_markup=markup)

    elif message.text == 'Ближайшие матчи Лиги Конференций':
        bot.send_message(message.chat.id, f'Ближайшие матчи: {conference_league}')
        
    elif message.text == 'АПЛ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Ближайшие матчи АПЛ')
        button2 = types.KeyboardButton('Таблица АПЛ')
        button3 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'АПЛ', reply_markup=markup)

    elif message.text == 'Ближайшие матчи АПЛ':
        bot.send_message(message.chat.id, f'Ближайшие матчи: {epl_matches}')

    elif message.text == 'Таблица АПЛ':
        bot.send_message(message.chat.id, epl_table)

    elif message.text == 'ЛаЛига':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Ближайшие матчи ЛаЛиги')
        button2 = types.KeyboardButton('Таблица ЛаЛиги')
        button3 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'ЛаЛига', reply_markup=markup)

    elif message.text == 'Ближайшие матчи ЛаЛиги':
        bot.send_message(message.chat.id, f'Ближайшие матчи: {laliga_matches}')

    elif message.text == 'Таблица ЛаЛиги':
        bot.send_message(message.chat.id, f'Таблица: {laliga_table}')

    elif message.text == 'Серия А':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Ближайшие матчи Серии А')
        button2 = types.KeyboardButton('Таблица Серии А')
        button3 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'Серия А', reply_markup=markup)

    elif message.text == 'Ближайшие матчи Серии А':
        bot.send_message(message.chat.id, f'Ближайшие матчи: {seria_a_matches}')

    elif message.text == 'Таблица Серии А':
        bot.send_message(message.chat.id, f'Таблица: {seria_a_table}')

    elif message.text == 'Бундеслига':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Ближайшие матчи Бундеслиги')
        button2 = types.KeyboardButton('Таблица Бундеслиги')
        button3 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'Бундеслига', reply_markup=markup)

    elif message.text == 'Ближайшие матчи Бундеслиги':
        bot.send_message(message.chat.id, f'Ближайшие матчи: {bundesliga_matches}')

    elif message.text == 'Таблица Бундеслиги':
        bot.send_message(message.chat.id, f'Таблица: {bundesliga_table}')

    elif message.text == 'Лига 1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Ближайшие матчи Лиги 1')
        button2 = types.KeyboardButton('Таблица Лиги 1')
        button3 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'Лига 1', reply_markup=markup)

    elif message.text == 'Ближайшие матчи Лиги 1':
        bot.send_message(message.chat.id, f'Ближайшие матчи: {ligue_1_matches}')

    elif message.text == 'Таблица Лиги 1':
        bot.send_message(message.chat.id, f'Таблица: {ligue_1_table}')

    elif message.text == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Лига Чемпионов')
        button2 = types.KeyboardButton('Лига Европы')
        button3 = types.KeyboardButton('Лига Конференций')
        button4 = types.KeyboardButton('АПЛ')
        button5 = types.KeyboardButton('ЛаЛига')
        button6 = types.KeyboardButton('Серия А')
        button7 = types.KeyboardButton('Бундеслига')
        button8 = types.KeyboardButton('Лига 1')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
        bot.send_message(message.chat.id, f'Вы вернулись в главное меню {grinning_face_emoji}', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, f'Такой команды не существует!{smiling_tear_face_emoji}')


bot.polling(none_stop=True)
