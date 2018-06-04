import logging
from monitor import ServiceMonitor

__author__='Junkai Zhang'
__plugin_type__ = 'in-feed'

class Bitdefender(ServiceMonitor):
    def run(self):
        logging.error("this is Bitdefender run")
