Txt_1="World War 1."   #length 
print(len(Txt_1))      #all aditional sign is also count in it just like- full stop(.)

Txt_2="VARUN GAUTAM"    #lower case
print(Txt_2.lower())

Txt_3="varun gautam"   #upper case
print(Txt_3.upper())

Txt_4="            John wick          "     #remove whitespaces
print(Txt_4.rstrip())                       #removes right side whitespaces
print(Txt_4.lstrip())                       #removes left side whitespaces
print(Txt_4.strip())                        #removes whitespaces from both side

Txt_5="Apex lgeends"   #replace string 
print(Txt_5.replace("lgee","lege"))

Txt_6="Assassin's,Creed Valhalla"  #split string 
print(Txt_6.split(", "))
Txt_7="Call#of#duty#warzone"       #using separator
print(Txt_7.split("#"))
Txt_8="Battle:royal:or:gulag"      #using maxsplit 
print(Txt_8.split(":",2))

Txt_9="Modern warfare,Warzone,Battle royale"   #count
print(Txt_9.count("a"))           #using value 
print(Txt_9.count("a",0,20))      #using start and end parameters

Txt_10="cold war in call of duty" #title tag
print(Txt_10.title())   

Txt_11="Munna bhaiya"        #center tag
print(Txt_11.center(30))
