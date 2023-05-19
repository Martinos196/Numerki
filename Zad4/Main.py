from funkcje import newton_cotes, gauss
from prettytable import PrettyTable




liczba_wezlow = 0
eps = 0.0
wybor_funkcji = ''
menu = True

print("Witaj w programie obliczajacym kwadratury Newtona-Cotes'a oraz Gaussa-Laguerre'a wybranej funkcji ")
while menu:
    print("""
    __________________________________
                  MENU:
    __________________________________
        1: wybor funkcji
        2: zakonczenie programu
    __________________________________
        """)
    wybor_menu = input("Dokonaj wyboru: ")
    if wybor_menu in "2":
        print("Zakonczenie programu...")
        menu = False
    elif wybor_menu in "1":
        print("""
Wybor funkcji:
A: f(x) = e^(-x) * (x^4 - x^3 - x^2 - x + 1)
B: f(x) = e^(-x) * |x - 2|
C: f(x) = e^(-x) * 2^x
D: f(x) = e^(-x) * cos(x)
E: f(x) = e^(-x) * (cos(x) - x^3)
""")
        jest = True
        while jest:
            wybor_funkcji = input("Dokonaj wyboru: ").upper()
            if wybor_funkcji in "ABCDE":
                jest = False
            else:
                print("Prosze wybrac poprawnie funkcje z powyzszych")
        jest = True
        while jest:
            try:
                eps = float(input("Dokladnosc kwadratur Newtona-Cotesa: "))
                jest = False
            except ValueError:
                print("Prosze podac poprawna wartosc dokladnosci")
        print("-" * 100)
        print(" " * 45, end='')
        if wybor_funkcji in "A":
            print("e^(-x)*(x^4 - x^3 - x^2 - x + 1)")
        elif wybor_funkcji in "B":
            print("e^(-x)*|x - 2|")
        elif wybor_funkcji in "C":
            print("e^(-x)*2^x")
        elif wybor_funkcji in "D":
            print("e^(-x)*cos(x)")
        elif wybor_funkcji in "E":
            print("e^(-x)*(cos(x)-x^3)")
        dokladna_wartosc = round(newton_cotes(wybor_funkcji, 1e-8), 8)
        # obliczenie dokładnej wartości całki. Później bedziemy obliczać na tej podstawie błąd metod
        t = PrettyTable(['Liczba wezlow', "Gauss-Laguerre", "Newton-Cotes", "Blad (%) Gauss-Laugerre",
                         "Blad (%) Newton-Cotes"])   # tworzenie nagłówka tabeli
        for liczba_wezlow in range(2, 6):
            wartosc_gauss = round(gauss(wybor_funkcji, liczba_wezlow), 5)   # obliczenie kwadratury Gaussa
            if liczba_wezlow == 3:
                wartosc_newton = round(newton_cotes(wybor_funkcji, eps), 5)   # obliczenie kwadratury Newtona-Cotes'a
                t.add_row([liczba_wezlow, wartosc_gauss, wartosc_newton,    # wypełnienie tabeli
                           round(abs((wartosc_gauss - dokladna_wartosc) / dokladna_wartosc * 100), 2),
                           round(abs((wartosc_newton - dokladna_wartosc) / dokladna_wartosc * 100), 2)])
            else:
                t.add_row([liczba_wezlow, wartosc_gauss, '',
                           round(abs((wartosc_gauss - dokladna_wartosc) / dokladna_wartosc * 100), 2), ""])
        print(t)
    else:
        print("Prosze wybrac 1 lub 2")
