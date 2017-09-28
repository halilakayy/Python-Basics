import requests
from bs4 import BeautifulSoup
import locale

#locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")


url="http://sueadh.gov.tr/"
response= requests.get(url)


icerik=response.content
soup=BeautifulSoup(icerik, "html.parser")

for i in soup.find_all("ul", {"class":"kurumsal_ul"}):
    print(i)