import os
import logging
import download_tiktok
import telegram
import imaging

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
import imaging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
#PORT = int(os.environ.get('PORT', '8443'))
ROOT = os.path.dirname(__file__)
TOKEN = "5210758989:AAEhTnu8t5YrUB45zIJwDzngwesFsjwC4jc"

tiktok_command = 'TikTok'
help_command = 'Help!'


def tiktok(update, context):
    bot = telegram.Bot(token=TOKEN)
    chatid = update.message.chat_id
    video = download_tiktok.download()
    bot.send_video(chatid, video, width=1080, height=1920)
    print('done')

def start(update, context):
    
    buttons = [[telegram.KeyboardButton(tiktok_command)], [telegram.KeyboardButton(help_command)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hi! Choose what to do by enetering command or clicking on the button',
    reply_markup=telegram.ReplyKeyboardMarkup(buttons))


def help_f(update, context):

    context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://preview.redd.it/78h9b4mkurs31.png?auto=webp&s=e163f6ed1796319ff18da0d14782411998442bfc')

def echo(update, context):
    bot = telegram.Bot(token=TOKEN)
    text_for_image = update.message.text
    image = imaging.draw_image(text_for_image)
    chatid = update.message.chat_id
    bot.send_photo(chat_id=chatid, photo=image)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def message_handler(update, context):
    if tiktok_command in update.message.text:
        tiktok(update, context)
        return
    if help_command in update.message.text:
        help_f(update, context)
        return


def main():

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_f))
    dp.add_handler(MessageHandler(Filters.text, message_handler))
    dp.add_handler(CommandHandler('tiktok', tiktok))
    dp.add_handler(MessageHandler(Filters.text, message_handler))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # updater.start_webhook(listen="0.0.0.0",
    #                       port=int(PORT),
    #                       url_path=TOKEN,
    #                       webhook_url="https://kindgaulek-bot.herokuapp.com/" + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()