# Creador: Ian Bejenaru
# Fecha: 24/11/2024
# En este Script le pasaremos un texto y el se encargará de leerlo.
#------------------------------------------------------------------

# Paso 1: cargar las librerías necesarias.
import pyttsx3

# Creamos un menú en el que el usuario pueda decidir si quiere escribir un texto para que se lea, que pille el texto de un archivo .txt 
# o que lo lea de una pagina web
# variable que nos permite salir del bulce:
salir = True
while salir:
    opcion=input("Elige una opción que quieres convertir a texto:\n1) Escribir texto y convertir a voz\n2) Leer texto de un archivo txt\n3) Leer archivo de una WEB\n4) Salir\n")

    # El usuario escribe por pantalla el texto que quiere leer:
    if opcion =="1":
        # Creamos una variable en la que el usuario va a escribir un texto que quiera ser leído:
        texto_usuario = input("Escribe un texto que quieres que se lea: ")
        # Inicializamos el convertidor de texto a voz:
        engine = pyttsx3.init()
        # Le decimos lo que queremos que convierta a voz:
        engine.say(texto_usuario)
        # Iniciamos el audio:
        engine.runAndWait()
    elif opcion == "2":
        # Pedimos al usuario que elija un archivo txt que quiere leer de su PC:
        var =1
    elif opcion == "3":
        # Pedimos al usuario que pegue el link de la pagina web que quiere leer:
        pagina =1
    # Opción salir del programa:
    elif opcion == "4":
        print("Saliendo del programa....")
        salir = False
    # Cuando se selecciona una opcion que no existe:
    else:
        print("La opcion seleccionada no existe, prueba otra vez")


