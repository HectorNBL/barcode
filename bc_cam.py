import cv2
import numpy as np
from pyzbar.pyzbar import decode

def bc_cam_fun():
    cap = cv2.VideoCapture(0)
    cap.set(3,640) #width id=3
    cap.set(4,480) #height id=4
    decoded = 'empty'
    while decoded=='empty':
        #print (decoded)
        boolean, img = cap.read() #gives boolean and img data
        for barcode in decode(img):
            #print(barcode.data)
            decoded = barcode.data.decode('utf-8')
            #print(decoded)
        #cv2.imshow('Result',img) #remove comment to turn on display
        cv2.waitKey(1)
    return decoded

#print(bc_cam_fun())

''''  
    while True:
        #myColor = (0,255,0)
        boolean, img = cap.read() #gives boolean and img data
            #checks all barcodes
        for barcode in decode(img):
                #print(barcode.data)
                decoded = barcode.data.decode('utf-8')
                #print(decoded)
            #This can be used to add boxes around the barcodes to view in the screen
                pts = np.array([barcode.polygon],np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(img,[pts],True,myColor,5)
                pts2 = barcode.rect
                cv2.putText(img,decoded,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,myColor,2)

            #cv2.imshow('Result',img)
             cv2.waitKey(1) 
'''            

