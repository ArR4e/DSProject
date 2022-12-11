months = {
    "01": "jaanuar",
    "02": "veebruar",
    "03": "märts",
    "04": "aprill",
    "05": "mai",
    "06": "juuni",
    "07": "juuli",
    "08": "august",
    "09": "september",
    "10": "oktoober",
    "11": "november",
    "12": "detsember"
}

century = {
    "1": "18",
    "2": "18",
    "3": "19",
    "4": "19",
    "5": "20",
    "6": "20",
    "7": "21",
    "8": "21",
}
def sünnikuupäev(id):
    return f"{id[5:7]}. {months[id[3:5]]} {century[id[:1]]}{id[1:3]}"