sõnastik = {
  'Kalle': ('Teet', 'Maris'),
  'Maris': ('Konstantin', 'Mari'),
  'Rita': ('Teet', 'Maris'),
  'Siim': ('Teet', 'Maris'),
  'Mari': ('Karl', 'Leeni'),
  'Teet': ('Joosep', 'Adele'),
  'Adele': ('Johannes', 'Leida'),
  'Konstantin': ('Viktor', 'Jelena'),
  'Joosep': ('August', 'Emma'),
  'Viktor': ('Nikolai', 'Maria')
}

def search(searchFor, dictionary):
    result = []
    for k in dictionary:
        for v in dictionary[k]:
            if searchFor == v:
                result.append(k)
    return result
    
def create_line(a, dictionary):
    children = search(a, dictionary)
    if children:
        b = []
        for child in children:
            b.append(create_line(child, dictionary))
        return [a,*b]
    else:
        return a

def find_path(input_list, elem):
    for i in range(len(input_list)):
        if isinstance(input_list[i], list):
            result = find_path(input_list[i], elem)
            if result:
                return [i] + result
        elif input_list[i] == elem:
            return [i]
        
def is_child(input_list, n):
    flat_list = []
    for sublist_or_el in input_list:
        if isinstance(sublist_or_el, list):
            if is_child(sublist_or_el, n) == True:
                return True
        elif sublist_or_el == n:
            return True
    return False
        
def toConsole(line, path):
    print(line[0])
    if len(path) > 1:
        toConsole(line[path[0]], path[1:])
    else:
        print(line[path[0]])
        return

def väljasta_liin(eellane, järglane, sugupuu):
    line = create_line(eellane, sugupuu)
    isChild = any(järglane in sublist for sublist in line)
    if is_child(line, järglane):
        path = find_path(line, järglane)
        toConsole(line, path)
        return True
    else:
        return False
