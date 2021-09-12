def myfunc():    #variablescope
  x_1 = 300
  print(x_1)
myfunc()            #A variable created inside a function is available inside that function

def myfunc():       #function inside a function
  x_2 = 589
  def myinnerfunc():
    print(x_2)
  myinnerfunc()
myfunc()          #The local variable can be accessed from a function within the function:

x_3 = 500          #global scope
def myfunc():
  print(x_3)
myfunc()
print(x_3)

x_4 = 250           #Naming Variables
def myfunc():       #The function will print the local x_5, and then the code will print the global x_4:
  x_5 = 200
  print(x_5)
myfunc()
print(x_4)

x_7 = "awesome"            #global keyword 
def myfunc():
  x_8 = "fantastic"
myfunc()
print("Python is " + x_7) # if we want to use "x_8" provided inside the function then we use global keyword  

x_9="awesome"
def myfunc():              #global keyword
  global x_10
  x_10 = "fantastic"
myfunc() #aur hamloog nae jaan bhooj kae "myfunc()" phele likha hai taaki phele function call hoo aur function kae jo andar hai wahi sabse phele print hoo
print("Python is " + x_10) 



