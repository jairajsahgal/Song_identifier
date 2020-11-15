import requests
import json

def getlyrics(artist,song):
	url="https://api.lyrics.ovh/v1/"+artist+'/'+song
	response = requests.get(url)
	print(response.text)
	json_data = json.loads(response.text)
	data=dict(json_data)
	return data["lyrics"]