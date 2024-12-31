# Oppgave 4 c)

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }


for i in range(1):
    land = input("Legg til et land: ")
    hovedstad = input("legg til hovedstad: ")
    innbyggere = int(input("Hvor mange innbyggere er det i hovedstaden?"))
    data[land] = hovedstad, innbyggere


print(data)
