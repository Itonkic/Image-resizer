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
            ratio = float(desired_size1)/max(old_size)
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

















"""
asa=0
try:
    for entry in os.scandir(entries):
        if (entry.path.endswith(".bmp")
            or entry.path.endswith(".png") or entry.path.endswith(".jpg")) and entry.is_file():
            with open(entry.path, "r+b") as f:
                asa=asa+1
                img = cv2.imread(entry.path)
                old_image_height, old_image_width, channels = img.shape

                # create new image of desired size and color (blue) for padding
                new_image_width = 702
                new_image_height = 468
                color = (255,0,0)
                result = np.full((new_image_height,new_image_width, channels), color, dtype=np.uint8)

                # compute center offset
                x_center = (new_image_width - old_image_width) // 2
                y_center = (new_image_height - old_image_height) // 2

                # copy img image into center of result image
                result[y_center:y_center+old_image_height, 
                       x_center:x_center+old_image_width] = img
                # save result
                kk=str(asa)+'a.jpg'
                cv2.imwrite(kk, result)

except:
    
  #pass to continue loop or error handling
    print(entry)
    print("wer")
    pass

"""

"""
#print(os.getcwd())
entries=os.getcwd()
kk=os.getcwd()+'\\asd'
#print(kk)
a=0

for entry in os.scandir(entries):
    if (entry.path.endswith(".bmp")
        or entry.path.endswith(".png") or entry.path.endswith(".jpg")) and entry.is_file():
        with open(entry.path, "r+b") as f:
            a=a+1
            file_name = os.path.basename(entry.path )

            with Image.open(f) as image:
                cover = resizeimage.resize_height(image, 468)
                asd = str(a)+'.jpg'
                cover.save(asd, image.format)
                f.close()
                image.close()
                os.replace(entry.path, kk+file_name)

"""
                
"""            
        asd=entry.name.split('.')[0]
        csv=asd+'.csv'
        with open(csv, 'wb') as my_data_file:
            my_data_file.write(my_string)
            os.remove(entry.name)




        
        with open('test-image.jpeg', 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_height(image, 468)
            cover.save('test-image-cover.jpeg', image.format)
            print(entry)
"""
"""
with open('test-image.jpeg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_height(image, 468)
        cover.save('test-image-cover.jpeg', image.format)

"""
