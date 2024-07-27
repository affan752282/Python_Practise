print("2+4")
#output=2+4
print("hello", "Learning python")
#output=hello Learning python
print(10>5)
#output=True
a=10
b=10
print(a,b)
#output=10 10
print(id(a),id(b))
#output=140727728282328 140727728282328

#string concatenation
a="Affan"
b="Ahmad"
print(a+b)
#output=AffanAhmad
print(a+" "+b)
#output=Affan Ahmad
c=10
#print(a+c)    error dega string string ke saath hi concatenate ho sakta hai

#Operators
print(10//3)  #output=3  and  // =  floor division
print(11//3)   #ouput=3

print(5**2) #output=25  and **=power
a=5
a+=5
print(a)   #output=10    a+=5 means a=a+5

#logical operator
a=10
b=20
print(a==b and a<b) #output=false
print(a==b or a<b)  #output=true
print(not a==b)   #output=True

#membership operators -  in and not in
string1="hello"
print("H" in string1)  #output=False because python is case sensitive language
print("h" in string1) #output=True
array=[10,20,30,40]
print(50 not in array) #output=True

#identity operators  -  is and is not
a=10
b=20
print( a is b)   #output=False
print( a is not b) #output=True

#Bitwise operator - and(&), or(|), xor(^)
x=10
y=8
print(bin(x))
print(bin(y))
print(x&y)
print(bin(x&y))


