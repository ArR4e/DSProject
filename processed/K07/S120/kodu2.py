# nimi,sisestumise hind, km hind

with open('taksohinnad.txt', encoding='utf8') as f:
    lines = f.readlines()
    price_codes = [i.strip().split(',') for i in lines]

def get_price(prices, km):
    if len(prices) == 0:
        return None
    best_price = float(prices[0][1]) + float(prices[0][2]) * km
    best_firm = prices[0][0]
    for firm in prices:
        current_price = float(firm[1]) + float(firm[2]) * km
        if current_price < best_price:
            best_firm = firm[0]
            best_price = current_price
    return best_firm


km = float(input('Sisesta tee pikkus kilomeetrites: '))

print(f'Kõige odavam on {get_price(price_codes, km)}.')