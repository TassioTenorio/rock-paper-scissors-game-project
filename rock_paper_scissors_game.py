import os
import random

def options_menu():
    print('[1] Rock')
    print('[2] Paper')
    print('[3] Scissors')
    print('[0] Exit')

def user():
    while True:
        choice = input('Choose an option: ')
    
        if choice == '1':
            return 'Rock'
        elif choice == '2':
            return 'Paper'
        elif choice == '3':
            return 'Scissors'
        elif choice == '0':
            return None
        else:
            print('Invalid option! Try again.')
                        
        
def computer():
    choice_computer = random.choice(['Rock', 'Paper', 'Scissors'])
    print(f'The computer chose {choice_computer}')
    return choice_computer
        
def determine_winner(user, computer):   
    if user == computer:
        print('You tied!')
        return 'tie'
    elif(user == 'Rock' and computer == 'Scissors') or \
        (user == 'Scissors' and computer == 'Paper') or \
        (user == 'Paper' and computer == 'Rock'):
        print('You won!')
        return 'user'
    else:
        print('Computer won!')
        return 'computer'

        
                
def display_score(user_score, computer_score):    
    print(f'Score: You {user_score} x {computer_score} Computer')
        


def check_game_over(user_score, computer_score):
    if user_score == 5:
        print('Congratulations, You won the game!')
        input('\nPress ENTER to return to the menu...')
        return True

    elif computer_score == 5:
        print('Sorry, Computer won the game!')
        input('\nPress ENTER to return to the menu...')
        return True

    input('\nPress ENTER to continue...')
    return False

def main():
    user_counter = 0
    computer_counter = 0
    while True:
        os.system('cls')
        options_menu()
        user_choice = user()
        if user_choice is None:
            print('Leaving the game, see you later!')
            break
        
        computer_choice = computer()
        result = determine_winner(user_choice, computer_choice)
        if result == 'user':
            user_counter += 1
        elif result == 'computer':
            computer_counter += 1
        
        display_score(user_counter, computer_counter)
        if check_game_over(user_counter, computer_counter):
            user_counter = 0
            computer_counter = 0
if __name__ == '__main__':
    main()
      
        
        




               