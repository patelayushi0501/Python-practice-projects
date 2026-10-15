
Rules ="""Rocks defeats Scissor.
Scissor defeats Paper.
Paper defeats Rocks."""

x=int(input("Enter how many time you have played this game:"))
if x==0:
    print(Rules)
    print("Let's continue with the game:")
else:
    print("Let's continue with the game:")
l=['Rocks','Paper','Scissor']
while True:
    n=input("Enter your choice(Player 1):")
    m=input("Enter your choice(Player 2):")
    if n  in l and m in l :
       if n==m :
           print("It's a tie")
       elif n=='Rocks' and m=='Scissor'or n=='Scissor' and m=='Paper' or n=='Paper' and m=='Rocks':
           print("Player 1 win")
       else:
            print("Player 2 win")
    else:
     print("Invalid input. Try again.")
     continue
    y=input("Wanna play again:")
    while y  not in ['yes' ,'no']:
        print("Please enter yes or no ")
        y=input("Wanna play again:")
        
    if y =='yes':
                continue
    elif y=='no':
                print("Thank you")
                break