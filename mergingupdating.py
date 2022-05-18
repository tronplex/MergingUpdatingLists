list01 = [1,2,3,4,5]
list02 = [6,7,8,9,10]
print(list01)
print(list02)

merged = list01 + list02
print(merged)

# APPEND A NEW LIST AS AN ARGUMENT
merged.extend(['a','b','c','d','e'])
print(merged)

# UPDATE LIST ELEMENTS
merged[0] = "hello"
print(merged)

# COPY A LIST
list03 = list02
print(list03)
print(list02)

# REMOVE AN ELEMENT FROM A LIST
list01.pop(0)
print(list01)

del list01[0]
print(list01)

# IDENTIFY THE EXISTENCE OF AN ELEMENT IN A LIST
confirm01 = 3 in list01
print(confirm01)
confirm02 = 7 not in list01
print(confirm02)
