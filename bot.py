from instabot import Bot
import os
import logging

bot = Bot()
bot.login(username=os.environ.get('USERNAME'), password=os.environ.get('PASSWORD'))
bot.send_message('Fat fuck!', ["chocho.bossa", "nikola.diankov"])
bot.logout()

fp = os.path.expanduser('~/config/chocho.bossa_uuid_and_cookie.json')

if os.path.exists(fp):
    try:
        os.remove(fp)
        logging.info('Cookies removed!')
    except Exception as e:
        logging.error(f"Couldn't delete cookies: {e}")
else:
    logging.error(f'File: "{fp}" does not exist!')

print('Done')
