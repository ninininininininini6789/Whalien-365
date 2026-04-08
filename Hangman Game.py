import random

def hangman():
    words = ["Like", "Interlude", "No", "Coffee", "Paldogangsan", "Tomorrow", "Jump", "Danger", "Rain", "Heaven", "Embarassed", "Dope", "Run", "Butterfly", "Begin", "Lie", "Stigma", "Reflection", "Mama", "Awake", "Lost", "DNA", "Dimple", "Paradise", "Anpanman", "Euphoria", "Her", "Singularity", "Tear", "Idol", "Mikrokosmos", "Home", "Dionysus", "Heartbeat", "Lights", "Filter", "On", "Ugh", "Friends", "Moon", "Respect", "Ego", "Telepathy", "Disease", "Stay", "Dynamite", "Butter", "Hooligan", "Aliens", "Fya", "Swim", "Normal", "Please"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 12
    word_display = ["_"] * len(word_to_guess)

    print("Welcome to Hangman!!!")
    while attempts > 0 and "_" in word_display:
        print(f"\nWord: {''.join(word_display)}")
        print(f"Guessed letters: {','.join(guessed_letters)}")
        print(f"Attempts Left: {attempts}")
        guess = input("GAMBLE AND GUESS A LETTER!: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!!! Your being a bit dumb")
        elif guess in word_to_guess:
            print("YAY! ")