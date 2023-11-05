import requests
from bs4 import BeautifulSoup


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]

n = 99
while n >= 0:
    with open("100-movies-of-all-time.txt", "a") as file:
        file.write(f"{movies[n]}\n")
    n -= 1
