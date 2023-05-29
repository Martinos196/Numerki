from numpy import sin, cos
from horner import horner
import sympy as sp


def wartosc_funkcji(x, wybor_funkcji):
    wartosc = None
    if wybor_funkcji in "1":
        wartosc = 2 * x - 3
    elif wybor_funkcji in "2":
        wartosc = abs(x - 2)
    elif wybor_funkcji in "3":
        wartosc = horner([1, -1, -1, -1, 1], x)
    elif wybor_funkcji in "4":
        wartosc = sin(x)
    elif wybor_funkcji in "5":
        wartosc = cos(x) - x**3
    return wartosc


def wzor_funkcji(wybor_funkcji):
    wartosc = None
    x = sp.Symbol('x')
    if wybor_funkcji in "1":
        wartosc = 2 * x - 3
    elif wybor_funkcji in "2":
        wartosc = abs(x - 2)
    elif wybor_funkcji in "3":
        wartosc = horner([1, -1, -1, -1, 1], x)
    elif wybor_funkcji in "4":
        wartosc = sp.sin(x)
    elif wybor_funkcji in "5":
        wartosc = sp.cos(x) - x**3
    return wartosc

def wspolczynniki(liczba_wezlow, numer_wezla):
    dane = (
        ((- 0.577350, 1), (0.577350, 1)),
        ((- 0.774597, 5 / 9), (0, 8 / 9), (0.774597, 5 / 9)),
        ((- 0.861136, 0.347855), (- 0.339981, 0.652145), (0.339981, 0.652145), (0.861136, 0.347855)),
        ((- 0.906180, 0.236927), (- 0.538469, 0.478629), (0, 0.568889), (0.538469, 0.478629), (0.906180, 0.236927))
    )
    return dane[liczba_wezlow - 2][numer_wezla]


def funkcja_bazowa(k, x):
    p = [1, x]
    for n in range(2, k + 1):
        p.append(((2 * (n - 1) + 1) / n * x * p[n - 1] - (n - 1) / n * p[n - 2]))
    return p[k]


def gauss_licznik(wybor_funkcji, liczba_wezlow, k):
    calka = 0
    for i in range(liczba_wezlow):
        x = (wspolczynniki(liczba_wezlow, i)[0])
        w = (wspolczynniki(liczba_wezlow, i)[1])
        calka += w * wartosc_funkcji(x, wybor_funkcji) * funkcja_bazowa(k, x)
    return calka


def gauss_blad(wybor_funkcji, k, tab_wsp, liczba_wezlow):
    calka = 0
    for i in range(liczba_wezlow):
        x = (wspolczynniki(liczba_wezlow, i)[0])
        # x = - 1 + 2 * (x - a)/(b - a)
        w = (wspolczynniki(liczba_wezlow, i)[1])
        calka += w * (wartosc_funkcji(x, wybor_funkcji) - wart_wielomian(k, x, tab_wsp))**2
    return calka


def wsp_apro(wybor_funkcji, liczba_wezlow, k):
    wsp = (2 * k + 1) / 2 * gauss_licznik(wybor_funkcji, liczba_wezlow, k)
    return wsp


def wsp_wielomian(wybor_funkcji, liczba_wezlow, k):
    wielomian = []
    for i in range(k + 1):
        wielomian.append(wsp_apro(wybor_funkcji, liczba_wezlow, i))
    return wielomian


def wart_wielomian(k, x, tab_wsp):
    poly = 0
    for i in range(k + 1):
        poly += tab_wsp[i] * funkcja_bazowa(i, x)
    return poly
