import cv2
import numpy as np


def Raster(rows):
    image = np.zeros((rows, rows))

    for i in range(0, rows):
        if i % 2 == 0:
            for j in range(0, rows):
                if j % 2 == 0:
                    image[i, j] = 0
                else:
                    image[i, j] = 255
        else:
            for j in range(0, rows):
                if j % 2 == 0:
                    image[i, j] = 255
                else:
                    image[i, j] = 0

    cv2.imshow('my pic 1', image)
    cv2.waitKey()


size = int(input("Please size : "))
Raster(size)

board = np.zeros((size, size))
board[::2, 1::2] = 0
board[1::2, ::2] = 255
cv2.imshow('my pic 2', board)
cv2.waitKey()
