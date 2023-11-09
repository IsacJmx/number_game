#main
import random

def main():
    
    minimum = 1
    maximum =1000

    choice = menu()
        
    while choice > 0 and choice < 3:
        
        if choice == 1:
            
            p1,p2 = players()
            
            turns(minimum, Maximum, p1, p2)
            
        
        elif choice == 2:
            minimum,maximum = get_number()

        
        
        
        
def menu():
    
    Choice = 0
    while Choice < 1 or Choice > 4:
        print('Welcome to the number guesser game')
        print('1. start game')
        print('2. Choose Range')
        print('3.Exit')
        
        Choice = int(input(': '))
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


def turns(Minimum, Maximum, p1, p2):
    
    
    answer = random.randint(Minimum, Maximum)
    guess = 0
    while guess != answer: 
        print("What is "+ p1 + "'s guess? ", end='')
        int(input(': '))
        
        if guess != answer:
            
            print("What is "+ p2 + "'s guess? ", end='')
        int(input(': '))
            
            
            
    else:
        print("You guessed the correct number!1!!!")
    

  
