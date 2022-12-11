#poolik
def väljasta_liin(eellane, järglane, sõnastik):
    if järglane == sõnastik.get(eellane):
        return True
    else:
        järglane = sõnastik[järglane]
        return väljasta_liin(eellane, järglane, sõnastik)
print(väljasta_liin("Maris", "Kalle",
{'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari')}))