import RPi.GPIO as GPIO
from time import sleep

from firebase import firebase


import urllib2, urllib,httplib
import json
import os
from functools import partial

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
firebase = firebase.FirebaseApplication('https://temp-and-humi-c3c77.firebaseio.com/', None)
def update_firebase():
    if(GPIO.input(4)) == False:
        value=1
        print 'slot is empty'
    elif(GPIO.input(4)) == True:
        value=0
        print 'slot is full search for other slot'

    data = value
    firebase.post('/sensor', data)

while True:
    update_firebase()
    sleep(2)
