import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 
from pyzbar import pyzbar

# Read Image
img = cv.imread('test2.png', cv.IMREAD_GRAYSCALE)

closed = cv.morphologyEx(img, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_RECT, (1, 21)))

#Statistics
#print(img.shape)
dens = np.sum(img, axis=0)
mean = np.mean(dens)
#print(mean)

#Thresholding
thresh = closed.copy()
for idx, val in enumerate(dens):
    if val< 10800:
        print("Needs fixing")
        thresh[:,idx] = 0

(_, thresh2) = cv.threshold(thresh, 128, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)


#plotting results
'''
plt.figure(num='barcode')

plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(224)
plt.imshow(thresh, cmap='gray')
plt.title('Thresholded')
plt.axis('off')
'''
plt.subplot(223)
plt.imshow(thresh2, cmap='gray')
plt.title('Result')
plt.axis('off')
'''
plt.subplot(222)
plt.hist(dens)
plt.axvline(dens.mean(), color='k', linestyle='dashed', linewidth=1)
plt.title('dens hist')
'''
#plt.show() # remove comment to show graph thresholded img

barcodes = pyzbar.decode(thresh2)

for barcode in barcodes:
    fixed_bc = barcode.data.decode('utf-8')
    #print(fixed_bc)
#print(type(barcodes[0]))