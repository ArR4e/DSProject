import film

def töötleKäsk(cmd, args):

        if cmd == "K":
            
            print("Võimalikud filmid on:")
            #Loop through the list returned by loetlefilmid() and print each item.
            for i in film.loetleFilmid(args[0]): print(i)
            print("\n")

        elif cmd == "L":

            #call lisaFilm() method with a string formed by joining
            #all of the arguments from list into a film name,
            #we join from position 1 to max arg position to get the whole film name,
            #and avoid position 0 as it is the genre argument.
            film.lisaFilm(str(" ".join(args[1:len(args)])), args[0])
            print("Film lisatud!")
            print("\n")

        elif cmd == "V":
            
            #call kustutaFilm() with the correct string representation of
            #the movie name by joining items from args list, starting from 0,
            #and ending with the max index.
            film.kustutaFilm(str(" ".join(args[0:len(args)])))
            print("Film nimekirjast kustutatud!\nHead vaatamist!")
            print("\n")

        elif cmd == "E":
            
            #print the cool arrows
            print(">>>")

try:
    #main loop and initial print calls
    loopcondition = True
    print("=== FILMIANDMEBAAS ===")
    print("Kuva filmid: K <žanr>")
    print("Lisa film:   L <žanr> <film>")
    print("Vaata filmi: V <filmi nimi>")
    print("Lõpeta:      E")
    print("===")
    while loopcondition:

        userinput = str(input()).split(" ")
        
        töötleKäsk(userinput[0], userinput[1:len(userinput)])
        
        if userinput[0] == "E":
            loopcondition = False

except Exception as e:
    print(e)