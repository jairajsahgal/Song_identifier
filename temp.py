import requests
import json


data = {
    'url': f'https://www.mboxdrive.com/Marshmello%20ft.%20Bastille%20-%20Happier%20(Official%20Lyric%20Video)-RE87rQkXdNw.m4a',
    'return': 'spotify',
    'api_token': '239616f0e7dc8106a2165fadec751a61'
}
result = requests.post('https://api.audd.io/', data=data)
json_data = json.loads(result.text)
data=dict(json_data)
if data["status"]=="success":
	data=data["result"]
	for i in data:
		print(i, "=>" ,data[i])











else:
	print("Song not found. SORRY")