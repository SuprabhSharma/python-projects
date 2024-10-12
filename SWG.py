import random 
options = ["snake","water","gun"]
computer_choice = random.choice(options)
user_choice = input("enter any one of the options:")
if computer_choice==user_choice:
    print("draw")
elif  user_choice == "snake":
    if computer_choice=="water":
        print("computer chose water ,user wins!")
    else :
        print("user chose gun , you loss")
elif user_choice =="water":
    if computer_choice=="gun":
        print("computer chose gun,user wins")
    else :
        print("user chose snake , you loose")
elif user_choice =="gun":
    if computer_choice=="snake":
        print("computer chose snake,user wins!")
    else :
        print("user chose water,you loss")
else:
    print("game ended")
