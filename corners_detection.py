#shi-tomasi corner detection algoritm
import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)
print (corners)

for corner in corners:
    x,y  = corner.ravel()
    #draw corners
    cv2.circle(img, (x,y), 3, (255,0,0), -1)
    
# for i in range (len(corners)):
#     for j in range (i+1, len(corners)):
#         corner1 = tuple(corners[i])
#         corner2 = tuple(corners[j])
#         color = np.random.randint(0,255,(3)).to
#         cv2.line(img, corner1, corner2, color, 2)
        


#euclidean distance
# (x1,y1) (x2,y2)
# sqrt((x2-x1)^2 + (y2-y1)^2)

cv2.imshow("frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()