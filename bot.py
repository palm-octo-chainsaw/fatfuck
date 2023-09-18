import os
import sys
import logging
import datetime
from time import sleep
from instabot import Bot


count = 0

logging.basicConfig(level=logging.DEBUG)
del_file_path = os.path.expanduser(r"~\Desktop\test\config")

while True:

    current_time = datetime.datetime.now().time()
    logging.info(f"Current time: {current_time} {count}")

    if current_time.hour == 10 and current_time.minute == 0:
        if count == 0:
            try:
                bot = Bot()
                bot.login(username=sys.argv[1], password=sys.argv[2])
                bot.send_message('Fat fuck!', ["nikola.diankov"])
                logging.info('Message sent!')
                count += 1
            except:
                logging.error('Error!')
            finally:
                bot.logout()
                logging.info('Logged out!')
                
                if os.path.exists(del_file_path + r"\chocho.bossa_uuid_and_cookie.json"):
                    os.remove(del_file_path + r"\chocho.bossa_uuid_and_cookie.json")
                    logging.info('Cookies removed successfuly!')
                else:
                    logging.error("File to delete not found!")
        else:
            logging.info('Message already sent!')
        count = 0
     
    sleep(60)
