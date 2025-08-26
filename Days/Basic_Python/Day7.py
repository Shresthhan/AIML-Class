'''
User defined functions
'''

'''
syntax:

def functionName (parameter(S), default parameters can also be defined):
    statements.....
    return variable/value

->Function Call
functionName(value(s) / Variable(S))

'''
'''
# Task 1: To write a program that greets the user using function 
def greet(n):
    print(f"Welcome {n}")
    
name = input("Enter your name: ")
greet(name)

# Default parameter 
def greet(name = "Samriddha"): # n = name
    print(f"Welcome {name}")

def main():
    name = input("Enter your name: ")
    greet()
    greet(name)

main()


# Task 2 : temperature converter celsius to farenheit 
def cel_to_faren(c):
    faren = c * 9 / 5 + 32
    return faren 

celsius = float(input("Enter the temperature in Celsius: "))
farenheit = cel_to_faren(celsius)
print(f"Temperature in farenheit: {farenheit:.2f}")


# Task 3 : Write a program to find the maximum among 3 numbers 

def min_three_no(num1, num2, num3):
    return min(num1, num2, num3)


def main():
    num1, num2, num3 = input("Enter three number: ").split(" ")# -> 1 2 3 -> [1, 2, 3] -> num1 = 1, num2 = 2, num3 = 3
    smallest = min_three_no(int(num1), int(num2), int(num3))
    print(f"The smallest number among {num1}, {num2}, {num3} = {smallest}")
    
main()  

def min_three_no(num1, num2, num3):
    return min(num1, num2, num3)


def main():
    numbers = input("Enter three number: ").split(" ")# -> 1 2 3 -> [1, 2, 3] -> num1 = 1, num2 = 2, num3 = 3
    smallest = min_three_no(int(numbers[0]), int(numbers[1]), int(numbers[2]))
    print(f"The smallest number among {numbers[0]}, {numbers[1]}, {numbers[2]} = {smallest}")
    
main()  
'''

'''
 Task 4: Build a simple calculator that performs addition, substraction, multiplication and 
 devision of 2 numbers according to the user input using  the concept of functional programming.
'''

def addition( num1 , num2 ):
    add = num1 + num2
    return print(f"The addition result is: {add}")

def substraction( num1 , num2):
    if num1 > num2:
        sub = num1 - num2
    else:
        sub = num2 - num1
    return print(f"The substraction result is: {sub}")

def multiplication( num1 , num2):
    mul = num1*num2
    return print(f"The multiplication result is: {mul}")

def division( num1 , num2):
    div = num1/num2
    return print(f"The division result is: {div}")

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    ch = int(input("Choices:  \n 1. for Addition \n 2. for Substraction \n 3. for Multiplication \n 4. for Division \n Enter:"))
    match ch:
        case 1:
            addition(num1, num2)
        case 2:
            substraction(num1 , num2)
        case 3:
            multiplication(num1 , num2)
        case 4:
            division(num1 , num2)
        case _ :
            print("Enter correct choice.")

main()
            
            