import cv2
import numpy as np

# Creating face_cascade and eye_cascade objects
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Loading the image...
img = cv2.imread('face01.png')

# cascade를 사용해서 얼굴에 bounding box 그리기. 윤곽선 따서 좌표.
# Converting the image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4) # 박스 4개(x,y,w,h)

# Defining and drwing the rectangles around the face
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2) # 선 굵기:2

roi_gray = gray[y:(y+h), x:(x+w)] # 이 부분을 크롭하는 것
roi_color = img[y:(y+h), x:(x+w)]

# eyes
eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4) # 전체 이미지를 주는 것이 아닌 얼굴바운딩박스 이미지만 크롭.
'''[[ 41  82  45  45]
 [112  48  52  52]]'''

index = 0
# Creating for loop in order to divide one eye from another
for (ex, ey, ew, eh) in eyes:
    if index == 0 :
        eye_1 = (ex, ey, ew, eh)
    elif index == 1 :
        eye_2 = (ex, ey, ew, eh)

    cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,0,255), 2)
    index = index + 1

if eye_1[0] < eye_2[0]:
    left_eye = eye_1
    right_eye = eye_2
else:
    left_eye = eye_2
    right_eye = eye_1

# Central points of the rectangles
left_eye_center = (int(left_eye[0] + (left_eye[2]/2)),
                   int(left_eye[1] + (left_eye[3]/2)))
'''(63, 104)'''
left_eye_center_x = left_eye_center[0]
left_eye_center_y = left_eye_center[1]

right_eye_center = (int(right_eye[0] + (right_eye[2]/2)),
                   int(right_eye[1] + (right_eye[3]/2)))
'''(138, 74)'''
right_eye_center_x = right_eye_center[0]
right_eye_center_y = right_eye_center[1]

# 포인트가 제대로 나오는지 확인하기
cv2.circle(roi_color, left_eye_center, 5, (255,0,0), -1) # 크기5, 튜플형태로 들어간다
            # = (roi_color, (left_eye_center_x, right_eye_center), 5, ...)
cv2.circle(roi_color, right_eye_center, 5, (255,0,0), -1)
cv2.line(roi_color, right_eye_center, left_eye_center, (0,250,250), 2)

if left_eye_center_y > right_eye_center_y:
    A = (right_eye_center_x, left_eye_center_y)
    direction = -1 # 정수 -1 : 이미지가 시계방향으로 회전함을 나타낸다.
else:
    A = (left_eye_center_x, right_eye_center_y)
    direction = 1           # 반시계 방향

cv2.circle(roi_color, A, 5, (255,0,0), -1)  # 눈 2 개 점과 이어줬을 때 직각삼각형이 되도록 하는 점 찍기.
cv2.line(roi_color, left_eye_center, A, (0,200,200), 2)
cv2.line(roi_color, right_eye_center, A, (0,200,200), 2)

# 각도 구하기
# np.arctan() :  함수 단위가 라디안 단위.
# 라디안 단위 : 각도 = (theta * 80) / np.pi
delta_x = right_eye_center_x - left_eye_center_x
delta_y = right_eye_center_y - left_eye_center_y
angle = np.arctan(delta_y / delta_x)    # 각도 구하기 : 라디안 단위
angle = (angle * 180) / np.pi           # 우리가 아는 각도로 나온다.  -21.80140948635181도

h, w = img.shape[:2]    # = h, w, _ = img.shape
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, (angle), 1.0)
rotated = cv2.warpAffine(img, M, (w,h))

cv2.imshow('face', rotated)
cv2.waitKey(0)
