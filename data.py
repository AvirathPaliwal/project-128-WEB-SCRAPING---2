import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(URL)
soup = bs(page.text, "html.parser")

star_table = soup.find_all("table")

temp_list = []

table_rows = star_table[7].find_all("tr")
for tr in table_rows:
    td_tag = tr.find_all("td")
    #rstrip()
    row = [i.text.rstrip() for i in td_tag]
    temp_list.append(row)
    
star_name = []
distance = []
mass = []
radius = []

for r in range(1,len(temp_list)):
    star_name.append(temp_list[r][0])
    distance.append(temp_list[r][5])
    mass.append(temp_list[r][7])
    radius.append(temp_list[r][8])

#homework
df = pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=["Name","Distance","Mass","Radius"])
df.to_csv("Dwarf_start.csv")


