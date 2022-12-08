import cv2
import numpy as np

img_rectangle = np.ones((400,400), dtype='uint8')
cv2.rectangle(img_rectangle, (50,50), (300,300), (255,255,255), -1)

img_circle = np.ones((400,400), dtype='uint8')
cv2.circle(img_circle, (300,300), 70, (255,2555,255), -1)

bitwiseAnd = cv2.bitwise_and(img_rectangle, img_circle)
bitwiseOr = cv2.bitwise_or(img_rectangle, img_circle)
bitwiseXor = cv2.bitwise_xor(img_rectangle, img_circle)
rec_not = cv2.bitwise_not(img_rectangle)
circle_not = cv2.bitwise_not(img_circle)

cv2.imshow('image bitwiseAnd', bitwiseAnd)
cv2.imshow('image bitwiseOr', bitwiseOr)
cv2.imshow('image bitwiseXor', bitwiseXor)
cv2.imshow('rectangle not', rec_not)
cv2.imshow('circle not', circle_not)
cv2.waitKey(0)

# 합집합과 교집합으로 생각하면 쉽게 이해할 수 있다.

