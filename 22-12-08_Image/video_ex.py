import cv2

##### 동영상 속성 확인 #####
cap = cv2.VideoCapture('video01.mp4')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# 프레임 카운터 가져오기
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
'''
width: 1280.0 , height: 720.0
fps: 25.0
fram_count: 323.0
'''

##### 동영상 파일 읽기 #####
if cap.isOpened(): # 캡쳐 객체 초기화 확인. 캡쳐가 제대로 읽어졌는지 확인.
    while True: # 프레임을 한장 한장 받아서 표현
        ret, frame = cap.read()
        if ret :
            cv2.imshow('Video file show', frame)
            cv2.waitKey(25)
        else:
            break
else:
    print('비디오 파일 읽기 실패')

cap.release()
cv2.destroyAllWindows() # 전체 메모리 반환