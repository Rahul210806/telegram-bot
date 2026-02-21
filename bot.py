import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

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

# 🔥 NEW FUNCTION — THIS WILL PRINT FILE IDs
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        print("VIDEO FILE ID:", update.message.video.file_id)

    if update.message.photo:
        print("PHOTO FILE ID:", update.message.photo[-1].file_id)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, get_file_id))  # 🔥 added

app.run_polling()
