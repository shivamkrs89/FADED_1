import requests
from bs4 import BeautifulSoup
import re

header = {
    'User-Agent': 'Monzilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def codeChef(user_name:str):
    codeChef_url = "https://www.codechef.com/users/" + user_name
    response = requests.get(codeChef_url, headers=header)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    print(soup.prettify())
    rating = findRating(soup)
    solved_problems = findFullySolvedProblems(soup)
    partially_problems = findPartiallySolvedProblems(soup)
    totalContests = findTotalContests(soup)
    print(totalContests)
    return [rating, solved_problems, partially_problems, totalContests]


def findRating(soup):
    tag = "a"
    query = {"class": "rating"}
    return soup.find(tag, query).text.strip().split(" ")[0]


def findFullySolvedProblems(soup):
    tag = "section"
    query = {"class":"rating-data-section problems-solved"}
    return soup.find(tag, query).find("div", {"class":"content"}).find("h5").text.strip().split(" ")[2][1:-1]


def findPartiallySolvedProblems(soup):
    tag = "section"
    query = {"class":"rating-data-section problems-solved"}
    return soup.find(tag, query).find("div", {"class":"content"}).find_all("h5")[1].text.strip().split(" ")[2][1:-1]


def findTotalContests(soup):
    tag = "section"
    query = {"class": "rating-data-section problems-solved"}
    return len(soup.find(tag, query).find("div", {"class": "content"}).find("article").find_all("p"))


codeChef("shivamkrs89")