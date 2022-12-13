strike = 0

word = input("Name a word to guess: ")

word_count = len(word)
guessed = []
def hidden(word):
    wordcount = len(word)
    for x in range(wordcount):
        print("_", end = ' ')

print("Guess the " + str(word_count) + " letter word: ", end = '')
hidden(word)
print(guessed)
