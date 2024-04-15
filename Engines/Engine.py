from abc import *


class Engine (metaclass=ABCMeta):
    def __init__(self):
        self.running = False
