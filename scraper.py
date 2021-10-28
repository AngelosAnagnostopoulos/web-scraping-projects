#! python3
# An introduction to scrapping by youtuber Corey Schafer

import requests, os,csv
from bs4 import BeautifulSoup

"""
Bs4 quick tutorial in a mock index.html webpage
with open('index.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    soup.prettify() #Makes html more readable, as one would write it in code

match = soup.title
#soup.tag returns a tag with the brackets <tag>, <\tag>
#soup.tag.text returns just the text inside it.
#This method only returns the first instance, for a specific instance, use find()

match = soup.find('div', class_='footer')
#Inspect elements to get information as to what to put in the soup

article = soup.find('div', class_='article')
headline = article.h2.a.text #Returns the text of the link of the article header
summary = article.p.text #All the headline's text in the paragraph of the div

#Use find_all() to return a list of all instances
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    summary = article.p.text
    #Modify the data
"""

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')
csv_file = open('cms_scrape.csv', 'w+')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

for article in  soup.find_all('article'):
    headline = article.h2.a.text
    summary = article.find('div', class_='entry-content').p.text
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4].split('?')[0] #Getting youtube video link ID from it's link
        yt_link = f'https://youtube.com/watch?v={vid_id}'

    except TypeError:
        print("Video not found, continuing")
        yt_link = None
        continue

    rint(yt_link)
    csv_writer.writerow([headline,summary,yt_link])

csv_file.close()

