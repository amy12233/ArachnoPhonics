import random
import time
import spiderDraw as sd
from functions import load_words, build_display, check_word, clear_screen, introduction

MAX_WRONG = 6

SPIDER_STAGES = [
    sd.spider_0,
    sd.spider_1,
    sd.spider_2,
    sd.spider_3,
    sd.spider_4,
    sd.spider_5,
    sd.spider_6
]

def play_round():
    # Checklist 2: Call introduction at the top of play_round()
    player_name = input("Your name: ")
    clear_screen()
    introduction(player_name)
    print("\nLoading new word...")
    time.sleep(1.5)
    
    words = load_words("words.txt")
    secret = random.choice(words).upper()
    
    guessed_letters = []
    incorrect_letters = []
    wrong = 0
    game = True
    
    while game:
        clear_screen()
        # Draw the spider corresponding to wrong counts
        SPIDER_STAGES[wrong]()
        
        display_word = build_display(secret, guessed_letters)
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses: {', '.join(incorrect_letters)}")
        
        # Checklist 3: Win check (before input to see complete word)
        if "_" not in display_word:
            print("\n🎉 Congratulations! You saved yourself and won the game!")
            game = False
            break
            
        # Checklist 3: Lose check
        if wrong >= MAX_WRONG:
            print(f"\n☠️ Game Over! The spider caught you. The word was: {secret}")
            game = False
            break
            
        # Accept a new guess letter
        wrong = check_word(guessed_letters, incorrect_letters, secret, wrong)


# Checklist 4: Wrap play_round() in a play-again loop in main()
def main():
    playing = True
    while playing:
        play_round()
        
        print("\n" + "-"*30)
        again = input("Do you want to play another round? (yes/no): ").lower().strip()
        if again not in ['yes', 'y']:
            print("\nThank you for playing ArachnoPhonics! Goodbye!")
            playing = False

if __name__ == "__main__":
    main()
