#-- Strings Methods --
#------

# split()
# rsplit()
# center()
# count() [Case sensitive]
# swapcase()
# startswith() [Case sensitive]
# endswith() [Case sensitive]


# split()

a = "I Love Python and PHP"
print(a.split())
# ['I', 'Love', 'Python', 'and', 'PHP']

b ="I-Love-Python-and-PHP"
print (b.split ("-"))
# ['I', 'Love', 'Python', 'and', 'PHP'] 

c ="I-Love-Python-and-PHP-and-MySQL"
print (c.split ("-",2))
# ['I', 'Love', 'Python-and-PHP-and-MySQL']


# rsplit()

d ="I-Love-Python-and-PHP-and-MySQL"
print (d.rsplit ("-",2))
# ['I-Love-Python-and-PHP', 'and', 'MySQL']


# center()

e ="Osama"
print(e. center(9)) # spaces => "  Osama  "
print(e.center (9, "#")) # Hashes => ##Osama##
print(e.center (15, "@")) # @ => @@@@@Osama@@@@@


# count()

f = "I Love Python and PHP because PHP is easy"
print(f.count ("PHP")) # Only 2 PHP
print (f.count ("PHP",0,25)) # only 1 PHP


# Swapcase()

g = "I Love Python and PHP"
print(g.swapcase()) # i lOVE pYTHON AND php


# startswith()

h = "I love Python"
print(h.startswith("I")) # true
print(h.startswith("S")) # false
print(h.startswith("P", 7, 12)) # true


# endswith()

i = "I love Python"
print(i.endswith("n")) # true
print(i.endswith("S")) # false
print(i.endswith("e", 2, 6)) # true

