import numpy as np

# 실행 마다 결과 동일하도록
# 랜덤한 값이 실행할때 마다 변경되지 않도록 Seed 만들기
np.random.seed(950918)
print(np.random.randint(0, 10, (2, 3)))
