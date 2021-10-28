#! python3
# wikipediaScraper - Downloads all images in a specified wikipedia page

import sys,os,random,pprint,requests
from bs4 import BeautifulSoup

argument = str(sys.argv[1:]).split("'")[1]
arg = argument[0].upper() + argument[1:]
url = 'https://en.wikipedia.org/wiki/' + arg
os.makedirs(arg,exist_ok=True)

def scrapeWikiArticle(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    title = soup.find(id="firstHeading")
    print(title.text)
    images = {}
    ind = 0
    for image in soup.find_all("img"):

        image_link = image["src"]
        
        if image_link[0:5] != "https:":
            image_link = "https:" + image["src"]
        image_name = image_link.split("/")[-1].split("-")[-1]
        
        if image_name not in images:    
            images[image_link] = image_name
        
        try:
            res = requests.get(image_link)
            res.raise_for_status()
        except Exception as e:
            pass

        image_file = open(os.path.join(arg,os.path.basename(image_name)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)

        image_file.close()

scrapeWikiArticle(url)
