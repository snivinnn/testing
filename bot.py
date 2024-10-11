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
        Hey {update.effective_chat.first_name}! This is a bot being tested by @sniv1n
/help for more details!
        """)
    print(update.effective_chat.username, "\n\n\n")
async def help(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(
	chat_id= update.effective_chat.id, text=
	"""/id - sends your user id.
/info - gives user info.
	More commands coming soon :)""")

async def idd(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(
	chat_id= update.effective_chat.id, text=
	f"Your user ID: {update.effective_chat.id}")
	print(update.effective_chat.username)


async def info(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(
	chat_id= update.effective_chat.id, text=
	f"""
	User info:
	user ID: {update.effective_chat.id}
	First Name: {update.effective_chat.first_name}
	Username: @{update.effective_chat.username}
	""")
	print(update.effective_chat.username)
	
start_handler = CommandHandler("start", start)
help_handler = CommandHandler('help', help)
idd_handler = CommandHandler('id', idd)
info_handler = CommandHandler('info', info)


app.add_handler(start_handler)
app.add_handler(help_handler)
app.add_handler(idd_handler)
app.add_handler(info_handler)


app.run_polling()
