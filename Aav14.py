
# ACTIVITAT 1.4 - VARIABLES, TIPUS I CONVERSIÓ

# EXERCICI 1: Declaració de variables i tipus

numero = 10
decimal = 12.5
text = "Hola Python"
boolea = True

print("Exercici 1")
print(numero, type(numero))
print(decimal, type(decimal))
print(text, type(text))
print(boolea, type(boolea))


# EXERCICI 2: Conversió de text a número i càlcul de l'IVA

preu_text = "12.50"
preu = float(preu_text)
preu_amb_iva = preu * 1.21

print("\nExercici 2")
print("Preu amb IVA:", float(preu_amb_iva))


# EXERCICI 3: Comprovar si una persona és major d'edat

edat = 17
es_major = edat >= 18

print("\nExercici 3")
print("És major d'edat?", es_major)
print("Tipus:", type(es_major))


# EXERCICI 4: Conversió a booleà

print("\nExercici 4")
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print('bool(""):', bool(""))
print('bool("False"):', bool("False"))
print('bool("0"):', bool("0"))


# EXERCICI 5: Error en sumar text i número

print("\nExercici 5")

try:
    resultat = "5" + 5
    print(resultat)
except TypeError as error:
    print("Error:", error)

# Explicació:
# No es pot sumar directament una cadena de text (str)
# amb un número enter (int). Cal convertir un dels dos tipus.
