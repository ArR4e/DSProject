avand = open("kinganumbrid.txt", "r")
line_count = 0
for line in avand:
    if avand != "\n":
        line_count += 1
avand = open("kinganumbrid.txt", "r")

def arvutamine():
    print((round(2/3 * (float(avand.readline().strip()) - 2))))
    
if line_count == 1:
    try:
        arvutamine()
    except:
        print("vigane sisend" )
        
if line_count == 2:
    try:
        arvutamine()
    except:
        print("vigane sisend" )
    try:
        arvutamine()
    except:
        print("vigane sisend" )

if line_count == 3:
    try:
        arvutamine()
    except:
        print("vigane sisend" )
    try:
        arvutamine()
    except:
        print("vigane sisend" )
    try:
        arvutamine()
    except:
        print("vigane sisend" )
        
if line_count == 4:
    try:
        arvutamine()
    except:
        print("vigane sisend" )
    try:
        arvutamine()
    except:
        print("vigane sisend" )
    try:
        arvutamine()
    except:
        print("vigane sisend" )
    try:
        arvutamine()
    except:
        print("vigane sisend" )
        
if line_count == 5:
    try:
        arvutamine()
    except:
        print("vigane sisend" )
    try:
        arvutamine()
    except:
        print("vigane sisend" )
    try:
        arvutamine()
    except:
        print("vigane sisend" )
    try:
        arvutamine()
    except:
        print("vigane sisend" )
    try:
        arvutamine()
    except:
        print("vigane sisend" )