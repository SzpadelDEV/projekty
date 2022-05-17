import random
x = input("Podaj pierwszą liczbę:\n")
y = input("\nPodaj drugą liczbę:\n")
z = random.randint(int(x), int(y))
print("Wylosowana liczba to {} z zakresu liczb od {} do {}".format(z, x, y))
