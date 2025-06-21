#Q1.Take input from the user and check if the number is even or 
numb=int(input('Enter your number: '))
if (numb%2):
    print('This number is even ')
else:
    print('This number is odd')
#Q2.Take input for age and print
age=int(input('Enter your age: '))
if age<13:
    print('child')
if 13<=age<20:
    print('Teenager')
if age>=20:
    print('Adult')
#Q3.Take three number and print the largest
numb1=int(input("Enter your number 1: "))
numb2=int(input("Enter your number 2: "))
numb3=int(input("Enter your number 3: "))
if numb1>=numb2 and numb1>=numb3:
    print("Large is ",numb1)
elif numb2>=numb3:
    print('Large is ',numb2)
else:
    print('large is ',numb3)
#Q4.check if number positive,negative,zero
number=int(input("Enter a number :"))
if number>0:
    print("your number is positive ")
if number<0:
    print("Your number is negative ")
elif number==0:
    print("your number is ",0)
#Q5.Enter a program that check if  a given charecter is vowel or constant
chr=input('Enter a charecter:')
if chr in "aeiou":
    print("vowl")
else:
   print("constant")
#Q5.check password
password=input('Enter a password:')
if password=='rahul58708':
    print('password is granted')
else:
    print("Acess denied")