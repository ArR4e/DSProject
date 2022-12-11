def sünnikuupäev(isikukood):
    numbrid_to_kuud = {
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
    
    number_to_aasta = {
        "1": "18",
        "2": "18",
        "3": "19",
        "4": "19",
        "5": "20",
        "6": "20",
        "7": "21",
        "8": "21" 
    }
    
    return f"{isikukood[5:7]}. {numbrid_to_kuud[isikukood[3:5]]} {number_to_aasta[isikukood[0]]}{isikukood[1:3]}"
