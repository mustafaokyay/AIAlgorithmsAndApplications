"""
Lecture 3 - Introduction into AI Programming with Python
@author: Dominik Jung (dominik.jung42@gmail.com)
"""

secret = 42
guess = 123
while guess != secret: 
    guess = int(input("Please, give a guess: "))
    if guess == 0:
        break
print("You won!")
