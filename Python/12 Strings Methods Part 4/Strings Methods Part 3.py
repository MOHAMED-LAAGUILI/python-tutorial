#-- Strings Methods
#

# index(Substring, Start, End)
# find(Substring, Start, End)
# rjust()
# ljust()
# splitlines()


# index()
a = "I Love Python"
print(a.index("P")) # Index Number 7
print(a.index("P", 0, 10)) # Index Number 7
# print(a.index("P", 0, 5)) # if not found Through Error & stop execute


# find()
b  = "I love Python"
print(b.index("P")) # Index Number 7
print(b.index("P", 0, 10)) # Index Number 7
# print(b.index("P", 0, 5)) # -1 if not found Through Error & stop execute


# rjust()
c = "Mohamed"
print(c.rjust(10)) # "   Mohamed"     10 = 3(   ) + 7(Mohamed)
print(c.rjust(10, "#")) # "###Mohamed"     10 =  3(###) + 7(Mohamed)

# ljust()
d = "Mohamed"
print (d.ljust(10)) # "Mohamed   "     10 = 7(Mohamed) + 3(   )
print(d.ljust(10,"#")) # "Mohamed###"     10 = 7(Mohamed) + 3(###)


# splitlines()
e = """First Line
Second Line
Third Line"""
print (e.splitlines()) # ['First Line', 'Second Line', 'Third Line']

f = "First Line\nSecond Line\nThird Line"
print (f.splitlines ()) # ['First Line', 'Second Line', 'Third Line']


# expandtabs()
g = "Hello\tWorld\tI\tLove\tPython" 
print (g.expandtabs(5)) # Hello     World     I    Love Python


one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle()) # true
print (two.istitle()) # false => must be each letter from sart string must be uppercase

three = " "
four = ""
print (three.isspace()) # true
print(four.isspace()) # false

five ="i love python"
six = "I Love Python"
print (five.islower ()) # true
print(six.islower()) # false

seven= "osama_elzero"
eight = "OsamaElzero100"
nine ="Osama--Elzero100"
print(seven.isidentifier()) # true
print(eight.isidentifier()) # true
print(nine.isidentifier()) # false

x = "AaaaaBbbbbb"
y= "Aaaaa Bbbbbb111"
print(x.isalpha()) # true case it from A tp Z
print(y.isalpha()) # false

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print (u.isalnum()) # true 
print(z.isalnum()) # true cause it from A tp Z and from 1 to +9999999