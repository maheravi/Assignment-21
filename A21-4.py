import cv2

image = cv2.imread('4.jpg')
(h, w) = image.shape[:2]
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

for i in range(h):
    for j in range(w):
        if image[i, j] > 30:
            image[i, j] = 255

cv2.imshow('4', image)
cv2.waitKey()