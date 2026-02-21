import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
TOKEN = os.getenv("TOKEN")
# Video and Photo IDs / URLs
VIDEO_FILE_ID = [
    "BAACAgUAAxkBAAMhaZmCyqLQdpv_bvsoQOJKimypUtYAAsogAAKQJ9FUyEMWpJirlss6BA",
    "BAACAgUAAxkBAAMiaZmCyhz1cd-PzoDWnVWJ7Y-BpB8AAssgAAKQJ9FULV-rPg4pp8k6BA",
    "BAACAgUAAxkBAAMjaZmCyn93daXvkLKPi5J_7sZ15wwAAswgAAKQJ9FUBPsGf0W43Uk6BA",
    "BAACAgUAAxkBAAMdaZmCygXT7hJe7ASOfS1VIzz-JFsAAsYgAAKQJ9FUN3WXG6qEq-06BA",
    "BAACAgUAAxkBAAMeaZmCykuCx5DnlzhXmK32FmONtMMAAscgAAKQJ9FUuSfkyRHTVgc6BA",
    "BAACAgUAAxkBAAMfaZmCyuYRujn47K1v5SPYJGTQfWYAAsggAAKQJ9FUwZsDuWm4iqw6BA",
    "BAACAgUAAxkBAAMgaZmCyhyjFZC5cZTAEzP4x_9hznsAAskgAAKQJ9FUK_RVkThxjsQ6BA"
]
PHOTO_URLS = [
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/photo1.png",
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/baby%201-12%20age%20cxxp.jpeg",
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/dark%20web%20hard%20cxxp.jpeg",
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/desi%20cxxp.jpeg",
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/family%20cxxp.jpeg",
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/indian%20mallu%20cxxp.jpeg",
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/indian%20pure%20cxxp.jpeg",
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/pedo%20mom%20son%20cxxp.jpeg",
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/tamil%20mallu%20cxxp.jpeg",
    "https://raw.githubusercontent.com/Rahul210806/telegram-bot/main/teen%2015-16%20age%20cxxp.jpeg"
]
# Seller info
SELLER_LINK = "https://t.me/yourusername"
SELLER_ID_TEXT = "Seller ID: Rahul210806" # Change this to your actual ID
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
