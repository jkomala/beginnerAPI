#mini project using API to generate APOD (Astronomy Picture of Day) using NASA API

import requests

from PIL import Image
from io import BytesIO
from datetime import datetime

api_key = "0fmKXlo4YCneIDow3lXUduT6Z42gM5eidVn14vpe" #key is default demo-key off of NASA website. I received my own api key from NASA
day = datetime(2023,3,21).date()
api_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={day}"

#Make GET request
response = requests.get(api_url)

#Process Code under 200 OK

if response.status_code == 200:
    apod= response.json() #load json response

    #Need to fix: What if its a video/Audio? (Need to import display/audio in PIL)
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


def getDate():
    date = document.getElementById("date").value
    