i = 1                        #while loop
while i < 6:             
  print(i)
  i += 1

print('\n')                        #for getting whitespaces in the output

j = 1                         #break statement
while j < 6:
  print(j)
  if (j == 3):
    break
  j += 1

print('\n')

k = 0                          #continue statement
while k < 6:
  k += 1
  if k == 3:
    continue
  print(k)     # Note that number 3 is missing in the result

print('\n')

m = 1                            #else statement
while m < 6:
  print(m)
  m += 1
else:
  print("i is no longer less than 6")