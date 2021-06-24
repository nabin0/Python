import requests
import json
import time
from win32com.client import Dispatch


def speak(str):
    readNews = Dispatch("SAPI.SpVoice")
    readNews.Speak(str)


if __name__ == "__main__":
    jsonTxt = requests.get(
        "https://newsapi.org/v2/everything?q=keyword&apiKey=0baeb5b53b7a497bb41b4eedfba3cd43").text

    # -------- To write json into a .json file------------
    # with open("news.json", "w") as f:
    #     f.write(jsonTxt.text)

    speak("Here are the top headline for today.")
    text = json.loads(jsonTxt)
    articles = text["articles"]
    for artc in articles:
        print(artc["content"] + '\n')
        speak(artc["content"])
        time.sleep(2)
        speak("Now next headline")
        time.sleep(1)
