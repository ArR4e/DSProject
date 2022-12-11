def loetleFilmid(genre):

    try:

        films = []
        file = open("filmid.txt", "r", encoding="UTF-8")
        #loop through lines in file
        for line in file:
            #create a list of current line
            currentline = line.split(" - ")
            #compare the genre on position cuurentline[1] of the list
            # to the supplied genre argument
            if currentline[1].strip() == genre:
                #Found film with correct genre, append to returnable list
                films.append(currentline[0])
        file.close()
        return films
    except Exception as e:
        print(e)

def lisaFilm(name, genre):

    try:
        file = open("filmid.txt", "a", encoding="UTF-8")
        #Write the suuplied film and genre to the file
        #in the correct format
        file.write(f"\n{name} - {genre}")
        file.close()
    except Exception as e:
        print(e)

def kustutaFilm(name):

    #This method is quite inefficient, it reads the whole filmid.txt file into memory
    #and loops twice through the list.
    
    #Ma proovisin mitu tundi teha seda meetodit kasutamata mmällu lugemist,
    #aga ei leidnud lahendust. Proovisin mitut viisi, näiteks ühes tsüklis lugeda
    #ja kirjutada üle eelnevaid ridu, kasutasin selleks seek() meetodit ja see läks
    #väga keeruliseks, seega andsin alla ja tegin mälu kasutava lihtsama järgneva lahenduse.
    #Hea meelega sooviks õppida, kuidas seda meetodit mällu lugemiseta kirjutada!
    #Sest hetkel ma loen faili mällu, töötlen tsüklina mälus ja siis kirjutan uue tsüklina,
    #ehk siis põhimõtteliselt 3n, ehk aeg on O(n) aga mälu on ka O(n). Tahaks mälu O(1) vms

    try:
        file = open("filmid.txt", "r", encoding="UTF-8")
        #Read the file into a list/memory and close file immediately afterwards
        films = file.readlines()
        file.close()

        #Loop through each item in films list
        for film in films: 
            #Split the line to a list and compare the film name on index 0
            #to the supplied film name string
            if film.split(" - ")[0] == name:
                #On string match, remove this film from film list
                films.remove(film)

        #Open file again for writing
        file = open("filmid.txt", "w", encoding="UTF-8")

        #find the length of the films list that was used earlier in deletion,
        #here the list length is equal to original - 1, the deleted film
        #The updated length is needed to remove the last newline at the end
        #of the file rewriting process to keep the correct format inside the file
        length = len(films)
        
        #Loop through the now processed films list using enumerate,
        #to keep track of cuurent line number, as it is needed to remove the
        #last newline
        for index,film in enumerate(films):
            #If we are not at the last film, write normally
            #as the film string already has a newline embedded
            if not index == length - 1:
                file.write(film)
            else:
                #Strip the newline argument from the last film to
                #keep the file in correct format
                file.write(film.strip())

        #Close file after write operation
        file.close()

    except Exception as e:
        print(e)
