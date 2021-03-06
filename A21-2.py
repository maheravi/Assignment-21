import cv2

image = cv2.imread('1.jpg')

rows = image.shape[0]
cols = image.shape[1]

for i in range(rows):
    for j in range(cols):
        image[i, j] = 255 - image[i, j]

cv2.imshow('1', image)

image2 = cv2.imread('2.jpg')

rows = image2.shape[0]
cols = image2.shape[1]

for i in range(rows):
    for j in range(cols):
        image2[i, j] = 0 - image2[i, j]

cv2.imshow('2', image2)
cv2.waitKey()