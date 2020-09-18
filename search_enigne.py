from bs4 import BeautifulSoup
import requests

#for Headline
import pyfiglet

#search
search = input("Search Here: ")

URL = "https://en.wikipedia.org/wiki/" + search

#Get url
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

tag = soup.find_all("p")

#parse <p> tags
para1 = tag[1].get_text()
para2 = tag[2].get_text()

#Headline
print(pyfiglet.figlet_format(search) + "\n")

#paragraphs
print(para1 + "\n")
print(para2)
