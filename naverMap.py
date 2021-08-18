'''
    필수 설치 라이브러리
    >> !pip install haversine

    naverMap.Geocode(*address)  # 주소 -> 좌표 변환
    naverMap.direction(**start, ***goal)  # 시작위치(좌표), 도착위치(좌표)

    parameter
    *address : 입력할 주소 (string) (ex. 서울시 강동구)
    **start : Geocode 반환 값 > 출발지
    ***code : Geocode 반환 값 > 도착지
'''

from urllib import parse
import pandas as pd
import numpy as np
import requests
import datetime
from haversine import haversine

def Geocode(address):
    '''
    parameter
        *address = string type (주소지)
    
    repeat => list형식 => [위도, 경도]  각각 string type
    '''
    try:
        url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
        queryParams =parse.urlencode({ 'query' : address,
                                       'X-NCP-APIGW-API-KEY-ID' : 'dcvrglx1m9',
                                       'X-NCP-APIGW-API-KEY' : 'PpvXvQqp9gCFZNidOvsR99oiFfgLgbpGRxk9grFT' })
        res = requests.get(url, params=queryParams)
        data=(float(res.json()['addresses'][0]['y']),float(res.json()['addresses'][0]['x']))
        return data
    except:
        print(res.json()['error']['message'])
        
def direction(start, goal):
    '''
    parameter
        *start = (float, float) (위도, 경도)
        **gaol = (float, float) (위도, 경도)

    repeat => float type 단위 km  >> 거리  
    '''
    return np.round(haversine(start, goal),2)