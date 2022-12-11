maksuvaba_tulu = float(input("Sisesta aastatulu: "))
valem = round(6000 - 6000 / 10800 * (maksuvaba_tulu - 14400), 2)
if maksuvaba_tulu < 6000:
    print(f"Maksuvaba tulu on {maksuvaba_tulu} eurot.")
if maksuvaba_tulu >= 6000 and maksuvaba_tulu < 14400:
    print("Maksuvaba tulu on 6000 eurot.")
if maksuvaba_tulu >= 14400 and maksuvaba_tulu < 25200:
    print(f"Maksuvaba tulu on {valem} eurot.")
if maksuvaba_tulu > 25200:
    print("Maksuvaba tulu on 0 eurot.")