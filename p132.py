from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/sebastianfranciosi/Desktop/p127/chromedriver")
browser.get(START_URL)
time.sleep(10)
headers = ["Proper_name", "Bayer_designation", "Distance", "stellar_magnitude", "discovery_date", "hyperlink", "planet_type", "planet_radius", "orbital_radius", "orbital_period", "eccentricity"]
planet_data = []
new_planet_data = []

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page=requests.get(url)
soup=bs(page.text,'htmp.parser')
star_table=soup.final_all('table')
table_rows=star_table[7].find_all('tr')

df = df[df['Proper_name'].notna()]
df = df[df['Distance'].notna()]

del df["Distance"]
del df["discovery_date"]
del df["orbital_radius"]

gravity = (float(planet_masses[index])*1.989e+30) /
(float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*63710
00) * 6.957e+8

planet_masses.append()

find_all()