import requests
from bs4 import BeautifulSoup

# base_url = 'https://finance.naver.com/sise/sise_market_sum.naver?sosok=0'
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'}
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

# response = requests.get(base_url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')

arr = []
# 코스피 & 코스닥 반복
for i in range(2):

    # 페이지 반복
    for j in range(12):
        # 조건부 url
        j += 1
        market_cap_res = requests.get(f'https://finance.naver.com/sise/sise_market_sum.naver?sosok={i}&page={j}', headers=headers)
        soup = BeautifulSoup(market_cap_res.text, 'html.parser')
        # 시가총액 리스트를 뽑는다.
        market_cap_tags = soup.select('tr > td:nth-child(7)')
        
        # 시가총액이 기준을 넘긴 것 중에서, PER가 N/A이 아니면 a href에서 code를 추출하여 배열에 추가한다.
        for market_cap_tag in market_cap_tags:
            if int(market_cap_tag.text.replace(",", "")) <= 50000 and int(market_cap_tag.text.replace(",", "")) >= 1500:
                code = market_cap_tag.find_previous_siblings()[4].find('a')['href']
                print(code)




# f'https://finance.naver.com/sise/sise_market_sum.naver?sosok={0}'
# for category in sosok1
# for page in page 쭉
# if 시가총액이 1700 넘는게 없으면 멈춘다 
# 현재 페이지에서 if 시가총액 1700이 넘고, per이 n/a가 아니면
# a태그 href에서 코드넘버 추출해서 배열에 다 넣자
# f'https://finance.naver.com/item/board.naver?code={}&page={}' 이동
# 거래대금 이상이면 넘어가기 
# 타이틀 요소 안에 img 태그가 있으면 크롤링 / 날짜, 제목, 내용, 공감, 비공감, 댓글들

# 구글시트, json파일 받아서 내가 html 꾸미던지


