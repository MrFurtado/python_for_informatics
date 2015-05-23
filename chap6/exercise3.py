# accept a word and a letter and count how many times the letter is in the word. Do it in a function
def count(letter, word):
    count = 0
    for i in word:
        if i == letter:
            count = count + 1
    print count

word = raw_input("Enter a word: ")
letter = raw_input("Enter a letter: ")
count(letter, word)

