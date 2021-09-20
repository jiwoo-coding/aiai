## **AIAI project**
* **HPAI(Highly Pathogenic Avian Influenza) 발생시 시군구별 위험 수준 확산 예측 Project**
* 선행 연구 자료를 활용 및 데이터 마이닝을 통해 독립변수 및 종속변수 추출
  * 독립변수 : 시군구 간 거리, 철새수, 일별 평균온도, 일별 강수량
  * 종속변수 : 시군구 위험 수준
* Project WBS : [NOTION](https://trapezoidal-spinach-1e3.notion.site/596f31867c5a4623a754564ba49cac78?v=8f8e93bb6cdd49febaef28a3655c823d)
* Meeting Minutes : [회의록](https://trapezoidal-spinach-1e3.notion.site/0e0084b0c77f48eb911556aed084e786?v=fb9c6158b6fd4113b4fa198c80ebbe5a)
* Reference : [자료](https://trapezoidal-spinach-1e3.notion.site/bbad4dd453504c3ca165e70345cb946a?v=ace54e7b20f44467bda0105a702ef57d)
-----------------------------------------------

#### Data collection Folder
* 모델 제작을 위한 최종 Train_data set, Test_data set 제작 구현 code 

#### Data mininig Folder
* 검증된 독립변수를 모델에 구현하기 위한 Risk Table 구현 code
* 각 변수별 시행착오 포함 (과정)

#### Data preprocessing Folder
* 비정형, 정형화된 데이터 정제 구현 code
* 독립변수 가설검증 구현 code

#### model Folder
* AUTOML를 통해 선별하여 저장된 모델별 pickle 파일 수록

#### presentation Folder
* AI 개발자 양성교육 中 금번 Project의 발표 자료 수록

#### Risk_data_set Folder
* 독립변수 및 사용된 Train_data set 파일 수록
* 범주화된 변수 파일 수록

#### Sample_data Folder
* 시각화 구현을 위한 일부 가정된 data set

#### use_data Folder
* 초기 data 수집 파일
* 정제된 데이터 등 실제 코드 구현시 사용된 파일 

#### Models.ipynb
* AutoML 중 일부인 pycaret을 이용하여 top5 모델 선정 (정확도)
  * RandomForest(75%)
  * XGboost(91%)
* Train_data 일부

|month|day|시군구index|철새수(마리)|최초발생거리(km)|일평균온도(c)|일강수량(mm)|
|-----|---|-----------|-----|-----------|-------|--------|
|1|1|0|126690|0|-1.8|0.0|
* Label data 일부

|위험도(위험수준)|  
|-----|
|7.0|

#### naverMap.py
* 네이버 openAPI 중 geocode를 이용하여 주소 입력시 위치 좌표(위도, 경도) 데이터 값을 불러오는 함수 구현
  * Geocode(address)
* 두 위도, 경도 좌표를 받아 두 좌표간 거리를 구하는 함수 구현 (haversine 모듈 이용)
  * direction(start, goal)

#### weatherAPI.py
* 기상청 AOS 종관형 일별 API 호출 함수 구현
  * 시작일자와 지역코드 입력시 아래와 같은 변수데이터 추출 (use_data folder 내 지역코드 참고)
    * 위치, 날짜, 평균기온, 최저기온, 최고기온, 일강수량, 최대풍속풍향, 평균풍속, 평균상대습도 
  * load(start, code) : 시작일자와 지역코드 입력시 시작일 시점부터 현재 시점 이전날까지 DataFrame 형태로 일자별 데이터 추출
  * load2(start, final, code) : 시작일자와 종료일자, 지역코드 입력시 시작일부터 종료일까지 DataFrame 형태로 일자별 데이터 추출
