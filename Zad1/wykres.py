import pylab as pb  # do generowania wykresu
from metody import funkcja_wzor


def pokaz(rozwiazanie_bisekcja, rozwiazanie_newton, wybor):
    pb.xlabel("x")  # opis osi x
    pb.ylabel("y")  # opis osi yb
    pb.legend(['wykres funkcji f(x)', 'miejsce zerowe z metody bisekcji: {}'.format(rozwiazanie_bisekcja),
               'miejsce zerowe z metody Newtona: {}'.format(rozwiazanie_newton)],
              loc='upper left')  # tworzy legendę wykresu
    pb.title('f(x)=' + str(funkcja_wzor(wybor)))  # tworzy tytuł wykresu
    pb.grid(True)  # tworzy siatke na wykresie
    pb.show(block=True)  # pokazuje wykres
