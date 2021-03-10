#-------------------------webscrapping...   install beautifulsoup4,requests mudule
import requests
import pandas as pd
from bs4 import BeautifulSoup
page=requests.get("https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.YBpEO2PhVhE")
soup=BeautifulSoup(page.content,'html.parser')
# print(soup)  #will display all html,css,javascript
# print(soup.find_all('a'))  # to find all <a> tags of above website
week=soup.find(id='seven-day-forecast-body')
# print(week)
items=week.find_all(class_='tombstone-container') # gives all tags details of class_='tombstone-container' in list format
# print(items)
period_name=[item.find(class_="period-name").get_text() for item in items]
short_descrption=[item.find(class_="short-desc").get_text() for item in items]
tempatures=[item.find(class_="temp").get_text() for item in items]
weather_stuff=pd.DataFrame(
    {
        "period":period_name,
        "short_desc":short_descrption,
        "temp":tempatures
    }
)
# print(weather_stuff)
weather_stuff.to_csv("scrapping.csv")
