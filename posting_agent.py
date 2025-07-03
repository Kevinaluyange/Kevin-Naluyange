#Agent to automate posting on telegram channel
#Import necessary libraries
import requests
import time
import os
from dotenv import load_dotenv 

#Load secrets from .env file
load_dotenv()  # Load environment variables from .env file

# Define a class to handle Telegram bot operations
class TelegramBotAgent:
    def __init__(self, bot_token, channel_username):
        self.bot_token = bot_token
        self.channel_username = channel_username
        self.api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

    def create_post(self, message):
        payload = {
            'chat_id': self.channel_username,
            'text': message,
            'parse_mode': 'HTML'
        }

        try:
            # Send a POST request to the Telegram API
            response = requests.post(self.api_url, json=payload)
            print(f"Response: {response.text}")
            response.raise_for_status()  # Raise error if status is not 200
            return response.json()       # Return the JSON response
        except requests.exceptions.RequestException as e:
            # Handle any errors that occur during the request
            print(f"[ERROR] Failed to send message: {e}")
            return None

    def automate_posts(self, messages, delay=10):
        for msg in messages:
            result = self.create_post(msg)
            if result:
                print(f"[SUCCESS] Posted: {msg}")
            time.sleep(delay)


#Main block: runs when the script is executed
if __name__ == "__main__":
    # Get bot token and channel username from environment variables
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    channel_username = os.getenv("TELEGRAM_CHANNEL_USERNAME")

    #Ensue that bot token and channel username are provided
    if not bot_token or not channel_username:
        print("[ERROR] Bot token or channel username is missing in the .env file")
    else:
        # Create an instance of the TelegramBotAgent
        agent = TelegramBotAgent(bot_token, channel_username)

        # Define a list of messages to post
        posts = [
            "Welcome to our channel!",
            "Stay updated with our latest posts!",
            "This message was posted by an AI bot!",
            "What topics would you like us to cover next?",
            "Reply with your suggestions!"
        ]
        # Automate posting with a delay of 5 seconds between each post
        agent.automate_posts(posts, delay=5)