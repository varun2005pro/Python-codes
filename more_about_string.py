a ="Yeh naya hindustan hai!" #Strings are Arrays   #The first character has the position 0
print(a[4]) 

x="hello, my name is varun" #To check the length of the string 
print(len(x))

test="Jai Hind,Jai Bharat" #to check the word wheather it was present in the string
print("Hind" in test)

test="Jai Hind,Jai Bharat"
if "Hind" in test: #agar hame chachte kee output mai woh hame "True" kae alawa yeh likha tu ham "if" ka use karenge
 print("Yes, hind is present")

test2="hello guys,what is up?" #to check the word wheather it was present in the string or not
print("bye" not in test2)

test_2="hello guys,what is up?" #agar hame chachte kee output mai woh hame "False" kae alawa yeh likha tu ham "if" ka use karenge
if "bye" not in test_2: 
    print("yes,'bye' is not present in test_2")

test_3_a="hello world"  #Mixed Slicing   
#The first character has the position 0   #syntax=(start argument:Stop argument+1) #we can also take negative indexing 
print(test_3_a[-3:9])
test_3_b="hello world" #Slice From the Start
print(test_3_b[:2])
test_3_c="hello world" #Slice To the End
print(test_3_c[5:])  
test_3_D="hello world" #Negative indexing
print(test_3_D[-5:-3]) 

v="ham shaan se jalne nikle hai" #if we want to convert all the characters of the string into UPPER CASE ( or CAPITAL)
print(v.upper()) 
m='Ab hoga Yalgaar' #if we want to convert all the characters of the string into lower case (or small letters)
print(m.lower())
z=" Ham shaan se jalne nikle hai " #to remove the whitespaces which is before and after the actual text.
print(z.strip())
l="Ham shaan se jalne nikle hai" #Replace String 
print(l.replace("Ham shaan se jalne nikle hai","Varun is great"))
p="I love my India"  #Split string                                                      
print(p.split())
p="I love my India"  #Split string                                                      
print(p.split())

n="hello world,"
m="i am varun"
print(n+"we are Indians") #combine both text and a variable 
b=n+m #add a variable to another variable
print(b)
