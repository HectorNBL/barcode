import os
from base64 import decode
import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = ((os.path.dirname(os.path.abspath(__file__)))+'/test_img.png')
img = cv2.imread(img)
code = decode(img)
for barcode in decode(img):
    decoded = barcode.data.decode('utf-8')
    print(decoded)
