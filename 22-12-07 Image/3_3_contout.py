import cv2
import matplotlib.pyplot as plt
import numpy as np
from utils import image_show_compare
from utils import image_show


img_ori = cv2.imread('car_number.png')


height, width, channel = img_ori.shape
print(height, width,channel)

# Convert Image
img_rgb = cv2.cvtColor(img_ori, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)

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

contours, _ = cv2.findContours(
    img_blur_thresh, # 이진화가 잘된 이미지
    mode = cv2.RETR_LIST, # 윤곽선 따오기
    method = cv2.CHAIN_APPROX_SIMPLE  # 윤곽선 읽는 방법
)
temp_result = np.zeros((height, width, channel), dtype=np.uint8)# 컨투어 정보 그리기 위해서
#cv2.drawContours(temp_result, contours=contours, contourIdx=-1, color=(0,255,0))

contours_dict = []

for i, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)
    contours_dict.append(
        {
            'contour':contour,
            'x':x,
            'y':y,
            'w':w,
            'h':h,
            'cx':x+(w/2),
            'cy':y+(h/2)
        }
    )
    # 박스 그려주기 왼쪽 상단 좌표, 오른쪽 하단좌표
    cv2.rectangle(temp_result, pt1=(x,y), pt2=(x+w, y+h), color=(255,255,255), thickness=2)
#     cv2.imshow('temp_result', temp_result)
#     cv2.waitKey(0)
# #image_show(temp_result)

MIN_AREA = 80
MIN_WIDTH, MIN_HEIGHT = 2, 8 # 픽셀 이상이어야 한다. 수정하면서 최적 값을 찾아야한다.
MIN_RATIO, MAX_RATIO = 0.25, 0.8 # 숫자라면 최소, 최대 이 비율이다. 비율을 통해 숫자 박스인지 아닌지 확인

possible_contours = []

cnt = 0
for d in contours_dict:
    area = d['w'] * d['h']
    ratio = d['w'] / d['h']

    if area > MIN_AREA and d['w'] > MIN_WIDTH and d['h'] > MIN_HEIGHT and MIN_RATIO < ratio < MAX_RATIO:
        d['idx'] = cnt
        cnt += 1
        possible_contours.append(d)

temp_result = np.zeros((height,width,channel), dtype=np.uint8)

for d in possible_contours:
    cv2.rectangle(temp_result, (d['x'],d['y']),(d['x']+d['w'],d['y']+d['h']), (0,255,0))
#image_show(temp_result)

MAX_DIAG_MULTIPLAYER = 5
MAX_ANGLE_DIFF = 12.0
MAX_AREA_DIFF = 0.5
MAX_WIDTH_DIFF = 0.8
MAX_HEIGHT_DIFF = 0.2
MIN_N_MATCHED = 3

def find_chars(contour_list):
    matched_result_idx = []
    for d1 in contour_list:
        matched_contours_idx = []
        for d2 in contour_list:
            if d1['idx'] == d2['idx']:
                continue

            dx = abs(d1['cx'] - d2['cx'])
            dy = abs(d1['cy'] - d2['cy'])

            diagonal_length1 = np.sqrt(d1['w']**2 + d1['h']**2)
            distance = np.linalg.norm(np.array([d1['cx'], d1['cy']]) - np.array([d2['cx'], d2['cy']]))

            if dx == 0:
                angle_diff = 90
            else:
                angle_diff = np.degrees(np.arctan(dy/dx))

            area_diff = abs(d1['w'] * d1['h'] - d2['w'] * d2['h']) / (d1['w'] * d1['h']) # d1, d2의 비율
            width_diff = abs(d1['w'] - d2['w']) / d1['w']
            height_diff = abs(d1['h'] - d2['h']) / d1['h']

            if distance < diagonal_length1 * MAX_DIAG_MULTIPLAYER \
                    and angle_diff < MAX_ANGLE_DIFF \
                    and area_diff < MAX_AREA_DIFF \
                    and width_diff < MAX_WIDTH_DIFF \
                    and height_diff < MAX_HEIGHT_DIFF:
                    matched_contours_idx.append(d2['idx'])

        matched_contours_idx.append(d1['idx']) # d1박스와 d2박스가 닮았으면 넣어라

        if len(matched_contours_idx) < MIN_N_MATCHED:
            continue

        matched_result_idx.append(matched_contours_idx)
        unmatched_countour_idx = []
        for d4 in contour_list:
            if d4['idx'] not in matched_contours_idx:
                unmatched_countour_idx.append(d4['idx'])

        unmatched_countour = np.take(possible_contours, unmatched_countour_idx)
        recursive_countour_list = find_chars(unmatched_countour)

        for idx in recursive_countour_list:
            matched_result_idx.append(idx) # 비슷한 것들이 계속 들어감

        break
    return  matched_result_idx

