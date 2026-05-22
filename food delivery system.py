#food delivery system 
name=input("enter your name :")
amount=float(input("what is the amount for the food :"))
distance=float((input("enter the total distance,(km)")))
delivery_type=input("what delivery type,(norml/express/priority) :")
time=input("what time is it (peak/off-peak)")

if  delivery_type=="normal" :
      delivery_fee="10"
else:delivery_type=="express" :
      delivery_fee="20" 
else delivery_type=="priority":
    delivery_fee="35"

if time ="peak" :
    delivery_fee*0.15
else amount >="200"
     delivery_fee/0.10
else distance >= 15
     delivery_fee+20


#calculations
total_cost=(distance+amount)*delivery_fee


if distance==0
  print("invalid input")
elif >=0
     print("invalid input")

print("----------------------")
print("\n\n display of the total results of the delivery of Food")
print("customer name:{name}")   
print("the delivery type:{delivery_type}")
print("total before changes")
print("total cost of the delivery:{total_cost}")
    
    


