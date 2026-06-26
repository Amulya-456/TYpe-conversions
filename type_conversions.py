# int -----> float
x=10
print(float(x))
# int -----> str
x=10
print(str(x))
# int -----> complex
x=10
print(complex(x))

# float
# float -----> int
y=10.5
print(int(y))
# float -----> str
y=10.5
print(str(y))
# float -----> complex
y=10.5
print(complex(y))

# str
# str -----> int
z="10"
print(int(z))
# str -----> float
z="10.5"
print(float(z))
# str -----> complex
z="10"
print(complex(z))

# complex
# complex -----> int
w=10+5j
# print(int(w))
# complex -----> float
w=10+5j
# print(float(w))
# complex -----> str
w=10+5j
print(str(w))

#  bool
print(bool(10))
print(bool(0))
print(bool("hello"))
print(bool(""))

# list
# list -----> tuple
my_list = [1, 2, 3]
print(tuple(my_list))
# list -----> set
my_list = [1, 2, 3]
print(set(my_list))
