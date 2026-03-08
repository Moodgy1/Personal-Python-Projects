import random

# 🔥 Put your funny meme words or phrases here 🔥
WORDS = [
    "skull emoji",
    "ohio final boss",
    "rizz",
    "gyatt",
    "sigma male",
    "npc energy",
    "caught in 4k",
    "bro thinks he's him",
    "side eye",
    "sus",
    "based",
    "no bitches",
    "goofy ahh",
    "skill issue"
]

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

def choose_word():
    return random.choice(WORDS).lower()

def display_progress(secret_word, guessed_letters):
    display = ""
    for char in secret_word:
        if char == " ":
            display += "  "
        elif char in guessed_letters:
            display += char + " "
        else:
            display += "_ "
    return display

def hangman():
    print("🎮 Welcome to MEME HANGMAN 💀")
    secret_word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    while wrong_guesses < max_wrong:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word:", display_progress(secret_word, guessed_letters))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower().strip()

        if not guess or len(guess) != 1 or not guess.isalpha():
            print("❌ Enter ONE letter, you NPC 💀")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that, lil bro.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("✅ W guess 😎")
        else:
            wrong_guesses += 1
            print("❌ L guess 😭")

        if all(char in guessed_letters or char == " " for char in secret_word):
            print("\n🎉 YOU WON BRO 🏆")
            print("The word was:", secret_word)
            return

    print(HANGMAN_PICS[wrong_guesses])
    print("\n💀 YOU GOT HANGED")
    print("The word was:", secret_word)

if __name__ == "__main__":
    hangman()
