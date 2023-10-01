
from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from bruteforce import decrypt

TOKEN: final = '6257474593:AAGma0TAgDVu2F1PKM-kuUqIyQqvqWAQ10s'
BOT_USERNAME: final = '@Encryptron_Bot'
md5: bool = False
file: bool = False

#commands

async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me. press 1 to crack file or 2 to crack password')
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command-just for example!')
def crack_password(text):
    return text

#responses
def handle_response(text: str)->str:
  global file
  global md5

  if '1' == text:
      file = True
      return 'hey there,please give me the file to crack'
  if '2' == text:
      md5 = True
      return 'hey there,please give me the password to crack'
  if md5 == True:
      md5 = False
      return decrypt(text)
  if file:
      file = False
      return decrypt(text)

  return 'wrong value inserted'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str =update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    response: str=handle_response(text)
    print('Bot:',response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
   print(f'update{update} caused error {context.error}')

if __name__=='__main__':
    app =Application.builder().token(TOKEN).build()
    print('starting bot...')

   #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('custom', custom_command))
    #messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    #errors
    app.add_error_handler(error)


    print('polling...')
    app.run_polling(poll_interval=3)
