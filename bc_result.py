from distutils.log import fatal
from unicodedata import name
from unittest import result
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import bc_sql
import bc_cam

names = bc_sql.food_name()
#print(names[0])
ids = bc_sql.food_id() #tuple with ids
#print(ids[0])
scanned_bc = bc_cam.bc_cam_fun()
#print(scanned_bc)


def check_exists():
    try:
        result = ids.index(scanned_bc)
        #print(result)
        return result
    except:
        result = 'Food Not Found'
        #print(result)
        return result

def food_name(i):
    try:
        name = names[i]
        print(name)
        return name
    except:
        not_found = i
        print(not_found)
        return not_found

#check_exists()
food_name(check_exists())