
# Activitat 1.5: Entrada de dades i f-strings

# Exercici 1: Demanar nom i edat
nom = input("Introdueix el teu nom: ")
edat = int(input("Introdueix la teva edat: "))

print(f"{nom} té {edat} anys")

# Exercici 2: Sumar dos números
numero1 = float(input("Introdueix el primer número: "))
numero2 = float(input("Introdueix el segon número: "))

suma = numero1 + numero2

print(f"La suma és {suma}")

# Exercici 3: Edat d'aquí a 10 anys
print(f"D'aquí a 10 anys tindràs {edat + 10} anys")

# Exercici 4: Preu amb dos decimals
preu = 19.5

print(f"El preu és {preu:.2f} euros")

# Exercici 5: Diferència entre concatenació i f-strings
# La concatenació amb + uneix textos, però pot necessitar conversions
# quan volem combinar textos i números.
# Les f-strings permeten inserir variables i expressions directament
# dins d'un text de manera més clara i senzilla.