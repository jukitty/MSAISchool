import cv2

large_img = cv2.imread('ex_image.png')
wartermark = cv2.imread('ex_image_logo.png')

small_img = cv2.resize(wartermark, (300,300))

x_offset = 25
y_offset = 365

x_end = x_offset + small_img.shape[0]
y_end = y_offset + small_img.shape[1]

large_img[y_offset:y_end, x_offset:x_end] = small_img
# crop = large_img[y_offset:y_end, x_offset:x_end]
# cv2.imshow('test', crop)
cv2.imshow('test', large_img)
cv2.waitKey(0)

