#Raquel Alejandra Ramírez Valencia A01632596

import random
import time

#Función explicar reglas del juego - no recibe nada
def instrucciones ():
    print("INSTRUCCIONES DEL JUEGO")
    print('''Se va a desplegar una baraja en la parte superior, donde algunas cartas serán múltiplos o divisores
    de tus cartas, que son las que están en la parte de abajo. Por ejemplo si tienes una carta 8, y en la baraja hay un 16,
    puedes colocarla ahí''')
    time.sleep(8)
    print('''Tienes que ingresar primero el número de tu carta, y después la posición de la carta que quieres cambiar''')
    time.sleep(6)
    print('''Cada vez que ingreses una carta, la carta de la baraja se divide entre el número de tu carta''')
    print("Ganas cuando la baraja quede sólo con unos (1)")
    time.sleep(8)
    print('\n\n\n\n\n')

#Función para desplegar la matriz 1x5 de la baraja - recibe una matriz vacía       
def despliega_matriz (matriz):
    print("Baraja: ")
    for lista in matriz:
        print(f"---- "*5)
        for valor in lista:                 
            valor=str(valor)
            print(valor.center(4,' '),end = '|')    
        print()
        print(f"---- "*5)

#Función para crear la primera matriz al empezar el juego de la baraja - recibe numero de renglones y columnas
def crea_primer_matriz (ren,com):
    matriz = []                  
    for renglon in range(ren):
        fila = []                  
        for columna in range(com):       
            x = random.randint(11,100)
            fila.append(x)
        matriz.append(fila)
    return matriz

#Función para generar las cartas del usuario - recibe la lista vacía del usuario
def generar_cartas (lista):
    for cantidad_lista in range(5):
        cartas = random.randrange(1,10)
        lista.append(cartas)

#Función para desplegar cartas del usuario  - recibe las lista de cartas generadas para el usuario

def despliega_cartas (lista):
    print(f"---- "*len(lista)) 
    for elemento in lista:
        elementi = str(elemento)
        print(elementi.center(4,' '), end = '|')    
    print()
    print(f"---- "*len(lista))   
    
#Función para que si ingresa cero, darle una nueva carta - recibe la lista, para poder modificar la última carta
def ingresar_carta (lista):
    nv = random.randrange(1,10)
    lista_user[-1] = nv

    
'''Función para ver si su carta si es multiplo o divisor de la baraja - recibe el número ingresado, la carta de la baraja a cambiar
y la matriz de ésta'''                                                                        
def comprobar_mult_div (numero,carta_acambiar,mat):
    if carta_acambiar>5 or carta_acambiar<1:
        print("Acuérdate de ingresar la posición, no el número de la carta. Ingresa números del 1 al 5 sólamente")
        return False
    else:
        carta = mat[0][carta_acambiar-1]
        if carta<numero:
            print("Prueba con otra carta, la carta que has ingresado es mayor al número que quieres dividir")
            return False
        else:
            if carta%numero == 0:
                return True
            else:
                print(f"El {numero} no es divisor de {carta}")
                return False 
        
'''Función para cambiar la baraja por la división de la carta de la baraja entre carta del usuario - recibe la carta el usuario, la posición
de la carta de la baraja, la matriz y la lista del usuario'''
def cambiar_baraja_avalor (valor,posicion,mat,lista_user):
    mat[0][posicion-1] = mat[0][posicion-1]//valor
    index = lista_user.index(valor)
    nv = random.randrange(1,10)
    lista_user[index] = nv
    
#Si su carta es número primo comprobar - recibe la lista del usuario para añadirle un número primo
def si_primo(lista_user):
    primo = int(input("¿Qué número primo necesitas?"))
    if primo in [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,
                 59,61,67,71,73,79,83,89,97]:
        print("Buena jugada! Acaso eres Einstein?")
        lista_user[-1] = primo
    else:
        print(f"El número {primo} no es un número primo")
        
        
#Comprobar que el usuario ya tenga uno's y haya terminado el juego - recibe la matriz para evaluar si esta en unos
def comprobar_si_unos (mat):
    contador = 0
    for elementos in range(5):
        if mat[0][elementos] == 1:
            contador += 1
    return contador
    
    
#PROGRAMA PRINCIPAL
print("BIENVENIDO AL SOLITARIO DE LAS MULTIPLICACIONES".center(478,' '))
print("§".center(134,'-'))
print("¿Estás listo para empezar?".center(133,' '))
listo = input(">>>Dale enter")
instrucciones()
lista_user = []
if listo == '':
    print("Empieza a jugar!!".center(133,' '))         
    mat = (crea_primer_matriz(1,5))               #Crear matriz de un reglón y 5 columnas
    generar_cartas(lista_user)                    #Generar las cartas del usuario
    unos = 0  
    while unos<5:                                 #Mientras las 5 cartas no sean uno, repetir
        print("\n\n")
        despliega_matriz(mat)
        print("Tus cartas son: ")
        despliega_cartas(lista_user)
        #A continuación el usuario debe de ingresar el número de su carta
        valor=int(input("Ingresa el número de tu carta -(Escribe 0 si quieres cambiar la última carta y -1 si necesitas un número primo)")) 
        if valor == 0:
            ingresar_carta(lista_user)
        elif valor == -1:  
            primo = si_primo(lista_user)     
        elif valor not in lista_user:
            print("Esa carta no está en tu baraja. No hagas trampa")
        else:
            posicion = int(input("Ingresa la posición donde está la carta a cambiar (1,2,3,4 o 5): "))  #Pone posición de la carta que quiere cambiar
            comprobar = comprobar_mult_div(valor, posicion, mat)                                        #Se comprueba si es múltiplo
            if comprobar == False:       #Si no es múltiplo, se vuelve al inicio del while
                continue
            else:
                cambiar_baraja_avalor(valor,posicion,mat,lista_user)  #Cambia el valor de la baraja si si es múltiplo
                unos = comprobar_si_unos(mat)
    despliega_matriz(mat)
    print("Felicidades!!! Eres el mejor jugador que ha visto este progama. Has logrado dejar todas las cartas en 1")  #Se acaba el juego
                    
                    
    
