import pylab as pb
import numpy as np
from funkcje import interpolacja_wprzod, interpolacja_wstecz, wartosc_funkcji, wzor_funkcji
import sympy as sp
from horner import horner

x_pkt_inter = []
y_pkt_inter = []
liczba_wezlow_interpolacyjnych = 0
zmienna_iteracyjna = 1
lewy_przedzial = prawy_przedzial = 0
menu = True
wybor_funkcji = ""
while menu is True:
    wybor_opcji = input("""
Menu:
t: wczytanie stabularyzowanej funkcji z pliku zewnetrznego
g: wczytanie funkcji sposrod gotowych
q: wyjscie z programu
""").lower()
    if wybor_opcji == 'q':
        menu = False
        print("Zamkniecie programu")
    elif wybor_opcji in 'gt':
        jest = True
        while jest:
            try:
                lewy_przedzial = int(input("Wartosc poczatka przedzialu: "))
                jest = False
            except ValueError:
                print("Prosze podac prawidlowa wartosc przedzialu")
        jest = True
        while jest:
            try:
                prawy_przedzial = int(input("Wartosc konca przedzialu: "))
                jest = False
            except ValueError:
                print("Prosze podac prawidlowa wartosc przedzialu")
        argumenty = list(np.linspace(lewy_przedzial, prawy_przedzial, 1000))
        if wybor_opcji == "g":
            print("""
Wybor funkcji:
a: funkcja wielomianowa: 4*x^3+2*x^2+2x+5
b: funkcja trygonometryczna: 2*sin(x)
c: funkcja |x|: |x - 2|
d: liniowa: x - 1
e: funkcja zlozona: |cos(x) - 0.5|
""")
            jest = True
            while jest:
                wybor_funkcji = input("Dokonaj wyboru z powyzszych: ").upper()
                if wybor_funkcji in 'ABCDE':
                    jest = False
                else:
                    print("Prosze wpisac A, B, C, D lub E. Wielkosc liter nie ma znaczenia")
            jest = True
            while jest:
                try:
                    liczba_wezlow_interpolacyjnych = int(input("Liczba wezlow interpolacyjnych: "))
                    if liczba_wezlow_interpolacyjnych > 0:
                        jest = False
                    else:
                        print("Prosze podac dodatnia wartosc")
                except ValueError:
                    print("Prosze podac prawidlowa liczbe wezlow")
            wartosci_funkcji = []
            for argument in argumenty:
                wartosci_funkcji.append(wartosc_funkcji(argument, wybor_funkcji))
            pb.plot(argumenty, wartosci_funkcji, label='wykres funkcji f(x)')
            pb.title('f(x)=' + str(wzor_funkcji(wybor_funkcji)))  # tworzy tytuł wykresu
            x_pkt_inter = np.linspace(lewy_przedzial, prawy_przedzial, liczba_wezlow_interpolacyjnych)
            y_pkt_inter = wartosc_funkcji(x_pkt_inter, wybor_funkcji)
            x_pkt_inter = list(x_pkt_inter)
            y_pkt_inter = list(y_pkt_inter)
        else:
            jest = True
            while jest:
                try:
                    with open("dane.txt", 'r') as dane:
                        for i in range(7):
                            next(dane)
                        x_pkt_inter = dane.readline().split()
                        y_pkt_inter = dane.readline().split()
                    x_pkt_inter = [float(i) for i in x_pkt_inter]
                    y_pkt_inter = [float(i) for i in y_pkt_inter]
                    if len(x_pkt_inter) == len(y_pkt_inter) and len(x_pkt_inter) > 1:
                        jest = False
                    else:
                        print("""Prosze podac rowna liczbe argumentow i wartosci (conajmniej 2 punkty).
Nastepnie zamknac, zapisac plik z danymi i nacisnac dowolny klawisz""")
                        input()
                except ValueError:
                    print("""Prosze usunac teraz wszystkie znaki literowe z pliku dane.txt i dokonac jego zapisu. 
Gdy zmiany zostana wprowadzone prosze nacisnac dowolny klawisz""")
                    input()
        x = sp.Symbol('x')
        wzor_interpolacji_wprzod = interpolacja_wprzod(x_pkt_inter, y_pkt_inter)
        wzor_interpolacji_wstecz = interpolacja_wstecz(x_pkt_inter, y_pkt_inter)
        wspolczynniki_interpolacji_wprzod = sp.Poly(wzor_interpolacji_wprzod, x).all_coeffs()
        wspolczynniki_interpolacji_wstecz = sp.Poly(wzor_interpolacji_wstecz, x).all_coeffs()
        wartosci = []
        for argument in argumenty:
            if argument < (argumenty[-1] + argumenty[0]) / 2:
                wartosci.append(horner(wspolczynniki_interpolacji_wprzod, argument))
            else:
                wartosci.append(horner(wspolczynniki_interpolacji_wstecz, argument))
        pb.scatter(x_pkt_inter, y_pkt_inter, label='wezly interpolacyjne')
        pb.plot(argumenty, wartosci, linestyle=":", label='wielomian interpolacyjny')
        pb.xlabel("x")  # opis osi x
        pb.ylabel("y")  # opis osi y
        pb.grid(True)
        pb.legend(loc='upper right')  # tworzy legendę wykresu
        print("Prosze zamknac okno z Wykresem {} aby kontynuowac".format(zmienna_iteracyjna))
        print("""Wielomian interpolacyjny jest postaci:
<{0}:{1}): {3}
<{1}:{2}>: {4}
        """.format(lewy_przedzial, (lewy_przedzial + prawy_przedzial) / 2, prawy_przedzial, wzor_interpolacji_wprzod,
                    wzor_interpolacji_wstecz))
        pb.show(block=True)  # pokazuje wykres
        zmienna_iteracyjna += 1
    else:
        print("Prosze dokonac prawidlowego wyboru. Wielkosc liter nie ma znaczenia")
