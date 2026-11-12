edat = 17
preu = 12.50
nom = "Maria" 
es_estudiant = True 
print(edat, type(edat))
print(preu, type(preu))
print(nom, type(nom))
print(es_estudiant, type(es_estudiant))
preu_text ="12.50"
preu_numero = float(preu_text)
preu_amb_iva = preu_numero * 1.21
print("Preu amb IVA:", float(preu_amb_iva))
edat = 17
es_major = edat >=18
print("Es major d´ edat:", es_major)
print("Tipus:", type(es_major))
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print('bool(""):', bool(""))
print('bool("False"):', bool("False"))
print('bool("0"):', bool("0"))
resultat = "5" + 5
print(resultat)