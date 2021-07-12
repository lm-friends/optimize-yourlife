# optimize-yourlife
Introduction to mixed integer programming for pythonistas

# Background

This set of programs explains some fundamentals of mixed integer programming with Google/OR for Pythonistas.

You can go through solving knapsack using brute force or dynamic programming. 
But for unbounded problems, the order of complexity grows too high for efficient solution. At that point, the techniques of MIP start to show their usefulness.  Not only do they reduce compute
time but they allow you to represent a complex problem in simple mathematical terms for solution by a solver.

And if the problem becomes non linear, thats OK too. You may still be able to solve using non linear optimization ala Boyd with cvxopt.

https://www.youtube.com/watch?v=gF8flc_a4D0&t=2s for a fuller explanation

# Dependencies

pip install numpy pandas ortools cvxopt



