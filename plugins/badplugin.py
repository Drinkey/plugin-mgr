import logging
from monitor import Monitor

__autho__='Tony Stark'
__plugin_type__ = 'feeds'

class BadPlugin(Monitor):
    # The run() is not implemented so this plugin
    # is not supposed to run
    def rdun(self):
        logging.error("this is Bitdefender run")
