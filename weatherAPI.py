from urllib import parse
import pandas as pd
import requests
import datetime

'''
    weatherAPI.load(*start, **code) 
    
    parameter
    *start : 시작일자 입력 (string) (ex. 20200701)
    **code : *날씨별지역코드 폴더에서 코드입력 (string)
'''

# class로 했어야 했는데 넘나 귀찬..
def check_null(dic): 
    if len(dic['avgTa'])==0:
        dic['avgTa']=0.0
    if len(dic['sumRn'])==0:
        dic['sumRn']=0.0
    if len(dic['avgWs'])==0:
        dic['avgWs']=0.0
    if len(dic['avgRhm'])==0:
        dic['avgRhm']=0.0
    return dic

# 위치, 날짜, 평균기온, 일강수량, 평균풍속, 평균상대습도
def Weathers(weather_df, startdt, enddt,  station,  yesterday):
    try:
        enc_key='xJqcekPN2GS33RwoLWGuWQx9elptv0GMsruCz3/y8J6XNwoMpyxx9x6HxS3UfXxgYtMZ0pSL3jRLhUB7el44Ig=='
        url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?'
        queryParams =parse.urlencode({ 'ServiceKey' : enc_key,
                                       'numOfRows' : '100',
                                       'dataType' : 'JSON', 
                                       'dataCd' : 'ASOS', 
                                       'dateCd' : 'DAY', 
                                       'startDt' : startdt, 
                                       'endDt' : enddt, 
                                       'stnIds' : station })
        res = requests.get(url, params=queryParams)
        for dic in res.json()['response']['body']['items']['item']:
            temp={}
            dic=check_null(dic)
            temp['location']=dic['stnNm']
            date=datetime.datetime.strptime(dic['tm'], '%Y-%m-%d')
            temp['date']=date.strftime('%Y%m%d')
            temp['avg_temperature(C)']=float(dic['avgTa'])
            temp['daily_rain(mm)']=float(dic['sumRn'])
            temp['avg_wind(m/s)']=float(dic['avgWs'])
            temp['avg_r_humidity(%)']=float(dic['avgRhm'])
            temp_df=pd.DataFrame.from_dict([temp])  # 리스트로 해야하는 것 잊지말자!!
            weather_df=weather_df.append(temp_df, ignore_index=True)

        check_date=datetime.datetime.strptime(weather_df.iloc[-1,1], '%Y%m%d')
        checking=check_date+datetime.timedelta(days=1)
        if (yesterday.year==checking.year) and (yesterday.month==checking.month):
            return weather_df
        else:
            return Weathers(weather_df, checking.strftime('%Y%m%d'), enddt, station,  yesterday)
    except:
        print('API error')
        
def load(start, code):
    '''
    parameter
    *start : 시작일자 입력 (string) (ex. 20200701)
    **code : *날씨별지역코드 폴더에서 코드입력 (string)
    '''
    now=datetime.datetime.now()
    yesterday = now - datetime.timedelta(days=1)
    enddt=yesterday.strftime('%Y%m%d')

    column_list=['location','date','avg_temperature(C)','daily_rain(mm)','avg_wind(m/s)','avg_r_humidity(%)']
    weather_df=pd.DataFrame(columns=column_list)
    data_df=Weathers(weather_df, start, enddt, code, yesterday)
    
    return data_df
