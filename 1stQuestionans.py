from PIL import Image
import cv2
import numpy as np
res=[]
img=cv2.imread("iiit-test-image1.png")
img1 = Image.open(img)
# get width and height
width = img1.width
height = img1.height
contours, hierarchies = cv.findContours(
thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
for i in contours:
    M = cv.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv.drawContours(image, [i], -1, (0, 255, 0), 2)
        cv.circle(image, (cx, cy), 7, (0, 0, 255), -1)
        cv.putText(image, "center", (cx - 20, cy - 20),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cx1=cx
    cx2=cy
    res.append(cx1)
    res.append(cx2)
res.append(width)
res.append(height)
print(ans)

