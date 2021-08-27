# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 17:19:25 2021

@author: kumar
"""

import cv2
import os
desired_size = 224
im_path = "C:/Users/kumar/Desktop/axmind works/image_download_clean/dataset2/1_raw/random"
os.chdir(im_path)
arr = os.listdir()
i1=int(0)
for i in arr:
    i1=i1+1
    name=i
    new_path=im_path+'/'+i
    im = cv2.imread(new_path)
    size=(os.stat(new_path).st_size)/1024
    if size<=3:
        os.remove(i)
        continue
    old_size = im.shape[:2] # old_size is in (height, width) format
    
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    
    # new_size should be in (width, height) format
    
    im = cv2.resize(im, (new_size[1], new_size[0]))
    
    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
    
    color = [0, 0, 0]
    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
        value=color)
    x = i.split('.')
    name=x[0]
    new_name=name+str(i1)+'as'+'.jpg'
    cv2.imwrite(new_name, new_im)
    os.remove(i)
    no_samples=len(arr)
    percentage=(i1/no_samples)*100
# cv2.imshow("image", new_im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()