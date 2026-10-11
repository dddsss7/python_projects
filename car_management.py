def adauga_masina(masini):
    marca = input("Marca: ")
    model = input("Model: ")
    anul = int(input("Anul: "))

    masina = {"Marca": marca, "Modelul": model, "Anul": anul}
    masini.append(masina)

masini = []

adauga_masina(masini)
adauga_masina(masini)

print(masini)

