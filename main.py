import threading
import time
import Engines.DCEngine as DCEngine
import Sensors.Infrared as InfraRed
import Sensors.Ultrasound as UltraSound
import Sensors.RGB as RGB


import abc

class Main():
    def main(self):
        infra = InfraRed()
        DC1 =  DCEngine(1, 2, 3)
        DC2 =  DCEngine(1, 2, 3)