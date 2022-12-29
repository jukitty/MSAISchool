from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request

'''폴더 구성'''
def creat_folder(directory):
    try :
        if not os.path.exists(directory):
            os.makedirs(directory)
        pass
    except OSError:
        print('error : Creating directory ...' + directory)


'''키워드 입력, chromedriver 실행'''
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

keyword = 'Bengal cat'
chromedriver_path = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver_path, options=options)
# driver.implicitly_wait(5) 버전 차이로 인해 wait이 먹히지 않음. 그래서 강제로 옵션을 줌.

#####
##### 키워드 입력 selenium 실행
#####
elem = driver.get('https://www.google.co.kr/imghp?h1=ko')  # 구글 검색창 띄워진다.

# # Xpath 가져오기
# # input -> /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input
# # button -> /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button
# keyword = driver.find_element_by_xpath(
#     '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# keyword.send_keys(keyword)
# keyword.send_keys(Keys.RETURN)
# # 위 코드와 같음.
# # driver.find_element_by_xpath(
# #     '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button').click()

elem = driver.find_element_by_name('q')
elem.send_keys(keyword)
elem.send_keys(Keys.RETURN) # 검색버튼 눌러짐

##### 스크롤 자동 내리기 #####
print(keyword + '스크롤 중 .......')
elem = driver.find_element_by_tag_name('body')# 페이지 전체
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2) # 스크롤이 너무 빨리 내려가면 웹사이트에서 막아버림. 사용자처럼 스크롤 내리는 것 처럼. 0.2도 좀 빠름.

try:
    driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input').click()
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
except:
    pass

links = []
images = driver.find_elements_by_css_selector('img.rg_i.Q4LuWd') # 이미지 class id 가져오기

for image in images:
    if image.get_attribute('src') != None:
        links.append(image.get_attribute('src'))
                    # 64비트짜리 이진화 파일. Ascii코드로 바꿔준 것. 기본적으로 base64로 이미지 인코딩,디코딩.

print(keyword + '찾은 이미지 개수 : ', len(links))
#print(links)
time.sleep(2)


'''데이터 다운로드'''
creat_folder('./' + keyword + '_img_download')
for index, i  in enumerate(links):
    url = i
    start = time.time()
    urllib.request.urlretrieve(url, './' + keyword + '_img_download/' + keyword + '_' + str(index) + '.jpg')
    print(str(index) + '/' + str(len(links)) + ' ' + keyword + ' 다운로드 시간 -------- : ', str(time.time()-start)[:5] + '초')

print(keyword + '!!!다운로드 완료 !!!!!')


#
# # 검색 키워드 호출
# key = pd.read_csv('keyword.txt', encoding='utf-8', names=['keyword'])
# keyword = []
# [keyword.append(key['keyword'][x]) for x in range(len(key))]
#
# def image_download(keywords):
#     creat_folder('./' + keywords + '_low_resolution')
#
#     # 크롬 드라이버 호출
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option('detach', True)
#     chromedriver_path = 'chromedriver.exe'
#     driver = webdriver.Chrome(chromedriver_path, options=options)
#     driver.implicitly_wait(3)
#
#     # 키워드 검색
#     print('검색 >> ', keywords)
#     driver.get('https://www.google.co.kr/imghp?h1=ko')
#     keyword = driver.find_element_by_name('q') # 검색 창
#     keyword.send_keys(keywords) # 키워드 작성
#     keyword.send_keys(Keys.RETURN)  # 검색 버튼 클릭
#
#     # 스크롤 내리기 -> 결과 더보기 버튼 클릭
#     print("스크롤 ..... ", keywords)
#     elem = driver.find_element_by_tag_name('body')
#     for i in range(100):
#         elem.send_keys(Keys.PAGE_DOWN)
#         time.sleep(0.4)
#
#     try:
#         # //*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input
#         driver.find_element_by_xpath(
#             '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input').click()
#         for i in range(100):
#             elem.send_keys(Keys.PAGE_DOWN)
#             time.sleep(0.4)
#     except:
#         pass
#
#     links = []
#     links = []
#     images = driver.find_elements_by_css_selector('img.rg_i.Q4LuWd')  # 이미지 class id 가져오기
#     for image in images:
#         if image.get_attribute('src') != None:
#             links.append(image.get_attribute('src'))
#     print(keywords + ' 찾은 이미지 개수 : ', + len(links))
#     time.sleep(2)
#
#     for index, i in enumerate(links):
#         url = i
#         start = time.time() # 시작 시간
#         urllib.request.urlretrieve(url, './' + keywords + '_low_resolution/' + keywords + '_' + str(index) + '.jpg')
#         print(str(index+1) + '/' + str(len(links)) + ' ' + keywords + ' 다운로드 시간 -------- : ',
#               str(time.time() - start)[:5] + '초')
#     print('다운로드 완료 ~!~!~!~!~!~!')

