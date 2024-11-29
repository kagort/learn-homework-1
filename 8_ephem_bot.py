import ephem
import logging
import datetime
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')


async def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Введи название планеты на английском в таком формате: /planet Mars')
    print('Вызван /start')
    print(update)

#дальше - GPT- coding, но осмысленный :) И вцелом приглось структуру немного поменять, т.к библиотека Python-telegram изменилась. Код из видео не работал
async def planet_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        # Разделяем команду и название планеты
        command, planet_name = user_text.split(maxsplit=1)
    except ValueError:
        await update.message.reply_text("Пожалуйста, введите название планеты после команды /planet.")
        return

    # Приводим название планеты к правильному формату
    planet_name_capitalized = planet_name.capitalize()

    # Проверяем, существует ли планета в модуле ephem
    if hasattr(ephem, planet_name_capitalized):
        # Получаем текущую дату
        date = datetime.datetime.now()
        # Создаём объект планеты
        planet = getattr(ephem, planet_name_capitalized)(date)
        # Определяем созвездие, в котором находится планета
        constellation = ephem.constellation(planet)
        # Отправляем ответ пользователю
        await update.message.reply_text(f"Планета {planet_name_capitalized} сейчас находится в созвездии {constellation[1]}.")
    else:
        await update.message.reply_text("Извините, я не знаю такую планету. Пожалуйста, проверьте название и попробуйте снова.")


async def talk_to_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(text)
    await update.message.reply_text(text)

def main():
    mybot = ApplicationBuilder().token('7054240709:AAGrU_8F5UD5GO1nxgxDXBamrVFjKfbBGNs').build()


    start_handler = CommandHandler('start', greet_user)
    mybot.add_handler(start_handler)


    planet_handler = CommandHandler('planet', planet_info)
    mybot.add_handler(planet_handler)


    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, talk_to_me)
    mybot.add_handler(message_handler)

    logging.info('Бот в деле...')
    mybot.run_polling()

if __name__ == '__main__':
    main()
