# 컬러 히스토그램 특성 인코딩
import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'cat.jpg'
image_bgr = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

features = [] # 특성 값을 담을 리스트
colors = ['r', 'g', 'b'] # 각 컬러 채널에 대해 히스토그램을 계산

for i, channerl in enumerate(colors):
    # cv2.calcHist([이미지], [채널 인덱스], [마스크값. 없으니까 None], [히스토그램 크기], [범위:0~256])
    histogram = cv2.calcHist([image_rgb], [i], None, [256], [0,256])
    plt.plot(histogram, color=channerl)
    plt.xlim([0,256])

plt.show()
