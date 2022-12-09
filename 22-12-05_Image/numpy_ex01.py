import numpy as np

# 단일 객체 저장 및 불러오기
array = np.arange(0, 10)
print(array)

# .npy 파일에 저장하기
np.save('./save.npy', array)

# 불러오기
result = np.load('./save.npy')
print('result >> ', result)
