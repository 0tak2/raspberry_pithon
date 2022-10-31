import requests
import re
import tkinter
import tkinter.font

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1144063000"

def getLatestData(content: str) -> tuple:
    temp_list = re.findall(r'<temp>(.+)</temp>', content)
    humi_list = re.findall(r'<reh>(.+)</reh>', content)

    return (temp_list[0], humi_list[0])

def refreshLabelBy1Min() -> None:
    response = requests.get(url)
    temp, humi = getLatestData(response.text)
    labelContent = f'{str(temp)}℃ {str(humi)}%'
    
    label.config(text = labelContent)
    print("새로운 데이터를 가져왔습니다")

    window.after(60000, refreshLabelBy1Min)

window = tkinter.Tk()
window.title("TEMP HUMI DISPLAY")
window.geometry("400x100")
window.resizable(False, False)

font = tkinter.font.Font(size=30)
label = tkinter.Label(window, text=" ", font=font)
label.pack()

refreshLabelBy1Min()

window.mainloop()
