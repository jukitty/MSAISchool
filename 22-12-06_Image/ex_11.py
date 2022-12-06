# 평균색 특성 인코딩
import cv2
import numpy as np

image_path = 'kuromi.jpg'
image = cv2.imread(image_path)
channels = cv2.mean(image)
print('channels >> ',channels)

observation = np.array([(channels[2], channels[1], channels[0])])
print('R, G, B 값의 평균 >>', observation)

