import threading
import time
import Engines.PCA9685 as PCA
import Engines.DCEngine as DCEngine
import Sensors.Infrared as InfraRed
import Sensors.Ultrasound as UltraSound
import Sensors.RGB as RGB

import abc

class Main():
    def main(self):
        UltraSound_front = UltraSound(5, 6)
        UltraSound_left = UltraSound(9, 11)
        UltraSound_right = UltraSound(19, 26)