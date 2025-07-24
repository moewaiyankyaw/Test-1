import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the API endpoint and headers
API_URL = "https://api.paxsenix.biz.id/ai/deepseek"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-paxsenix-45-dpDQ7eXYt8esnLxDyjFLV0X1XOWWrV218mhTqMEcdJW1J"
}

# Function to handle messages
def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = requests.get(API_URL, headers=HEADERS, params={"text": user_message, "thinking_enabled": "false", "search_enabled": "false"})
    
    if response.ok:
        data = response.json()
        reply_message = data.get("message", "Sorry, I didn't understand that.")
        update.message.reply_text(reply_message)
    else:
        update.message.reply_text("Error communicating with the API.")

# Main function to start the bot
def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater("8430701285:AAEp60qHh8XMncchveg5_0EKEABflNEO2nc")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
