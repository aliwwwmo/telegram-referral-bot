import telebot
from telebot import types
import mysql.connector

cnx = mysql.connector.connect(user = 'youtube' , password = '1234', host= '127.0.0.1', database = 'test1')
cursor = cnx.cursor()

bot = telebot.TeleBot('6805122603:AAE6ZCE0lzVxoSrp8GsOkIEH5hyNHXlSmjc')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    cursor.execute("select user_id from rfl where user_id = %s ",(user_id,))
    cheak_user = cursor.fetchone()
    if cheak_user:
        bot.send_message(user_id , 'شما از قبل داخل این ربات عضو بودید')
    else:
        text = message.text
        if len(text)>7:
            textsplit = text.split(' ')
            inviteid = textsplit[1]
            cursor.execute('select count from rfl where user_id =%s',(inviteid,))
            result = cursor.fetchone()
            if result :
                count = result[0]+1
                cursor.execute('update rfl set count = %s where user_id = %s' , (count,inviteid,))
        cursor.execute('insert into rfl (user_id , count ) values  (%s,%s)',(user_id,0))
        bot.send_message(user_id,'اطلاعات شما وارد دیتابیس شد')
        cnx.commit()
    markup = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton('زیرمجموعه گیری')
    markup.row(btn)
    bot.reply_to(message,'یکی از دکمه های ریر رو انتخاب کن', reply_markup=markup)
@bot.message_handler(func=lambda msg:True)
def echo(message):
    if message.text == 'زیرمجموعه گیری':
        user_id = message.chat.id
        cursor.execute('select count from rfl where user_id =%s', (user_id,))
        result = cursor.fetchone()
        if result:
            if result[0]>=5:
                bot.send_message(user_id ,'این پکیج شماست')
            else:
                bot.send_message(message.chat.id , 'برای استفاده ار این دکمه شما باید 5 نفر رو اضافه کنید تعداد افراد اضافع شده : %s' %(result[0]))
                bot.send_message(message.chat.id , 'http://telegram.me/Testt7ttttbot?start=%s' %(user_id))


bot.polling()
