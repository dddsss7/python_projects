while True:
    try:
        virsta = int(input("Introdu virsta: "))
    except ValueError:
        print("Introdu numar intreg!: ")
        continue
    if virsta < 0 or virsta > 120:
        print("Vârsta trebuie să fie între 0 și 120!")
        continue
    break

if virsta >= 18:
    print("matur")
else:
    print("minor")