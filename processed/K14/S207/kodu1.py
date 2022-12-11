def rek_abs(lists):
    collection = []
    for item in lists:
        if isinstance(item, list):
            collection += [rek_abs(item)]
        else:
            collection += [abs(item)]
    return collection