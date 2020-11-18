import logging
from monitor import Monitor

__author__='Jason B'
__plugin_type__ = 'services'

class Lastline(Monitor):
    def run(self):
        logging.error("this is lastline run")

    def __del__(self):
        logging.info("exit plugin")
