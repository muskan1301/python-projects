import random
from hangman_art import stages, logo
from hangman_words import word_list
print(logo)
end_of_game = False
lives = len(stages) - 1
chosen_word = random.choice(word_list)
word_choosen = random.choice(word_list)
lives = 6
print(f'Solution is: {word_choosen}')
display = []
for _ in range(len(word_choosen)):
    display += "_"
print(display)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(word_choosen)):
        letter = word_choosen[position]
        if letter == guess:
            display[position] = letter
    if guess not in word_choosen:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])