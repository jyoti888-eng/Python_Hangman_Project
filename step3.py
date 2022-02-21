"""TODO if choosen letter , if that exist in the random word choosen 
by list then print that number of underscore and , put the letters at their respective position"""

import random
name_list=['aardvark','baboon','camela']
choose_word=random.choice(name_list)
print(f'Pass the solution is {choose_word}')
display=[]
word_len=len(choose_word)
for letter in range(word_len):
    display.append("_")
guess =input("guess a letter").lower()

for position in range(word_len):
    letter=choose_word[position]
    if letter==guess:
        display[position]=guess
print(display)