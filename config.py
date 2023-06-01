from redis import Redis
from os import environ
from aiogram import Bot, Dispatcher

r = Redis(host=environ.get('REDIS_HOST'), port=int(environ.get('REDIS_PORT')),
          username=environ.get('REDIS_USERNAME', 'default'), password=environ.get('REDIS_PASSWORD'), db=0)

TOKEN = environ.get('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
