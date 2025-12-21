import random

# lista de palabras posibles
palabras = ["python", "programacion", "ahorcado", "software", "ingenieria"]

# selecciona una palabra aleatoria
palabra_secreta = random.choice(palabras)

# convierte la palabra en lista
palabra_lista = list(palabra_secreta)

# lista que muestra el progreso del jugador
palabra_oculta = ["_"] * len(palabra_lista)

# lista para guardar letras usadas
letras_usadas = []

# variable de control para los intentos
intentos_maximos = 6
intentos_restantes = intentos_maximos

# booleano para controlar el estado del juego
juego_activo = True

print("===================================")
print("            JUEGO EL AHORCADO      ")
print("===================================\n")

# bucle principal del juego
while juego_activo and intentos_restantes > 0 and "_" in palabra_oculta:

    print("Palabra:", " ".join(palabra_oculta))
    print("Intentos restantes:", intentos_restantes)
    print("Letras usadas:", ", ".join(letras_usadas))

    # pedir letra
    letra = input("Ingresa una letra: ").lower()

    # validación: solo una letra
    if len(letra) != 1 or not letra.isalpha():
        print(" Ingresa solo UNA letra válida.\n")
        continue

    # validación: letra repetida
    if letra in letras_usadas:
        print(" Ya usaste esa letra.\n")
        continue

    # guardo la letra usada
    letras_usadas.append(letra)

    # booleano para saber si la letra acierta
    acierto = False

    # verifico si la letra está en la palabra
    for i in range(len(palabra_lista)):
        if palabra_lista[i] == letra:
            palabra_oculta[i] = letra
            acierto = True

    if acierto:
        print(" La letra está en la palabra.\n")
    else:
        print(" La letra no está en la palabra\n")
        intentos_restantes -= 1

# fin del juego
if "_" not in palabra_oculta:
    print("Palabra:", " ".join(palabra_oculta))
    print("\n ¡Felicidades, adivinaste la palabra!")
else:
    print("\n Te quedaste sin intentos")
    print("La palabra correcta era:", palabra_secreta)

print("\nPrograma terminado")
