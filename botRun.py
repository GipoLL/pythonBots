import telebot
import openpyxl

wb_val = openpyxl.load_workbook(filename='time.xlsx', data_only=True)
sheet_val = wb_val['Лист1']
L6_val = sheet_val['L6'].value

bot = telebot.TeleBot('1315612054:AAGkqcWwMNwO-9hwfTGI2vYCIKfO-9NETaQ')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, L6_val)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Сегодня', 'Неделя')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == "Расписание":
        bot.send_message(message.chat.id, 'Сегодня или вообще?', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Сегодня':
        bot.send_message(message.chat.id, 'Хорошо, сегодня') # Ф-ция для сегодняшнего дня
    elif message.text.lower() == 'Неделя':
        bot.send_message(message.chat.id, 'Хорошо, неделя') # Ф-ция для недели



bot.polling()