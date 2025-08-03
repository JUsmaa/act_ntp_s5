
print ("Ejercicios condicionales: ")
print ("-------------------------")
# Ejercicio 1: Verificar si la persona es mayor de edad para ingresar al evento
print ("solo puedes entrar si eres mayor de edad")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print ("Bienvenido al evento del año!!")
else:
    print ("No puedes ingresar, eres menor de edad")
#Ejercicio 2: crear un mensaje
print ("-------------------------")
print ("Envia un mensaje a tu jefa: ")
mensaje = input("Escriba su mensaje: ")
if mensaje == "":
    print ("No has escrito nada, por favor escribe un mensaje")
else:
    print ("Mensaje enviado a tu jefa: " + mensaje)
#Ejercicio 3: calculadora de figuras
print ("calculadora de perimetrode figuras")
figura = int (input("marca un numero para seleccionar la figura: 1.cuadrado, 2. triangulo, 3. circulo, 4 rectangulo"))
longitud = int (input("ingrese la longitud de uno de sus lados: "))
if figura == 1:
    resultado = longitud * 4
print (resultado)