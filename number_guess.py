import random

secret = random.randint(1,100)

incercari = 0

while True:
    try:
        nr = int(input("Ghiceste numarul: "))
    except ValueError:
        print("Introdu un numar intreg!")
        continue
    if nr < 1 or nr > 100:
        print("Introdu un nr de la 1 la 100!")
        continue
    incercari += 1
    if nr > secret:
        print("Prea mare!")
    elif nr < secret:
        print("Prea mic!")
    else:
        print("Bravo, ai ghicit numarul!")
        print("Încercări:", incercari)
        break




