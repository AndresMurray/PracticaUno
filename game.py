import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)

# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print('Tiene 5 fallos como máximo hasta adivinar la palabra. ¡Buena suerte!')
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
max_fallos=0
while (max_fallos<5):
 # Pedir al jugador que ingrese una letra

    letter = input("Ingresa una letra: ").lower()
    
    if letter =="":
        print("Valor inválido,por favor ingrese otro:")
        continue

 # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
 # Agregar la letra a la lista de letras adivinadas

    guessed_letters.append(letter)
 # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        max_fallos=max_fallos+1
        if(max_fallos<5):
            print(f"¡Cuidado! Vas cometiendo: {max_fallos} fallos.")
            print(f"te quedan: {5-max_fallos} fallos disponibles")
        else:
            print("Perdiste :(")
            print(f"La palabra secreta era: {secret_word}")
            break
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
    else:
        print(f"Palabra: {word_displayed}")
        continue
     



