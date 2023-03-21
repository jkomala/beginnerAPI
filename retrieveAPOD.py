#mini project using API to generate APOD (Astronomy Picture of Day) using NASA API

import requests

from PIL import Image
from io import BytesIO

api_key = "DEMO-KEY" #key is default demo-key off of NASA website. I received my own api key from NASA
api_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

#Make GET request
response = requests.get(api_url)

#Process Code under 200 OK

if response.status_code == 200:
    apod= response.json() #load json response

    image_url = apod["url"]
    image_title = apod["title"]
    #Download image data
    image_data = requests.get(image_url).content

    #open URL image
    image = Image.open(BytesIO(image_data))

    image.show()
    print(image_title)
else:
    print("Error:", response.status_code)

