
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load environment variables from the .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    #  keyboard = [
    #     [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url="https://796b-196-191-156-150.ngrok-free.app/tel-bot/web/"))]
    # ]
    keyboard = [
        # [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url="https://abenuy.com/"))]
        [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url="https://pms-1.vercel.app/"))]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click the button to open the app!", reply_markup=reply_markup)

def main():
    # Create an Application instance
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add the command handler
    application.add_handler(CommandHandler("start", start))
    
    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()

