#data types
#(1) Numeric- Integers , Floats , Complex Numbers
#(2) Sequence Type- String , List , Tuple
#(3) Dictionary
#(4) Set
 
#Mutable Data Types - List , Dictionary, Byte Araay
# Mutable data types are those whose contents cam be changed
#Immutable Data Types - Int , Float , Complex, String , Tuple, Set

#Find the data type of given data
a=8
print(type(a)) #output=<class 'int'>
b=4+8
print(type(b)) #output=<class 'int'>
s=''' 
    Run          #triple quotation is used for multiline string
    for unity
'''
print(s)  #output-  Run
#                   for unity
 
# LIST 
#List is an ordered sequence of items 
# [ ]  -  denotion of list

a=[10,4,25,20,15]
print(a)   #output = [10, 4, 25, 20, 15]
a[2]=30
print(a) #output = [10, 4, 30, 20, 15]

# TUPLE
#Tuple is an ordered sequence of items 
# ( )  ->  denotion of tuples and items of tuple separated by commas
# Tuples can be access faster than list

b=(10)
print(type(b))  #output=  <class 'int'>   
# tuple me ek se jyada items hone chahiye tabhi tuple hota hai

b=(10,15,20)
print(b, type(b)) #output = (10, 15, 20) <class 'tuple'>
#b[2]=25
#print(b) #error dega kuonki tuple object does not support item assignment

# DICTIONARY
# dictionary is an unordered collection of key-value pairs
# defined by curly braces { }
# Each item in form of key:value and separated by comma
d={1:5,2:10}
print(d) #output = {1: 5, 2: 10}
# database se jo data aata hai wo dictionary ke form mein hi aata hai
# key of the dictionary sgould be unique
print(d[1]) # output=5

# SET
# Set is an unordered collection of items . Every item should be unique
# Set is defined by { }
s= {1,2,3}
print (s) # output = {1, 2, 3}
#s[1]=5
#print(s)  #error dega set does not support item assignment

s={4,5,10,4,5,4,20}
print(s) #output = {10, 5, 20, 4}  Remove duplicate elements

s={4,5,10,5,4,20,10,6}
print(s) # output = {4, 5, 6, 20, 10}

# input( ),  int( ), float( ),  eval( )

a= input("Enter the number - ")
print(a) # ouput = Enter the number -  

a= input("Enter the num1 - ")
b= input("Enter the num2 - ")
print(a+b)
# output=  Enter the num1 - 10
#          Enter the num2 - 20
#          1020
# Abhi a and b string mein hai

# int() FUNCTION
c=int(a)    #Typecasting
d=int(b)    #Typecasting
# Ab a and b int me change ho gaya Typecasting karke
print(c+d) #output=30

# float() FUNCTION
a=float(input("Enter the value1 - "))
b=float(input("Enter the value2 - "))
print(a+b)
#output=  Enter the value1 - 4.8
#         Enter the value2 - 5.4
#         10.2

#eval() FUNCTION
a=eval(input("Enter the value1 - "))
b=eval(input("Enter the value2 - "))
print(a+b)
#output=  Enter the value1 - 5
#         Enter the value2 - 4.5
#         9.5

#output=Enter the value1 - 4
#       Enter the value2 - 0b1010    # 0b1010 is binary of 10 so eval() converts it to 10
#       14