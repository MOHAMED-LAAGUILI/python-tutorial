# Escape Sequences Characters
# \b => Back Space
# \newline => Escape New Line + \
# \ => Escape back slash
# \' Escape Single Quote
# \" Escape Double Quote
# \n => line feed
# \r => carriage Return
# \t => Horizontal Tab
# \xhh => character hex value


# Back Space
print("Hello \bWorld") # Will Remove previous caracter

# Escape New Line + \
print("Hello \
    ilove \
    python")

# Escape back slash
print("Hello World \\") 

# Escape Single Quote
print('Ilove Single Quote \'test\'')

# Escape Double Quote
print('Ilove Single Quote \'test\'')

# Escape back slash
print("line1 \n line2") 

# carriage return
print("123456\rabcde") # => abcde6

# horizontal tab
print("line1\tline2") 

# horizontal tab
print("\x4D\x4F\x48\x41") 