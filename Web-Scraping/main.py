import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

website = requests.get(URL)
website_html = website.text
soup = BeautifulSoup(website_html,"html.parser")    
all_movies = soup.find_all(name = "h3",class_="jsx-2692754980")
print(all_movies)