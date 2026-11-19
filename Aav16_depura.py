
# Activitat 2: Depuració amb VSCode

nota1 = 6
nota2 = 7
nota3 = 8

mitjana = (nota1 + nota2 + nota3) / 3

aprova = mitjana >= 5

print(f"Mitjana: {mitjana}, aprova: {aprova}")

# Explicació:
# La divisió té prioritat sobre la suma.
# Per això, sense parèntesis, Python dividia només nota3 entre 3.
# Amb els parèntesis, primer suma les tres notes i després divideix.
