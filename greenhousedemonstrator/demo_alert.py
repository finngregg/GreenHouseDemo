# Imports
# for board
import spidev
import time
import os
import RPi.GPIO as GPIO
# for email
import smtplib

class api_demonstrator:
    # Global Variables 
    pwm_alert = None 
    LED_alert = 12

    def setup():
        GPIO.setmode(GPIO.BCM) 
        GPIO.setwarnings(False)
        GPIO.setup(LED_alert, GPIO.OUT)
        pwm_alert = GPIO.PWM(LED_alert, 100) # sets up the first LED used for alerts

    def alert(humid,temp):
        if (humid < 50) | (humid > 70):  
            pwm_alert.start(100)

            content = ("The humidity in the greenhouse has risen or dropped below optimal conditions")
            mail = smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login('placeholder@gmail.com','password')
            mail.sendmail('placeholder@gmail.com','receiver@gmail.com',content) 
            mail.close()
        elif (temp < 18) | (temp > 30):
            pwm_alert.start(100)
            content = ("The temperature in the greenhouse has risen or dropped below optimal conditions")
            mail = smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login('placeholder@gmail.com','password')
            mail.sendmail('placeholder@gmail.com','receiver@gmail.com',content) 
            mail.close()
        else:
            pwm_alert.stop()