import requests

from_currency= input("Enter the original currency \n").upper() #drop1.get().upper()
to_currency =  input("Enter the new currency\n").upper()

amount = float(input("enter the amount"))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from{from_currency}&to{to_currency}"
)

print(f"{amount} {from_currency} is {response.json()['rates'][from_currency]} {to_currency}")