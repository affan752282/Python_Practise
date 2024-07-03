age=int(input("Enter your age - "))
day=str(input("Enter the day - "))
price=12 if age>=18 else 8
if(day=="wednesday"):
   price=price-2
print(price)
