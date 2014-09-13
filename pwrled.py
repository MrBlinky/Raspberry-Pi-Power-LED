## Raspberry Pi B+ power LED v0.1 by Mr.Blinky ##

## General Info ##

#On the rasperry Pi B+ the power LED is controlled by an APX803 circuit.
#This circuit is a precision voltage monitor that gets activated when the
#Pi's power supply voltage drops below a certain level. When this happens
#the circuits output will be pulled low and the P's power LED turns off.
#But in the normal case when the input power is ok, the circuit is not 
#activated and the power LED is on.
#To give the Raspberry Pi the ability to detect a low voltage, the circuits
#output is also connected to a GPIO pin that can be read. This GPIO pin can
#also be configured as an output and by setting it to low we can simulate a
#low voltage and turn off the power LED.

#to turn the LED off the GPIO pin is configured as output and set to low.
#to turn the LED back on the GPIO pin is configured as input again.

#This can be safely done as the the circuits output is an opendrain output
#which acts like a switch. When not active it is open and the GPIO pin is
#pulled high by an external resistor. When active it pulls the output low.

## Notes ##

# Turning the power LED off saves about 14mW of power.
# The power LED will not turn on if the input power is too low.

## Usage ##

#sudo python pwrled.py     #toggle power led on/off
#sudo python pwrled.py off #turn led off
#sudo python pwrled.py on  #turn led back on

## Code ##
from sys import argv
from time import sleep
import RPi.GPIO as GPIO

PWR_LED = 35 #Under voltage GPIO input pin(Active low)(PWR_LOW_N in schematic)

def pwr_led_off():
 GPIO.setup(PWR_LED, GPIO.OUT, initial=GPIO.LOW) #Turn power LED off

def pwr_led_on():
 GPIO.setup(PWR_LED,GPIO.IN)                     #Turn power LED on

GPIO.setwarnings(False)                          #We don't want warnings
GPIO.setmode(GPIO.BCM)                           #use BCM chip pin numbering
if 'on' in argv[1:]:
 pwr_led_on()
elif 'off' in argv[1:]:
 pwr_led_off()
elif 'flash' in argv[1:]:
 for i in range (0,10):
  pwr_led_on() 
  sleep(.100)
  pwr_led_off()
  sleep(.100)
else:
 print GPIO.gpio_function(PWR_LED)
 if GPIO.gpio_function(PWR_LED)==0:
  pwr_led_on()
 else:
  pwr_led_off()

#No GPIO.cleanup() otherwise power LED GPIO pin is set to input.
