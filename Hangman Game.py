import random
import words.txt
print(r'''_
      | |
      | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
      | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
      | | | | (_| | | | | (_| | | | | | | (_| | | | |
      |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/                   ''')
stages = [r'''
    ___________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
    
    ''',r'''
     ___________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___''',r'''
    ___________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___''', r'''
    ___________
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___''', r'''
    ___________
     |/      |
     |      (_)
     |      \|
     |       
     |     
     |
    _|___''',r'''
    ___________
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___
          ''',r'''
    ___________
     |/      |
     |      (_)
     |       
     |      
     |
    _|___
          ''',r'''
    ___________
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___
          ''']
# Creating word by computer

lives = 7
user_name = input("Enter your username")

Choosen_word = random.choice(words.word_list).lower()
# Creating placeholder
length_of_word = len(Choosen_word)
placeholder = ""
for placeholder in range(length_of_word):
    placeholder+="_"
print("Word to guess:",placeholder," " "Length of word", length_of_word)

# Guessing number and checking
Game_over = False
correct_letter = []
while not Game_over:

    guess = input(f"Guess a letter{user_name}!!: ").lower()

    if guess in correct_letters:
        print(f"Aw! You've already guessed the letter {guess} {user_name}!.")

    display = ""

    for letter in Choosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display+= "_"
    print(display)


    if guess not in Choosen_word:
        lives -= 1
        print(stages[lives])
        print(f"You guessed {guess}, which is not in the word. You lose a life ૮(˶ㅠ︿ㅠ)ა")
    if lives == 0:
        Game_over = True
        print(f"YOU LOST {user_name}｡°(°.◜ᯅ◝°)°｡ hangman is complete. The word was", Choosen_word+".")

    if "_" not in display:
        Game_over = True
        print(f"YOU WIN {user_name}ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧ The word was", Choosen_word+".")

print(stages[lives])