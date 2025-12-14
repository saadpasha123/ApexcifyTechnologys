import requests
from bs4 import BeautifulSoup
url = "https://www.instagram.com/prmldmeak_media/reels/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.string
with open("webpage_title.txt", "w") as file:
    file.write(title)
print(f"Webpage title saved: {title}")
