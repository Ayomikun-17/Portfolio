#electricity checker 
name=input("enter your name ")
unit=float(input("enter total units used"))
value=input("enter the type of electricity system,(standard/suite/advanced):")
time=float(input("enter the amounts of time for electricity:(minutes)"))
  

 
#process 
 
if value =="standard":
     electricity_fare="10"
elif value =="suite":
     electricity_fare="20"
elif value =="advanced":
     electricity_fare="30"

if unit == 0 :
   print("invalid response")


#total calculations 
total_units_used=(unit + time)*electricity_fare

#output 
print("--------------")
print("\n display total units used")
print(f"goodmorinig:{name}")
print(f"total amount of  unit:{value}")
print(f"total_units_used:{total_units_used}")


