from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from asyncio import sleep
from telegram_token import token as telegram_token


async def start(update: Update, context):
    await update.message.reply_text("Спаааааам")


async def repeat(update: Update, context):
    if len(context.args) < 2:
        await update.message.reply_text("хуйня")
        return

    try:
        repeat_count = int(context.args[0])
    except ValueError:
        await update.message.reply_text("хуйня х2")
        return

    message = " ".join(context.args[1:])

    for i in range(repeat_count):
        await update.message.reply_text(message)
        await sleep(0.2)


async def repeatInOne(update: Update, context):
    if len(context.args) < 2:
        await update.message.reply_text("хуйня")
        return

    try:
        repeat_count = int(context.args[0])
    except ValueError:
        await update.message.reply_text("хуйня х2")
        return

    message = " ".join(context.args[1:])

    repeat_message = message * repeat_count
    await update.message.reply_text(repeat_message)


if __name__ == '__main__':
    app = ApplicationBuilder().token(telegram_token).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(CommandHandler("repeat", repeat))

    app.add_handler(CommandHandler("repeatone", repeatInOne))

    print("бот")
    app.run_polling()
