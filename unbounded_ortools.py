#Author - John and Sean @ Last Mile but its not too many edits away from the Google/OR example here
#https://developers.google.com/optimization/mip/integer_opt
'''
This is when we start to get clever and use the optimization algorithms from Operations Research.
Under the hood, the solvers reduce the solution space cleverly which reduces the order of complexity.
Another advantage is that you can start to express complex business problems in a manageable way. If we kept with 
heuristics, the programs would become very complex to manage corner cases
'''

from ortools.linear_solver import pywraplp

"""
x[0]: Suncream (1, 3)
x[1]: Suncream (1, 5)
x[2]: Clothes (10, 20)

"""

# Set matching values/weights for the objects
    w = [1,4,1]
    v = [3,5,2]

# Create the mip solver with the SCIP backend
solver = pywraplp.Solver.CreateSolver('SCIP')

# All values for x are integer non-negative variables (item quantities)
infinity = solver.infinity()
x = [solver.IntVar(0, infinity, 'x[{}]'.format(i)) for i in range(3)]

# Total sum for all qty*weight <= 20
solver.Add(sum(x[i]*w[i] for i in range(len(x))) <= 20)

# 1 <= qty of suncream <= 3
solver.Add(1 <= x[0])
solver.Add(x[0] <= 3)

# 1 <= Qty of books <= 5
solver.Add(x[1] >= 1)
solver.Add(x[1] <= 5)

# 10 <= Qty of clothes >= 20
solver.Add(x[2] >= 10)
solver.Add(x[2] <= 20)

# Maximise sum for all qty*value
solver.Maximize(sum([x[i]*v[i] for i in range(len(x))]))

# Solve and show results
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    weight = sum([x[i].solution_value()*w[i] for i in range(len(x))])
    print('Solution:')
    print('Objective value =', int(solver.Objective().Value()))
    print('Total weight = ', weight)
    for i in range(len(x)):
        print('x[{}] = {}'.format(i, x[i].solution_value()))
else:
    print('The problem does not have an optimal solution.') 
