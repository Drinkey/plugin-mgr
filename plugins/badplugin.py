import logging
from monitor import ServiceMonitor

__autho__='Junkai Zhang'
__plugin_type__ = 'in-feed'

class BadPlugin(ServiceMonitor):
    def rdun(self):
        logging.error("this is Bitdefender run")
