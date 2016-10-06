#!/usr/bin/python
import time
import picamera
import datetime as dt

#To stop te red LED on camera board
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
CAMLED = 32
GPIO.setup(CAMLED, GPIO.OUT, initial=False) 

timeRecord = 300

framerate = 30
resolution = (1280,860)

movie_path_name = "/path/to/directory/filename_prefix"

try:
    with picamera.PiCamera(framerate = framerate, resolution=resolution) as camera:
        camera.exposure_mode = 'night'
	camera.iso = 1600
	camera.rotation = 270
	GPIO.output(CAMLED,False)
        
    	recordtime = dt.datetime.now().strftime('%Y-%m-%d_%Hh%Mm%Ss_0')
        camera.start_recording("/movie_path_name_%s.h264" %(recordtime), format="h264") 
      	camera.wait_recording(timeRecord)        
        while(1):
            recordtime = dt.datetime.now().strftime('%Y-%m-%d_%Hh%Mm%Ss_%m')
            camera.split_recording("movie_path_name_%s.h264" %(recordtime), format="h264")
 	    camera.wait_recording(timeRecord)
    camera.stop_recording()

except KeyboardInterrupt:
    print("Bye !\n")

finally:
    GPIO.cleanup()

