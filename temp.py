import requests
import json
from lyrics import getlyrics

def getlink():
	link=input("Enter")

def platforms(data):
	print("Available platforms:")
	for i in data:
		#Platforms
		if i in ["apple_music","spotify","deezer"]:
			platform(i,data[i])
def platform(platform_name,platform_content):
	# print(platform_name,"->",platform_content)
	if platform_name=="apple_music":
		print("Apple Music\n",platform_content["url"])
	if platform_name=="deezer":
		print("Deezer","\n",platform_content["link"])
	if platform_name=="spotify":
		temp=platform_content["external_urls"]
		print("Spotify","\n",temp["spotify"])





data = {
    'url': "http://s000.tinyupload.com/index.php?file_id=83506311356586439225",
    'return': 'spotify,apple_music,deezer',
    'api_token': '239616f0e7dc8106a2165fadec751a61'
}
result = requests.post('https://api.audd.io/', data=data)
json_data = json.loads(result.text)
data=dict(json_data)

if data["status"]=="success":
	data=data["result"]
	platforms(data)
	print("")
	print("Artist","\n",data["artist"])
	print("Album","\n",data["album"])
	print("Released Date","\n",data["release_date"])
	print("Label","\n",data["label"])

	print(data.keys())
	
else:
	print("Song not found. SORRY")
