import sys
import logging
from instabot import Bot

try:
    bot = Bot()
    bot.login(username=sys.argv[1], password=sys.argv[2], proxy=f"{sys.argv[1]}:{sys.argv[2]}@10.10.1.10:3128")
    bot.send_message('Fat fuck!', ["nikola.diankov"])
    logging.info('Message sent!')
except:
    logging.error('Error!')
finally:
    bot.logout()
    logging.info('Logged out!')