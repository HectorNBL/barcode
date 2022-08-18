# barcode
Decode barcodes, compare values to database in mysql

## tester.py

Views img in same directory, scans barcode in img, print resulting numbers

## bc_cam.py

Run this to scan barcode with camera

Remove this comment to view display:
`#cv2.imshow('Result',img)`

## bc_sql.py

Api to access MySQL database

## by_result.py

Compares results scanned from bc_cam.py and bc_sql.py. 
Print out f`ood name` if found in database otherwise prints out `food not found` 

## thresholding.py

Fixes blurry barcodes from images placed in same directory as the script
