price = 49
txt_1= "The price is {} dollars"
print(txt_1.format(price))

price_2 = 9000                        #We can add parameters inside the curly brackets to specify how to convert the value:
txt_2 = "The price is {:.6f} rupees"
print(txt_2.format(price_2))

quantity_1 = 50
itemno_1 = 20
price_3 = 11
myorder_1 = "I want {} pieces of item number {} for {:.2f} dollars."  #multiple values
print(myorder_1.format(quantity_1, itemno_1, price_3))

quantity_2 = 3                                                         
itemno_2 = 567
price_4 = 49
myorder_2 = "I want {0} pieces of item number {1} for {2:.2f} dollars." #we can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
print(myorder_2.format(quantity_2, itemno_2, price_4)) 

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."    
print(txt.format(age, name)) #Also, if we want to refer to the same value more than once, use the index number

myorder_3 = "I have a {carname}, it is a {model}." #-Named Indexes
print(myorder_3.format(carname = "Ford", model = "Mustang")) #You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

txt_4 = "You scored {:%}" #Use "%" to convert the number into a percentage format:
print(txt_4.format(0.25))
txt_5= "You scored {:.0%}" #Or, without any decimals:
print(txt_5.format(0.46))

txt_6 = "We have {:^10} chicken"#To demonstrate, we insert the number 49 to set the available space for the value to 10 characters.
print(txt_6.format(49)) #Use "^" to center-align the value

txt_7= "We have {:>15} laptops." #To demonstrate, we insert the number 49 to set the available space for the value to 15 characters.
print(txt_7.format(49))          #Use ">" to right-align the value:

txt_8 = "We have {:<20} fruits." #To demonstrate, we insert the number 49 to set the available space for the value to 20 characters.
print(txt_8.format(49)) #Use "<" to left-align the value:












