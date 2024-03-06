import random
import math

def zad1():
    A=[1- x for x in range(1,11)]
    print(A)

    B=[4**n for n in range(0,7)]
    print(B)

    C=[x for x in B if x % 2 ==0]
    print(C)
def zad2():
    lista_parzyste=[]
    lista1=[]
    for i in range(1,11):
        n=random.randint(1,1000)
        lista1.append(n)
        if n % 2 == 0:
            lista_parzyste.append(n)
    print(lista_parzyste)
    print(lista1)
def zad3():

    produkty_spozywcze = {
        'Chleb': 'sztuki',
        'Mleko': 'litr',
        'Jajka': 'sztuki',
        'Marchewki': 'kg',
        'Pomarańcze': 'kg',
        'Cukier': 'kg',
        'Herbata': 'sztuki',
    }


    produkty_szukane = [produkt for produkt, jednostka in produkty_spozywcze.items() if jednostka == 'sztuki']


    print("Produkty spożywcze:")
    print(produkty_spozywcze)

    print("\nProdukty, których jednostką są sztuki:")
    print(produkty_szukane)


def zad4():
    def czy_trojkat_prostokatny(a, b, c):

        if a <= 0 or b <= 0 or c <= 0:
            return False


        a, b, c = sorted([a, b, c])


        return a ** 2 + b ** 2 == c ** 2
    bok1=int(input("wprowadz pierwsza dlugosc boku"))
    bok2=int(input("wporwadz druga dlugosc boku"))
    bok3=int(input("wprowad trzecia dlugosc boku"))

    wynik = czy_trojkat_prostokatny(bok1, bok2, bok3)
    if wynik:
        print(f"Trójkąt o bokach {bok1}, {bok2}, {bok3} jest prostokątny.")
    else:
        print(f"Trójkąt o bokach {bok1}, {bok2}, {bok3} nie jest prostokątny.")

def zad5():
    a=int(input("podaj dlugosc"))
    b=int(input("podaj dlugosc"))
    h=int(input("podaj wysokosc"))
    trapez =((a+b)*h)/2
    print(trapez)
def zad6(a=1, b=4, ile=10):
    wynik = a
    for i in range(1,ile):
        wynik *= b
    return wynik

wynik1 = zad6()
wynik2 = zad6(a=2, b=3, ile=5)

print(wynik1)
print(wynik2)


def zad7():

    a = int(input("Podaj liczbe calkowita nieujemna: "))
    if a < 0:
        print("To liczba ujemna!")
        return a
    print(math.sqrt(a))



def main():
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    #zad5()
    #zad6()
    zad7()
if __name__ == '__main__':
     main()