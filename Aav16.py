
# Activitat 1.6 - Operadors i expressions

# Exercici 1: Operadors aritmètics

print("Divisió entera:", 17 // 5)
print("Resta de la divisió:", 17 % 5)
print("Divisió normal:", 17 / 5)

# Activitat 1.6 - Operadors i expressions

# Exercici 1: Operadors aritmètics

print("Divisió entera:", 17 // 5)
print("Resta de la divisió:", 17 % 5)
print("Divisió normal:", 17 / 5)

# Exercici 2: Divisió amb nombres negatius

print("Divisió entera negativa:", -17 // 5)
print("Resta de la divisió negativa:", -17 % 5)

# Explicació:
# Amb nombres negatius, // arrodoneix cap avall.
# El resultat del % pot ser diferent del que esperem,
# perquè Python manté el signe del divisor en el residu.

# Exercici 3: Operadors de comparació i lògics

a = 5
b = 10
c = 15

resultat = a < b and b < c

print("Resultat de la comparació:", resultat)
print("Tipus de dada:", type(resultat))

# Exercici 4: Precedència d'operadors

resultat1 = 2 + 3 * 4 ** 2
resultat2 = (2 + 3) * 4 ** 2

print("Resultat sense parèntesis:", resultat1)
print("Resultat amb parèntesis:", resultat2)

# Exercici 5: Precedència dels operadors lògics

resultat = 5 > 3 and 2 > 4 or 1 == 1

print("Resultat de l'expressió:", resultat)

# Explicació:
# Primer es resolen les comparacions.
# Després s'avalua and, que té prioritat sobre or.
# True and False dona False.
# Finalment False or True dona True.
