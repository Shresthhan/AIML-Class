# Looping or Iterative statements

# for Loop 
'''
fruits = ['Apple', 'Banana', 'Kiwi']
for fruit in fruits:
    print(fruit)
'''

# my_list = range(Starting value, ending value , step -> 1)
'''
my_list = list(range(1,11,2))
print(my_list)


# Task 1 : print numbers from 1 to 20
for i in range(1,21):
    print(i , end = " ")  # -> this end = " " prints in same line with single space. It has default value end="\n "
'''

# While Loop
'''
while condition -> True
    runs.......
'''

# break -> when a particular condition occurs, break the loop
'''
for i in range(1,10):
    if i == 6:
        break
    print(i)
'''

# continue -> when a particular condition occurs skip the iteration 
'''
for i in range(1,13):
    if (i == 7) or (i == 9) or (i == 10):
        continue
    print(i , end = " ")
'''
skipped = []
for i in range(1,13):
    if i in [5, 6, 7]:
        skipped.append(i)
        continue
    print(i , end = " ")
print(f"Skipped values = {skipped}")


