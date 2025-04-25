from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = '7773629696:AAF93QYGlkVpxku2VxMrPLaQ6NuSqwPhgGg'  # Replace with your real token

RESPONSES = {
    "happy": "That's great! Keep spreading positivity 🌞",
    "sad": "It's okay to feel sad. Try listening to calming music or talk to a friend 💙",
    "angry": "Take deep breaths and try a short walk. It can help you cool down 😌",
    "anxious": "Pause and breathe. Meditation apps like Headspace might help 🧘",
    "lonely": "Reach out to someone you trust or join a community online 🤝",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! How are you feeling today? (e.g., happy, sad, angry)")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.lower()
    reply = RESPONSES.get(user_input, "Thanks for sharing. I'm here for you. Try expressing more or say 'happy', 'sad', 'angry' etc.")
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
