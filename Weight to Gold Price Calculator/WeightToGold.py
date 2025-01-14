import requests

from datetime import datetime
now = datetime.today().isoformat()

api_url = "https://data-asg.goldprice.org/dbXRates/GBP"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"
}

data = requests.get(api_url, headers=headers).json()

weight = int(input("What is your weight? "))
gold_ounce = data["items"][0]["xauPrice"]
unit = input("Is that (L)b or (K)g?")
gold_conversion = gold_ounce * 35.274

if unit == "K" or unit == "k":
    your_worth = gold_conversion * weight
    print("If you were made of gold, you would weigh £" + str(your_worth) + " as of " + str(now))
elif unit == "L" or unit == "l":
    converted_weight = weight / 2.20462
    your_worth = gold_conversion * converted_weight
    print("If you were made of gold, you would weigh £" + str(your_worth) + " as of " + str(now))
else:
    print("Error you fucked up")

    
input('Press ENTER to exit')