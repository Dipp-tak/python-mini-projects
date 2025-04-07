import random


user_score = 0
comp_score = 0


game = str(input("Enter\n 1-'start' - 'Play' the game 2-'Exit' Quit the game")).lower()
if game == 'start':
    while(True):
        user_choice = str(input("Please make your choice:\n rock\n paper\n scissor\nexit-quit the game\n")).lower()
        comp_choice_list = ["rock","paper","scissor"]
        comp_choice = random.choice(comp_choice_list)

        if (user_choice == 'rock' and comp_choice == 'scissor'):
            user_score = user_score +1
            print("You won.\nYour score is:",user_score,'\ncomputer score:',comp_score)

        elif (user_choice == 'paper' and comp_choice == 'rock'):
            user_score = user_score +1
            print("You won.\nYour score is:",user_score,'\ncomputer score:',comp_score)
        elif (user_choice == 'scissor' and comp_choice == 'paper'):
            user_score = user_score +1
            print("You won.\nYour score is:",user_score,'\ncomputer score:',comp_score)

        elif (user_choice == 'rock' and comp_choice == 'paper'): 
            comp_score = comp_score +1
            print("Computer won.\ncomputer score:",comp_score,'\nYour score is:',user_score)

        elif (user_choice == 'paper' and comp_choice == 'scissor'):
            comp_score = comp_score +1
            print("Computer won.\ncomputer score:",comp_score,'\nYour score is:',user_score)

        elif (user_choice == 'scissor' and comp_choice == 'rock'):
            comp_score = comp_score +1
            print("Computer won.\ncomputer score:",comp_score,'\nYour score is:',user_score)

        elif (user_choice=='exit'):
            print("computer score:",comp_score,'\nYour score is:',user_score)
            if comp_score > user_score:
                print("Computer won the game")
            elif user_score > comp_score:
                print("You won the game")
            else:
                print("The Game is Draw")
            break
        elif user_choice == comp_choice:
            print("It's a Draw")
            print("Computer's total score is:",comp_score,"\nYour total score is:",user_score)
        else:
            print("Invalid input. Please choose rock, paper, or scissor.")

else:
    print("Hope you will play in the future.")

