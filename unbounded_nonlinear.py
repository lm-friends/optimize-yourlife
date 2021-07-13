import numpy as np
from scipy.optimize import minimize

#ref for inequality constraint example syntax https://stackoverflow.com/questions/21765794/python-constrained-non-linear-optimization

'''
This is scipy kicking Google ORs a**.  Not only does it handle the linear version, it also 
handles a nonlinear objective function with ease.  There must be a downside somewhere. Maybe not 
as performant at scale? But so far so good...
'''

def objective(x):
    #linear objective
    # return - ( np.dot(x, v) ) # x[1]*v[1] + ...x[n]*v[n]
    
    #non linear objective
    return -( np.dot(x, v) + x[1]*v[1]*x[2]*v[2] )

def constraint1(x):
    return 20.0 -(np.dot(x, w)) # x[1]*w[1] + ...x[n]*w[n]


n = 3
x0 = np.array([1, 1, 5]) # initial guesses
w = np.array([1,4,1]) # weights
v = np.array([3,5,2]) # values

# show initial objective
print('Initial SSE Objective: ' + str(objective(x0)))

# optimize
bnds = ((1.0, 3.0), (1.0, 5.0), (10.0, 20.0))
con1 = {'type': 'ineq', 'fun': constraint1} 
cons = ([con1])
solution = minimize(objective,x0,method='SLSQP',\
                    bounds=bnds,constraints=cons)
x = solution.x

# show final objective
print('Final SSE Objective: ' + str(round(objective(x))*(-1)))

#debug:check weight constraint is working. this number should be close to zero or going over weight
print(str(20-(x[0]*w[0]+x[1]*w[1]+x[2]*w[2]) ))

# print solution
print('Solution')
print('x1 = ' + str(round(x[0])))
print('x2 = ' + str(round(x[1])))
print('x3 = ' + str(round(x[2])))
