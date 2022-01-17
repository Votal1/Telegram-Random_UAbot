import redis
import telebot
from os import environ

r = redis.Redis(host=environ.get('REDIS_HOST'), port=int(environ.get('REDIS_PORT')),
                password=environ.get('REDIS_PASSWORD'), db=0)

TOKEN = environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)
