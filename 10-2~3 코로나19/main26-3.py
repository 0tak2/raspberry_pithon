import requests
import re
import json
import datetime
import tkinter
import tkinter.font

jsonFile = open('token.json', encoding='utf-8')
jsonDict = json.load(jsonFile)
token = jsonDict['token']

def getTodayData():
    today_query = datetime.datetime.now().strftime('%Y%m%d')
    today = datetime.datetime.now().strftime('%Y년 %m월 %d일')

    # [DEPRECATED] 아래 API는 2023-2-11부터 서비스 중단
    url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey={token}&pageNo=1&numOfRows=30&startCreateDt={today_query}&endCreateDt={today_query}'
    
    response = requests.get(url) 

    gubun = re.findall(r'<gubun>(.+?)</gubun>', response.text)
    incDec = re.findall(r'<incDec>(.+?)</incDec>', response.text)

    totalIndex = gubun.index('합계')

    dateLabel.config(text=today)
    totalValueLabel.config(text=incDec[totalIndex] + '명 확진')

    print('데이터를 업데이트 했습니다.')
    print('오늘 날짜: ' + today)
    print('확진자 합계: ' + incDec[totalIndex])

    window.after(60000*60, getTodayData)

window = tkinter.Tk()
window.title("COVID-19")
window.geometry("400x200")
window.resizable(False, False)

font = tkinter.font.Font(size = 30)
dateLabel = tkinter.Label(window, text="", font=font)
totalValueLabel = tkinter.Label(window, text="", font=font)
dateLabel.pack()
totalValueLabel.pack()

getTodayData()

window.mainloop()
