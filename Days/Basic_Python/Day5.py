'''
if 
if else 
if elif.......... else 
nested
match case statement 
'''

'''
if condition:
    statement(s)


num = int(input("Enter the number:"))
if num > 0:
    print("The number is positive")
else:
    print("THe number is negative")  
    '''
    
'''
num = int(input("Enter the number:"))
if num == 0:
    print("The number is zero")
elif num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd") 
'''

'''   
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

# if num1 > num2:
#     if num1 > num3:
#         print(f"num1 {num1} is greatest")
#     else:
#         print(f"num3 {num3} is greatest")
# else:
#     if num2 > num3:
#         print(f"num2 {num2} is greatest")
#     else:
#         print(f"num3 {num3} is greatest")
   
# //////
     
if (num1 >= num2) and (num1 >= num3):
    print(f"{num1} is greatest")
elif (num2 >= num1) and (num2 >= num3):
    print(f"{num2} is greatest")
else:
    print(f"{num3} is greatest")
'''

 # add, sub, pro
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

ch = int(input("Choices:  \n 1. for Addition \n 2. for Substraction \n 3. for Product \n Enter:"))
match ch:
    case 1:
        add = num1 + num2
        print(f"{num1} + {num2} = {add}")
    case 2:
        if num1 > num2:
            sub = num1 - num2
            print(f"{num1} - {num2} = {sub}")
        else: 
            sub = num2 - num1
            print(f"{num2} - {num1} = {sub}")
    case 3: 
        pro = num1 * num2
        print(f"{num1}  {num2} = {pro}")
    case _ :
        print("Enter correct choice")