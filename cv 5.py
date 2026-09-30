import cv2
import numpy as np
image=cv2.imread("C:\\Users\\Student\\Desktop\\khushi shetty\\lung cancer.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gradients_sobelx=cv2.Sobel(image,-1,1,0)
graidents_sobely=cv2.Sobel(image,-1,0,1)
gradirnts_sobelxy=cv2.addWeighted(gradients_sobelx,0.5,graidents_sobely,0.5,0)

gradients_laplacian=cv2.Laplacian(image,-1)

canny_output=cv2.Canny(image,80,150)

cv2.imshow('sobelx',gradients_sobelx)
cv2.imshow('sobely',graidents_sobely)
cv2.imshow('sobelxy',gradirnts_sobelxy)
cv2.imshow('laplacian',gradients_laplacian)
cv2.imshow('canny',canny_output)

cv2.waitKey(0)