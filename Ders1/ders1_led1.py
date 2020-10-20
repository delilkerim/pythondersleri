import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # GPIO.setmode(GPIO.BOARD)
GPIO.setup(14,GPIO.OUT)

while(True):
	GPIO.output(14,GPIO.HIGH)
	time.sleep(1) # 1 saniye bekle
	GPIO.output(14,GPIO.LOW)
	time.sleep(1)

GPIO.cleanup()

