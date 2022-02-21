import random

name_list=['aardvark','baboon','camela']
choose_word=random.choice(name_list)
print(f'Pass the solution is {choose_word}')
display=[]
word_len=len(choose_word)
for letter in range(word_len):
    display.append("_")
end_of_game=False

while not end_of_game:
    guess =input("guess a letter a").lower()

    for position in range(word_len):
        letter=choose_word[position]
        if letter==guess:
            display[position]=guess
    print(display)
    if "_" not in display:
        end_of_game=True;
        print("you win!")

