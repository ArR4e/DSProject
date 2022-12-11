import csv


def get_prices():
    with open('taksohinnad.txt', newline='', encoding="UTF-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        companies = dict()
        for row in spamreader:
            companies[row[0]] = [float(row[1]), float(row[2])]
        return companies


def get_cheapest(prices, km):
    try:
        priceList = dict()
        for co in prices:
            priceList[co] = prices[co][0]+prices[co][1]*km

        return min(priceList, key=priceList.get)
    except:
        return None

trip = float(input("Sisesta tee pikkus (km): "))
print(f"Kõige odavam on {get_cheapest(get_prices(), trip)}.")