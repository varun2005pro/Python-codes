my_list = []                  # empty list
my_list = [1, 2, 3]           # list of integers
my_list = [1, "Hello", 3.4]   # list with mixed data types  

my_list = ["mouse", [8, 4, 6], ['a']]    # nested list

my_list = ['p', 'r', 'o', 'b', 'e']    # List indexing
print(my_list[0])    # Output: p
print(my_list[2])    # Output: o
print(my_list[4])    # Output: e
n_list = ["Happy", [2, 0, 1, 5]]      # Nested List
# Nested indexing
print(n_list[0][1])
print(n_list[1][3])
# Error! Only integer can be used for indexing
#print(my_list[4.0])

my_list = ['p','r','o','b','e']      # Negative indexing in lists
print(my_list[-1])
print(my_list[-5])

#slicing of a list
my_list_2=['V','A','R','U','N','G','A','U','T','A','M']
print(my_list_2[:5])  #to a pre-defined point using Slice (sliced till 5th element from last)   
print(my_list_2[:-6]) #to a pre-defined point using Slice (sliced till 6th element from last)
print(my_list_2[4:])  #pre-defined point to end    
print(my_list_2[0:4])  #using Slice operation (elements in a range 0-4)
print(my_list_2[:])    #beginning till end
print(my_list_2[::-1])  #List in reverse:

#Add/Change List Elements
my_list_3=['V','U','C','I','F','E','R']  #correcting mistakes in the list 
my_list_3[0]='L'                         #changing the first item of the list
print(my_list_3)
my_list_3[0:7]='D','E','V','I','L'      #change 1st to 7th items of the list
print(my_list_3)

# Appending and Extending lists in Python
my_list_4=['M','R','G','A','U','T','A']
my_list_4.append('M')
print(my_list_4)
my_list_4.extend("you are the creator of earth")
print(my_list_4)

# Concatenating and repeating lists
odd = [1, 3, 5]
print(odd + [9, 7, 5])
print(["re"] * 3)

# Demonstration of list insert () method
odd = [1, 9]
odd.insert(1,3)
print(odd)
odd[2:2] = [5, 7]
print(odd)

# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
# delete one item
del my_list[2]
print(my_list)
# delete multiple items
del my_list[1:5]
print(my_list)
# delete entire list
del my_list
# Error: List not defined
#print(my_list)

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')         # Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)
print(my_list.pop(1))      # Output: 'o' (according to the new list after removing 'p' character)
my_list.clear()            # Output: []
print(my_list)                                 
























