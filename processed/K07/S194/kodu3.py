def sünnikuupäev(ik):
    if ik[0] == "1" or ik[0] == "2":
        birfyear_firstdigits = "18"
    elif ik[0] == "3" or ik[0] == "4":
        birfyear_firstdigits = "19"
    elif ik[0] == "5" or ik[0] == "6":
        birfyear_firstdigits = "20"
    birfyear_lastdigits  = ik[1:3]
    birfyear_full = birfyear_firstdigits + birfyear_lastdigits
    kuunr = ik[3:5]
    if kuunr.startswith("0"):
        kuunr = int(ik[4])
    else:
        kuunr = int(kuunr)
    
    kuunimed = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni",
                "juuli", "august", "september" , "oktoober", "november", "detsember"]
    kuunimi = kuunimed[kuunr - 1]
    p2evanr = ik[5:7]
    if p2evanr.startswith("0"):
        p2evanr = ik[6]
    tervetulemsone = f"{p2evanr}. {kuunimi} {birfyear_full}"
    
    return tervetulemsone