fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

print('\n')

for x in range(7):   #range function
  print(x)

print('\n')

for y in range(6, 10):    #range function but specific value  at starting
  print(y)    

print('\n')

for i in range(1, 12, 4):   #third parameter 
   print(i)   
for t in range(15, 0, 4):
  print(t)

print('\n')

for x_1 in "banana":    #Looping Through a String
    print(x_1) 

print('\n')

fruits_2 = ["apple", "banana", "cherry"]    #the break statement 
for x_2 in fruits_2:
  print(x_2) 
  if x_2 == "banana":
    break

print('\n')

fruits_1 = ["apple", "banana", "cherry","mango","grapes"]     #the continue statement
for x_3 in fruits_1:
  if x_3 == "banana":
    continue
  print(x_3) 

print('\n')

for x_4 in range(6):                     #the else statement
  print(x_4)
else:
  print("Finally finished!")

print('\n')

for x_5 in range(6):    
  if x_5 == 3: 
    break    #If the loop breaks, the else block is not executed.
  print(x_5)
else:
  print("Finally finished!")

print('\n')

for x_6 in [0, 1, 2]: #having an empty for loop like this, would raise an error without the pass statement
  pass

print('\n')

adj = ["red", "big", "tasty"]                            #the nested loop
fruits = ["apple", "banana", "cherry"]    
for x_7 in adj:
  for y in fruits:
    print(x_7, y)

print('\n')

fruits=["apple", "banana", "cherry"]
adj=["red", "big", "tasty"]
for x_8 in fruits: 
  for y_2 in adj: 
    print(x_8,y_2)