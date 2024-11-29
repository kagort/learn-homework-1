import logging
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
logging.basicConfig(filename = 'bot.log', level=logging.INFO)

async def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет!')
    print('Вызван/start')
    print(1/0)
    print(update)


def main():
    mybot = ApplicationBuilder().token('7054240709:AAGrU_8F5UD5GO1nxgxDXBamrVFjKfbBGNs').build()


    start_handler = CommandHandler('start', greet_user)
    mybot.add_handler(start_handler)

    logging.info('Bot run')
    mybot.run_polling()

main()


