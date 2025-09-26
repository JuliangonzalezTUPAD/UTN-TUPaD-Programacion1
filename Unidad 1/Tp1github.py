#Actividad 1
print("Hola mundo!")

#Actividad 2
nombre = input("Por favor ingrese su nombre: ")
print(f"Hola {nombre}!")

#Actividad 3
print("Ingrese los siguientes datos:")
nombre = input("Nombre:")
apellido = input("Apellido:")
edad = int(input("Edad:"))
residencia = input("Residencia:")
print(f"Hola, soy {nombre} {apellido} tengo {edad} años de edad y actualemte vivo en {residencia}")

#Actividad 4
radio = int(input("Ingrese el radio de un circulo:"))
pi = float(3.14)
print("En base al radio ingresado calculamos su area y perimetro:")
print("Su area:")
print(pi * radio**2)
print("Su perimetro:")
print(radio * 2 * pi)

#Actividad 5
segundos = int(input("Ingrese una cantidad de segundos:"))
horas = segundos * 1 / 3600 
print(f"La cantidad de segundos ingresdados equivale a {horas} horas")

#Actividad 6
numero = int(input("Ingrese un numero: "))
print("A continuacion se mostrara su tabla de multiplicacion: ")
print(f"{numero} * 1 : {numero * 1}")
print(f"{numero} * 2 : {numero * 2}")
print(f"{numero} * 3 : {numero * 3}")
print(f"{numero} * 4 : {numero * 4}")
print(f"{numero} * 5 : {numero * 5}")
print(f"{numero} * 6 : {numero * 6}")
print(f"{numero} * 7 : {numero * 7}")
print(f"{numero} * 8 : {numero * 8}")
print(f"{numero} * 9 : {numero * 9}")
print(f"{numero} * 10 : {numero * 10}")

#Actividad 7
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print(f"Resultado de su suma: {num1 + num2}")
print(f"Resultado de su resta: {num1 - num2}")
print(f"Resultado de su multiplicacion: {num1 * num2}")
print(f"Resultado de su division: {num1 / num2}")

#Actividad 8
print("Se calculara su indice de masa corporal (IMC), para ello ingrese su peso y altura")
peso = int(input("Peso en kg:"))
altura = float(input("Altura en m:"))
IMC = peso / (altura**2)
print(f"Su IMC es: {IMC}")

#Actividad 9 
celsius = float(input("Ingrese una temperatura en grados Celsius "))
fahrenheit = ((9/5) * celsius + 32)
print(f"Su equivalencia en grados Fahrenheit es: {fahrenheit}")

#Actividad 10
print("Ingrese tres numero y se mostrara su promedio")
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio entre dichos numeros es: {promedio}")