import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

# Seller info
SELLER_LINK = "https://t.me/yourusername"

# Video IDs from your logs
VIDEO_FILE_IDS = [
    "BAACAgUAAxkBAAMhaZmCyqLQdpv_bvsoQOJKimypUtYAAsogAAKQJ9FUyEMWpJirlss6BA",
    "BAACAgUAAxkBAAMiaZmCyhz1cd-PzoDWnVWJ7Y-BpB8AAssgAAKQJ9FULV-rPg4pp8k6BA",
    "BAACAgUAAxkBAAMjaZmCyn93daXvkLKPi5J_7sZ15wwAAswgAAKQJ9FUBPsGf0W43Uk6BA",
    "BAACAgUAAxkBAAMdaZmCygXT7hJe7ASOfS1VIzz-JFsAAsYgAAKQJ9FUN3WXG6qEq-06BA",
    "BAACAgUAAxkBAAMeaZmCykuCx5DnlzhXmK32FmONtMMAAscgAAKQJ9FUuSfkyRHTVgc6BA",
    "BAACAgUAAxkBAAMfaZmCyuYRujn47K1v5SPYJGTQfWYAAsggAAKQJ9FUwZsDuWm4iqw6BA",
    "BAACAgUAAxkBAAMgaZmCyhyjFZC5cZTAEzP4x_9hznsAAskgAAKQJ9FUK_RVkThxjsQ6BA"
]

# Custom captions for each video/photo
VIDEO_CAPTIONS = [
    "Custom caption for video 1",
    "Custom caption for video 2",
    "Custom caption for video 3",
    "Custom caption for video 4",
    "Custom caption for video 5",
    "Custom caption for video 6",
    "Custom caption for video 7"
]

PHOTO_CAPTIONS = [
    "Custom caption for photo 1"
    # Add more captions if you have more photos
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Button
    keyboard = [[InlineKeyboardButton("Contact Seller", url=SELLER_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send videos
    for video_id, caption in zip(VIDEO_FILE_IDS, VIDEO_CAPTIONS):
        await update.message.reply_video(
            video=video_id,
            caption=f"{SELLER_ID_TEXT}\n{caption}",
            reply_markup=reply_markup
        )

    # Send photos
    for photo_url, caption in zip(PHOTO_URLS, PHOTO_CAPTIONS):
        await update.message.reply_photo(
            photo=photo_url,
            caption=f"{SELLER_ID_TEXT}\n{caption}",
            reply_markup=reply_markup
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
