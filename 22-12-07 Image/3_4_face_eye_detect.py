import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

face_img = cv2.imread('face.png')
face_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(face_gray, 1.1, 4)

for(x,y,w,h) in faces:
    cv2.rectangle(face_img, (x,y), (x+w, y+h), (0,0,255), 3)

roi_color = face_img[y:(y+h), x:(x+w)]
roi_gray = face_gray[y:(y+h), x:(x+w)]

eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)

index = 0
for (ex, ey, ew, eh) in eyes:
    if index == 0:
        eye_1 = (ex, ey, ew, eh)
    elif index == 1:
        eye_2 = (ex, ey, ew, eh)

    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,0,255), 3)
    index = index + 1

if eye_1[0] < eye_2[0]:
    left_eye = eye_1
    right_eye = eye_2
else:
    left_eye = eye_2
    right_eye = eye_1

left_eye_center = (int(left_eye[0]+(left_eye[2]/2)), int(left_eye[1]+(left_eye[3]/2)))
left_eye_x = left_eye_center[0]
left_eye_y = left_eye_center[1]


right_eye_center = (int(right_eye[0]+(right_eye[2]/2)), int(right_eye[1]+(right_eye[3]/2)))
right_eye_x = right_eye_center[0]
right_eye_y = right_eye_center[1]


cv2.circle(roi_color, left_eye_center, 5, (255,0,0),-1)
cv2.circle(roi_color, right_eye_center, 5, (255,0,0),-1)
cv2.line(roi_color, right_eye_center, left_eye_center,(0,200,200),3)

cv2.imshow('Face', face_img)
cv2.waitKey(0)

if left_eye_y > right_eye_y:
    A = (right_eye_x, left_eye_y)
    direction = -1
else:
    A = (left_eye_x, right_eye_y)
    direction = 1

cv2.circle(roi_color, A, 5, (255,0,0), -1)

cv2.line(roi_color,right_eye_center,left_eye_center,(0,200,200),3)
cv2.line(roi_color,left_eye_center, A, (0,200,200), 3)
cv2.line(roi_color,right_eye_center, A, (0,200,200), 3)

##### 모듈 만들 때는 파일 이름 숫자로 시작되면 절대 안된다!
cv2.imshow('face box', face_img) # 얼굴이 기울어져 있음. 눈이 직선이 되도록 기울기를 맞추자.
cv2.waitKey(0)
