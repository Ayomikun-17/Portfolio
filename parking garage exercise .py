while True :
    #input 
    name=input("goodday pls enter your name :")
    number_of_hours=float(input("pls enter the total number of hours uu spent :"))
    
    #validation 
    if number_of_hours <=0:
        print("invalid statement pls enter the correct input")
        
    #process
    if number_of_hours >=2:
        fine=10
    elif number_of_hours <=2:
        fine=15
    elif  number_of_hours >=5:
        print("fine was given")
        fine=20
    elif  number_of_hours<=1:
        print("freee parking")
        
    #process
    total_calculations=( fine*number_of_hours)
    
    
    #output
    print("---------------")
    print("\n DISPLAY OF RESULTS")
    print(f"goodday:{name}")
    print(f"the total number of hours spent:{number_of_hours}")
    print(f"this is your total fee:R{total_calculations}")
    
    repeat=input("would like to return to the main menu :")
    
    if repeat !="yes" :
        print("the program has ended")
        break

