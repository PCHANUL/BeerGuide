import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.ratebeer.com/Places/FindPlacesByCity.asp?CountryID=111&StateID=0&City=Seoul&Show=1',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')


pubs = soup.select('#rbbody > div.container-fluid.shaded > div > div.col-sm-12.col-lg-offset-1.col-lg-8 > div > table > tbody > tr')
print(pubs)

for pub in pubs:

    a_tag = pub.select_one('td > span > h3 > a')
    if a_tag is not None:

        print (a_tag.text)

