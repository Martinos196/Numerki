from horner import horner
import numpy as np
import sympy as sp  

def funkcjaWartosc(x, funkcja):
    if funkcja == "A":    
        wart = horner([4,-2, 2, 5], x)  
    elif funkcja == "B":  
        wart = 2*np.sin(x)
    elif funkcja == "C":  
        wart = abs(x-2)
    elif funkcja == "D": 
        wart = x-1
    elif funkcja == "E": 
        wart = abs(np.cos(x) - 0.5)
    else:
        print("Nie wybrano żadnej z podanych funkcji.")
        wart = None
    return wart    

def funkcjaWzor(funkcja):
    x = sp.Symbol('x')
    if funkcja == "A":   
        wzor = horner([4,-2, 2, 5], x)     
    elif funkcja == "B":  
        wzor = 2*sp.sin(x)
    elif funkcja == "C":  
        wzor = abs(x-2)
    elif funkcja == "D":  
        wzor = x-1
    elif funkcja == "E": 
        wzor = abs(sp.cos(x) - 0.5)    
    else:
        print("Nie wybrano żadnej z podanych funkcji.")
        wzor = None
    return wzor 

def silnia(x):
    n = x
    if x > 1:
        for i in range(1, x):
            n *= x - i
        return n
    elif x == 1 or x == 0:
        return 1
    else:
        print("Prosze podac dodatnia liczbe calkowita")
        return None


def roznice_skonczone(tab_y):
    liczba_wezlow_interpolacji = len(tab_y)
    delta_y = [[]]
    delta_y[0] = tab_y
    for licznik in range(1, liczba_wezlow_interpolacji):
        delta_y.append([round(delta_y[licznik - 1][i + 1] - delta_y[licznik - 1][i], 8)
                        for i in range(liczba_wezlow_interpolacji - licznik)])
    return delta_y


def interpolacja_wprzod(tab_x, tab_y):

    h = tab_x[1] - tab_x[0]
    liczba_wezlow = len(tab_y)
    delta_y = roznice_skonczone(tab_y)
    args_x = sp.Symbol('x')
    # if arg_x < (tab_x[0] + tab_x[-1]) / 2:
    q = (args_x - tab_x[0])/h
    wspolczynniki = []
    for i in range(liczba_wezlow):
        wspolczynniki.append(round(delta_y[i][0]/silnia(i), 4))
    wielomian = [wspolczynniki[0], q * wspolczynniki[1]]
    wspolczynniki_kopia = wspolczynniki.copy()
    wspolczynnik = wspolczynniki[-1]
    i = 1
    while wspolczynnik == 0 and len(wspolczynniki) > 1:
        del wspolczynniki[wspolczynniki.index(wspolczynnik)]
        wspolczynnik = wspolczynniki_kopia[-1 - i]
        i += 1
    qt = q
    for i in range(len(wspolczynniki) - 2):
        qt -= 1
        q *= qt
        wielomian.append(q * wspolczynniki[i + 2])
    wartosc = 0
    for item in wielomian:
        wartosc += item
    wartosc = sp.simplify(wartosc)
    return wartosc


def interpolacja_wstecz(tab_x, tab_y):
    x = sp.Symbol('x')
    h = tab_x[1] - tab_x[0]
    q = (x - tab_x[-1])/h
    liczba_wezlow = len(tab_y)
    delta_y = roznice_skonczone(tab_y)
    wspolczynniki = []
    for i in range(liczba_wezlow):
        wspolczynniki.append(round(delta_y[i][-1] / silnia(i), 4))
    wielomian = [wspolczynniki[0], q * wspolczynniki[1]]
    wspolczynniki_kopia = wspolczynniki.copy()
    wspolczynnik = wspolczynniki[-1]
    i = 1
    while wspolczynnik == 0 and len(wspolczynniki) > 1:
        del wspolczynniki[wspolczynniki.index(wspolczynnik)]
        wspolczynnik = wspolczynniki_kopia[-1 - i]
        i += 1
    qt = q
    for i in range(len(wspolczynniki) - 2):
        qt += 1
        q *= qt
        wielomian.append(q * wspolczynniki[i + 2])
    wartosc = 0
    for item in wielomian:
        wartosc += item
    wartosc = sp.simplify(wartosc)
    return wartosc