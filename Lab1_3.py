import cv2
img1 = cv2.imread('123.png')
img2 = cv2.flip(img1,1)
img3 = cv2.flip(img1,0)
cv2.imwrite('3.png',img2)
cv2.imwrite('4.png',img3)