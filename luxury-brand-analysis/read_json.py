#가격측정2
import json

brand = input('브랜드 명을 입력하시오 : ')

with open('%s_naver_shop.json' % (brand), 'r',  encoding='utf-8') as f :
    data = json.load(f)

lprice_sum = 0
i = 0

while i < 100 :
    lprice_sum += data[i]['lprice']
    i += 1

lprice_mean = lprice_sum / i

print('%s의 토트백 평균가는 %d원 입니다.' % (brand,lprice_mean))