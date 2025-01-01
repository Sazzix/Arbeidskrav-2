# Oppgave 6
import numpy as np
import matplotlib.pyplot as plt

# Definer funksjonen f(x)
def f(x):
    return -x**2 - 5

# Opprett x-verdier
x = np.linspace(-10, 10, 200)

# Beregn y-verdier
y = f(x)

# Plot funksjonen
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = -x^2 - 5", color="blue")
plt.title("Graf av f(x) = -x^2 - 5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Legg til x-aksen
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Legg til y-aksen
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
