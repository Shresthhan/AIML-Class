'''
split() default ma Space bhako thau ma string lai break garcha 
capitalize() only capitalizes the first letter of first word 
title() capitalizes the first letter of each word in a set of words 
'''

''' 
name = "   ---sujata @@ pathak 1 2 3 __  "
#sujata @@ pathak
new_name = name.strip(" -123_")
print(new_name)

new_name1 = new_name.replace(" @@ ", " ")
print(new_name1)
# sujata pathak = Sujata Pathak
new_name_final = new_name1.title()
print(new_name_final)

# first_name = Sujata and last_name = Pathak

after breaking 
first part -> first name 
last part -> last name

first_name, last_name = new_name_final.split()
print(first_name)
print(last_name)
'''
''' 
name = "ankit shrestha"
print(name.capitalize()

TASK 1
name= " __-- firoj ##&&  karki 123 @@"
first_name = Firoj
last_name = Karki

name= " __-- firoj ##&&  karki 123 @@"
name1 = name.strip(" _-123@").replace(" ##&&  " , " ").title()
first_name , last_name = name1.split()
print(first_name)
print(last_name)
'''
'''
TASK 2
name = "  __--&*) firoj ##&&  karki 123 @@("
first_name = Firoj
last_name = karki

name = "  __--&*) firoj ##&&  karki 123 @@("
name1 = name.strip(" _-&*)@123(").replace(" ##&&  "," ").capitalize()
first ,  last = name1.split()
print(first)
print(last) 
'''

'''
TASK 3 
Text = " $$ Samip ** % (+977)9702187444"
# first_name = Samip
# ph_no = 9702187444
clean_text = Text.strip(" $").replace(" ** % ", " ")
# print(clean_text)
first_name, nonclean_ph = clean_text.split()
ph_no = nonclean_ph.replace("(+977)","")
print(first_name)
print(ph_no)
'''