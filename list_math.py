
"""Add functions to the module
In the module file, add the following functions. Each function takes a list as input:

count: count the number of elements in the list
sum: calculate the sum of all elements in the list
average: calculate the average of the list elements
max: find and return the value and index of the maximum element of the list as a tuple
min: find and return the value and index of the minimum element of the list as a tuple
"""

#list_math1 = [1,6,4]
#print(list_math)

def _count(list_math):
     return len(list_math)

def _sum(list_math):
    _sum = 0
    for i in list_math:
        _sum = _sum + i
    return _sum

def _average(list_math):
    _sum = 0
    for i in list_math:
        _sum = _sum + i
    average = _sum/len(list_math)
    return average

def _max(list_math):
    maxValue = max(list_math)
    maxIndex = list_math.index(maxValue)
    _max     = (maxValue,maxIndex)
    return _max

def _min(list_math):
    minValue = min(list_math)
    minIndex = list_math.index(minValue)
    _min     = (minValue,minIndex)
    return _min

#def max(list_math):
#     return max(list_math)

#print(count(list_math))
#print(sum(list_math))
#print(average(list_math))
#print(_max(list_math))
#print(_min(list_math))