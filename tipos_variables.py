# Curso introductorio a python
import string

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


# print(type(nombre))
# print(type(numero_entero))
# print(type(numero_flotante))
# print(booleano, type(booleano))
# print(numero_complejo, type(numero_complejo))


# ** Manejo de cadenas de textos **

# Las cadenas de textos (str) en python se comportan con una lista (estructura de datos) a las cuales se les pueden
# aplicar metodos propios de las listas.

#** Constantes de la clase string **#

# print(type(string.ascii_letters))
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(type(string.punctuation))
# print(string.digits)
# print(string.whitespace.split())

#** Manipulando cadenas de textos **#

nombre = "Vicente Fernandez"
apellido = "Gómez"

nombre_completo = nombre + ' ' + apellido

# Imprimir nombre completo
print(nombre_completo)

# Accediendo a un valor (caracter) de la de la cadena
print(nombre_completo[0])
print(nombre_completo[1])
print(nombre_completo[2])
print(nombre_completo[-1])
print(nombre_completo[-2])

# Accediendo a porciones del texto
print(nombre_completo[0:4])
print(nombre_completo[:])
print(nombre_completo[3:6])
print(nombre_completo[:5])
print(nombre_completo[:-2])


mensaje = 'Bienvenido {} al curso de Python!'.format('Joel')
mensaje2 = f'Bienvenido {nombre_completo} al curso de Python!'



print(mensaje2.upper())
print(mensaje2.lower())
print('1234'.isnumeric())




