#!/usr/bin/env python

# 1. create a list (list_a) with numbers from 1 to 10
#list_a = [1,2,3,4,5,6,7,8,9,10]
list_a = list(range(1,11))
print('This is list_a: ' + str(list_a))

#2. import the numpy library and calculate the mean of the first 5 items from the list_a
import numpy as np
print('The mean for the 1st 5 entries is: ' + str(np.mean(list_a[0:5])))

#3. create a list (list_b) with 10 random number in a range from 1 to 10
import random
list_b = []
for i in range(10):
    list_b.append(random.randint(1, 10))
print('This is list_b: ' + str(list_b))

#3.1 generate a certain amount of numbers
for i in range(12):
    print(i)

#4. identify how many elements are in the intersection between list_a and list_b
print('Intersection: ' + str(len(set(list_a)&set(list_b))))

#5. create a function that defines if a number is 'even' or 'odd'
def even_odd(n):
    if n%2 == 0:
        return 'even'
    else:
        return 'odd'

print(even_odd(1))
print(even_odd(2))
print(even_odd(4))

#6. create a list (list_c) that merges list_a and list_b
list_c = list_a + list_b
print('list_a : ' + str(list_a))
print('list_b : ' + str(list_b))
print('Merged list_c: ' + str(list_c))

#7. organize the list_c into a dictionary according to whether the number is 'even' or 'odd'
dict_number = {}
dict_number['even'] = []
dict_number['odd'] = []
for v in list_c:
    number_type = even_odd(v)
    dict_number[number_type].append(v)

print(dict_number)

#8. how many numbers are even and how many are odd
print('#odds', len(dict_number['odd']))
print('#evens', len(dict_number['even']))
