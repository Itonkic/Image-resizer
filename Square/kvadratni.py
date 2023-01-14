from PIL import Image
import cv2
import numpy as np
from resizeimage import resizeimage
import os


#print(os.getcwd())
entries=os.getcwd()
kk=os.getcwd()+'\\gotovo\\'
#print(kk)
a=0
asa=0
for entry in os.scandir(entries):
    if (entry.path.endswith(".bmp")
        or entry.path.endswith(".png") or entry.path.endswith(".jpeg") or entry.path.endswith(".jpg")) and entry.is_file():
        with open(entry.path, "r+b") as f:
            a=a+1
            asa=asa+1
            file_name = os.path.basename(entry.path )
            desired_size = 468
            desired_size1 =702
            im = cv2.imread(entry.path)
            old_size = im.shape[:2] # old_size is in (height, width) format
            print(old_size)
            print(file_name)
            ratio = float(desired_size)/max(old_size)
            new_size = tuple([int(x*ratio) for x in old_size])

            # new_size should be in (width, height) format

            im = cv2.resize(im, (new_size[1], new_size[0]))

            delta_w = desired_size1 - new_size[1]
            delta_h = desired_size - new_size[0]
            top, bottom = delta_h//2, delta_h-(delta_h//2)
            left, right = delta_w//2, delta_w-(delta_w//2)

            color = [0, 0, 0]
            new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
                value=color)

            #cv2.imshow("image", new_im)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            
            kka=str(asa)+'a.jpg'
            print(kk)
            cv2.imwrite(kka, new_im)
            f.close()
            os.replace(entry.path, kk+file_name)

