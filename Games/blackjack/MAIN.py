import random
import replit
import art
def deal_card():
    '''Generates a random card from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Calculates the total score of the cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
    '''Compare the total score from both the user and the computer.'''
    if user_score == computer_score:
        return "It's a draw."   
    elif user_score == 0:
        return 'You win with a Blackjack!'
    elif computer_score == 0:
        return 'You lose, oponent had a Blackjack.'
    elif user_score > 21:
        return 'You lose, you went over.'
    elif computer_score > 21:
        return 'You win, oponent went over!'
    elif user_score > computer_score:
        return 'You win!'
    else:
        return 'You lose.'


def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    game_end = False
    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print('Your cards:', user_cards, "Your score:", user_score)
        print('Computer cards:', computer_cards[0])
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True
        while True:
            user_pick_card = input("Do you wish another card? Type 'y' or 'n'. ")
            if user_pick_card == "y":
                user_cards.append(deal_card())
                break
            elif user_pick_card == 'n':
                game_end = True
                break
            else:
                print("Invalid input. Please type 'y' or 'n'.")
        
    while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        
    print(f'    Your score is: {user_score}, your deck is {user_cards}.')
    print(f'    Oponent score is {computer_score}, oponent deck is {computer_cards}.')
    print(compare(user_score, computer_score))
        
while True:
    a = input('Do you want to play a game of blackjack? Type "y" or "n": ')
    if a == 'n':
        break
    elif a == 'y':
        replit.clear()
        play_game()
    else:
        print("Invalid input. Please type 'y' or 'n'.")
    