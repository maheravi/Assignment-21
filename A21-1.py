import cv2
import numpy as np


blockSize = 75
imageSize = blockSize * 8
chessBoard = np.zeros((imageSize, imageSize))

for i in range(0, imageSize, blockSize):
    if i % 2 == 0:
        for j in range(0, imageSize, blockSize):
            if j % 2 == 0:
                chessBoard[i:imageSize, j:imageSize] = 0
            else:
                chessBoard[i:imageSize, j:imageSize] = 255

    else:
        for j in range(0, imageSize, blockSize):
            if j % 2 == 0:
                chessBoard[i:imageSize, j:imageSize] = 255
            else:
                chessBoard[i:imageSize, j:imageSize] = 0


cv2.imshow("Chess board", chessBoard)
cv2.waitKey()
