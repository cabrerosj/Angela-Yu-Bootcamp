import random
from wordList import word_list
from hangmanArt import stages, logo

chosen_word = random.choice(word_list).upper()
display = []
tries = 6
guessBank = []
triesLeft = f"Number of tries left: "

print(f"\nWelcome to:{logo}")
print(f"\nYour word is: {chosen_word}")
print(stages[len(stages)-1])

for letter in chosen_word:
    if letter == " ":
        display += " "
    else:
        display += "_"

print(" ".join(display))

while "_" in display and tries > 0:
    guess = input("\nGuess a letter.\n").upper()
    print(f"\nYou guessed {guess}.")

# ****** If the guessed letter is in the word, the letter replaces "_" in display ******
    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            if guess in guessBank:
                print(f"\nYou've already guessed {guess}. Try again.")
            else:
                display[position] = guess

    if guess in chosen_word and guess not in guessBank:
        # ****** Adds the guessed letter into the Letter Bank ******
        guessBank += guess
    if guess not in chosen_word and guess not in guessBank:
        guessBank += guess
        tries -= 1
        print(f"\n{guess} is not in the word.\n")
    elif guess not in chosen_word and guess in guessBank:
        print(f"\nYou've already guessed {guess}. Try again.\n")

    print(f"Your word is {chosen_word}\n")
    print(triesLeft, tries)
    print(f"\nLetters you've guessed so far: {guessBank}")
    print(stages[tries])
    print(" ".join(display))
        
    if "_" not in display:
        print("YOU WIN. You've saved this man from hanging.")
    
    if tries == 0:
        print("YOU LOSE. You're responsible for this man's death.")