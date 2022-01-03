#rps
import random
def rps():
    print("Welcome to rock paper scissors game")
    user= str(input("Enter your name : "))
    list=["rock", "paper", "scissors"]
    player_points= 0
    cpu_points=0
    print("three points to win the game")
    while player_points<3 and cpu_points<3:
        cpu_choice=random.choice(list)
        player_choice=input("Rock, Paper or scissors?")
        player_choice=player_choice.lower()
        print(f"Cpu: {cpu_choice} vs {user}: {player_choice}")
        if player_choice==cpu_choice:
            print("Its a tie. No points!")
        elif player_choice=="rock":
            if cpu_choice=="scissors":
                print(f"{user} wins! 1 point.")
                player_points+=1
            elif cpu_choice=="paper":
                print(f"Cpu wins! 1 point.")
                cpu_points+=1
        elif player_choice=="paper":
            if cpu_choice=="rock":
                print(f"{user} wins! 1 point.")
                player_points+=1
            elif cpu_choice=="scissors":
                print(f"Cpu wins! 1 point.")
                cpu_points+=1
        elif player_choice=="scissors":
            if cpu_choice=="paper":
                print(f"{user} wins! 1 point.")
                player_points+=1
            elif cpu_choice=="rock":
                print(f"Cpu wins! 1 point.")
                cpu_points+=1
        else:
            print("Invalid statement. Try again")
    if player_points==3:
        print(f"{user} wins the game!")
    else:
        print("Game over! Cpu Wins!")
    print("Exited rock paper scissors game")
if __name__=="__main__":
    rps()