# Sets have really fast access compared to lists.
# Sets doesn't print duplicate items.

x = {3, 5, 3, 5}
print(x)

y = set()
print(y)

list1 = [3, 4, 5]
z = set(list1)
print(z)

# Mathematical Set operations.

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
print(s1 - s2)
print(s1 <= s2)
print(s1 >= s2)
