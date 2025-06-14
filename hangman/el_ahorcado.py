import random

def draw_hangman(guesses):
    hangman_pics = ['''
      +---+
          |
          |
          |
          |
          |
    =========''','''
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
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    print(hangman_pics[guesses])

def graf_game_over():
    print('''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''')

def play_again():
    while True:
        decision = input('¿Quieres jugar otra vez? (s/n): ')
        if decision == 's':
            return True
        elif decision == 'n':
            return False
        else:
            print('Por favor, introduce "s" o "n".')

def get_guess(word, guessed_letters):
    while True:
        guess = input('Adivina una letra o escribe la palabra completa: ').lower()
        if len(guess) == len(word):
            return guess
        elif len(guess) != 1:
            print('Por favor, introduce solo una letra o la palabra completa.')
        elif guess in guessed_letters:
            print('Ya has adivinado esa letra. Prueba otra.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor, introduce una letra.')
        else:
            return guess

def play_game():
    print('¡Bienvenido al juego del ahorcado!')
    words = ['python🐍', 'programacion📅⌨️', 'juego🕹️', 'ordenador💻', 'informatica⌨️🖱️🖥️']
    word = random.choice(words)
    guesses = 0
    max_guesses = 7
    guessed_letters = []
    game_over = False

    while not game_over:
        draw_hangman(guesses)
        print(' '.join([letter if letter in guessed_letters else '_' for letter in word]))

        if set(guessed_letters) == set(word):
            print('¡Felicidades! Has adivinado la palabra.')
            game_over = True

        guess = get_guess(word, guessed_letters)
        if len(guess) == len(word) and guess != word:
            print('¡La palabra', guess, 'no es correcta! Te quedan', max_guesses - guesses, 'intentos.')
            guesses += 1
        else:
            if guess in word:
                guessed_letters.append(guess)
            else:
                print('¡La letra', guess, 'no está en la palabra! Te quedan', max_guesses - guesses, 'intentos.')
                guesses += 1

        if guesses == max_guesses:
            print('Fucked!!🥴')
            graf_game_over()
            print('¡Oh no! Te has quedado sin intentos😭😭. La palabra era', word)
            game_over = True

def main():
    while True:
        play_game()
        if not play_again():
            break


if __name__ == "__main__":
    main()
