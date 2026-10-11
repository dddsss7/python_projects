print ("Hello World!") # First code line

# Simple things 

nume = "Bruce"
prenume = "Wayne"
age = 21
money = True

print("Welcome back home", nume, prenume)
answer = input("Are you here? ")
print(f"You said {answer}")
input("are you gonna lock in? ")

# Operators

x = 5
y = x / 2 # Float
z = x // 2 # Integer
a = x % 2 # Remainder

print(y, z, a)

# Conditions 

age = 18

if age >= 18:
    print("Major")
elif age >= 10:
    print("Teen")
else:
    print("Minor")

# Loops for

cars = ["bmw", "mercedes", "porsche"]

for car in cars:
    print(car)

# Loops range

range(5) # 0 1 2 3 4
range(2,6) # 2 3 4 5
range(0, 10, 2) # 0 2 4 6 8 (step of 2)

for i in range(1,4):
    print("round", i)

for letter in "This is Bruce Wayne":
    print(letter)

# Looping over a dictionary

person = {"name": "Bruce", "age": 25}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

# while loop 

count = 0
while count<3:
    print(count)
    count += 1


password = ""
while password != "batman":
    password = input("Enter the password: ")
    if password != "batman":
        print("Wrong password! try again")
print("Acces granted!")  

# break and continue 

for n in range(1000):
    if n == 4:
        break
    print(n)

for n in range(6):
    if n == 3:
        continue
    print(n)

# while true - example with "Keep going until something happens"

while True:
    answer = input("Type 'quit' to stop: ")
    if answer == "quit":
        break

# nested loop

for a in range(1,4):
    for b in range(1,4):
        print(a * b, end = " ")
    print()

# Functii: def, parametrii, return

def salut(nume):  # nume = parametru
    print(f"Salut, {nume}")

salut("batman")  # batman = argument

