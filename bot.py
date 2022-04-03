import os
import logging
import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

import imaging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
PORT = int(os.environ.get('PORT', 5000))
ROOT = os.path.dirname(__file__)

def start(update, context):
    
    update.message.reply_text('Hi! Send me text, which has to be put on the image')

def help(update, context):
    
    update.message.reply_text('Help!')

def echo(update, context):
    bot = telegram.Bot(token="5210758989:AAEhTnu8t5YrUB45zIJwDzngwesFsjwC4jc")
    text_for_image = update.message.text
    imaging.draw_image(text_for_image)
    chatid = update.message.chat_id
    bot.send_photo(chat_id=chatid, photo=open('Telegram-quote-bot//1.jpg', 'rb'))

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    TOKEN = "5210758989:AAEhTnu8t5YrUB45zIJwDzngwesFsjwC4jc"

    updater = Updater("5210758989:AAEhTnu8t5YrUB45zIJwDzngwesFsjwC4jc", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://kindgaulek-bot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()