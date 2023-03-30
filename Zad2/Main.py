import numpy as np
import sys
from funkcje import Seidl, is_gauss_seidel_convergent

with open('Macierz.txt', 'r') as file:
    lines = file.readlines()[:-1] # pomijamy ostatni wiersz

matrix = []
for line in lines:
    row = [float(x) for x in line.strip().split()]
    matrix.append(row)

with open('Macierz.txt', 'r') as file:
    lines = file.readlines() # bierzemy tylko ostatni wiersz

last_line = lines[-1].strip()
row = [float(x) for x in last_line.split()]

file.close()


if is_gauss_seidel_convergent(matrix) is False:
    print("Podana macierz nie spełnia warunków zbieżności")
    sys.exit()

x = True
while x:
        wyborKryterium = input("""\nWybierz warunek stopu:
d- uzyskanie podanej dokladnosci
i- ilosc iteracji\n""").lower()
        if wyborKryterium in "di":
            x = False
        else:
            print("Wpisano bledna wartosc")
x = True
if wyborKryterium == "i":
    while x:
        try:
            liczbaIteracji = int(input("Wpisz liczbe iteracji: "))
            if liczbaIteracji > 0:
                x = False
                e = abs(float(input("Wpisz dokladnosc epsilon: ")))
            else:
                print("Wpisano bledna wartosc")
        except ValueError:
            print("Wpisano bledna wartosc")
elif wyborKryterium == "d":
    while x:
        try:
            e = abs(float(input("Wpisz dokladnosc epsilon: ")))
            x = False
            liczbaIteracji = 0
        except ValueError:
            print("Wpisano bledna wartosc")

Seidl(matrix, row, e, liczbaIteracji)
