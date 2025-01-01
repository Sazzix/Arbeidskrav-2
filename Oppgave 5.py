# Oppgave 5
import math

a = float(input("skriv inn en verdi for a: "))
b = float(input("skriv inn en verdi for b: "))

# Arealet av trekanten
område_trekant = (a * b) / 2

# Radiusen til halvsirkelen er hypotenusen til trekanten delt på 2
hypotenuse = math.sqrt(a**2 + b**2)
radius = hypotenuse / 2

# Arealet av halvsirkelen
halvsirkel_areal = (math.pi * radius**2) / 2

# Totalt areal
total_areal = område_trekant + halvsirkel_areal

# Ytre omkrets: summen av de to kantene og halvsirkelens bue
omkrets = a + b + (math.pi * radius)

rund_omkrets = round(omkrets, 2)
rund_areal = round(total_areal, 2)

print("Ytre omkretsen er: ",rund_omkrets)
print("Total areal er: ", rund_areal)