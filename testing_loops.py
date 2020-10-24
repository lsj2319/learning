#testing_loops.py

"""n = 1
# while the value of n is less than 5, print n. add 1 to n each time
# use while loops for infinate loops or for a set number of executions/loops
while n<5:
    print(n)
    n = n + 1"""
"""
num = float(input("Enter a postive number:"))

while num <= 0:
    print("That's not a positive number!")

    num = float(input("Enter a positive number:"))
"""

"""# use for loops to loop over a collection of items
for letter in "Python":
    print(letter)"""

# loop over a range of numbers with range / any positive #, n times
# range(5) returns range of integers starting with 0 and up to, not including, 5.  (0,1,2,3,4)
"""for n in range(5):
    print("Python is awesome")"""

# you can give range a starting point (great for dice rolls)
"""for n in range(10,20):
    print(n * n)"""
# you can use it to calculate a split check:
amount = float(input("Enter an amount:"))

for num_people in range(2,6):
    print(f"{num_people} people: ${amount / num_people:,.2f} each")

