import requests                                                                #this program will iterate through the comments of the first N posts on a subreddit
import csv                                                                     #It will then create a csv document that has each word, in order of how many times each was used
import time
from bs4 import BeautifulSoup


url = "https://old.reddit.com/r/AskReddit/"
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
wordBuffer = ""
wordsList = {}
linksList = []                                                                 #will be appended with the links to comments of first 100 posts 


attrs = {'class': 'thing', 'data-domain': 'self.AskReddit'}
counter = 1
                                                                               #What follows is the code to populate a list of links to the comments of all 100 posts
while counter <= 1:                                                           #How many posts will be counted
    time.sleep(2)
    for post in soup.find_all("div", attrs=attrs):

        forward_link = post.find("a", class_="title").attrs["href"]
        print(forward_link)
        linksList.append(forward_link)
        
        counter += 1
        
    next_button = soup.find("span", class_="next-button")                      #lines 24 through 27 used to go to the next page on the subreddit
    next_page_link = next_button.find("a").attrs['href']
    page = requests.get(next_page_link, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    
attrs = {'class': 'thing', 'data-type': 'comment'}
for link in linksList:
   
    time.sleep(2)                                                              #go through all of the previously created links, scraping the text from every comment
    page = requests.get(("https://old.reddit.com" + str(link)), headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    for comment in soup.find_all("div", attrs = attrs):
        wordbuffer += comment.find('div', class_='md').p
        print(wordbuffer.get_text())
    
    