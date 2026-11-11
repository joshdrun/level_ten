# some variables are mutable, which means they can be changed after creation, maintaining the same identity in memory.
# Examples of mutable types include lists, dictionaries, and sets.
# In contrast, immutable types cannot be changed after creation. Examples of immutable types include integers, floats, strings, and tuples.
# Understanding mutability is important in Python because it affects how variables are passed to functions, how they are modified, and how memory is managed.
# For example, if a list is passed to a function and modified inside the function, the changes will be reflected in the original list. However, if an integer is passed and modified, the original integer remains unchanged.
# This distinction is crucial when working with complex data structures and when managing memory in Python.
# It also helps in understanding why certain operations on mutable objects can have side effects, while operations on immutable objects do not.
# In summary, mutability is a fundamental concept in Python that impacts how data is stored, modified, and shared across the program.
# Example demonstrating mutability:
import pandas as pd


#some_rando_list = []
#some_rando_list.append(1)
#print(some_rando_list)  # Output: [1]

#some_rando_list.extend([2, 3])
#print(some_rando_list)  # Output: [1, 2, 3]
    
#print(some_rando_list[-1])  # Output: 3

#some_rando_list.pop()
#print(some_rando_list)  # Output: [1, 2]

#some_rando_list.append(3)
#print(some_rando_list)  # Output: [1, 2, 3]

#some_rando_list.pop(0)
#print(some_rando_list)  # Output: [2, 3]

#some_rando_list = [1, 2, 3]

#some_rando_list.remove(2)
#print(some_rando_list)  # Output: [3]

#if 2 in some_rando_list:
#                   print("2 is in the list")

#tuples are immutable sequences, meaning they cannot be changed after creation.
#some_rando_tuple = (1, 2, 3)
#print(some_rando_tuple)  # Output: (1, 2, 3)

#Attempting to modify a tuple will raise an error
#some_rando_tuple.append(4)  # This will raise an AttributeError


#sets are unordered collections of unique elements.
#some_rando_set = {1, 2, 3}
#print(some_rando_set)  # Output: {1, 2, 3}

#some_rando_set.add(4)
#print(some_rando_set)  # Output: {1, 2, 3, 4}

#some_rando_set.remove(2)
#print(some_rando_set)  # Output: {1, 3, 4}

#if 3 in some_rando_set:
#    print("3 is in the set")



#dictionary is a collection of key-value pairs.
student_info = {
        "name": "John Doe",
        "age": 20,
        "grade": "A"
}

student_info2 = {
    "name": ["Jane Smith", "LebRon"],
    "gpa": ["3.5", "4.0"]
}

restraunt_info = pd.read_csv("restraunt_info.csv")

restraunt_info.at[0, "Rating"] = 4.5

df = pd.DataFrame([student_info])
df2 = pd.DataFrame([student_info2])
#print(df)
#print(df2)
print(restraunt_info)







#print(student_info)  # Output: {'name': 'John Doe', 'age': 20, 'grade': 'A'}

#student_info["grade"] = "B"
#print(student_info)  # Output: {'name': 'John Doe', 'age': 20, 'grade': 'B'}
