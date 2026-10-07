from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import threading
import os

app = Flask(__name__)
BOT_TOKEN = "8561145973:AAGuqkm0PhDxWEobFMjPTVwp2fuQdBz3IQU"

@app.route('/')
def home():
    return "Бот работает! ✅"

async def start(update: Update, context):
    await update.message.reply_text("Привет! Я работаю! 🎉")

async def echo(update: Update, context):
    await update.message.reply_text(f"Ты написал: {update.message.text}")

def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
