#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
# An example from the book Automate the boring stuff with Python

import requests,os,bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok = True)
while not url.endswith('#'):
    print("Downloading page {}".format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    #Find URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("Could not find comic image.")
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        #Download the image
        print("Downloading image: {}".format(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

    #Save the image to ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    #Get the prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print("Done.")
