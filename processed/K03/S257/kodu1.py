atulu = float(input("sisesta aasta tulu; "))
if atulu <= 6000:
    mvaba = atulu
elif 6000 <= atulu <= 14400:
    mvaba = 6000
elif 14400 <= atulu <= 25200:
    mvaba = 6000 - 6000/10800*(atulu - 14400)
elif 25200 > atulu:
    mvaba = 0
mvaba = round(float(mvaba), 2)
print("Maksuvaba tulu on", str(mvaba))