import cv2

# 이미지 경로
image_path = 'cat.jpg'
# 이미지 읽어오기
image = cv2.imread(image_path)

# 이미지 좌우:1 및 상하:0 반전
dst_temp1 = cv2.flip(image, 1)
dst_temp2 = cv2.flip(image, 0)

# cv2에선 한글 처리 안됨
cv2.imshow('dst_temp1', dst_temp1)
cv2.imshow('dst_temp2', dst_temp2)
cv2.waitKey(0)