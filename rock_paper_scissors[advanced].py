import random as r

ratings = {}
global name, rating
rating = 0

def hello():
    rating_txt = open("rating.txt", 'r')
    for x in rating_txt.readlines():
        username, rate = x.split()
        ratings[username] = int(rate)
    name = input('Enter your name: ')
    if ratings.get(name):
        rating = ratings[name]
    print(f'Hello, {name}')
    rating_txt.close()

hello()

options = input().split(',')
if not any(options):
    options = ['rock', 'paper', 'scissors']
print("Okay, let's start")

while True:
    user = input()
    if user == '!exit':
        print("Bye!")
        break
    elif user == '!rating':
        print(f'Your rating: {rating}')
        continue
    elif user not in options:
        print("Invalid input")
        continue

    i = options.index(user)
    without_user = options[i:] + options[:i]
    win = without_user[:len(options) // 2 + 1]
    computer = r.choice(options)
    
    if user == computer:
        print(f"There is a draw ({user})")
        rating += 50
    elif computer not in win:
        print(f"Well done. Computer chose {computer} and failed")
        rating += 100
    else:
        print(f"Sorry, but computer chose {computer}")
