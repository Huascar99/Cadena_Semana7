vector = ["j", "u", "a", "n"]
print(type(vector))

for letra in vector:
    print(letra)

nombre ="juan"
print("*"*13)
for letra in nombre:
    print(letra)


print(len(vector))
print(len(nombre))

def convertirAMayuscula(texto):
    return f"El texto original {texto} en mayuscula es: {texto.upper()}"

def convertitAMinuscula(texto):
    return f"{texto.lower()}"

def capitalizar(texto):
    return f"{texto.capitalize()}"

def titulo(texto):
    return f"{texto.title()}"

def generarEmail(texto):
    nombre = texto.split()
    email = ''.join(palabra [:3].lower() for palabra in nombre)
    return f"{email} @uamv.edu.ni "    



print(convertirAMayuscula(nombre))
print(convertitAMinuscula(nombre))
print(capitalizar(nombre))
print(titulo(nombre))
print(generarEmail("Jose Alberto Baca Moreno"))

for letra in vector:
    print(convertirAMayuscula(letra))
    