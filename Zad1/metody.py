from horner import horner
import numpy as np
import sympy as sp  # do tworzenia wzorów funkcji z parametrem oraz obliczeń pochodnych

def funkcja_wart(x, funkcja):
    """Zwracanie wartości wybranej funkcji dla argumentu x

            Parametry
            ----------
            arg_x : float
                wartosc argumentu x
            wybor  : String
                wybór funkcji A, B, C lub D
            Dane wyjsciowe
            -------
            wart_fun : float
                wartość funkcji dla argumentu x
    """
    if funkcja == "A":    # A dla funkcji wielomianowej
        wart = horner([4,2, 2, 5], x)  # obliczenie wartosci schematem hornera
    elif funkcja == "B":  # B dla funkcji trygonometrycznej
        wart = 2*np.sin(x)
    elif funkcja == "C":  # C dla funkcji wykładniczej
        wart = 3**x-2
    elif funkcja == "D":  # D dla funkcji złożonej
        wart = np.sin(x)+3*x**2-4
    else:
        print("Nie wybrano żadnej z podanych funkcji.")
        wart = None
    return wart     # zwróc wartość funkcji dla konkretnego argumentu x

def funkcja_wzor(funkcja):
    """Zwracanie wzoru funkcji z parametrem x

            Parametry
            ----------
            wybor  : String
                wybór funkcji A, B, C lub D
            Dane wyjsciowe
            -------
            wzor_fun : Symbol
                wzór funkcji zapisany ze zmienną x
    """
    x = sp.Symbol('x')
    if funkcja == "A":    # A dla funkcji wielomianowej
        wzor = horner([4,-2, 2, 5], x)     # przedstawienie funkcji w formie schematu Hornera
    elif funkcja == "B":  # B dla funkcji trygonometrycznej
        wzor = 2*sp.sin(x)
    elif funkcja == "C":  # C dla funkcji wykładniczej
        wzor = 3**x-2
    elif funkcja == "D":  # D dla funkcji złożonej
        wzor = sp.sin(x)+3*x**2-4
    else:
        print("Nie wybrano żadnej z podanych funkcji.")
        wzor = None
    return wzor     # zwroc wzór funkcji



def metoda_bisekcji(poczatek_przedzialu, koniec_przedzialu, epsilon, iteracje, wybor):
    """Przyblizone rozwiazanie f(x)=0 z uzyciem metody bisekcji

        Parametry
        ----------
        poczatek_przedzialu : int
            wartosc poczatku przedzialu badanej funkcji
        koniec_przedzialu : int
            wartosc konca przedzialu badanej funkcji
        epsilon : float
            zadana dokladnosc obliczen
        iteracje : int
            zadana maksymalna liczba iteracji
        wybor : String
            wybor funkcji między A, B, C lub D

        Dane wyjsciowe
        -------
        x1 : float
            rozwiazanie funkcji
        """
    x1 = 0
    if funkcja_wart(poczatek_przedzialu, wybor) * funkcja_wart(koniec_przedzialu, wybor) > 0:
        # założenie, które musi być spełnione aby można było skorzystać z metody bisekcji
        return False
    else:
        if iteracje <= 0:       # jeśli użytkownik wybierze obliczenia wg kryterium dokladnosci epsilon
            arg_x = sp.Symbol('x')
            df = sp.diff(funkcja_wzor(wybor))  # obliczenie pochodnej funkcji
            n = 1       # zmienna iteracyjna
            while True:  # dopóki nie uzyskamy zadanej dokładności
                x1 = (poczatek_przedzialu + koniec_przedzialu) / 2      # nadpisywanie kolejnej wartosci argumentu
                dfxn = df.subs(arg_x, x1)       # obliczenie wartosci pochodnej dla argumentu
                if abs(funkcja_wart(x1, wybor)) <= epsilon and (abs(dfxn) > epsilon):
                    # jeżeli znaleźliśmy miejsce zerowe mniejsze bądź równe przybliżeniu zera
                    # oraz funkcja w tym miejscu nie dąży do stałej wartości
                    print("Metoda bisekcji: znaleziono rozwiazanie po " + str(n) + " iteracjach.")
                    return x1
                elif funkcja_wart(x1, wybor) * funkcja_wart(poczatek_przedzialu, wybor) < 0:
                    koniec_przedzialu = x1  # nadpisywanie prawego krańca przedziału
                else:
                    poczatek_przedzialu = x1  # nadpisywanie lewego krańca przedziału
                n += 1
        else:       # jeśli użytkownik wybierze obliczenia wg kryterium liczby iteracji
            for n in range(iteracje):  # dopóki nie uzyskamy zadanej liczby iteracji
                x1 = (poczatek_przedzialu + koniec_przedzialu) / 2      # nadpisywanie argumentu funkcji
                if funkcja_wart(x1, wybor) == 0.0:       # gdy rozwiązaniem funkcji jest zero
                    print("Metoda bisekcji: znaleziono dokladne rozwiazanie epsilon= 0 po {} iteracjach.".format(n + 1))
                    return x1
                if funkcja_wart(x1, wybor) * funkcja_wart(poczatek_przedzialu, wybor) < 0:
                    koniec_przedzialu = x1  # nadpisywanie prawego krańca przedziału
                else:
                    poczatek_przedzialu = x1  # nadpisywanie lewego krańca przedziału
            epsilon = abs(funkcja_wart(x1, wybor))   # obliczenie dokładności obliczeń
            print("Metoda bisekcji: "
                  "znaleziono rozwiazanie po {0} iteracjach z dokladnoscia epsilon={1}".format(iteracje, epsilon))
            return x1    # zwracanie znalezionego miejsca zerowego


