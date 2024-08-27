a = 32
print(a)

b = 42.23
print(b)

c = True

d = 'This is a string'
e = "This is also a string"
f = """
This is a multi line string
"""
d = 'Today\'s weather is nice'
print(d)


d = "Today's weather is nice"
print(d)

# This is a list
test_list = ["hello", "world", "python"]
print(test_list)

# Tuple
test_tuple = ("hello", "world", "python")
print(test_tuple)

# Dict
test_dict = {'a': 1, 'b': 2}
print(test_dict)

# Set
# consider the values in an arbitrary way
test_set = {'a', 'b', "abc"}
print(test_set)

# type() function -> prints the datatype of the variable
print(type(test_dict))
print(type(print))
print(type(test_tuple))

# Add
a = 42
b = 45.32
c = a + b
print(c)

d = a - b
print(d)

e = a * b
print(e)

f = 12
g = 3
h = f / g
print(h, type(h))

# Integer division
h = f // g
print(h)

# Modulo division(remainder)
i = f % g
print(i)

# Addition
a = "42"
b = "43"
print(a + b) # Concatenation

# Power
a = 10
print(a**2) # a²

# Comparison operators
a = 10
b = 20
res = a > b
res_1 = a < b
res_2 = a != b
res_3 = a == b
print(res, res_1, res_2, res_3)

# Logical operators
# AND, NOT, OR
a = True
b = False

res = a and b
res_1 = a or b
res_2 = not a
res_3 = not b
print(res, res_1, res_2, res_3)
