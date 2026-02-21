import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("TOKEN")

# Video file IDs
VIDEO_FILE_ID = [
    "BAACAgUAAxkBAAMhaZmCyqLQdpv_bvsoQOJKimypUtYAAsogAAKQJ9FUyEMWpJirlss6BA",
    "BAACAgUAAxkBAAMiaZmCyhz1cd-PzoDWnVWJ7Y-BpB8AAssgAAKQJ9FULV-rPg4pp8k6BA",
    "BAACAgUAAxkBAAMjaZmCyn93daXvkLKPi5J_7sZ15wwAAswgAAKQJ9FUBPsGf0W43Uk6BA",
    "BAACAgUAAxkBAAMdaZmCygXT7hJe7ASOfS1VIzz-JFsAAsYgAAKQJ9FUN3WXG6qEq-06BA",
    "BAACAgUAAxkBAAMeaZmCykuCx5DnlzhXmK32FmONtMMAAscgAAKQJ9FUuSfkyRHTVgc6BA",
    "BAACAgUAAxkBAAMfaZmCyuYRujn47K1v5SPYJGTQfWYAAsggAAKQJ9FUwZsDuWm4iqw6BA",
    "BAACAgUAAxkBAAMgaZmCyhyjFZC5cZTAEzP4x_9hznsAAskgAAKQJ9FUK_RVkThxjsQ6BA"
]

# Unique caption for each video
VIDEO_CAPTIONS = [
    "Graceful classical dance in vibrant attire",
    "Elegant pose with traditional jewelry",
    "Festive celebration full of joy and color",
    "Beautiful ethnic wear showcase",
    "Charming smile in soft evening light",
    "Timeless cultural elegance captured",
    "Vibrant energy of traditional performance"
]

# Photo URLs (only allowed ones)
PHOTO_URLS = [
    "https://github.com/Rahul210806/telegram-bot/raw/main/baby%201-12%20age%20cxxp.jpeg",
    "https://github.com/Rahul210806/telegram-bot/raw/main/teen%2015-16%20age%20cxxp.jpeg",
    "https://github.com/Rahul210806/telegram-bot/raw/main/family%20cxxp.jpeg",
    "https://github.com/Rahul210806/telegram-bot/raw/main/dark%20web%20hard%20cxxp.jpeg",
    "https://github.com/Rahul210806/telegram-bot/raw/main/desi%20cxxp.jpeg",
    "https://github.com/Rahul210806/telegram-bot/raw/main/indian%20mallu%20cxxp.jpeg"
]

# Unique caption for each photo
PHOTO_CAPTIONS = [
    "Serene portrait in natural surroundings",
    "Warm family moment full of love",
    "Authentic desi style and grace",
    "South Indian beauty and tradition"
]

# Seller contact link (button only – no text in media captions)
SELLER_LINK = "https://t.me/yourusername"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create contact button
    keyboard = [[InlineKeyboardButton("Contact Seller", url=SELLER_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
   
    # Send videos – each with its own caption
    for video_id, caption in zip(VIDEO_FILE_ID, VIDEO_CAPTIONS):
        await update.message.reply_video(
            video=video_id,
            caption=caption,
            reply_markup=reply_markup
        )
   
    # Send photos – each with its own caption
    for photo_url, caption in zip(PHOTO_URLS, PHOTO_CAPTIONS):
        await update.message.reply_photo(
            photo=photo_url,
            caption=caption,
            reply_markup=reply_markup
        )

# Helper to print file IDs when you forward media to the bot
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        print("VIDEO FILE ID:", update.message.video.file_id)
    if update.message.photo:
        print("PHOTO FILE ID:", update.message.photo[-1].file_id)

# Start the bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, get_file_id))
app.run_polling()
