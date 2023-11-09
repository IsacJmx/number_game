#main
import random

def main():


def menu():
    
    Choice = 0
    while Choice < 1 or Choice > 4:
        print('Welcome to the number guesser game')
        print('1. start game')
        print('2. Choose Range')
        print('3.Exit')
        
        Cice = int(input(': '))
        return Choice
    
def players():
    
    # get the players names
    p1 = input("Who is player one? ")
    p2 = input("Who is player two? ")
    
    # print welcome
    print("Welcome ", p1, " ", "and ", p2,
          "!",sep='')
    

def get_number():
    
    # get min and max numbers
    Minimum  = int(input("What is the minimum number? "))
    Maximum  = int(input('What is the maximum number? '))


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
    

  
