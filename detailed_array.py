# Array Data Structure Exercise

'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

expenses = [2200,2350,2600,2130,2190]

print("1) In Feb this much dollars was spent compared to Jan: ")
print(expenses[1] - expenses[0])

print("2) The total expenses for first 3 months was: ")
print(expenses[0] + expenses[1] + expenses[2])

if expenses == 2000:
    print("3) True")
else:
    print("3) False")
    
expenses.insert(5, 1980)
print("4) The expenses for June month was " + str(expenses[5]) + " dollars.")

print("5) The refund for the month of April was 200 dollars. Correction for April month's expenses was: ")
print(expenses[3] + 200)
