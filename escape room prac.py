#escape room prac 
name=input("enter your name :")
score=0
lives=3
round_number=1
game_running =True
choice=int(input("chose an option (1. solve door challenges/2. view score and lives/3. Quite Game):"))
#processs of the game 

number=0

#user option
if choice =="1. solve door challenges.":
    print("enter a number")
    number=float(input("enter number 1-10"))
   
elif number > 1 or number <10:
    print("invalid input buddy")
    
else:
    if number % 2==0:
        score+=10
        print("the door is unlocked")
    else:
        lives -=1
        print("wrong input buddy ")
        
    #bonu combonation
    if number ==8:
        print("bonus door found!!!!")
        score+= 20
        
#increase rounf number 
round_number += 1

#option 2
if choice =="2. view score and lives":
        print(f"\PLAYER:{name}")
        print("final score:{score}")
       
        
elif choice =="3. Quite Game":
     print("\n game over")
     print("final score:{score}")
     game_running=False

else:
    print("invalid option try again")

#if lives reach 0
while True:
    repeat=input("\n do you want to restart the game :")
    if repeat != "yes":
        print("the game has ended")
        break
    while lives >0 and game_running:
        
        print("\n ESCAPE ROOM MENU")
        print("1. solve door challenges")
        print("2. view score and lives")
        print("3. Quite Game")
        


                
            
                



