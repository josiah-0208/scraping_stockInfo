import requests
from bs4 import BeautifulSoup
# 정규표현식
import re
import json
import time

start = time.time()
# base_url = 'https://finance.naver.com/sise/sise_market_sum.naver?sosok=0'
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'}
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}


# response = requests.get(base_url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')

arr = []
result_dict = {}
# 코스피 & 코스닥 반복
for i in range(2):
    # 페이지 반복
    for j in range(12):
        # 조건부 url
        j += 1
        market_cap_res = requests.get(f'https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http%3A%2F%2Ffinance.naver.com%2Fsise%2Fsise_market_sum.naver%3Fsosok%3D{i}%26page%3D{j}%26fieldIds%3Damount%26fieldIds%3Dmarket_sum%26fieldIds%3Dper&fieldIds=amount&fieldIds=market_sum&fieldIds=per', headers=headers)
        soup = BeautifulSoup(market_cap_res.text, 'html.parser')
        # 시가총액 리스트를 뽑는다.
        market_cap_tags = soup.select('tr > td:nth-child(8)')
        
        # 시가총액이 기준을 넘긴 것 중에서, PER가 N/A이 아니면 a href에서 code를 추출하여 배열에 추가한다. 
        # 아냐 페이지 들어가서 거래대금으로 거르지 말고 여기 페이지에서도 거래대금 조건을 추가해여기서 조건을 다거르고 
        # 페이지 이동 후 추출한다.
        for market_cap_tag in market_cap_tags:
            if int(market_cap_tag.text.replace(",", "")) <= 50000 and int(market_cap_tag.text.replace(",", "")) >= 1500:
                amount_tag = market_cap_tag.find_previous()
                per_tag = market_cap_tag.find_next()
                if int(amount_tag.text.replace(",", "")) <= 20000 and per_tag.text != 'N/A':
                    code = re.search(r'code=(\d+)',market_cap_tag.find_previous_siblings()[5].find('a')['href'])
                    arr.append(code.group(1))


# phase.2

for code in arr:
    page = 1
    while True:
        detail_res = requests.get(f'https://finance.naver.com/item/board.naver?code={code}&page={page}', headers=headers)
        soup = BeautifulSoup(detail_res.text, 'html.parser')
        stock_title = soup.select_one('dt > strong').text
        print(stock_title)
        stock_title_comments = []
        title_td_tags = soup.find_all('td', class_="title")
        page_empty = False
        for td in title_td_tags:
            img_tag = td.select_one('a > img')
            if not img_tag:
                page_empty = True
                break
            a_tag = td.find('a')
            nid = re.search(r'nid=(\d+)',a_tag['href']).group(1)
            content_res = requests.get(f'https://finance.naver.com/item/board_read.naver?code={code}&nid={nid}', headers=headers)
            soup = BeautifulSoup(content_res.text, 'html.parser')
            title_content = soup.find('strong', class_='p15').text
            content = soup.select_one('#body').text
            likes = soup.find('strong', class_='_goodCnt').text
            dislikes = soup.find('strong', class_='_badCnt').text
            # comments_tag = soup.select_one('#cbox_module > div > div.u_cbox_content_wrap')
            # comments = []
            # if comments_tag:
            #     for tag in comments_tag:
            #         comments.append(tag.text)
            stock_title_comments.append({'글제목': title_content, '글내용': content, '공감': likes, '비공감': dislikes})
        result_dict[stock_title] = stock_title_comments
        if page_empty:
            break
        page += 1



with open('./result.json','w', encoding='utf-8') as f:
  json.dump(result_dict, f, ensure_ascii=False, indent=2)

print(f'{time.time()-start:.4f} sec 걸렸어요.')

# 종목명, 타이틀, 내용, 공감, 비공감, 댓글
# f'https://finance.naver.com/sise/sise_market_sum.naver?sosok={0}'
# for category in sosok1
# for page in page 쭉
# if 시가총액이 1700 넘는게 없으면 멈춘다 
# 현재 페이지에서 if 시가총액 1700이 넘고, per이 n/a가 아니면 거래대금 이상이면 넘어가기 
# a태그 href에서 코드넘버 추출해서 배열에 다 넣자
# f'https://finance.naver.com/item/board.naver?code={}&page={}' 이동
# 타이틀 요소 안에 img 태그가 있으면 크롤링 / 날짜, 제목, 내용, 공감, 비공감, 댓글들

# 구글시트, json파일 받아서 내가 html 꾸미던지


