import logging
from monitor import Monitor

__author__='Steven Rogers'
__plugin_type__ = 'feeds'

class Bitdefender(Monitor):
    def run(self):
        logging.error("this is Bitdefender run")
