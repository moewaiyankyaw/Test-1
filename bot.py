import logging
import requests
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the API endpoint and headers
API_URL = "https://api.paxsenix.biz.id/ai/deepseek"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-paxsenix-45-dpDQ7eXYt8esnLxDyjFLV0X1XOWWrV218mhTqMEcdJW1J"
}

# Function to handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    response = requests.get(API_URL, headers=HEADERS, params={"text": user_message, "thinking_enabled": "false", "search_enabled": "false"})
    
    if response.ok:
        data = response.json()
        reply_message = data.get("message", "Sorry, I didn't understand that.")
        await update.message.reply_text(reply_message)
    else:
        await update.message.reply_text("Error communicating with the API.")

# Main function to start the bot
async def main() -> None:
    # Create the Application and pass it your bot's token
    application = ApplicationBuilder().token("8430701285:AAEp60qHh8XMncchveg5_0EKEABflNEO2nc").build()

    # Register handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    await application.run_polling()

if __name__ == '__main__':
    # Use the existing event loop
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except RuntimeError as e:
        if str(e) == 'This event loop is already running':
            asyncio.run(main())
