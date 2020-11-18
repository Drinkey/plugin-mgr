import logging
import abc

class Monitor(abc.ABC):
    def __init__(self):
       logging.debug("[init] launching monitor")

    @abc.abstractmethod
    def run(self):
        pass


