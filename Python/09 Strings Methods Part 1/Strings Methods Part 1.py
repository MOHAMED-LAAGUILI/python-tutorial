#
# -- Strings Methods --
#
# len()
# strip() rstrip() lstrip()
# title()
# Capitalize()
# zfill()
# upper()
# lower()


# len()

a ="I Love Python"
b ="    I Love Python    "
print(len(a))
print(len(b))


# strip() rstrip() 1strip()

c ="    I Love Python    "
print(c.strip())  # "I Love Python"
print(c.lstrip()) # "I Love Python    "
print(c.rstrip()) # "    I Love Python"

d ="#####I Love Python ####*"
print(d.strip("#"))
print(d.rstrip("#"))
print(d.lstrip ("#"))


# title()
e ="I Love 2d Graphics and 3g Technology and python"
print (e.title())
# I Love 2D Graphics And 3G Technology And Python


# Capitalize ()
f = "I Love 2d Graphics and 3g Technology and python"
print(f.capitalize())
# I love 2d graphics and 3g technology and python


# Zfill

g, h, i, j = "1", "11", "111","1111"
print(g) # 1
print (h) # 11
print (i) # 111
print (j) # 1111

print(g.zfill(3)) # 0001
print(h.zfill(3)) # 0011
print(i.zfill(3)) # 0111
print(j.zfill(3)) # 1111



# upper()
k = "laaguili"
print(k.upper()) # LAAGUILI


# lower()
l = "MOHAMED"
print(l.lower()) # mohamed
