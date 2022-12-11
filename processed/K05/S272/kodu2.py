def suurväike(inputString):
    def replace(text):
        from random import randint
        a = randint(1,32)
        symbol = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"[a]
        return text.replace("!",symbol).replace("\"",symbol).replace("#",symbol).replace("$",symbol).replace("&",symbol).replace("'",symbol).replace("(",symbol).replace(")",symbol).replace("*",symbol).replace("+",symbol).replace(",",symbol).replace("-",symbol).replace(".",symbol).replace("/",symbol).replace(":",symbol).replace(";",symbol).replace("<",symbol).replace("=",symbol).replace(">",symbol).replace("?",symbol).replace("@",symbol).replace("[",symbol).replace("\\",symbol).replace("]",symbol).replace("^",symbol).replace("_",symbol).replace("`",symbol).replace("{",symbol).replace("|",symbol).replace("}",symbol).replace("%",symbol)
    return replace(inputString.swapcase())