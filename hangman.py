import random

def play():
    words = ('python', 'java', 'kotlin', 'javascript')
    word = random.choice(words)
    guessword = '-' * len(word)
    cache = set()
    counter = 8
    while counter > 0:
        print()
        print(guessword)
        if guessword == word:
            print("You guessed the word!\nYou survived!")
            break
        
        letter = input("Input a letter: ")
        if letter in cache:
            print("You already typed this letter")
            continue
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if  not (97 <= ord(letter) <= 122):
            print("It is not an ASCII lowercase letter")
            continue
        cache.add(letter)
        for i in range(0,len(word)):
            if letter == word[i]:
                guessword = guessword[:i] + letter + guessword[i+1:]
                

        pos = word.find(letter)
        if pos < 0:
            print("No such letter in the word")
            counter -= 1
            
    if counter == 0:
        print("You are hanged!")

print("H A N G M A N")

while True:
    action = input('Type "play" to play the game, "exit" to quit: ')
    if action == "play":
        play()
    elif action == "exit":
        break
