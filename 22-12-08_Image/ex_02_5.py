import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

image = cv2.imread('soju.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

face_crop = []
for (x,y,w,h) in faces:
    face_crop.append(image[y:(y+h), x:(x+w)])
print(len(face_crop))   # 이상한 부분 한 곳이 얼굴로 인식되어서 3이 아닌 4가 출력됨.

mask = np.zeros((683, 1024, 3), dtype='uint8')
cv2.rectangle(mask, (60,50), (280,280), (255,255,255), -1)
cv2.rectangle(mask, (420,50), (550,230), (255,255,255), -1)
cv2.rectangle(mask, (750,50), (920,280), (255,255,255), -1)

x_offset = [60,420,750]
y_offset = [50,50,50]

x_end = [280,550,920]
y_end = [280,230,280]


face_crop_resize1 = cv2.resize(face_crop[0],(x_end[0]-x_offset[0],y_end[0]-y_offset[0]))
face_crop_resize2 = cv2.resize(face_crop[1],(x_end[1]-x_offset[1],y_end[1]-y_offset[1]))
face_crop_resize3 = cv2.resize(face_crop[2],(x_end[2]-x_offset[2],y_end[2]-y_offset[2]))

mask[y_offset[0]:y_offset[0]+face_crop_resize1.shape[0],
          x_offset[0]:x_offset[0]+face_crop_resize1.shape[1]] = face_crop_resize1
mask[y_offset[1]:y_offset[1]+face_crop_resize2.shape[0],
          x_offset[1]:x_offset[1]+face_crop_resize2.shape[1]] = face_crop_resize2
mask[y_offset[2]:y_offset[2]+face_crop_resize3.shape[0],
          x_offset[2]:x_offset[2]+face_crop_resize3.shape[1]] = face_crop_resize3

cv2.imshow('Original image', image)
cv2.imshow('Mask image', mask)
cv2.waitKey(0)
