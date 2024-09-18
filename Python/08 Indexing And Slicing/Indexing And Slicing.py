# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero)
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
#-------------------------------------------------------

#Indexing (Accessing single item)
 
mystring = "I Love Python"
print (mystring[0]) # Index e => I
print (mystring[9]) # Index 9 => t
print (mystring[-1]) # # Index -1 => First Character From End  
print (mystring[-6]) # Index -6 => 6th Character From End


#Slicing ( Access Multiple Sequence Items)
# [Start: End]
# [Start: End : Steps]

print (mystring[8:11]) #yth
print (mystring[3:5]) #ov
print(mystringl [:10]) # If Start Is Not Here Will start From (I Love Pyt)
print (myString[5:]) # If End Is Not Here Will Go To The End (e Python)
print (myString[:]) # Full string

print (mystring [0: :1]) # Full Data
print (myString[::1]) # Full Data

print (mystring[: :2]) # ILv yhn
print (mystring [ : :3]) # tn