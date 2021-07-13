#Author - Sean Donohue - Last Mile
#https://www.youtube.com/watch?v=cJ21moQpofY for explanation of dynamic programming for 0/1 knapsack
#note that this is tabulated dynamic programming. could also do it recursively with or without memoization

'''
This program says hey, I'm a software engineer. While I dont want to mess with no linear programming, Im definitely not
going to keep duplicating calculations.  I'll use a classic CS algo to reduce the order of complexity
'''
import numpy as np
import pandas as pd

#Read parameters from an input file this time
with open('sack.txt', 'r') as sack:
    max_weight = int(sack.readline())
    items = sack.read().splitlines()

# Split items into values and weights
v = [int(item.split(' ')[0]) for item in items]
w = [int(item.split(' ')[1]) for item in items]

# Array of zeroes to hold table
grid = np.zeros([len(items)+1, max_weight+1], dtype=int)

#dynamic programming using tabulation
for i in range(1, len(items)+1):
    for j in range(1, max_weight+1):
        # Current item's V + best value from one row up & W squares to the left
        value1 = v[i-1] + grid[i-1, j-w[i-1]]
        # Value one square above
        value2 = grid[i-1, j]
        
        # If current item's W will fit in the sack
        if w[i-1] <= j:
            grid[i, j] = max(value1, value2)
        else:
            grid[i, j] = value2

items.insert(0, 'Empty')
table = pd.DataFrame(grid, index=items)
print(table)
print(f'Best possible value: {table.max().max()}')