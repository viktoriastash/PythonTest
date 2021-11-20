import telebot
from ConfigToken import keys, TOKEN
from extensions import ConvertionException, Cryptoconverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help']) 
def help(message: telebot.types.Message):    
  text = 'Добро пожаловать в конвертер, введите команду в следующем формате:\n \
<имя валюты, цену которой он хочет узнать>\n \
<имя валюты, в которой надо узнать цену первой валюты>\n \
<количество первой валюты. Например доллар рубль 1>\n Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])  
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:  
            raise ConvertionException('Неверное количество параметров')

        quote, base, amount = values
        total_base = Cryptoconverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя \n {e}') 
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n {e}') 
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()
