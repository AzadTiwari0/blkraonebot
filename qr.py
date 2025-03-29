from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import requests

# Telegram Bot API Token
TOKEN = "8020235151:AAFW_I9ulGEilVI0WKKVcj2VopNISsh_uzU"

# QR Code API URL
QR_API_URL = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={}"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Send me an image, and I'll generate its QR code!")

async def handle_image(update: Update, context: CallbackContext):
    # Get the file ID of the sent image
    file_id = update.message.photo[-1].file_id
    file = await context.bot.get_file(file_id)
    image_url = file.file_path

    # Generate QR Code
    qr_code_url = QR_API_URL.format(image_url)

    # Send QR Code back to the user
    await update.message.reply_photo(photo=qr_code_url, caption="Here is your QR code!")

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Send me an image, and I'll return its QR code!")

def main():
    app = Application.builder().token(TOKEN).build()

    # Command Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Message Handler for images
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
