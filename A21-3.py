import cv2

image = cv2.imread('3.jpg')
(h, w) = image.shape[:2]
center = (w / 2, h / 2)
rotate = cv2.getRotationMatrix2D(center, 180, 1)
image = cv2.warpAffine(image, rotate, (w, h))

cv2.imshow('3', image)
cv2.waitKey()