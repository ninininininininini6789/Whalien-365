import random
words = ("abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie")
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

Choosen_word = random.choice(words).lower()
# Creating placeholder
length_of_word = len(Choosen_word)
placeholder = ""
for _ in range(length_of_word):
    placeholder += "_"
print("Word to guess:",placeholder," " "Length of word", length_of_word)

# Guessing number and checking
Game_over = False
correct_letter = []
while not Game_over:

    guess = input(f"Guess a letter {user_name}!!: ").lower()

    if guess in correct_letter:
        print(f"Aw! You've already guessed the letter {guess} {user_name}!.")

    display = ""

    for letter in Choosen_word:
        if letter == guess:
            display += letter
        if guess not in correct_letter:
            correct_letter.append(guess)
        elif letter in correct_letter:
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

if lives >= 0:
    print(stages[lives])