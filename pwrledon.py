## Raspberry Pi B+ power LED on v0.1 by Mr.Blinky ##

## Info ##

#Turns power LED off
#For more info see pwrled.py

## Code ##
import RPi.GPIO as GPIO

PWR_LED = 35 #Under voltage GPIO input pin(Active low)(PWR_LOW_N in schematic)

GPIO.setwarnings(False)                          #We don't want warnings
GPIO.setmode(GPIO.BCM)                           #use BCM chip pin numbering
GPIO.setup(PWR_LED,GPIO.IN)                      #Turn power LED on

#No GPIO.cleanup() otherwise power LED GPIO pin is set to input.
