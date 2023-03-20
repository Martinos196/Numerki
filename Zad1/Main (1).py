import pylab as pb
import numpy as np
from funkcje import styczne, metodaBisekcji,funkcjaWartosc
from wykres import wykres

wyborKryterium = ""
lewyPrzedzial = 0
prawyPrzedzial = 0
epsilon = 0
liczbaIteracji = 0

while True:
    print("""Wybierz funkcje nieliniowa:
a- funkcja wielomianowa: 4*x^3-2*x^2-2x+5
b- funkcja trygonometryczna: 2*sin(x)
c- funkcja wykladnicza: 3^x-2
d- funkcja zlozona: sin(x)+3*x**2-4
    """)
    wybranaFunkcja = input("Wpisz a, b, c lub d: ").upper()
    if wybranaFunkcja in "ABCD":
        x = True
        while x:
            try:
                lewyPrzedzial = int(input("Wpisz lewy przedzial: "))
                x = False
            except ValueError:
                print("Bledna wartosc poczatku przedzialu")
        x = True
        while x:
            try:
                prawyPrzedzial = int(input("Wpisz prawy przedzial: "))
                x = False
            except ValueError:
                print("Bledna wartosc konca przedzialu")
        x = True
        while x:
            wyborKryterium = input("""\nWybierz kryterium zatrzymania algorytmu:
d- spelnienie warunku nalozonego na dokladnosc
i- osiagniecie zadanej liczby iteracji\n""").lower()
            if wyborKryterium in "di":
                x = False
            else:
                print("Wpisano bledna wartosc")
        x = True
        if wyborKryterium == "d":
            while x:
                try:
                    epsilon = abs(float(input("Wpisz dokladnosc epsilon: ")))
                    x = False
                except ValueError:
                    print("Wpisano bledna wartosc")
        elif wyborKryterium == "i":
            while x:
                try:
                    liczbaIteracji = int(input("Wpisz liczbe iteracji: "))
                    if liczbaIteracji > 0:
                        x = False
                        epsilon = 0
                    else:
                        print("Wpisano bledna wartosc")
                except ValueError:
                    print("Wpisano bledna wartosc")
        x = np.linspace(lewyPrzedzial, prawyPrzedzial, 1000)
        pb.plot(x, funkcjaWartosc(x, wybranaFunkcja), label='wykres funkcji f(x)')
        wynikBisekcja = metodaBisekcji(lewyPrzedzial, prawyPrzedzial, epsilon, liczbaIteracji, wybranaFunkcja)
        if wynikBisekcja is False:
            print("Metoda bisekcji: funkcja nie spelnia zalozen w danym przedziale.")
            pb.plot(False)
        else:
            pb.plot(wynikBisekcja, 0, '+', label='miejsce zerowe')
        wynikNewton = styczne(lewyPrzedzial, prawyPrzedzial, epsilon, liczbaIteracji, wybranaFunkcja)
        if wynikNewton is False:
            print("Metoda Newtona: funkcja nie spelnia zalozen w danym przedziale.")
            pb.plot(False)
        else:
            pb.plot(wynikNewton, 0, 'x', label='miejsce zerowe2')
        wykres(wynikBisekcja, wynikNewton)
    else:
        print("Wpisano bledna wartosc")
