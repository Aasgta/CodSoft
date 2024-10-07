import random
import string

len =  int(input("Enter the length of the password."))
print('''Enter the level of complexity of password:
      1 for low level
      2 for medium level
      3 for high level
      ''')

level = int(input(""))

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

lst = ""
if level ==1:
    lst += letters
elif level ==2:
    lst += letters
    lst += digits
elif level ==3:
    lst += letters
    lst += digits
    lst += special_chars
else:
    print("Invalid input")    

password = []  

for i in range(len):
    randomchar = (random.choice(lst))
    password.append(randomchar)
  
print("The strong password is "+"".join(password) )
