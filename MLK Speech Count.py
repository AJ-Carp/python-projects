from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = "http://www.analytictech.com/mb021/mlk.htm"
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")

#all paragraphs saved to variable
mlk_speech = soup.find_all("p")

#removing tags and making each paragraph an element of the list
speech_combined = [p.text for p in mlk_speech]

#joining all paragraphs in one string and seperating them with a space
string_speech = " ".join(speech_combined)

# removing "\r\n"
string_speech_cleaned = string_speech.replace("\r\n", " ")

#removing punctuation 
string_no_punc = re.sub(r"[^\w\s]", "", string_speech_cleaned)

#making speech all lower case letters and saving to variable
speech_lower = string_no_punc.lower()

# for every one or more space we seperate as own elemnt of list 
speech_broken_out = re.split(r"\s+", speech_lower)

df = pd.DataFrame(speech_broken_out).value_counts()

#exporting df to csv file and changing header and index_label
df.to_csv(r"/Users/ajcarpinello/Desktop/web scraping\MLK_Speech_counts.csv", header = ["Counts"], index_label = ["Word"])