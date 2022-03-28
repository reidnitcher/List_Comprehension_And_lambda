''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
from turtle import color
from numpy import sort
from pyparsing import col
import os
clear = lambda: os.system("cls")
clear()

original_numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda num: num % 2 == 0, original_numbers_list))
print(even_list)

odd_list = list(filter(lambda num: num % 2 > 0, original_numbers_list))
print(odd_list)
''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

six_list = list(filter(lambda n: len(n) == 6, weekdays))

print(six_list)

''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
new_list = list(filter(lambda n: n != 'orange' and n != 'black', colors))
print(new_list)



''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

new_list = list(filter(lambda n: n not in list2, list1))
print(new_list)

''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
Original_list =['red', 'black', 'white', 'green', 'orange']

new_list = list(filter(lambda n: 'ack' in n, Original_list))
print(new_list)

new_list1 = list(filter(lambda n: 'abc' in n, Original_list))
print(new_list1)

''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''
password = input("Enter a password: ")
verified_password = lambda s: (any(x.isupper() for x in s)
and any(x.islower() for x in s) 
and any(x.isdigit() for x in s) and  
len(s) >= 8, password)
print(verified_password)     
    



''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted = sorted(original_scores, key=lambda x: x[1])
print(sorted)
