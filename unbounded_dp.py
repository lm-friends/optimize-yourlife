#Author: Anant Agarwal on https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
# This code is contributed by .
# Python3 program to find maximum
# achievable value with a knapsack
# of weight W and multiple instances allowed.
 
# Returns the maximum value
# with knapsack of W capacity

'''
This program deals even with unbounded knapsack using DP with a recursive formula this time. Just goes to prove that even 
even beyond the 1/0 problem, its perfectly cromulent to use a classic CS approach. Very elegant code.
However things will explode if n is large or the range of values allowed for each item is large
'''
def unboundedKnapsack(W, n, val, wt):
 
    # dp[i] is going to store maximum
    # value with knapsack capacity i.
    dp = [0 for i in range(W + 1)]
 
    ans = 0
 
    # Fill dp[] using above recursive formula
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
 
    return dp[W]
 
# Driver program
W = 100
val = [10, 30, 20]
wt = [5, 10, 15]
n = len(val)
 
print(unboundedKnapsack(W, n, val, wt))
 
