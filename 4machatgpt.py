import telebot
import time
bot = telebot.TeleBot("6296471869:AAEQZy1Ojefa3VL3RT4fWgZdEsek6gcrW-8")

import openai
openai.api_key = "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"

# Define the message handler for the /start command
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Hello! Send me a message and I'll try to generate a response using OpenAI's GPT-3.")

# Define the message handler for all other messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Generate a response using OpenAI's GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Send the response back to the user
    bot.reply_to(message, response.choices[0].text)

# Start the bot
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        time.sleep(3)
        print(str(e))
