import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("TOKEN")

# Video and Photo IDs / URLs
VIDEO_FILE_IDS = [
    "BAACAgUAAxkBAAMhaZmCyqLQdpv_bvsoQOJKimypUtYAAsogAAKQJ9FUyEMWpJirlss6BA",
    "BAACAgUAAxkBAAMiaZmCyhz1cd-PzoDWnVWJ7Y-BpB8AAssgAAKQJ9FULV-rPg4pp8k6BA",
    "BAACAgUAAxkBAAMjaZmCyn93daXvkLKPi5J_7sZ15wwAAswgAAKQJ9FUBPsGf0W43Uk6BA",
    "BAACAgUAAxkBAAMdaZmCygXT7hJe7ASOfS1VIzz-JFsAAsYgAAKQJ9FUN3WXG6qEq-06BA",
    "BAACAgUAAxkBAAMeaZmCykuCx5DnlzhXmK32FmONtMMAAscgAAKQJ9FUuSfkyRHTVgc6BA",
    "BAACAgUAAxkBAAMfaZmCyuYRujn47K1v5SPYJGTQfWYAAsggAAKQJ9FUwZsDuWm4iqw6BA",
    "BAACAgUAAxkBAAMgaZmCyhyjFZC5cZTAEzP4x_9hznsAAskgAAKQJ9FUK_RVkThxjsQ6BA"
]

PHOTO_URLS = [
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/photo1.png"
]

# Captions for each video/photo
VIDEO_CAPTIONS = [
    "Caption for video 1",
    "Caption for video 2",
    "Caption for video 3",
    "Caption for video 4",
    "Caption for video 5",
    "Caption for video 6",
    "Caption for video 7"
]

PHOTO_CAPTIONS = [
    "Caption for photo 1"
]

# Seller info
SELLER_LINK = "https://t.me/yourusername"
SELLER_ID_TEXT = "Seller ID: Rahul210806"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Contact Seller", url=SELLER_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send all videos
    for video_id, caption in zip(VIDEO_FILE_IDS, VIDEO_CAPTIONS):
        await update.message.reply_video(
            video=video_id,
            caption=f"{SELLER_ID_TEXT}\n{caption}",
            reply_markup=reply_markup
        )

    # Send all photos
    for photo_url, caption in zip(PHOTO_URLS, PHOTO_CAPTIONS):
        await update.message.reply_photo(
            photo=photo_url,
            caption=f"{SELLER_ID_TEXT}\n{caption}",
            reply_markup=reply_markup
        )

# Optional: to get file IDs in the future
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        print("VIDEO FILE ID:", update.message.video.file_id)
    if update.message.photo:
        print("PHOTO FILE ID:", update.message.photo[-1].file_id)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, get_file_id))

app.run_polling()
