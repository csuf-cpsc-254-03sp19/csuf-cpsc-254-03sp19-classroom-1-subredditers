import requests                                                                
import csv
import time
import re
from bs4 import BeautifulSoup

#this program will iterate through the comments of the first 20 posts on a subreddit
#It will then create a csv document that has each word, with a count of how many times it was mentioned

def SubtoCSV(thisSub):

    url = "https://old.reddit.com/r/" + thisSub + "/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    wordsList = {} #this will hold all words mentioned, with a corresponding value meaning how many times it was used
    linksList = [] #this will hold all the links to the comments sections we need                                


    attrs = {'class': 'thing', 'data-context' : 'listing'}
    counter = 1
    
    #The following while loop generates a list object full of links to all the comment sections of the first 20 posts                                                                          
    #20 is an arbitrary number that we decided to use just for time sake
    while counter <= 20:                                                       
        time.sleep(1) #a rest between searches so that we don't overload the subreddit
        for post in soup.find_all("a", class_="bylink comments may-blank"):

            forward_link = post.attrs["href"]
            print(forward_link)
            linksList.append(forward_link)
        
            counter += 1
        #moves onto the next page of the subreddit  
        next_button = soup.find("span", class_="next-button")
        next_page_link = next_button.find("a").attrs['href']
        page = requests.get(next_page_link, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
    
    attrs = {'class': 'thing', 'data-type': 'comment'}

    #go through all of the previously created links
    for link in linksList:
        
        #create a new "beautifulsoup" object from the current link
        time.sleep(1)
        page = requests.get(str(link), headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        #for every comment on the new webpage, get the text
        for comment in soup.find_all("div", attrs = attrs):
            wordBuffer = comment.find('div', class_='md').get_text()
            wordBuffer = str.split(wordBuffer)
            
            #formatting junk
            for word in wordBuffer:
                word = re.sub(r'\W+', '', word)
                word = word.lower()
                
                #This bit of code here finds if the word is already in our word count
                if word in wordsList:     #if it is, we increase the count
                    wordsList[word] += 1
                else:                     #if it isn't, we make a new entry in the wordsList Dictionary object
                    wordsList[word] = 1
                
    #this while creates a CSV with the title of the subreddit, that contains the data in "wordsList"
    with open((thisSub + ".csv"), 'w') as csvfile:
        subWriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for key, value in sorted(wordsList.items(), key=lambda item: item[1], reverse = True):
            subWriter.writerow([key, value])

    csvfile.close()

