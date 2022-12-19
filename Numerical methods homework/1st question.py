import numpy as np
import matplotlib.pyplot as plt
def bisection(f, x0, x1, eps_f=0.001, eps_x=0.001, n_iter=1000):
    """
    Solves f(x)=0 with bisection method
  
      Outputs:
       xg is the root approximation
       fg is the function evaluated at final guess f(xg)
       N_eval is the number of function evaluations
      Inputs:
  
    f is the function handle to the desired function,
    xn and xp are borders of search, i.e. root brackets,
    eps_f defines maximum deviation of f(x_sol) from 0,
    eps_x defines maximum deviation from the true solution
    """
    # TOOD: Check that f(x0) < 0. Raise an error otherwise.
    # Your code goes here.
    if f(x0) < 0:
        print("Greate")
    else:
        print('Error')

    # TODO: Check that f(x1) > 0. Raise an error otherwise.
    # Your code goes here.
    if f(x1) > 0:
        print("Good")
    else:
        print('Error')

    # Initialization
    xg = (x1 + x0) / 2  # Initial root guess
    fg = f(xg)  # Initial function evaluation
    iter_num = 1  # We just evaluated the function

    # Search for root
    while (np.abs(xg - x1) > eps_x or np.abs(fg) > eps_f) and (iter_num < n_iter):
        if fg > 0:
            x1 = xg
        else:
            x0 = xg

        # TODO: Update xg, fg, and increase the iteration number.
        # Your code goes here.
    while (np.abs(xg - x1) > eps_x or np.abs(fg) > eps_f) and (iter_num < n_iter):
        values = [fg, xg]
        for i, a in enumerate(values):
            values[i] = a + 42
        if conditions:
            for iter_num in range(iter_num, iter_num + 6):
            iter_num = iter_num + 6
        else:
            break