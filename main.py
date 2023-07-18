from pyrogram import Client, filters
from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Retrieve environment variables
bot_token = os.environ.get('BOT_TOKEN')
database_url = os.environ.get('DATABASE_URL')
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

# Connect to PostgreSQL database
conn = psycopg2.connect(database_url)
cur = conn.cursor()

# Create a Pyrogram client
client = Client("my_account", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        telegram_name = request.form['telegram_name']
        telegram_username = request.form['telegram_username']

        # Insert the data into the database
        cur.execute("INSERT INTO registrations (telegram_name, telegram_username) VALUES (%s, %s)",
                    (telegram_name, telegram_username))
        conn.commit()

        # Show success message
        success_message = 'Thank you for registering.'
        return render_template('index.html', success_message=success_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
