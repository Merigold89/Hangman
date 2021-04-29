import random

print('H A N G M A N')


def ask():
    menu = str(input('\nType "play" to play the game, "exit" to quit: '))
    if menu == "play":
        game_menu()


def game_menu():
    answers = ['python', 'java', 'kotlin', 'javascript']  # word base to guess
    answer = random.choice(answers)
    masked = '-' * (len(answer))  # hidden letters as '-' in word
    a = 0
    letter = ()
    letter_used = [0]
    while a <= 7:
        if ('-' in masked) is False:
            a = 8
            print(f'You guessed the word {masked}!\nYou survived!')
            ask()
        else:
            print(f'\n{masked}')
            letter = input(f'Input a letter: ')
            if (letter.isalpha() is True) and (letter.islower() is True) and (len(letter) == 1):
                if letter in answer:
                    for sign in answer:
                        if sign == letter:
                            hint = int(answer.index(sign))
                            answer = answer.replace(letter, '-', 1)
                            masked = masked[:hint] + letter + masked[hint + 1:]
                else:  # wrong letter or already used reduce "life"
                    if letter in letter_used:
                        print("You've already guessed this letter")
                    else:
                        print("That letter doesn't appear in the word")
                        a += 1
                    if a == 8:
                        print(f'You lost!')
                        ask()
                letter_used += letter
            else:  # life does not decrease when you enter an incorrect answer
                if letter == '':  # no answer / enter
                    print('You should input a single letter')
                elif len(letter) > 1:  # more than 1 character entered
                    print('You should input a single letter')
                elif letter.isdigit() is True:  # the entered character is a number
                    print('Please enter a lowercase English letter')
                elif letter.islower() is False:  # capital letter entered
                    print('Please enter a lowercase English letter')

ask()