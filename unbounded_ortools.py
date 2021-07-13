from ortools.linear_solver import pywraplp
import numpy as np
def main():
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')

    infinity = solver.infinity()
    # x and y are integer non-negative variables.
    x = solver.IntVar(0.0, infinity, 'x')
    y = solver.IntVar(0.0, infinity, 'y')
    z = solver.IntVar(0.0, infinity, 'y')

    print('Number of variables =', solver.NumVariables())

    w = [1,4,1]
    v = [3,5,2]

    # x + 7 * y <= 17.5.
    solver.Add(x >= 1)
    solver.Add(x <= 3)
    solver.Add(y >= 1)
    solver.Add(y <= 5)
    solver.Add(z >= 10)
    solver.Add(z <= 20)
    solver.Add(x*w[0] + y*w[1] +z*w[2]<=20)

    print('Number of constraints =', solver.NumConstraints())

    # Maximize x + 10 * y.
    solver.Maximize(x*v[0] + y*v[1] + z*v[2])

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('x =', round(x.solution_value()))
        print('y =', round(y.solution_value()))
        print('z =', round(z.solution_value()))
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
    print('Problem solved in %d branch-and-bound nodes' % solver.nodes())


if __name__ == '__main__':
    main()