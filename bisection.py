def bisection(a0, b0, df, tol):
    t, a, b, c = 0, a0, b0, (a0+b0)/2
    while abs(df(c)) > tol:
        c = (a+b)/2
        print(f'Iteration {t}')
        print(f'a{t} = {a}, b{t} = {b}')
        print()
        if df(c)*df(a) < 0: b = c
        else:               a = c
        t += 1
    return c

print(bisection(-1, 2, lambda x: 2*x, 0.01))