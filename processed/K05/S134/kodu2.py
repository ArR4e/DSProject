def suurväike(s):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in s:
        import string
        import random
        r = random.choice(string.punctuation)
        for ele in punc:
            s = s.replace(ele, r) 
    return(s.swapcase())
    
