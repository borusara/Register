import os
from flask import Flask, request
from pyrogram import Client

app = Flask(__name__)

# Get the bot token from environment variable
bot_token = os.environ.get('BOT_TOKEN')

# Get the PostgreSQL database URL from environment variable
database_url = os.environ.get('DATABASE_URL')

# Initialize the Pyrogram client
with Client('my_account', api_id=12345, api_hash='your-api-hash', bot_token=bot_token) as app_client:
    @app.route('/registered', methods=['POST'])
    def handle_registered():
        # Get the Telegram name and username from the request
        telegram_name = request.form['telegram_name']
        telegram_username = request.form['telegram_username']

        # Save the Telegram name and username to the database (using the database_url variable)

        # Construct the message
        message_body = f"Event Registration\nTelegram Name: {telegram_name}\nTelegram Username: {telegram_username}"

        try:
            # Send the message via Twilio

            # Return success response
            return 'Registration successful'
        except Exception as e:
            # Return error response
            return str(e), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
