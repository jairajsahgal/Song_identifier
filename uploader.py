import requests
import json
from bs4 import BeautifulSoup as BS
params = (
    ('expires', '1d'),
)

files = {
    'file': ('temp.mp3', open('temp.mp3', 'rb')),
}

response = requests.post('https://file.io/', params=params, files=files)

json_data = json.loads(response.text)
data=dict(json_data)


response=requests.get(data["link"])
soup=BS(response.text,"html.parser")
print(soup.prettify())


