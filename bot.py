import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

SELLER_LINK = "https://t.me/yourusername"

PHOTO_URLS = [
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/photo1.png"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Contact Seller", url=SELLER_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    for photo in PHOTO_URLS:
        await update.message.reply_photo(
            photo=photo,
            caption="Seller ID 👇",
            reply_markup=reply_markup
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
