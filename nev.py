import datetime
now = datetime.datetime.now()
hour = now.hour

nev = 'Béla'

bemenet = input('Neved ')


while bemenet != nev:
    print('Szia,', bemenet,'!')
    break


if bemenet == nev:
    if hour < 12:
        print("Szép reggelt, Béla!")
    elif hour < 18:
        print("Szép délelutánt, Béla!")
    else:
        print("Szép estét, Béla!")
