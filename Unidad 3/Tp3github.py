#Actividad 1
edad = int(input("Ingrese su edad: "))
if (edad >= 18):
    print("Es mayor de edad")

#Actividad 2
nota = int(input("Ingrese su nota: "))
if (nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")

#Actividad 3
numero = int(input("Escribe un numero: "))
if (numero % 2 == 0):
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#Actividad 4
edad = int(input("Escriba su edad: "))
if (edad < 12):
    print("Niño")
elif (edad >= 12 and edad < 18):
    print("Adolecente")
elif (edad >= 18 and edad < 30):
    print("Adulto joven")
elif (edad >= 30):
    print("Adulto")
else:
    pass

#Actividad 5
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
if (len(contraseña) >= 8 and len(contraseña) <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
promedio = mean(numeros_aleatorios)
media = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
if (promedio > media > moda):
    print("Sesgo positivo")
elif (promedio < media < moda):
    print("Sesgo negativo")
elif (promedio == media == moda):
    print("Sin sesgo")
else:
    pass

#Actividad 7
vocales = ("a", "e", "i", "o", "u" , "A", "E", "I", "O", "U") #TUPLA
frase = input("Ingrese palabra o frase: ")
if (frase[-1] in vocales): #[-1] toma la ultima letra
    print(frase,"!")
else:
    print(frase)

#Actividad 8
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese el numero 1 si quiere su nombre en mayuscula, el numero 2 si lo quiere en minuscula o el numero 3 si solo quiere la primera letra en mayuscula "))
if (numero == 1):
    print(nombre.upper())
elif (numero == 2):
    print(nombre.lower())
elif(numero == 3):
    print(nombre.title())
else:
    pass

#Actividad 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if (magnitud < 3):
    print("Es muy leve, imperceptible")
elif (magnitud >= 3 and magnitud < 4):
    print("Leve, ligeramente perceptible")
elif (magnitud >= 4 and magnitud < 5):
    print("Moderado, se siente por la persona pero no suele causar daño")
elif (magnitud >= 5 and magnitud < 6):
    print("Fuerte, puede causar daños estructurales leves")
elif (magnitud >= 6 and magnitud < 7):
    print("Muy fuerte, puede causar daños significativos")
elif(magnitud >= 7):
    print("Extremo, puede causar graves daños a gran escala, empezá a correr!")
else:
    pass

#Actividad 10