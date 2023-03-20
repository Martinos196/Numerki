from horner import horner
import numpy as np
import sympy as sp  

def funkcja_wart(x, funkcja):
    if funkcja == "A":    
        wart = horner([4,2, 2, 5], x)  
    elif funkcja == "B":  
        wart = 2*np.sin(x)
    elif funkcja == "C":  
        wart = 3**x-2
    elif funkcja == "D": 
        wart = np.sin(x)+3*x**2-4
    else:
        print("Nie wybrano żadnej z podanych funkcji.")
        wart = None
    return wart    

def funkcja_wzor(funkcja):
    x = sp.Symbol('x')
    if funkcja == "A":   
        wzor = horner([4,-2, 2, 5], x)     
    elif funkcja == "B":  
        wzor = 2*sp.sin(x)
    elif funkcja == "C":  
        wzor = 3**x-2
    elif funkcja == "D":  
        wzor = sp.sin(x)+3*x**2-4
    else:
        print("Nie wybrano żadnej z podanych funkcji.")
        wzor = None
    return wzor 


def metoda_bisekcji(poczatek_przedzialu, koniec_przedzialu, epsilon, iteracje, wybor):
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


def styczne(pprzedzial, kprzedzial, e, iter, funkcja):
    if funkcja_wart(pprzedzial, funkcja) * funkcja_wart(kprzedzial, funkcja) > 0:
        return False
    DF = sp.diff(funkcja_wzor(funkcja))  
    x = sp.Symbol('x')
    Xi = (pprzedzial + kprzedzial) / 2
    if abs(DF.subs(x, pprzedzial)) < abs(DF.subs(x, kprzedzial)):
        Xi = kprzedzial
    elif abs(DF.subs(x, pprzedzial)) > abs(DF.subs(x, kprzedzial)):
        Xi = pprzedzial
    if iter != 0: 
        for i in range(0, iter):
            FXI = funkcja_wart(Xi, funkcja)  
            DFXi = DF.subs(x, Xi)   
            Xi = Xi - float(FXI / DFXi)  
        e = abs(funkcja_wart(Xi, funkcja))       
        print("""Metoda stycznych: 
            znaleziono rozwiazanie po {0} iteracjach z dokladnoscia epsilon={1}""".format(iter, e))
        return Xi
    else:  
        i = 0   
        while True:
            FXI = funkcja_wart(Xi, funkcja)   
            DFXi = DF.subs(x, Xi)   
            if (abs(FXI) < e) and (abs(DFXi) > e):
                print('Metoda stycznych: znaleziono rozwiazanie po ', i + 1, 'iteracjach.')
                return Xi
            Xi = Xi - float(FXI / DFXi)    
            i += 1 
