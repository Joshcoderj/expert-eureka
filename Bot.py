from telegram.ext import Updater, CommandHandler, MessageHandler

TOKEN = 'YOUR_API_TOKEN'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello!')

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    updater = Updater(TOKEN, None)  # Add None as the update_queue argument
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```
