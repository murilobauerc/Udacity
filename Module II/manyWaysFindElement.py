# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(list, value):
    i = 0
    while i < len(list):
        if list[i] == value:
            return i
        i += 1
    return -1

#solution using index
def find_element_ternary(list,value):
    return list.index(value) if value in list else -1


print (find_element([1,2,3],3))
print (find_element_ternary([1,2,3],3))
#>>> 2

print (find_element(['alpha','beta'],'gamma'))
print (find_element_ternary(['alpha','beta'],'gamma'))
#>>> -1
