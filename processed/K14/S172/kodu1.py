def rek_abs(pikk_jar):
    for i in range(0, len(pikk_jar)):
        if isinstance(pikk_jar[i], list):
            pikk_jar[i] = rek_abs(pikk_jar[i])
        else:
            pikk_jar[i] = abs(pikk_jar[i])
            
    return pikk_jar

    