
# import os
# from dotenv import load_dotenv
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# # Load environment variables from the .env file
# load_dotenv()
# BOT_TOKEN = os.getenv("BOT_TOKEN")

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

#     #  keyboard = [
#     #     [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url="https://796b-196-191-156-150.ngrok-free.app/tel-bot/web/"))]
#     # ]
#     keyboard = [
#         # [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url="https://abenuy.com/"))]
#         [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url="https://evant4forum.netlify.app/"))]
#     ]
    
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text("Click the button to open the app!", reply_markup=reply_markup)

# def main():
#     # Create an Application instance
#     application = ApplicationBuilder().token(BOT_TOKEN).build()

#     # Add the command handler
#     application.add_handler(CommandHandler("start", start))
    
#     # Start the bot
#     application.run_polling()

# if __name__ == '__main__':
#     main()




import os
import asyncio
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask

# Load environment variables from the .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create a simple Flask app to serve the web service
app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url="https://evant4forum.netlify.app/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click the button to open the app!", reply_markup=reply_markup)

async def main():
    # Create an Application instance
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add the command handler
    application.add_handler(CommandHandler("start", start))

    # Run the bot with long polling
    await application.run_polling()

# Add a simple route to bind to a port (Render expects web services to bind to a port)
@app.route('/')
def index():
    return "Telegram bot is running!"

if __name__ == '__main__':
    # Start the Flask app and also run the bot in the background using asyncio
    from threading import Thread

    # Run the Flask app in a separate thread
    def run_flask():
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))

    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Run the Telegram bot in the main thread with asyncio
    asyncio.run(main())
