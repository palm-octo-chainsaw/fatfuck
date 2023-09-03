import sys
from instabot import Bot


bot = Bot()
bot.login(username=sys.argv[1], password=sys.argv[2])
bot.send_message('Fat fuck!', ["nikola.diankov"])
bot.logout()
