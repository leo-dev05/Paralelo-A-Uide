# palabra secreta fija por ahora
palabra_secreta = "python"

# convierte la palabra en lista
palabra_lista = list(palabra_secreta)

# lista que muestra el progreso del jugador
palabra_oculta = ["_"] * len(palabra_lista)

# variable de control para los intentos permitidos
intentos_maximos = 6
intentos_restantes = intentos_maximos

print("===================================")
print("            JUEGO EL AHORCADO      ")
print("===================================\n")

# el bucle while controla el flujo del juego
# se repite mientras queden intentos y aun haya letras sin descubrir
while intentos_restantes > 0 and "_" in palabra_oculta:

    # muestro el estado actual de la palabra oculta
    print("Palabra:", " ".join(palabra_oculta))
    print("Intentos restantes:", intentos_restantes)

    # pido la letra
    letra = input("Ingresa una letra: ").lower()

    # condicion logica para verificar si la letra esta en la palabra
    if letra in palabra_lista:
        print("La letra está en la palabra.\n")

        # bucle for con range() para recorrer cada posición de la palabra
        # aqui comparo cada letra y reemplazo los guiones donde corresponda
        for i in range(len(palabra_lista)):
            if palabra_lista[i] == letra:
                palabra_oculta[i] = letra

    else:
        print("La letra no está en la palabra.\n")

        # variable de control se reduce un intento cada vez que se falla
        intentos_restantes -= 1

# aqui ya termino el while: o el jugador adivino la palabra o se le acabaron los intentos 
if "_" not in palabra_oculta:
    print("Palabra:", " ".join(palabra_oculta))
    print("\n¡Felicidades, adivinaste la palabra!")
else:
    print("\nTe quedaste sin intentos.")
    print("La palabra correcta era:", palabra_secreta)

print("\nPrograma terminado.")
