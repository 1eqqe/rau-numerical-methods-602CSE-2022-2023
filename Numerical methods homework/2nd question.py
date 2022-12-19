def f(x):
    x0 = g(x)
    n_iter = 1000
    while (n_iter & x0 > 0):
        x0 = g(x)
        print(x0)
    print(f0(x), f1(x), f2(x))