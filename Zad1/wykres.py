import matplotlib.pyplot as plt
from funkcje import funkcja_wzor


def wykres(rozwiazanie_bisekcja, rozwiazanie_newton):
    plt.xlabel("x") 
    plt.ylabel("y") 
    plt.legend(['miejsce zerowe z metody bisekcji: {}'.format(rozwiazanie_bisekcja), 'miejsce zerowe z metody stycznych: {}'.format(rozwiazanie_newton)]) 
    plt.grid()  
    plt.show()  
