import numpy as np
import cv2
import os
files = os.listdir('~/val_256')

count=0
for f in files:
    im = cv2.imread('./val_256/'+f)
    im = cv2.resize(im,(128,128))
    cv2.imwrite('./val_final/'+str(count)+'.jpg',im)
    #l.append(str(count)+'.jpg')
    count = count+1