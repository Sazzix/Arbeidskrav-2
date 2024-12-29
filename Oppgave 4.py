# Oppgave 4

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }
# b) Lag et program som ber brukeren skrive inn et land (eksempelvis England).
# Programmet skal på bakgrunn av dette skrive ut følgende setning:
# London er hovedstaden i England og det er 8.982 mill. innbyggere i London

land = input("Skriv inn et land: ")
navn = data[land]


print(navn[0], "er hovedstaden i", land , "og det er", navn[1], "mill. innbyggere i", navn[0])


