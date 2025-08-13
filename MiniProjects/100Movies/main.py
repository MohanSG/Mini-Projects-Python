from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empirewebsite = response.text

soup = BeautifulSoup(empirewebsite, 'html.parser')
movie_list = []

contents = soup.find_all("span", class_="content_content__i0P3p")
for content in contents:
    heading = content.find("h2")
    if heading is not None:
        movie_title = heading.find("strong")
        if movie_title is not None:
            movie_list.append(movie_title.text)

movie_list.reverse()

with open("movies.txt", "w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")



# response = requests.get("https://news.ycombinator.com/")
# ycwebsite = response.text
#
# soup = BeautifulSoup(ycwebsite, "html.parser")
#
# heading_tags = soup.find_all("span", class_='titleline')
#
# article_score = [vote.text.split(" ")[0] for vote in soup.find_all("span", class_="score")]
# article_titles = [heading.text.split(" (")[0] for heading in heading_tags]
# article_links = [link.contents[0]['href'] for link in heading_tags]
# highest_voted_index = 0
#
# for index in range(len(article_score)):
#     if article_score[index] > article_score[highest_voted_index]:
#         highest_voted_index = index
#
# print(f"The article with the most votes is {article_titles[highest_voted_index]} with a score of {article_score[highest_voted_index]}")