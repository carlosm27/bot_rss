import telegram
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from feed_parser import list_of_links
import os


telegram_bot_token = ""

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


# set up the introductory statement for the bot when the /start command is invoked
def start(update, context):
    chat_id = update.effective_chat.id
    print(chat_id)
    context.bot.send_message(chat_id=chat_id, text="Hello there. Provide any RSS Link")


def return_links(update, context):
    link_info = update.message.text
    print(link_info)
    links = list_of_links(link_info)
    for link in links:
        print(link)

        update.message.reply_text(link)

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text, return_links))


updater.start_webhook(listen="127.0.0.1",
                      port=int(os.environ.get('PORT', 5000)),
                      url_path=telegram_bot_token,
                      webhook_url= "" + telegram_bot_token
                      )    