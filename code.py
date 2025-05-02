import time


with open("lista2.txt", "r") as file:
    lista = [int(line.strip()) for line in file]

posortowanalista = sorted(lista)

while True:
    try:
        szukanaliczba = int(input("Wprowadź liczbę, którą chcesz wyszukać (od 1 do 1000000): "))
        if 1 <= szukanaliczba <= 1000000:
            break
        print("Liczba musi być w zakresie od 1 do 1000000.")
    except ValueError:
        print("Proszę wprowadzić poprawną liczbę.")


def binarne2(posortowanalista, szukanaliczba):
    lewa = 0
    prawa = len(posortowanalista) - 1

    while lewa<=prawa:
        srodek = (lewa+prawa)//2
        if posortowanalista[srodek] >= szukanaliczba:
            prawa = srodek-1
        else:
            lewa = srodek+1
        if posortowanalista[srodek]==szukanaliczba:
            return srodek
    return -1

def binarne3(posortowanalista, szukanaliczba):
    lewa = 0
    prawa = len(posortowanalista) - 1

    while lewa<=prawa:
        srodek = (lewa+prawa)//2
        if posortowanalista[srodek]==szukanaliczba:
            return srodek
        elif posortowanalista[srodek] > szukanaliczba:
            prawa = srodek-1
        else:
            lewa = srodek+1
    return -1


def pokaz_wynik(lista, posortowanalista, szukanaliczba, funkcja_wyszukiwania):
    start = time.perf_counter()  # Start pomiaru czasu
    indeks = funkcja_wyszukiwania(posortowanalista, szukanaliczba)
    czas_wykonania = time.perf_counter() - start  # Koniec pomiaru czasu

    if indeks != -1:
        # Znaleziony element - znajdź indeks w oryginalnej liście
        indeks_w_nieposortowanej = lista.index(szukanaliczba)
        print(f"Element {szukanaliczba} znaleziony na indeksie {indeks} w posortowanej liście.")
        print(f"W oryginalnej liście znajduje się na pozycji {indeks_w_nieposortowanej + 1}.")
    else:
        print(f"Element {szukanaliczba} nie został znaleziony.")

    print(f"Czas wyszukiwania: {czas_wykonania:.8f} sekund.")

# Wywołanie z binarne2
print("DWUPOZYCYJNE")
pokaz_wynik(lista, posortowanalista, szukanaliczba, binarne2)

# Wywołanie z binarne3
print("TRÓJPOZYCYJNE")
pokaz_wynik(lista, posortowanalista, szukanaliczba, binarne3)
