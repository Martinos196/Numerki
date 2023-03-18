import pylab as pb  # do generowania wykresu
import numpy as np  # do obliczeń trygonometrycznych oraz generowania argumentów funkcji do stworzenia wykresu
from metody import newton, metoda_bisekcji,funkcja_wart
from wykres import pokaz



menu = True
i = 1
wybor_kryterium = ""
lewy_przedzial = 0
prawy_przedzial = 0
eps = 0
liczba_iteracji = 0

while menu:
    print("""Witaj w programie obliczajacym rozwiazania rownan liniowych metoda bisekcji:
            A- funkcja wielomianowa: 4*x^3-2*x^2-2x+5
            B- funkcja trygonometryczna: 2*sin(x)
            C- funkcja wykladnicza: 3^x-2
            D- funkcja zlozona: sin(x)+3*x**2-4
            """)
    wybor_funkcji = input("Wpisz A, B, C lub D, wybierz Q zeby zakonczyc: ").upper()
    # wybor funkcji wielomianowej, trygonometrycznej, wykladniczej lub zlozonej
    if wybor_funkcji == "Q":
        menu = False
        print("Zamkniecie programu...")
    elif wybor_funkcji in "ABCD":
        jest = False
        while jest is False:
            try:
                lewy_przedzial = int(input("Podaj lewy przedzial: "))   # wybor przedzialu funkcji
                jest = True
            except ValueError:
                print("Podaj prawidlowa calkowita liczbowa wartosc poczatku przedzialu")
        else:
            jest = False
        while jest is False:
            try:
                prawy_przedzial = int(input("Podaj prawy przedzial: "))   # wybor przedzialu funkcji
                jest = True
            except ValueError:
                print("Podaj prawidlowa calkowita liczbowa wartosc konca przedzialu")
        else:
            jest = False
        while jest is False:
            wybor_kryterium = input("""Wybierz kryterium zatrzymania algorytmu:
                d- spelnienie warunku nalozonego na dokladnosc
                i- osiagniecie zadanej liczby iteracji\n""").lower()
            if wybor_kryterium in "di":
                jest = True
            else:
                print("Prosze podac prawidlowa wartosc: d lub i (wielkosc liter nie ma znaczenia)")
        jest = False
        if wybor_kryterium == "i":      # wybór kryterium końca obliczeń, gdy wybrano liczbe iteracji
            while jest is False:
                try:
                    liczba_iteracji = int(input("Podaj liczbe iteracji: "))
                    if liczba_iteracji > 0:
                        jest = True
                        eps = 0
                    else:
                        print("Podaj prawidlowa calkowita dodatnia wartosc liczby iteracji")
                except ValueError:
                    print("Podaj prawidlowa calkowita dodatnia wartosc liczby iteracji")
            else:
                jest = False
        elif wybor_kryterium == "d":       # gdy wybrano dokladnosc obliczen
            while jest is False:
                try:
                    liczba_iteracji = 0
                    eps = abs(float(input("Podaj dokladnosc epsilon: ")))
                    jest = True
                except ValueError:
                    print("Podaj prawidlowa liczbowa wartosc dokladnosci epsilon")
        x = np.linspace(lewy_przedzial, prawy_przedzial, 1000)   # generowanie argumentów funkcji
        pb.plot(x, funkcja_wart(x, wybor_funkcji), label='wykres funkcji f(x)')    # generowanie wykresu funkcji
        wynik_bisekcja = metoda_bisekcji(lewy_przedzial, prawy_przedzial, eps, liczba_iteracji, wybor_funkcji)
        # obliczenie rozwiazania wg metody bisekcji
        if wynik_bisekcja is False:
            # gdy funkcja przyjmuje te same znaki na obu końcach przedziału dla metody bisekcji
            print("Metoda bisekcji: funkcja nie spelnia zalozen w danym przedziale.")
            pb.plot(False)
        else:     # sprawdzenie czy miejsce zerowe zostało poprawnie obliczone i istnieje, sprawdzenie założeń
            pb.plot(wynik_bisekcja, 0, '+', label='miejsce zerowe')
            # generowanie miejsca zerowego na wykresie dla metody bisekcji
        wynik_newton = newton(lewy_przedzial, prawy_przedzial, eps, liczba_iteracji, wybor_funkcji)
        if wynik_newton is False:
            # gdy funkcja przyjmuje te same znaki na obu końcach przedziału dla metody Newtona
            print("Metoda Newtona: funkcja nie spelnia zalozen w danym przedziale.")
            pb.plot(False)
        else:
            pb.plot(wynik_newton, 0, 'x', label='miejsce zerowe2')
            # jeśli rozwiazanie obliczono poprawnie to pokaz je na wykresie, metoda Newtona
        pokaz(wynik_bisekcja, wynik_newton)
        i += 1
    else:
        print("Prosze podac prawidlowa wartosc spomiędzy: a, b, c, d lub q (wielkosc liter dowolna)")
