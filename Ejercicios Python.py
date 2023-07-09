# Imports #

import math

# Variable Global #

usuarios = {}

# Funcion Menu Principal #

def menu_principal():
    print("")
    print("Menu de opciones:")
    print("")
    print("1. Ingresar año.") # Ejercicio de año biciesto. #
    print("2. Calcular el Area de un rectangulo.") # Segun la consigna pide 15 de base y 10 de altura. #
    print("3. Calcular el Area de un circulo.") # La consigna pedia sacar el area de 5 de radio. #
    print("4. Funcion de relacion.") # El ejercicio solicitaba comparar (5, 10) / (10, 5) / (5, 5). #
    print("5. Funcion de intermedio.") # Nos pide que a partir de dos numeros nos devuelva el numero intermedio. #
    print("6. Funcion de recortar.") # No entendi bien la consigna, pero creo que funciona bien. #
    print("7. Funcion de separar.") # De una lista "X" de numeros, las separamos por pares e impares y luego, las ordenamos de menor a mayor. / Editar la lista en la configuracion. #
    print("8. Funcion de registro.") # Consigna de la pre-entrega. #
    print("9. Salir.") # Salimos del programa. #
    print("")

# Funcion año biciesto. #

def biciesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print("Su año es biciesto.")
    else:
        print("Su año no es biciesto.")

# Funciones Adicionales de la clase 10 #

# Area de un rectangulo #

def area_rectangulo(base, altura):
    calculo = base * altura
    resultado = print("El area de este rectangulo es de: " + str(calculo) + " m2.")
    return resultado

# Area de un circulo #

def area_circulo(radio):
    calculo = (radio)**2
    calculo1 = calculo * math.pi
    resultado = print("El area de su circulo es de: " + str(calculo1))
    return resultado

# Funcion de relacion #

def relacion(num1, num2):
    if num1 > num2:
        print("El numero " + str(num1) + " es mayor que " + str(num2) + ", por lo tanto, el resultado es: 1.")
    elif num1 < num2:
        print("El numero " + str(num1) + " es menor que " + str(num2) + ", por lo tanto, el resultado es: -1.")
    elif num1 == num2:
        print("Ambos numeros son iguales, por lo tanto el resultado es: 0.")
    else:
        print()
        print("Ingreseo caracteres invalidos, por favor, ingrese dos numeros.")

# Funcion de intermedio #

def intermedio(num1, num2):
    calculo = num1 + num2
    calculo1 = calculo / 2
    resultado = print("El punto intermedio entre ambos numeros es de: " + str(calculo1))
    return resultado

# Funcion de recortar #

def recortar(num1, num2, num3):
    if num1 < num2:
        print (str(num2))
    elif num1 > num3:
        print (str(num3))
    else:
        print (str(num1))

# Funcion Separar #

def separar(lista):
    num_pares = []
    num_impares = []
    for numero in lista:
        if numero % 2 == 0:
            num_pares.append(numero)
        elif numero % 2 != 0:
            num_impares.append(numero)
        else:
            num_impares.append(numero)
    num_pares.sort()
    num_impares.sort()
    print(num_pares, num_impares)


# Funciones de registro #

def sub_menu():
    print("")
    print("Sub Menu de opciones: ")
    print("")
    print("A. Ver Usuarios Registrados.")
    print("B. Volver al Menu Principal.")
    print("")

def registro(user, password):
    if user in usuarios:
        print("Usuario existente, por favor ingrese otro.")
    else:
        usuarios[user] = password
        print("")
        print("Su Usuario: " + user)
        print("Su Contraseña: " + password)
        print("")
        print("¡Su registro ha sido generado exitosamente!")

def mostrar(user, password):    
    for user, password in usuarios.items():
        print("")
        print("Usuario: " + user + "\nContraseña: " + password)

# Desplegamos las opciones del menu principal #

def programa(menu):
    menu = input("Ingrese una opcion: ")
    while menu != "9":
        if menu == "1":
            print("")
            consulta = int(input("Ingrese su año a saber si es biciesto o no: "))
            print("")
            biciesto(consulta)
            menu_principal()
            menu = input("Ingrese una opcion: ")
        elif menu == "2":
            print("")
            base = float(input("Ingrese la Base del rectangulo: "))
            altura = float(input("Ingrese la Altura del rectangulo: "))
            print("")
            area_rectangulo(base, altura)
            menu_principal()
            menu = input("Ingrese una opcion: ")
        elif menu == "3":
            print("")
            radio = float(input("Ingrese el Area a calcular: "))
            print("")
            area_circulo(radio)
            menu_principal()
            menu = input("Ingrese una opcion: ")
        elif menu == "4":
            print("")
            numuero1 = float(input("Ingrese el Primer Numero: "))
            numuero2 = float(input("Ingrese el Segundo Numero: "))
            print("")
            relacion(numuero1, numuero2)
            menu_principal()
            menu = input("Ingrese una opcion: ")
        elif menu == "5":
            print("")
            num1 = float(input("Ingrese el Primer Numero: "))
            num2 = float(input("Ingrese el Segundo Numero: "))
            print("")
            intermedio(num1, num2)
            menu_principal()
            menu = input("Ingrese una opcion: ")
        elif menu == "6":
            print("")
            number1 = float(input("Ingrese el Numero a recortar: "))
            number2 = float(input("Ingrese el Numero que se posiciona en el Limite Inferior: "))
            number3 = float(input("Ingrese el Numero que se posiciona en el Limite Snferior: "))
            print("")
            recortar(number1, number2, number3)
            menu_principal()
            menu = input("Ingrese una opcion: ")
        elif menu == "7":
            print("")
            lista = [45, 23, 2, 197, 14, 100, 21, 14, 5, 92] # Lista editable. # -----------------------------------> ACA
            separar(lista)
            menu_principal()
            menu = input("Ingrese una opcion: ")
        elif menu == "8":
            print("")
            acc = input("Ingrese su Usuario: ")
            pss = input("Ingrese su Contraseña: ")
            registro(acc, pss)
            sub_menu()
            menu2 = input("Ingrese una sub opcion: ").upper()
            while menu2 != "B":
                if menu2 == "A":
                    mostrar(acc, pss)
                    sub_menu()
                    menu2 = input("Ingrese una sub opcion: ").upper()
                else:
                    print("")
                    print ("Ingreso un dato erroneo, por favor, ingrese una de las siguientes opciones.")
                    sub_menu()
                    menu2 = input("Ingrese una sub opcion: ").upper()
            menu_principal()
            menu = input("Ingrese una opcion: ").upper()
        else:
            print("")
            print ("Ingreso un dato erroneo, por favor, ingrese una de las siguientes opciones.")
            menu_principal()
            menu = input("Ingrese una opcion: ")
    
    print("")
    print("Gracias por utilizar nuestro programa.")
    print("")

# Llamamos a la funcion #

programa(menu_principal())