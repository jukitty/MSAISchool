import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool
import time
import os
import urllib.request
import pandas as np


def creat_folder(directory):
    # 폴더 생성
    try :
        if not os.path.exists(directory):
            os.makedirs(directory)
        pass
    except OSError:
        print('error : Creating directory ...' + directory)

# 검색 키워드 호출
key = pd.read_csv('keyword.txt', encoding='utf-8', names=['keyword'])
keyword = []
[keyword.append(key['keyword'][x]) for x in range(len(key))]

def image_download(keywords):
    creat_folder('./' + keywords + '_high_resolution')

    # 크롬 드라이버 호출
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    chromedriver_path = 'chromedriver.exe'
    driver = webdriver.Chrome(chromedriver_path, options=options)
    driver.implicitly_wait(3)

    # 키워드 검색
    print('검색 >> ', keywords)
    driver.get('https://www.google.co.kr/imghp?h1=ko')
    keyword = driver.find_element_by_name('q') # 검색 창
    keyword.send_keys(keywords) # 키워드 작성
    keyword.send_keys(Keys.RETURN)  # 검색 버튼 클릭

    # 스크롤 내리기 -> 결과 더보기 버튼 클릭
    print("스크롤 ..... ", keywords)
    elem = driver.find_element_by_tag_name('body')
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.4)

    try:
        driver.find_element_by_xpath(
            '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input').click()
        for i in range(60):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.4)
    except:
        pass

    images = driver.find_elements_by_css_selector('img.rg_i.Q4LuWd')  # 이미지 class id 가져오기
    print(keywords + ' 찾은 이미지 개수 : ', + len(images))

    links = []
    for i in range(1, len(images)):
        try:
            print('//*[@id="islrg"]/div[1]/div['+ str(i) +']/a[1]/div[1]/img')
            driver.find_element_by_xpath(
                '//*[@id="islrg"]/div[1]/div['+ str(i) +']/a[1]/div[1]/img').click()
            links.append(driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img').get_attribute(
                'src'))
            print(keywords + ' 링크 수집 중..... number :' + str(i) + '/' + str(len(images)))
        except:
            continue

    forbidden = 0
    for k, i in enumerate(links):
        try:
            url = i
            start = time.time()
            urllib.request.urlretrieve(
                url, "./" + keywords + "_high_resolution/" + keywords + "_" + str(k - forbidden) + ".jpg")
            print(str(k + 1) + '/' + str(len(links)) + ' ' + keywords +
                  ' 다운로드 중....... Download time : ' + str(time.time() - start)[:5] + ' 초')
        except:
            forbidden += 1
            continue
    print(keywords + ' 다운로드 완료~!~!~!~!')

# ================================================================
# 실행
# ================================================================
if __name__ == '__main__':
    pool = Pool(processes=3)
    pool.map(image_download, keyword)




