import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("TOKEN")

# Video and Photo IDs / URLs
VIDEO_FILE_ID = "BAACAgUAAxkBAAMQaZl_LRw1LGM3be_KKIKh7cFSiSsAArogAAKQJ9FUFPmRTgzzsws6BA"
PHOTO_URLS = [
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/photo1.png"
]

# Seller info
SELLER_LINK = "https://t.me/yourusername"
SELLER_ID_TEXT = "Seller ID: Rahul210806"  # Change this to your actual ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create the button
    keyboard = [[InlineKeyboardButton("Contact Seller", url=SELLER_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send video
    await update.message.reply_video(
        video=VIDEO_FILE_ID,
        caption=f"{SELLER_ID_TEXT}\nCustom text for the video",
        reply_markup=reply_markup
    )

    # Send photos
    for photo in PHOTO_URLS:
        await update.message.reply_photo(
            photo=photo,
            caption=f"{SELLER_ID_TEXT}\nCustom text for the photo",
            reply_markup=reply_markup
        )

# Optional: to get file IDs for future uploads
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        print("VIDEO FILE ID:", update.message.video.file_id)
    if update.message.photo:
        print("PHOTO FILE ID:", update.message.photo[-1].file_id)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, get_file_id))

app.run_polling()
