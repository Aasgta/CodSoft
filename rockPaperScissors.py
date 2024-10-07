import random

score = []

def check(computer,user):
    # global score
    if computer==user:
        print("It's a draw.")
        return 0
        
    if(computer==1 and user ==2):
        print("You won!")
        return 1
        
    if(computer==2 and user ==0):
        print("You won!")
        return 1
        
    if(computer==0 and user ==1):
        print("You won!")
        return 1
        
    print("You lose!")
    return -1    

print("Welcome to the Rock Paper Scissors Game !!!")

while(True):
    print('''Enter 0 for Rock
      1 for Paper
      2 for Scissors
      and 3 to QUIT the game . ''')
    user = int(input())
    computer = random.randrange(0,3)
    if(user==3):
        break
    print(f"Your choice is {user}")
    print(f"Computer's choice is {computer}")

    score.append(check(computer,user))
total=0
for i in range(0,len(score)):
    total += score[i]  
print("Thank for playing the game.")
print(f"The final score is {total}.")
