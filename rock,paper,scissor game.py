# rock, paper, scissor game

valid_moves=["rock","paper","scissor"]


print("valid moves are: rock, paper, scissor")
print("player1 and player2 will enter their picks")

# input from players
player1=input("enter your pick=")
player2=input("enter your pick=")

if player1 not in valid_moves or player2 not in valid_moves:
    print("invalid moves")
else:
    # tie case
    if(player1==player2):
        print("tie") 
        # rock cases

    elif(player1=="rock" and player2=="paper"):
        print("player2 wins")
    elif(player1=="rock" and player2=="scissor"):
        print("player1 wins")  

        # paper cases  
    elif(player1=="paper" and player2=="scissor"):
        print("player2 wins")
    elif(player1=="paper" and player2=="rock"):
        print("player1 wins")        

        # scissor cases 
    elif(player1=="scissor" and player2=="rock"):
        print("player2 wins")    
    elif(player1=="scissor" and player2=="paper"):
        print("player1 wins")    
        
#  end of code
