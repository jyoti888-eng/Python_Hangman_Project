# including hangman images and if reduces loose messege will prompt 
import random
from hangman_words import word_list            #importing word list from hangman_word
end_of_game = False

#name_list = ['aardvark','baboon','camel']
choose_word = random.choice(word_list)
word_len = len(choose_word)

lives = 6

from hangman_art import logo                      #importing logo from hangman art
print(logo)
print(f'Pass the solution is {choose_word}')

display=[]                                        #print underscore as many letter in the word
for letter in range(word_len):
    display.append("_")


while not end_of_game:
    guess = input("guess a letter").lower()
    if guess in display:
        print(f"You have already guessed{guess}")



    for position in range(word_len):              #check guessed letter
        letter = choose_word[position]
        if letter == guess:
           display[position] = letter

    if guess not in choose_word:
        print(f'you guessed {guess} that is not in the word, You loose a life')
        lives = lives-1
        if lives == 0:
         end_of_game = True
         print("You loose")

    print(f"{' '.join(display)}")             #join all the elements in a list and turn it in to string

    if "_" not in display:
        end_of_game=True
        print("you win!")
    from hangman_art import stages
    print(stages[lives])
