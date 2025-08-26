'''
Data CLeaning 
lstrip() to remove unwanted part form left 
rstrip() to remove unwanted part from right 
strip() powerful tool to remove the unwanted part as a whole
replace()
'''

name1 = '--- My name ___ is Ram 123 Karki --'
name2 = name1.strip("- ").replace(" ___ ", " ").replace(" 123 ", " ")
print(name2)