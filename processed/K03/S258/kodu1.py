mani = float(input("Sisesta aastatulu: "))
less_mani=0
if mani <6000:
    less_mani= round(mani,2)
elif 6000 <= mani <=14400:
    less_mani = 6000.00
elif 14400<mani<25200:
    glub =6000-6000*(mani-14400)/10800
    less_mani = round(glub,2)
else:
    less_mani =0.00
print(less_mani)