from bot.bot import Bot
from bot.handler import MessageHandler

TOKEN = "001.3154942192.1068193318:1011019675"
Bot_id = 1011019675
Bot_Name = "Voronezh36TeaBestbot"
api_url_base="https://api.icq.net/bot/v1"

bot = Bot(token=TOKEN)

def message_cb(bot, event):
    bot.send_text(chat_id=event.from_chat, text=event.text)

bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.start_polling()
bot.idle()

