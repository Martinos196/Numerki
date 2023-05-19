def horner(lista_wspolczynnikow, x):
    wynik = 0
    for item in reversed(lista_wspolczynnikow):  
        wynik = wynik * x + item
    return wynik    