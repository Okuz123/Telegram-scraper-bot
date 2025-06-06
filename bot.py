import requests
from bs4 import BeautifulSoup
import telebot
import os

TOKEN = os.getenv("8130659757:AAGleAUla0cGqiQJuTWMwWdGtX0Db1ZSJ5w")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Send /scrape to fetch website data.")

@bot.message_handler(commands=['scrape'])
def scrape_site(message):
    url = "https://example.com"  # Change to your target website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    bot.reply_to(message, f"Website Title: {title}")

bot.polling()
