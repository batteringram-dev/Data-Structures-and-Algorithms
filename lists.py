x = list()
y = ["dog", 3, "Cat", 8.5]
tuple1 = (500, 600)
z = list(tuple1)
print(y)
print(z)

# List Comprehension
a = [m for m in range(8)]
print(a)
b = [i**2 for i in range(10) if i>4]
print(b)

# Inserting a number into a sequence of numbers.
x = [3, 4, 8, 6]
x.insert(1, 7)
print(x)

# You can also add strings into a list of numbers.
y = [3, 4, 8, 6]
y.insert(1, ["a", "m"])
print(y)
