#!/usr/bin/env python3
from rpi_ws281x import PixelStrip, Color
import time
import threading
    
class Colour(object):
    
    def __init__(self):
        # LED strip 1 configuration:
        self.LED_1_COUNT = 108        # Number of LED pixels.
        self.LED_1_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
        # LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
        self.LED_1_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_1_DMA = 10          # DMA channel to use for generating signal (try 10)
        self.LED_1_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
        self.LED_1_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
        self.LED_1_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
    
        self.strip1 = PixelStrip(self.LED_1_COUNT, self.LED_1_PIN, self.LED_1_FREQ_HZ, self.LED_1_DMA, self.LED_1_INVERT, self.LED_1_BRIGHTNESS, self.LED_1_CHANNEL)
        self.strip1.begin()
        
        # LED strip 2 configuration:
        self.LED_2_COUNT = 110        # Number of LED pixels.
        self.LED_2_PIN = 13          # GPIO pin connected to the pixels (18 uses PWM!).
        # LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
        self.LED_2_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_2_DMA = 10          # DMA channel to use for generating signal (try 10)
        self.LED_2_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
        self.LED_2_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
        self.LED_2_CHANNEL = 1       # set to '1' for GPIOs 13, 19, 41, 45 or 53
    
        self.strip2 = PixelStrip(self.LED_2_COUNT, self.LED_2_PIN, self.LED_2_FREQ_HZ, self.LED_2_DMA, self.LED_2_INVERT, self.LED_2_BRIGHTNESS, self.LED_2_CHANNEL)
        self.strip2.begin()
    
    def colour(self,rgbList):
        # strip 1
        for i in range(self.strip1.numPixels()):
            self.strip1.setPixelColor(i, Color(rgbList[0], rgbList[1], rgbList[2]))
        #strip 2
        for i in range(self.strip2.numPixels()):
            self.strip2.setPixelColor(i, Color(rgbList[0], rgbList[1], rgbList[2]))
        self.strip1.show()
        self.strip2.show()
        
    def ambient1(self, stop, wait_ms=20, iterations=1):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        while True:
            for j in range(256*iterations):
                # strip1
                for i in range(self.strip1.numPixels()):
                    self.strip1.setPixelColor(i, self.wheel((int(i * 256 / self.strip1.numPixels()) + j) & 255))
                # strip2
                for i in range(self.strip2.numPixels()):
                    self.strip2.setPixelColor(i, self.wheel((int(i * 256 / self.strip2.numPixels()) + j) & 255))
                self.strip1.show()
                self.strip2.show()
                time.sleep(wait_ms/1000.0)
                if stop(): 
                    return
                    

    def ambient2(self, stop, wait_ms=20, iterations=5):
        """Draw rainbow that fades across all pixels at once."""
        while True:
            for j in range(256*iterations):
                # strip1
                for i in range(self.strip1.numPixels()):
                    self.strip1.setPixelColor(i, self.wheel((i+j) & 255))
                # strip2
                for i in range(self.strip2.numPixels()):
                    self.strip2.setPixelColor(i, self.wheel((i+j) & 255))
                self.strip1.show()
                self.strip2.show()
                time.sleep(wait_ms/1000.0)
                if stop(): 
                    return
                    
    def strobe(self, stop, wait_ms=83):
        while True:
            #on
            # strip 1
            for i in range(self.strip1.numPixels()):
                self.strip1.setPixelColor(i, Color(255, 255, 255))
            # strip 2
            for i in range(self.strip2.numPixels()):
                self.strip2.setPixelColor(i, Color(255, 255, 255))
            self.strip1.show()
            self.strip2.show()
            time.sleep(wait_ms/1000)
            #off
            # strip 1
            for i in range(self.strip1.numPixels()):
                self.strip1.setPixelColor(i, Color(0, 0, 0))
            self.strip1.show()
            # strip 2
            for i in range(self.strip2.numPixels()):
                self.strip2.setPixelColor(i, Color(0, 0, 0))
            self.strip1.show()
            self.strip2.show()
            time.sleep(wait_ms/1000)
            if stop():
                return
        
    def off(self):
        # strip 1
        for i in range(self.strip1.numPixels()):
            self.strip1.setPixelColor(i, Color(0, 0, 0))
        # strip 2
        for i in range(self.strip2.numPixels()):
            self.strip2.setPixelColor(i, Color(0, 0, 0))
        self.strip1.show()
        self.strip2.show()
        
    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)
            
    def startFunction(self, function):
        self.stop_threads = False
        self.thread = threading.Thread(target=function, args=(lambda: self.stop_threads, ))
        self.thread.start()
        
    def stopFunction(self):
        self.stop_threads=True
        self.thread.join()
        

        
    

