import requests, json
from pprint import pprint

count = 5
URL = f"https://api.odcloud.kr/api/15086437/v1/uddi:2a82ac44-e17a-4919-ab5d-a25ba16af19c?page=1&perPage={count}&serviceKey=wcLOE96pryBRHxTyf9xmZMkDrA27j9eCiSdBrC0Yy0sFDCSVfFlnKO5%2F1gMzic8xKoiLJxppculYPA5ZMDE6Dw%3D%3D"
url = requests.get(URL)
text = url.text
data = json.loads(text)

pprint(data)