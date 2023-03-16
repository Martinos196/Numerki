def horner(lista_wspolczynnikow, x):
    """Zwracanie wartości wybranego wielomianu z użyciem schematu Hornera

            Parametry
            ----------
            lista_wspolczynnikow : int list
                wartości współczynników wielomianu zapisane w liście
                w kolejności od stojącego przy najwyższej potędze do wyrazu wolnego
            x : float
                argument dla którego obliczamy wartość funkcji
            Dane wyjsciowe
            -------
            wynik : float
                wynik obliczeń
    """
    wynik = 0
    for item in reversed(lista_wspolczynnikow):    # pobiera współczynniki wielomianu od końca
        wynik = wynik * x + item
    return wynik    # zwrot wartosci wielomianu