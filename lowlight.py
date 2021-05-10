#!/usr/bin/python3

from picamera import PiCamera
import time
from fractions import Fraction
import datetime

cur_time = datetime.datetime.now()
stub = cur_time.strftime("%Y%m%d%H%M_low")

# camera = PiCamera(resolution=(4056,3040),framerate=Fraction(1,6))
camera = PiCamera(framerate=Fraction(1,6))

# camera.resolution = (3000,1500)
camera.shutter_speed = 1750000
camera.iso = 800

time.sleep(30)
camera.exposure_mode = 'off'

outfile = "%s.jpg" % (stub)
camera.capture(outfile)

camera.close()