result_idx = find_chars(possible_contours)

mached_result = []
for idx_list in result_idx:
    mached_result.append(np.take(possible_contours, idx_list))

temp_result = np.zeros((height, width, channel), dtype=np.uint8)

for r in mached_result:
    for d in r:
        cv2.rectangle(temp_result,(d['x'], d['y']),(d['x']+d['w'], d['y']+d['h']), color=(255,255,255), thickness=2)

cv2.imshow('contour box', temp_result)
cv2.waitKey(0)

### Rotate plate image
PLATE_WIDTH_PADDING = 1.3  # 1.3
PLATE_HEIGHT_PADDING = 1.5  # 1.5
MIN_PLATE_RATIO = 3
MAX_PLATE_RATIO = 10

plate_imgs = []
plate_infos = []

for i, matched_chars in enumerate(mached_result):
    sorted_chars = sorted(matched_chars, key=lambda x: x['cx'])

    plate_cx = (sorted_chars[0]['cx'] + sorted_chars[-1]['cx']) / 2
    plate_cy = (sorted_chars[0]['cy'] + sorted_chars[-1]['cy']) / 2

    plate_width = (sorted_chars[-1]['x'] + sorted_chars[-1]['w'] - sorted_chars[0]['x']) * PLATE_WIDTH_PADDING

    sum_height = 0
    for d in sorted_chars:
        sum_height += d['h']

    plate_height = int(sum_height / len(sorted_chars) * PLATE_HEIGHT_PADDING)
    print(sorted_chars[0]['cy'])
    triangle_height = sorted_chars[-1]['cy'] - sorted_chars[0]['cy']
    triangle_hypotenus = np.linalg.norm(
        np.array([sorted_chars[0]['cx'], sorted_chars[0]['cy']]) -
        np.array([sorted_chars[-1]['cx'], sorted_chars[-1]['cy']])
    )

    angle = np.degrees(np.arcsin(triangle_height / triangle_hypotenus)) # 로테이션 매트릭스 만들어주기. 원래 이미지에 행렬곱해서 회전된 이미지 받음
    rotation_matrix = cv2.getRotationMatrix2D(center=(plate_cx, plate_cy), angle=angle, scale=1.0)
    img_rotated = cv2.warpAffine(img_thresh, M=rotation_matrix, dsize=(width, height))

    img_cropped = cv2.getRectSubPix(
        img_rotated,
        patchSize=(int(plate_width), int(plate_height)),
        center=(int(plate_cx), int(plate_cy))
    )

    if img_cropped.shape[1] / img_cropped.shape[0] < MIN_PLATE_RATIO or img_cropped.shape[1] / \
            img_cropped.shape[0] < MIN_PLATE_RATIO > MAX_PLATE_RATIO: # 숫자 아닌거 한번 더 거르기
        continue

    x = int(plate_cx - plate_width / 2)
    y = int(plate_cy - plate_height / 2)
    w = int(plate_width)
    h = int(plate_height)

    for num_idx, sorted_char in enumerate(sorted_chars):
        number_crop = cv2.getRectSubPix(
            img_rotated,
            patchSize=(int(sorted_char['w']), int(sorted_char['h'])),
            center=(int(sorted_char['cx']), int(sorted_char['cy']))
        )
        plt.subplot(1, len(sorted_chars), num_idx+1)
        plt.imshow(number_crop, 'gray')
    plt.show()

    img_out = img_ori.copy()
    cv2.rectangle(img_out, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)
    cv2.imshow("test", img_cropped)
    cv2.imshow("orig", img_out)
    cv2.waitKey(0)
