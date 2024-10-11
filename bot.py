import logging
import telegram
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

app = ApplicationBuilder().token("7566081485:AAESjUfs31Aa3zAke2GIN04fr6Ao-Qe3-uM").build()

async def start(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id = update.effective_chat.id, text = f"""
      nna NAYINTEEEEEMWOLE MYRE THENDINCHETTE PANDIKARIMBARA""")
    print(update.effective_chat.username, "\n\n\n")


start_handler = CommandHandler("start", start)
app.add_handler(start_handler)

app.run_polling()
