import logging
from monitor import Monitor

__author__='Jay Chou'
__plugin_type__ = 'services'

class Webblocker(Monitor):
    def run(self):
        logging.error("this is Webblocker run")

    def __del__(self):
        logging.info("exit plugin")
