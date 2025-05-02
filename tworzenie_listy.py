import random

# Tworzenie listy pięciu tysięcy unikalnych liczb w zakresie od 1 do 10000
lista2 = random.sample(range(1, 1000001), 1000000)

# Zapis listy do pliku na komputerze
with open("lista2.txt", "w") as file:
    for number in lista2:
        file.write(f"{number}\n")

print("Lista została zapisana w pliku 'lista2.txt'.")