def newton(poczatek_przedzialu, koniec_przedzialu, epsilon, max_iter, wybor):
    """Przyblizone rozwiazanie f(x)=0 z uzyciem metody Newtona

    Parametry
    ----------
    epsilon : float
        warunek stopu abs(f(x)) < epsilon.
    max_iter : int
        maksymalna liczba iteracji algorytmu
    wybor : String
        wybor funkcji spomiędzy ["A", "B", "C", "D"]

    Dane wyjsciowe
    -------
    xn : float
        Implementacja metody Newtona: oblicza aproksymacje liniowa
        f(x) dla xn i znajduje x:
            x = xn - f(xn)/Df(xn)
        Kontynuacja dopoki abs(f(xn)) < epsilon i zwrot xn.
        Jesli Df(xn) == 0, zwroc None. Jesli liczba iteracji przekroczy max_iter, zwroc None.
    """

    if funkcja_wart(poczatek_przedzialu, wybor) * funkcja_wart(koniec_przedzialu, wybor) > 0:
        # sprawdzenie założeń metody Newtona
        return False
    arg_x = sp.Symbol('x')
    df = sp.diff(funkcja_wzor(wybor))       # obliczenie pochodnej wybranej funkcji
    if abs(df.subs(arg_x, poczatek_przedzialu)) < abs(df.subs(arg_x, koniec_przedzialu)):
        # blok instrukcji warunkowych ustalajacych w jakim miejscu rozpoczac algorytm,
        # eliminujemy miejsca, w których funkcja dąży do stałej wartości
        xn = koniec_przedzialu
    elif abs(df.subs(arg_x, poczatek_przedzialu)) > abs(df.subs(arg_x, koniec_przedzialu)):
        xn = poczatek_przedzialu
    else:
        xn = (poczatek_przedzialu + koniec_przedzialu) / 2
    if max_iter != 0:   # obliczenia dla wyboru kryterium liczby iteracji
        for n in range(0, max_iter):
            fxn = funkcja_wart(xn, wybor)  # obliczenie wartosci funkcji dla argumentu x
            dfxn = df.subs(arg_x, xn)   # obliczenie wartosci pochodnej dla argumentu x
            xn = xn - float(fxn / dfxn)  # kolejne wartosci argumentów
        epsilon = abs(funkcja_wart(xn, wybor))       # obliczenie dokladnosci epsilon
        print("""Metoda stycznych: 
            znaleziono rozwiazanie po {0} iteracjach z dokladnoscia epsilon={1}""".format(max_iter, epsilon))
        return xn
    else:   # obliczenia dla wyboru kryterium dokladnosci
        n = 0   # zmienna iteracyjna
        while True:
            fxn = funkcja_wart(xn, wybor)    # wartosc funkcji dla argumentu x
            dfxn = df.subs(arg_x, xn)   # obliczenie wartosci pochodnej dla argumentu x
            if (abs(fxn) < epsilon) and (abs(dfxn) > epsilon):
                # gdy wartosc funkcji jest z pewna dokladnoscia rowna zero oraz funkcja w tym punkcie nie dąży do zera
                print('Metoda Newtona: znaleziono rozwiazanie po ', n + 1, 'iteracjach.')
                return xn
            xn = xn - float(fxn / dfxn)     # kolejna wartość argumentu
            n += 1  # inkrementacja zmiennej iteracyjnej
