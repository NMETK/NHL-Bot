from bs4 import BeautifulSoup
import requests
from datetime import datetime

def main():

    year = datetime.today().strftime('%Y')
    month = datetime.today().strftime('%m')
    day = datetime.today().strftime('%d')

    while True:

        ye = input("Input a Year: ")
        if ye > year:
            while True:
                print(f"{ye} hasnt happend yet")
                ye = input("Input a Year: ")
                if ye <= year:
                    break
            

        m = input("Input a Month: ")
        if ye == year and m > month:
            while True:
                print(f"Date hasnt happend yet")                # cant input single numbers, ex - 1,2,3, etc / must be 01,02,03 etc
                m = input("Input a Month: ")
                if ye ==  year and m <= month:
                    break

        d = input("Input a Day: ")
        if ye == year and m <= month and d > day:
            while True:
                print("Date hasnt happend yet")
                d = input("Input a Day: ")
                if ye == year and m <= month and d <= day:
                    break
            
        
        print(" ")

        URL = f"https://www.hockey-reference.com/boxscores/index.fcgi?month={m}&day={d}&year={ye}"
        result = requests.get(URL).text
        doc = BeautifulSoup(result, "html.parser")

        bod = doc.body
        games = bod.find_all(class_="game_summary nohover")

        total = 0

        for game in games:
            total += 1

        print(f"{total} NHL game(s) were played on {m}/{d}/{ye}")
        print(" ")

        for game in games:
            x = game.find_all('a')
            for each in x:
                if each.string == None:
                    continue
            
            print(each.string)
            print(" ")
            
        xy = input("Would you like to input another date? (Y/N) ")

        if xy.upper() == "N":
            quit()
        if xy.upper() == "Y":
            continue


if __name__ == "__main__":
    main()