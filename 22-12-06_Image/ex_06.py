import cv2

# 이미지 경로
image_path = 'cat.jpg'
# 이미지 읽어오기
image = cv2.imread(image_path)

# 회전시키기
img90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE) # 시계방향으로 90도
img180 = cv2.rotate(image, cv2.ROTATE_180) # 180도
img270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE) # 270도 = 반시계방향 90도

cv2.imshow('Original Image', image)
cv2.imshow('Rotate_90', img90)
cv2.imshow('Rotate_180', img180)
cv2.imshow('Rotate_270', img270)

cv2.waitKey(0)