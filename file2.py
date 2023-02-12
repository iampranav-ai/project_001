import cv2
import numpy as np
import random
#blue green red  [0,0,0]
img = cv2.imread('assets/img1.jpg', -1)
#print ('shape' , img.shape)
#print (img[0][0])

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255),random.randint(0,255),random.randint(0,255)]   

cv2.imshow("New Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()