import cv2
import matplotlib.pyplot as plt

# image loading and input image -> gray
img = cv2.imread('Billiards.png', cv2.IMREAD_GRAYSCALE)

# 임계값 연산자의 출력을 mask라는 변수에 저장
# 230보다 작으면 모든 값 흰색 처리, 크면 모든 값 검은색.
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

titles = ['image', 'mask']
images = [img, mask]

for i in range(2): # 2 : 이미지, 마스크
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()