import cv2
import numpy as np

image_rectangle = np.ones((400,400), dtype='uint8') # 검정사각형
cv2.rectangle(image_rectangle, (50,50), (300,300), (255,255,255), -1) # 검정사각형 안에 흰 사각형 생성
cv2.imshow('image_rectangle', image_rectangle)
cv2.waitKey(0)
