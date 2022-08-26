#In the RPI run the following:
# workon cv
# pip install "picamera[array]"

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)
time.sleep(0.1)
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
cv2.imshow("Image", image)
cv2.waitKey(0)
