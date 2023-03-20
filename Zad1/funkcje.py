from horner import horner
import numpy as np
import sympy as sp  

def funkcjaWartosc(x, funkcja):
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

def funkcjaWzor(funkcja):
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


def metodaBisekcji(pprzedzial, kprzedzial, e, iter, funkcja):
    x1 = 0
    if funkcjaWartosc(pprzedzial, funkcja) * funkcjaWartosc(kprzedzial, funkcja) > 0:
        return False
    else:
        if iter <= 0:
            arg_x = sp.Symbol('x')
            df = sp.diff(funkcjaWzor(funkcja))
            n = 1
            while True:
                x1 = (pprzedzial + kprzedzial) / 2
                dfxn = df.subs(arg_x, x1)
                if abs(funkcjaWartosc(x1, funkcja)) <= e and (abs(dfxn) > e):
                    print("Metoda bisekcji: znaleziono rozwiazanie po " + str(n) + " iteracjach.")
                    return x1
                elif funkcjaWartosc(x1, funkcja) * funkcjaWartosc(pprzedzial, funkcja) < 0:
                    kprzedzial = x1
                else:
                    pprzedzial = x1
                n += 1
        else:
            for n in range(iter):
                x1 = (pprzedzial + kprzedzial) / 2
                if funkcjaWartosc(x1, funkcja) == 0.0:
                    print("Metoda bisekcji: znaleziono dokladne rozwiazanie epsilon= 0 po {} iteracjach.".format(n + 1))
                    return x1
                if funkcjaWartosc(x1, funkcja) * funkcjaWartosc(pprzedzial, funkcja) < 0:
                    kprzedzial = x1
                else:
                    pprzedzial = x1
            e = abs(funkcjaWartosc(x1, funkcja))
            print("Metoda bisekcji: znaleziono rozwiazanie po {0} iteracjach z dokladnoscia epsilon={1}".format(iter, e))
            return x1


def styczne(pprzedzial, kprzedzial, e, iter, funkcja):
    if funkcjaWartosc(pprzedzial, funkcja) * funkcjaWartosc(kprzedzial, funkcja) > 0:
        return False
    DF = sp.diff(funkcjaWzor(funkcja))  
    x = sp.Symbol('x')
    Xi = (pprzedzial + kprzedzial) / 2
    if abs(DF.subs(x, pprzedzial)) < abs(DF.subs(x, kprzedzial)):
        Xi = kprzedzial
    elif abs(DF.subs(x, pprzedzial)) > abs(DF.subs(x, kprzedzial)):
        Xi = pprzedzial
    if iter != 0: 
        for i in range(0, iter):
            FXI = funkcjaWartosc(Xi, funkcja)  
            DFXi = DF.subs(x, Xi)   
            Xi = Xi - float(FXI / DFXi)  
        e = abs(funkcjaWartosc(Xi, funkcja))       
        print("""Metoda stycznych: znaleziono rozwiazanie po {0} iteracjach z dokladnoscia epsilon={1}""".format(iter, e))
        return Xi
    else:  
        i = 0   
        while True:
            FXI = funkcjaWartosc(Xi, funkcja)   
            DFXi = DF.subs(x, Xi)   
            if (abs(FXI) < e) and (abs(DFXi) > e):
                print('Metoda stycznych: znaleziono rozwiazanie po ', i + 1, 'iteracjach.')
                return Xi
            Xi = Xi - float(FXI / DFXi)    
            i += 1 
