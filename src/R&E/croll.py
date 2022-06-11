import requests, json
from pprint import pprint
from bs4 import BeautifulSoup

count = 5
URL = f"https://api.odcloud.kr/api/15086437/v1/uddi:2a82ac44-e17a-4919-ab5d-a25ba16af19c?page=1&perPage={count}&serviceKey=wcLOE96pryBRHxTyf9xmZMkDrA27j9eCiSdBrC0Yy0sFDCSVfFlnKO5%2F1gMzic8xKoiLJxppculYPA5ZMDE6Dw%3D%3D"
data = json.loads(requests.get(URL).text)
links = [x['주소'] for x in data['data']]

for url in links:
    pprint(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # pprint(soup)
    # get = soup.select_one('#content > #text')
    # pprint(get)

pprint(links)