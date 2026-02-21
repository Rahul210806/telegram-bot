import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

SELLER_LINK = "https://t.me/yourusername"

PHOTO_URLS = [
    "PHOTO_LINK_1",
    "PHOTO_LINK_2",
    "PHOTO_LINK_3",
    "PHOTO_LINK_4",
    "PHOTO_LINK_5",
    "PHOTO_LINK_6",
    "PHOTO_LINK_7",
    "PHOTO_LINK_8",
    "PHOTO_LINK_9",
    "PHOTO_LINK_10",
    "PHOTO_LINK_11",
    "PHOTO_LINK_12",
    "PHOTO_LINK_13",
    "PHOTO_LINK_14",
    "PHOTO_LINK_15",
    "PHOTO_LINK_16",
    "PHOTO_LINK_17",
    "PHOTO_LINK_18",
    "PHOTO_LINK_19",
    "PHOTO_LINK_20"
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
