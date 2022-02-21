# including hangman images and if reduces loose messege will prompt 

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
name_list = ['aardvark','baboon','camel']
choose_word = random.choice(name_list)
word_len = len(choose_word)

lives = 6

print(f'Pass the solution is {choose_word}')

display=[]                                        #print underscore as many letter in the word
for letter in range(word_len):
    display.append("_")


while not end_of_game:
    guess = input("guess a letter").lower()

    for position in range(word_len):              #check guessed letter
        letter = choose_word[position]
        if letter == guess:
           display[position] = letter

    if guess not in (choose_word):
       lives = lives-1
       if lives == 0:
         end_of_game = True
         print("You loose")

    print(f"{' '.join(display)}")             #join all the elements in a list and turn it in to string

    if "_" not in display:
        end_of_game=True;
        print("you win!")

    print(stages[lives])
