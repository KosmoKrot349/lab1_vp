import cv2
import numpy as np
import random
height=500
width=500
image = np.zeros((height,width,3), np.uint8)
xmin=0
xmax=width
ymin=0
ymax=height
rgbmin=0
rgbmax=255
r=random.randrange(rgbmin, rgbmax, 1)
g=random.randrange(rgbmin, rgbmax, 1)
b=random.randrange(rgbmin, rgbmax, 1)
image = image+(r, g, b)
for i in range(0,3):
  x1=random.randrange(xmin, xmax, 5)
  x2=random.randrange(xmin, xmax, 5)
  x3=random.randrange(xmin, xmax, 5)
  y1=random.randrange(ymin, ymax, 5)
  y2=random.randrange(ymin, ymax, 5)
  y3=random.randrange(ymin, ymax, 5)
  r=random.randrange(rgbmin, rgbmax, 1)
  g=random.randrange(rgbmin, rgbmax, 1)
  b=random.randrange(rgbmin, rgbmax, 1)
  if i==0:
    image = cv2.rectangle(image, (x1,y1), (x2,y2), (r,g,b), 2)
  if i==1:
    image = cv2.line(image, (x1,y1), (x2,y2), (r,g,b), 2)
  if i==2:
    image = cv2.line(image, (x1,y1), (x2,y2), (r,g,b), 2)
    image = cv2.line(image, (x1,y1), (x3,y3), (r,g,b), 2)
    image = cv2.line(image, (x2,y2), (x3,y3), (r,g,b), 2)
cv2.imwrite('1.png',image)