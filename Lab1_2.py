import cv2
img = cv2.imread('123.png')
img2=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('2.png',img2)
