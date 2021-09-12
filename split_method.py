text_1 = 'tu kaise hai aap loog ?'  
#split with whitespace by default
print(text_1.split())

word = 'Welcome, Agent 47'  # Splits at ',' (using symbols)
print(word.split(','))

Inform = 'Mission: successfully: complete: 47' # Splitting at ':'
print(Inform.split(':'))

text_5 ='Hello eve Section eww'  # Splitting using an comman word in whole string
print(text_5.split('e'))

text_2= 'Kill the#Prime#Minister' #Splits at "#" (using symbol)
print(text_2.split('#'))

text_3='I$love$my$India$Jai$Hind$Jai$Bharat' 
print(text_3.split('$',5)) #splits using number(or maxsplit)
