import getpass
import random
iloscRund = input("Podaj ilosc rund ")
tryb = input("Podaj tryb: a-komputer, b-2 graczy ")
twojaNazwa = input("Podaj swoja nazwe ")
wyniki = []
if tryb == "b":
    nazwaPrzeciwnika = input("Drugi gracz podaje swoja nazwe ")
    for i in range(0, int(iloscRund)):
        ruch = getpass.getpass("ruch k-kamien, p-papier, n-nozyce ")
        ruch2 = getpass.getpass("rych2 k-kamien, p-papier, n-nozyce ")
        if ruch == "k" and ruch2 == "p" or ruch == "p" and ruch2 == "n" or ruch == "n" and ruch2 == "k":
            wynik = 2
            wyniki.append(wynik)
        elif ruch == "k" and ruch2 == "n" or ruch == "p" and ruch2 == "k" or ruch == "n" and ruch2 == "p":
            wynik = 1
            wyniki.append(wynik)
        else:
            wynik = "remis"
            wyniki.append(wynik)

    print("o to lista wyników (wygrywa osoba, ktorej numer wystepuje najwiecje razy w liscie): ")
    print(wyniki)

if tryb == "a":
    for i in range(0, int(iloscRund)):
        twojRuch = input("Twoj ruch k-kamien, p-papier, n-nozyce ")
        listaWyborowKomp =["p", "k", "n"]
        komputeRuch = listaWyborowKomp[random.randint(0,2)]

        if twojRuch == "k" and komputeRuch == "p" or twojRuch == "p" and komputeRuch == "n" or twojRuch == "n" and komputeRuch == "k":
            wynik = "ty"
            wyniki.append(wynik)
            print(wynik)

        elif twojRuch == "k" and komputeRuch == "n" or twojRuch == "p" and komputeRuch == "k" or twojRuch == "n" and komputeRuch == "p":
            wynik = "komputer"
            wyniki.append(wynik)
            print(wynik)
        else:
            wynik = "remis"
            wyniki.append(wynik)
            print(wynik)
    print("o to lista wyników (wygrywasz jesli wiecej jest w liscie ty niz komputer): ")
    print(wyniki)

