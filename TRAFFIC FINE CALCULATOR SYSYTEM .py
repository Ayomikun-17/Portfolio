#tarffic calculator 
driver_name=input("enter your name :")
speed_limit=int(input("enter the speed limit:"))
actual_speed=int(input("enter the actual speed limit :"))

#process
if speed_limit <=0:
    print("invalid response buddy")
elif actual_speed <=0:
    print("invalid response buddy")
    
#calculations
total_over_speed=(actual_speed-speed_limit)

#fine rules 
fine=0
status=""

if total_over_speed <=0:
    price_fine=0
    print("no fine")
elif 1<= total_over_speed <=20 :
    price_fine=200
    print("minor speeding limit")
elif 21<= total_over_speed <=40 :
    price_fine=500
    print("serious speeding limit")
else: #40+
    price_fine=1000
    print("serious speeding limit")

#output process 
print("\n\n display results")
print(f"good day:{driver_name}")
print(f" the speed limit:{speed_limit}")
print(f"actual speed:{actual_speed}")
print(f"the over speed:{total_over_speed} ")
print(f"your fine:R{price_fine}")

# optinal challenge 
if price_fine > 500 :
    print("court appreance need my nigga")
    
#part 6 
while True:
    repeat = input("\n do you want to enter another ?")
     
    if repeat != "yes":
        print("program has ended buddy")
        break
  
     







