
#Author: John Curry - Last Mile

'''
This program just says Feck it! Generate every possible combination of items for the knapsack.
Then just choose the best one that fits the constraints.  If the number of combos are small, its a perfectly
cromulent solution
'''

import numpy as np
import pandas as pd

def binary_combo(n):
    ##generate sequence of zeros of length n: s
    perms = np.zeros((1, n), dtype=int)
    for i in range (0, n):
        tmp = np.copy(perms) #copy existing matrix
        tmp[:,i] = 1 # set value of column i to 1
        perms = np.append(perms, tmp, axis = 0) # append to existing matrix
    return perms

def binary_combo2(length: int) -> list:
    #Seans version this is an awful lot nicer than the other function but too clever for me
    return [bin(i)[2:].zfill(length) for i in range(2**length)]

capacity = 12
n = 3
item_names = ['suncream', 'books', 'clothes']
item_values = np.array([10, 3, 1])
item_weights = np.array([3, 2, 10])

constraints = [f'total_weight < {capacity}']
constraint_qry = '&'.join(constraints)

#generate the possible combinations
base = pd.DataFrame(binary_combo(n), columns=item_names)

print('\nPermutations Matrix\n', base)

base['total_weight'] = (base * [int(x) for x in item_weights]).sum(axis=1)
base['total_value'] = (base[item_names] * [int(x) for x in item_values]).sum(axis=1)

print('\nBase Matrix\n', base)

solution = base.query(constraint_qry).nlargest(1,['total_value'])

print('\nSolution', solution)







    
   