import requests
from bs4 import BeautifulSoup
import re

header = {
    'User-Agent': 'Monzilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def codeForces(user_name:str):
    codeForces_url = "https://codeforces.com/profile/" + user_name
    response = requests.get(codeForces_url, headers=header)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    # print(soup.prettify())
    rating = findRating(soup)
    print(rating)
    solved_problems = findFullySolvedProblems(soup)
    print(solved_problems)
    maxrating= findMaxRating(soup)
    print(maxrating)
    codeForces_url2 = "https://codeforces.com/contests/with/"+user_name
    response2 = requests.get(codeForces_url2, headers=header)
    content2 = response2.content
    soup2 = BeautifulSoup(content2, "html.parser")
    #print(soup2.prettify())
    totalContests = findTotalContests(soup2)
    print(totalContests)
    return [rating,solved_problems,totalContests, maxrating]


def findRating(soup):
    tag = "ul"
    return soup.find_all(tag)[3].find("li").find("span").text


def findFullySolvedProblems(soup):
    tag = "div"
    query = {"class":"_UserActivityFrame_counterValue"}
    return soup.find(tag, query).text.strip().split(" ")[0]


def findMaxRating(soup):
    tag = "ul"
    return soup.find_all(tag)[3].find("li").find_all("span")[-1].text


def findTotalContests(soup):
    tag = "div"
    query = {"style": "background-color: white;margin:0.3em 3px 0 3px;position:relative;"}
    return len(soup.find(tag, query).find("table", {"class" : "tablesorter user-contests-table"}).find("tbody").find_all("tr"))


# codeForces("shivamkrs89")
# codeForces("bhaskartripathi2512")
# codeForces("adarsh__786")
# codeForces("tourist")