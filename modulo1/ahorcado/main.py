import random
ahorcado = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     -|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     -|-  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     -|-  |
     |    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     -|-  |
     | |  |
          |
    =========''']
palabras = """valoracion aprenderpython comida juego python web imposible
           variable curso volador cabeza reproductor mirada escritor billete
           lapicero celular valor revista gratuito disco voleibol
           anillo estrella""".split()


def buscar_palabra_aleatoria(lista_palabras):
    # Esta funcion retorna una palabra aleatoria.
    palabra_aleatoria = random.randint(0, len(lista_palabras) - 1)
    return lista_palabras[palabra_aleatoria]


def mostrar_tablero(ahorcado, letra_incorrecta, letra_correcta, palabra_secreta):
    print(ahorcado[len(letra_incorrecta)])
    print("")
    fin = " "
    print('Letras incorrectas:', fin)
    for letra in letra_incorrecta:
        print(letra, fin)
    print("")
    espacio = '_' * len(palabra_secreta)
    # Remplaza los espacios en blanco por la letra bien escrita
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] in letra_correcta:
            espacio = espacio[:i] + palabra_secreta[i] + espacio[i+1:]
    # Mostrará la palabra secreta con espacios entre letras
    for letra in espacio:
        print(letra, fin)
    print("")


def elije_letra(alguna_letra):
    # Devuelve la letra que el jugador ingreso.
    # Esta función hace que el jugador ingrese
    # una letra y no cualquier otra cosa
    while True:
        print('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print('Introduce una sola letra.')
        elif letra in alguna_letra:
            print('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print('Elije una letra.')
        else:
            return letra


def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar,
    # de lo contrario devuelve False
    print('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')


print('A H O R C A D O')
letra_incorrecta = ""
letra_correcta = ""
palabra_secreta = buscar_palabra_aleatoria(palabras)
finJuego = False
while True:
    mostrar_tablero(ahorcado, letra_incorrecta, letra_correcta, palabra_secreta)
    # El usuairo elije una letra.
    letra = elije_letra(letra_incorrecta + letra_correcta)
    if letra in palabra_secreta:
        letra_correcta = letra_correcta + letra
        # Se fija si el jugador ganó
        letrasEncontradas = True
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] not in letra_correcta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print('¡Muy bien! La palabra secreta es "'
                  + palabra_secreta
                  + '"! ¡Has ganado!')
            finJuego = True
    else:
        letra_incorrecta = letra_incorrecta + letra
        # Comprueba la cantidad de letras
        # que ha ingresado el jugador y si perdió
        if len(letra_incorrecta) == len(ahorcado) - 1:
            mostrar_tablero(ahorcado, letra_incorrecta,
                         letra_correcta, palabra_secreta)
            print('¡Se ha quedado sin letras!\nDespues de '
                  + str(len(letra_incorrecta))
                  + ' letras erroneas y '
                  + str(len(letra_correcta))
                  + ' letras correctas, la palabra era "'
                  + palabra_secreta + '"')
            finJuego = True
    # Pregunta al jugador si quiere jugar de nuevo
    if finJuego:
        if empezar():
            letra_incorrecta = ""
            letra_correcta = ""
            finJuego = False
            palabra_secreta = buscar_palabra_aleatoria(palabras)
        else:
            break
