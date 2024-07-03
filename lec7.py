distance=int(input("Enter the distance - "))
if(distance<3):
    print('walk')
elif(distance<15):
    print("use bike")
else:
    print("use car")