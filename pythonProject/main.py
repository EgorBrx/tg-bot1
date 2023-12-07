from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from telegram.ext import filters
import random

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def Chance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("команда Chance")
    await update.message.reply_text(f'Твои шансы сдать матан: {random.randrange(0,101)}%')
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    message = update.message
    user = update.effective_user

    await context.bot.send_message(chat_id=-1002133208960, text=user.username+": " + message.text)
    if user.username == "Fulcrum" and random.random() < 0.1:
        await context.bot.send_message(chat_id=message.chat.id, text="ты лох")



app = ApplicationBuilder().token("6780754279:AAG16Ox4MRzfJkP1cpFpPfOeDVuDs3NJUcw").build()
app.add_handler(CommandHandler("matan", Chance))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT, echo))


app.run_polling()