# EXCEPTION HANDLING 

'''
------ERROR-------
print("Hello World ) -> Syntax error  

sum = num1 - num2 -> This represents Logical Error (Finding logical error is tedious)
'''

#Exception
'''
x = int(input("Enter a number: "))
print(x)  #-> If we enter string here, it is exception 
'''
# To catch exception i.e exception handling
# Syntax
'''
try:  -> Risky codes ya lekhchau

except:
.....
.....
else:

finally:

'''
# ValueError
'''
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Please enter an integer!!")
else:
    print(f"number = {x}")   
'''
'''
while True:
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("Please enter an integer!!")   # error aayo warning dina man chaina vane "Pass" lekhe huncha
    else: 
        break
print(f"The entered number is: {x}")
'''

# Division by Zero error
'''
while True:
    try:
        x = int(input("Enter a number: "))
        result = 10/x
    except ValueError:
        print("Please enter an integer!!")
    except ZeroDivisionError:
        print("Cannot be divided by 0!!")
    else:
        break
print(f"The result is: {result}")
'''

def main(num1,num2,num3):
    print(f"The sum is: {num1 + num2 + num3}")
    print(f"The product is: {num1 * num2 * num3}")
    try:
        print(f"The operation (num1 + num2)/num3 is {(num1 + num2)/num3}")
    except ZeroDivisionError:
        print(f"num3 = {num3} thus Division Invalid!!")
    
def cal():
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            num3 = int(input("Enter third number: "))
        except ValueError:
            print("Please enter an integer!!")
        else:
            return main(num1,num2,num3)
cal()   

    
    











