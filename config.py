from redis import Redis
from os import environ
from aiogram import Bot, Dispatcher
import sentry_sdk

r = Redis(host=environ.get('REDIS_HOST'), port=int(environ.get('REDIS_PORT')),
          password=environ.get('REDIS_PASSWORD'), db=0)
sentry_sdk.init(environ.get('SENTRY'))

TOKEN = environ.get('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
