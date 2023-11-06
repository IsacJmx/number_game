#main
import random

def main():
    
    players()
    number = get_number()

def players():
    p1 = input("Who is player one? ")
    p2 = input("Who is player two? ")
    print("Welcome ", p1, " ", "and ", p2,
          "!",sep='')


def get_number():
    pass


def winner():
    pass


def turns(Minimum, Maximum):
    
    
    answer = random.randint(Minimum, Maximum)
    guess = 0
    while guess != answer: 
        guess = input("What is ", p1, "'s guess? ")
        get_number()
        
        if guess != answer:
            guess = input("What is ", p2, "'s guess? ")
            
    else:
        print("You guessed the correct number!1!!!")
    
