'''
list -> mutable(Bicha bicha ko value harulai access garera change garna sakchau) data structure 
tuples -> immutable (value access garna milcha tara change garna mildeina)
sets -> stores unique values , unordered (particular data access garna sakideina)
dictionaries -> key values pairs
'''

'''
NOTE: list as a values use garna sakincha ra tuples lai as a keys use garna sakincha cuz keys can't be changed
'''

# LIST 
'''
list = [1,2,4,"samriddha",True,9.1] list ma jun type ko value ni rakhna milcha 
empty_list = []

#Indexing

l2 = [1,True, "Ankit", "Amit", 32]
print(l2[3])
print(type(l2[3]))

print(l2[-1]) #-1 index gives the last element

l3 = [1,True, "Ankit", "Amit", 32, "Ram", "Shyam", False, "Red Bull", 3.25, "Gita", "Tensorflow", "Pytorch", "Numpy"]
# The last element
print(l3[-1])
# The second last element
print(l3[-2])
# The fifth element 
print(l3[4])

# Slicing -> list[starting_index : ending_index(not inclusive)]
l3 = [1,True, "Ankit", "Amit", 32, "Ram", "Shyam", False, "Red Bull", 3.25, "Gita", "Tensorflow", "Pytorch", "Numpy"]
print(l3[2:7])
print(l3[2:])
print(l3[-3:]) #last ko 3 ta 
print(l3[-4:-2])
print(l3[-14:-3])

# Append
l3 = [1,True, "Ankit", "Amit", 32, "Ram", "Shyam", False, "Red Bull", 3.25, "Gita", "Tensorflow", "Pytorch", "Numpy"]
l3.append("Apple")
l3.append("Kiwi")
print(l3)

# Insert -> insert(index, value) -> add garcha index position ma ra tya bhako element shift garcha 
l3.insert(1, "Alisha")
print(l3)

# Sort
my_list = [33,45,67,3,2,35,56,356,776,455,65,2,4,56,66]
print(my_list)
my_list.sort() # sort() changes original list in ascending order 
print(my_list)
my_list.sort(reverse=True) # sort(reverse = True) gives descending
print(my_list)


# Pop
l3 = [1, 'Alisha', True, 'Ankit', 'Amit', 32, 'Ram', 'Shyam', False, 'Red Bull', 3.25, 'Gita', 'Tensorflow', 'Pytorch', 'Numpy', 'Apple', 'Kiwi']
print(l3.pop())
print(l3)

# Remove
l3 = [1, 'Alisha', True, 'Ankit', 'Amit', 32, 'Ram', 'Shyam', False, 'Red Bull', 3.25, 'Gita', 'Tensorflow', 'Pytorch', 'Numpy', 'Apple', 'Kiwi']
l3.insert(9, "Ankit")
print(l3)
l3.remove("Ankit") # Remove() le jun element pass gareko cha tyo hataucha plus 2 ta cha vane suru ma jun cha tyo hatcha
print(l3)


# Clear() -> List ko sabai udaucha values thus empty list 
'''

# TUPLE -> immutable, indexing and slicing same as list 
'''
my_tuple = (3,4,5,6,"Ram", True,3,3,3,3)
print(my_tuple)
print(type(my_tuple))

number = my_tuple.count(3) # count(__) -> counts the number of elements in tuple  
NOTE: Count() ma True -> 1 ra False -> 0 count garcha 
print(number)


my_tuple = (1, 2, 4, 6, 9, 0, 9)
indx9 = my_tuple.index(9) # -> suru ma jun aaucha tesko index return garcha 
print(indx9)

my_tuple= (1) # NOTE: Single value dida tyo tuple haina int vanera aaucha so for tuple, bracket bhitra "," dina jaruri cha 
                my_tuple = (1,)
print(my_tuple)
print(type(my_tuple))
'''

# SETS
'''
NOTE: Stores unique value and is unordered 

my_set = {1, 2, 3, 4, 3, 5, 4} # NOTE: Set le dublicate value store gardeina 
print(my_set)
print(type(my_set))

my_set.add(6)
print(my_set)

my_set.add(1) # NOTE: changes aaudeina 
print(my_set)

my_set.remove(2)
print(my_set)

my_set = {1,3,2,5,4} NOTE: Positive number ascending ma sort gariracha 
print(my_set)

my_set = set() NOTE: for defining empty set 
print(my_set)
'''

# DICTIONARY 
'''
my_dict = {
    "key" : "value
    ..............
    NOTE : the key must be unique and immutable 
    }
'''

my_dict = {
     "Name" : "Amit",
     "Age" : 22,
     "ph_no" : 9999999999
}
print(my_dict)
print(type(my_dict))

print(my_dict.keys())
print(my_dict.values())

del my_dict["Age"] # NOTE: to delete the key value pair inside a dictionary
print(my_dict)