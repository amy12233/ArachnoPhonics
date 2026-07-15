def load_words(path):
    """Return a list of words read from `path` (one per line)."""
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]

def build_display(secret, guessed_letters):
    """Return the word with unguessed letters replaced by '_'."""
    return " ".join(c if c in guessed_letters else "_" for c in secret)

def check_word(correct, incorrect, word, wrong):
    """Prompts player for a guess and updates tracking sets."""
    guess = input("Guess a letter: ").upper().strip()
    if not guess:
        return wrong
    if guess in word:
        if guess not in correct:
            correct.append(guess)
    else:
        if guess not in incorrect:
            incorrect.append(guess)
            wrong += 1
    return wrong

def clear_screen():
    """Clears the console layout."""
    print("\n" * 40)

# Checklist 1: Add introduction(name) that prints a bordered welcome
def introduction(name):
    print("=" * 40)
    print(f"  WELCOME TO ARACHNOPHONICS, {name.upper()}!  ")
    print("=" * 40)
    print("Guess letters to reveal the hidden word.\nAvoid drawing the full spider!")
