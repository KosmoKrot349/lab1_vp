import cv2
img = cv2.imread('123.png')
(h, w, d) = img.shape
h=int(h/2)
w=int(w/2)
img2 = cv2.resize(img, (w,h), interpolation = cv2.INTER_AREA)
cv2.imwrite('6.png',img2)
cv2.imwrite('7.bmp',img2)
cv2.imwrite('8.jpg',img2)