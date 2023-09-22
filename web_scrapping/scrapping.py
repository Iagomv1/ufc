import pandas as pd
import requests 
from bs4 import BeautifulSoup
import re

r = requests.get('http://www.ufcstats.com/statistics/events/completed')
r_text = r.text

new_format = BeautifulSoup(r_text, 'html.parser') 

links = new_format.find_all('i', {'class': re.compile( "b-statistics__table-content")})

#most recent fight
most_recent_fight = links[0].contents[1].text

print(most_recent_fight)

#content[1] -> main event
#content[3] -> date of the event