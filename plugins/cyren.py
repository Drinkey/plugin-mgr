import logging

from monitor import Monitor

__author__='Winter'
__plugin_type__ = 'feeds'

class Cyren(Monitor):
    def run(self):
        logging.error("this is Cyren run")
