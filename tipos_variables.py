# Curso introductorio a python

# ** Tipo de datos primitivos y creación de variables **
# Pytohn define sus datos primitivos como Textos, Numeros y Booleanos
# Los textos (str) son cadenas de caracters alfanuméricos que se encapsulan
# entre comillas simples, dobles o triples.
# Los números se clasifican de punto flotante (float) y enteros (int). Ademas
# python soporta números complejos (x + yj)

# ** Definiendo variables. **
# Una variable es un dato almacenado en memoria que tiene una dirección en la misma. Para
# facilitar el acceso a este dato, python le asigna un nombre como referencia para luego
# ser utilizado en cualquier parte del código en donde sea accesible.
# Una variable se define de la siguiente manera: nombre_variable = dato

nombre = "Juan Pérez"
numero_entero = 10
numero_flotante = 0.05
booleano = False
numero_complejo = complex(2,5)

print(type(nombre))
print(type(numero_entero))
print(type(numero_flotante))
print(booleano, type(booleano))
print(numero_complejo, type(numero_complejo))

