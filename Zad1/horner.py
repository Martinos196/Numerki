def horner(xlist, x):
    wynik = 0
    for xy in reversed(xlist):    
        wynik = wynik * x + xy
    return wynik  
