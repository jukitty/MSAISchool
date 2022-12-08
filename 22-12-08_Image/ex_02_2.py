import cv2
import numpy as np

img_circle = np.ones((400,400), dtype='uint8')
cv2.circle(img_circle, (300,300), 70, (255,2555,255), -1)
cv2.imshow('image show', img_circle)
cv2.waitKey(0)