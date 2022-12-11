aastatulu = input("Sisesta aastatulu: ")

maksuvaba = 0
try:
    if float(aastatulu) < 6000:
        maksuvaba = aastatulu

    if 6000 <= float(aastatulu) < 14400:
        maksuvaba = 6000

    if 14400 <= float(aastatulu) < 25200:
        maksuvaba = 6000 - (6000/10800)*(float(aastatulu)-14400)

    if float(aastatulu) >= 25200:
        maksuvaba = 0

except:
    print("Tekkis viga!")

finally:
    print(f"Maksuvaba tulu on {round(float(maksuvaba), 2)} eurot.")