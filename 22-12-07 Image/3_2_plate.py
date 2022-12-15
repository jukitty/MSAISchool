import cv2
import matplotlib.pyplot as plt
import numpy as np

from utils import image_show_compare
from utils import image_show

img_ori = cv2.imread('car_number.png')
# img_rgb = cv2.cvtColor(img_ori, cv2.COLOR_BGR2RGB)
# img_rgb = img_ori[:,:,::-1]
# img_rgb[:,:,0]=0
# img_rgb[:,:,1]=0
#imshow(img_ori, 'Origin')
# image_show(img_rgb)

'''
channel : BGR
height : height
width : width
'''
height, width, channel = img_ori.shape
print(height, width,channel)

# Convert Image to grayscale
img_rgb = cv2.cvtColor(img_ori, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
# image_show_compare(img_rgb, img_gray)

# threshhold를 할때 가우시안(커널) 필터를 사용해 주파수를 낮춰주면 노이즈가 줄어든다.
# gray scale 명암비 차이를 부드럽게 해준다. 흐릿.
img_blurred = cv2.GaussianBlur(img_gray, ksize=(5,5), sigmaX=0)

img_blur_thresh = cv2.adaptiveThreshold(
    img_blurred,
    maxValue=255.0,
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    thresholdType=cv2.THRESH_BINARY_INV,
    blockSize=19,
    C=9 # 세부조정
)

img_thresh = cv2.adaptiveThreshold(
    img_gray,
    maxValue=255.0,
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    thresholdType=cv2.THRESH_BINARY_INV,
    blockSize=19, # odd over 3
    C=9
)
plt.figure(figsize=(10,10))
img_type = ['gray', 'blur', 'orig_thresh', 'blur_thres']
img_type_array = [img_ori, img_blurred, img_thresh, img_blur_thresh]

for idx, (name, image) in enumerate(zip(img_type, img_type_array)):
    plt.subplot(2,2,idx+1)
    plt.imshow(image, 'gray')
    plt.title(name)
plt.tight_layout()
plt.show()

