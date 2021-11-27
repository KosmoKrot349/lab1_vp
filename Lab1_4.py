import cv2
img = cv2.imread('123.png')
(h, w, d) = img.shape
center = (w // 2, h // 2)
map = cv2.getRotationMatrix2D(center, -90, 1)
img2 = cv2.warpAffine(img, map, (w, h))
cv2.imwrite('5.png',img2)