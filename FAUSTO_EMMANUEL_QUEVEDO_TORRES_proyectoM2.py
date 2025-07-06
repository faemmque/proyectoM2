opcion = 0 #variable que almacena las opciones del menu

while True:
    #menu que muestra las opciones que el usuario puede elejir
    print("------------MENU------------")
    print(" - Longitud de una frase (1)")
    print(" - Encuentra el cuadrante (2)")
    print(" - Salir (3).")
    print("----------------------------")
    opcion = int(input("Elija una opcion (1,2,3): "))
    
    #si se elije la opcion 1 se ejecuta el codigo del ejercicio para saber la longitud de una palabra
    if opcion == 1:
        palabra = input("Por favor ingrese una palabra que contenga entre 4 y 8 caracteres: ")
        
        #validaciones que muestran un mensaje dependinete del numero de letras de la palabra
        if len(palabra) >= 4 and len(palabra) <= 8:
            print("La palabra es correcta")
        elif len(palabra) <= 4:
            print(f"Hacen falta letras. Solo tiene {len(palabra)} letras")
        elif len(palabra) >= 8:
            print(f"Sobran letras. Tiene {len(palabra)} letras")
        input("Presione una tecla para continuar.")
    #si se elije la opcion 2 se ejecuta el codigo para el ejecicio para encontrar el cuadrante de un punto
    elif opcion == 2:
        x = 0
        y = 0

        while True:
            print("Ingrese números positivos o negativos diferente de 0.")
            x = int(input("Ingrese el valor de X: ")) #solicitud del valor de x
            y = int(input("Ingrese el valor de Y: ")) #solicitud del valor de y
            #se valida que x y y no sean 0
            if x == 0 or y == 0:
                print("Ingreso un valor en 0. Intente de nuevo por favor")
                continue
            #si x y y no son 0 se procede a verificar en que cuadrante se encuentra el punto
            else:
                #validacion para el cuadrante I
                if x > 0 and y > 0:
                    print("El punto se encuentra en el cuadrante I")
                #validacion para el cuadrante II
                elif x < 0 and y > 0:
                    print("El punto se encuentra en el cuadrante II")
                #validacion para el cuadrante III
                elif x < 0 and y < 0:
                    print("El punto se encuentra en el cuadrante III")
                #validacion para el cuadrante IV
                elif x > 0 and y < 0:
                    print("El punto se encuentra en el cuadrante IV")
                input("Presione una tecla para continuar.")
                break
    #salida del programa
    elif opcion == 3:
        break
    else:
        print("Elija una opcion correcta.")

