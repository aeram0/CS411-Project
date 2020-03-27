import requests
import json


list_of_currencies = {
    "EUR": ["Spain", "Portugal", "Italy"],
    "BRL": ["Brazil"],
    "USD": ["United States", "US"]
}


def curr(country):
    for key, values in list_of_currencies.items():
        for value in values:
            if value == country:
                return key



def finding_currency(location, destination):
    crr_dest = curr(destination)
    crr_loc = curr(location)

    currencyInput = crr_dest
    parameters = {
        "base": crr_loc,
        "symbols": currencyInput
    }
    response = requests.get("https://api.exchangeratesapi.io/latest", params=parameters)
    currency = response.json()["rates"][currencyInput]

    return currency


#print(type(finding_currency("US", "Spain")))

def backend(country, location, weather, inbound, outbound, people, budget):
    # right now country is only one. We have to do something to change it into multiple countries
    crr = finding_currency(location, country)
    actual_budget = crr * int(budget)
    return crr, int(actual_budget)

print(backend("US", "Spain", "", "", "", "", "3500"))