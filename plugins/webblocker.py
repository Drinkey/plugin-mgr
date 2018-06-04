import logging
from monitor import ServiceMonitor

__author__='Junkai Zhang'
__plugin_type__ = 'services'

class Webblocker(ServiceMonitor):
    def run(self):
        logging.error("this is Webblocker run")

    def __del__(self):
        logging.info("exit plugin")
