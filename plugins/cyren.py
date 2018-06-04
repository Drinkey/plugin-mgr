import logging

from monitor import ServiceMonitor

__author__='Junkai Zhang'
__plugin_type__ = 'in-feed'

class Cyren(ServiceMonitor):
    def run(self):
        logging.error("this is Cyren run")
