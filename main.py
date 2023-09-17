from bs4 import BeautifulSoup
import requests

month = input("Input a Month: ")
day = input("Input a Day: ")
year = input("Input a Year: ")
print(" ")

URL = f"https://www.hockey-reference.com/boxscores/index.fcgi?month={month}&day={day}&year={year}"
result = requests.get(URL).text
doc = BeautifulSoup(result, "html.parser")

bod = doc.body
games = bod.find_all(class_="game_summary nohover")

total = 0

for game in games:
    total += 1

print(f"{total} NHL games were played on {month}/{day}/{year}")
print(" ")

for game in games:
    x = game.find(class_="loser")
    l = x.a.string
    y = game.find(class_="loser")
    lf = y.find(class_="right").string

    z = game.find(class_="winner")
    w = z.a.string
    n = game.find(class_="winner")
    wf = n.find(class_="right").string

    print(f"{l} {lf}")
    print(f"{w} {wf}")
    print(" ")