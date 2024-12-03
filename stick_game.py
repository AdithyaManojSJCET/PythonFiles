def stickgame():
    print('''
    \t\t!!RULES!!
    There are 16 sticks.
    Two players take turns to play the game.
    Each player picks one set of sticks (needn’t be adjacent) during his turn. 
    A set contains 1, 2, or 3 sticks. The player who takes the last stick is the loser.
     \n''')

    #Stick Size
    sticks=int(input("Enter the Number of Sticks: "))

    #Names Of the Players
    name1=input("Enter the First Name: ")
    name2=input("Enter the second Name: ")

    #Game Body
    while sticks>0:
        print(f"Sticks remaining:{sticks}")
        play=int(input(f"{name1}, pick 1,2, or 3 sticks: "))

        sticks-=play
        player1=sticks
        print(f"Sticks remaining:{sticks}")
        play2=int(input(f"{name2}, pick 1,2,or 3 sticks:"))
        sticks-=play2
        player2=sticks

    #Declaring who lost the game
        if player1<= 0:
            print(f"{name1} picks the last stick and loses the game!!")
        else:
            print(f"{name2} picks the last stick and loses the game!!")


stickgame()








