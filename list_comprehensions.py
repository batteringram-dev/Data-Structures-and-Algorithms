# List Comprehensions

under_10 = [x for x in range(10)]
print("Under 10: " + str(under_10))

# List Comprehension 2

squares = [x**2 for x in range(10)]
print("Squares: " + str(squares))

# List Comprehension 3

s = " I love 2 go 2 the gym "
nums = [x for x in s if x.isnumeric()]
print("Nums: " + "".join(nums))
