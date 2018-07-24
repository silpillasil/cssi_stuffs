word = "hangman"
blanks = []
already_guessed = []

for letter in word:
    blanks.append("_ ")

play = True

while play:

    print "".join(blanks)
    print "Guesses: " + ",".join(already_guessed)
    guess_letter = input("Guess? -> ")

    if guess_letter in word:
        for i in word:
            if guess_letter == i:
                #print "yay"
                blanks.index(word.index(i)) = i + " "
    else:
        already_guessed.append(guess_letter)

    if "_ " in blanks:
        continue
    else:
        break
