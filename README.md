# 명품 브랜드 데이터 통합 분석 (Hermes, Louis Vuitton, Chanel, Dior)

## 프로젝트 개요
이 프로젝트는 네이버 OpenAPI(쇼핑, 뉴스)와 지리 데이터(매장 위치)를 활용하여 4대 주요 명품 브랜드의 **1) 평균 가격대**, **2) 뉴스 텍스트 기반 대중 관심도 및 감성**, **3) 지리적 매장 밀집도**를 다각도로 비교 분석하는 데이터 사이언스 프로젝트입니다. 최종적으로 세 가지 지표를 통합하여 브랜드별 포지셔닝을 시각화합니다.

<br>

## 기술 스택
- **Language**: Python 3
- **Data Analysis**: `pandas`, `numpy`, `scipy`
- **Visualization**: `matplotlib`, `folium`
- **API**: Naver OpenAPI (Search - News, Shop)

<br>

## 파일 구조 및 상세 설명

프로젝트는 크게 **[데이터 수집] - [전처리] - [분석 및 시각화]** 3단계로 구성되어 있습니다.

### 1. 데이터 수집 (Data Collection)
- `명품가격분석.py`
  - 네이버 쇼핑 API를 호출하여 특정 조건(패션잡화 > 여성가방 > 토트백, 100만 원 ~ 1억 원)을 만족하는 상품 데이터를 수집합니다.
- `에르메스_naver_news.ipynb`, `루이비통_naver_news.ipynb`, `샤넬_naver_news.ipynb`, `디올_naver_news.ipynb`
  - 네이버 뉴스 API를 활용하여 각 브랜드 관련 뉴스 기사를 크롤링하고 분석용 JSON 파일로 저장합니다.

### 2. 데이터 전처리 (Data Preprocessing)
- `read_json.py`
  - `api_shop.py`로 수집한 JSON 데이터를 읽어 들여 브랜드별 상품(토트백)의 평균 가격을 산출합니다.
- `xlsx_to_csv.ipynb`
  - 각 브랜드의 오프라인 매장 주소가 정리된 엑셀(Excel) 파일을 `pandas`, `openpyxl`, `xlrd`를 이용하여 CSV 파일로 일괄 변환합니다.

### 3. 분석 및 시각화 (Analysis & Visualization)
- `명품감성분석.ipynb`
  - 수집된 뉴스 데이터를 바탕으로 텍스트 감성 분석을 진행하여 브랜드에 대한 대중의 긍정/부정 반응(Affection)을 정량화합니다.
- `매장지리정보분석.ipynb`
  - `folium` 라이브러리를 이용하여 브랜드별 오프라인 매장의 주소 데이터를 지도 위에 시각화하고, 지역별 매장 밀집도(Density)를 계산합니다.
- `scaling_data.ipynb` 
  - 앞서 도출된 3가지 핵심 지표인 **가격(price)**, **관심도(affection)**, **밀집도(density)** 데이터를 통합합니다.
  - 데이터 스케일링(Scaling) 과정을 거쳐 브랜드별 종합 결과(Result)를 선 그래프(Line chart)로 최종 시각화하고 `sum_log.png` 파일로 저장합니다.

<br>
