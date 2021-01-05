# Tuples can't be changed but a list inside a tuple can be changed.
x = ([1, 2], 3)
del(x[0][1])
print(x)

# Adding an additional tuple.
x += (4,)
print(x)
