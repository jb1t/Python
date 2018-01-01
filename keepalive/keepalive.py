import requests
import time


while True:
    print("Requesting home page")
    r = requests.get("http://thefullstacknerd.com")
    print("Requesting blog page")
    r = requests.get("http://thefullstacknerd.com/2017/12/31/noise-maker-ring-in-the-new-year/")
    print("Sleep for 4 minutes")
    time.sleep(240)
