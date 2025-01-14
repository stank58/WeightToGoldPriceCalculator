import requests
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'en_GB')

now = datetime.today().strftime('%d-%m-%Y')
def format_currency(amount):
    return locale.currency(amount, grouping=True)

api_url = "https://data-asg.goldprice.org/dbXRates/GBP"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"
}

data = requests.get(api_url, headers=headers).json()

print("Weight To Gold Calculator")

while True:
    while True:
        try:
            weight = float(input("What is your weight?: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Error: Please enter just a number.")
    
    gold_ounce = data["items"][0]["xauPrice"] #pulls the data from the api for the price at the beginning of the morning.
    newdate = data["date"]
    gold_conversion = gold_ounce * 32.1507 #this is the calculation as the API pulls in ounces and the weight we want is in KG.

    while True:
        unit = input("Is that (L)b or (K)g?")
        if unit == "K" or unit == "k":
            your_worth = gold_conversion * weight
            total = format_currency(your_worth)
            gold_total = format_currency(gold_conversion)
            print("If you were made entirely of gold, you would weigh " + str(total) + " based on the gold price of " + str(gold_total) + " per kg as of " + str(newdate))
            break
        elif unit == "L" or unit == "l":
            converted_weight = weight / 2.20462
            your_worth = gold_conversion * converted_weight
            total = format_currency(your_worth)
            gold_total = format_currency(gold_conversion)
            print("If you were made entirely of gold, you would weigh " + str(total) + " based on the gold price of " + str(gold_total) + " per kg as of " + str(newdate))
            break
        else:
            print("Error: Please enter only L or K.")

    again = input("Thank you again for using this calculator, would you like to try again? (y or n)")

    while(again != "n") and (again != "y"):
        again = input("Please type a valid response. Would you like to try again? Please type y for yes or n for no-")

    if again == "n" :
        input("(Press Enter to Exit)")
        break
    elif again == "y" :
        continue