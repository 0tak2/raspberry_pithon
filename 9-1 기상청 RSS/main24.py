import requests

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1144063000"
response = requests.get(url)

print(response.text)
