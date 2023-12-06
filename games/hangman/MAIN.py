import random
from art import stages, logo

def hangman():
    word_list = ["baboon", "camel", 'python', 'programming', 'computer', 'code', 'algorithm']
    word = random.choice(word_list)
    display = [] 
    word_length = (len(word))
    lives = 6
    print(logo)
    print('Welcome to the hangman game!')
    for _ in range(word_length):
        display += '_'
    letters = []
    end_of_game = False
    while not end_of_game:
        guess = input('Chose a letter: ')
        if guess in letters:
            print('You have already chose that letter')
            continue
        letters.append(guess)
        for position in range(word_length):
            letter = word[position]
            if letter == guess:
                display[position] = letter
        
        if guess not in word:
                print(f'{guess} is not a letter.')
                lives -= 1
        print(display)
        if '_' not in display:
            end_of_game = True
            print('You win!')
        elif lives == 0:
            end_of_game = True
            print('You lose!')
            print('Word was',word)
        print(stages[lives])
hangman()
    
        