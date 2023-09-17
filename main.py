from bs4 import BeautifulSoup
import requests

URL = "https://www.hockey-reference.com/boxscores/index.fcgi?month=11&day=10&year=2005"
result = requests.get(URL).text
doc = BeautifulSoup(result, "html.parser")

bod = doc.body
x = bod.find(class_="game_summary nohover")

l = x.find(class_="loser")
w = x.find(class_="winner")

final = f"The {w.find_next().string} beat The {l.find_next().string}"

print(final)