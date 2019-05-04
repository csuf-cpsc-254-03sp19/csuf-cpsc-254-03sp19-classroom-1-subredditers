import requests                                                                #this program will iterate through the comments of the first N posts on a subreddit
import csv                                                                     #It will then create a csv document that has each word, in order of how many times each was used
import time
import re
import string
from bs4 import BeautifulSoup

thisSub = "Music"

url = "https://old.reddit.com/r/" + thisSub + "/"
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
wordsList = {}
linksList = []                                                                 #will be appended with the links to comments of first 100 posts 


attrs = {'class': 'thing', 'data-context' : 'listing'}
counter = 1
                                                                               #What follows is the code to populate a list of links to the comments of all 100 posts
while counter <= 19:                                                            #How many posts will be counted
    time.sleep(1)
    for post in soup.find_all("a", class_="bylink comments may-blank"):

        forward_link = post.attrs["href"]
        print(forward_link)
        linksList.append(forward_link)
        
        counter += 1
        
    next_button = soup.find("span", class_="next-button")                      #lines 24 through 27 used to go to the next page on the subreddit
    next_page_link = next_button.find("a").attrs['href']
    page = requests.get(next_page_link, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    
attrs = {'class': 'thing', 'data-type': 'comment'}

for link in linksList:
   
    time.sleep(1)                                                              #go through all of the previously created links, scraping the text from every comment
    page = requests.get(str(link), headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    for comment in soup.find_all("div", attrs = attrs):
        wordBuffer = comment.find('div', class_='md').get_text()
        wordBuffer = str.split(wordBuffer)
        for word in wordBuffer:
            word = re.sub(r'\W+', '', word)
            word = word.lower()
            if word in wordsList:
                wordsList[word] += 1
            else:
                wordsList[word] = 1
                
with open((thisSub + ".csv"), 'w') as csvfile:
    subWriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for key, value in sorted(wordsList.items(), key=lambda item: item[1], reverse = True):
        subWriter.writerow([key, value])

csvfile.close()
