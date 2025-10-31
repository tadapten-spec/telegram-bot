from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8375956137:AAGbMM3iWODAnURdlwnsHkKXYHkEbokI7Js"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🎬 Ek deewane ki diwaniyat")],
        [KeyboardButton("🔥 Bahubali 3")],
        [KeyboardButton("💥 Thamma")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🎥 Welcome to Movie Bot!\n\nChoose a movie below 👇",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text in ["🎬 Ek deewane ki diwaniyat", "🔥 Bahubali 3", "💥 Thamma"]:
        await update.message.reply_text(
            "🎬 Watch full movie here 👉 [Click Here](https://t.me/moviezone110)",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text("Please choose one of the movies from the list 👇")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
