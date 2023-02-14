def golden(a0, b0, f, tol):
    gr = (5**0.5-1)/2
    t, a, b = 0, a0, b0
    while b - a > tol:
        λ, μ = gr*a + (1-gr)*b, (1-gr)*a + gr*b
        print(f'Iteration {t}')
        print(f'a{t} = {a}, b{t} = {b}, λ{t} = {λ}, μ{t} = {μ}')
        print()
        if f(μ) > f(λ): b = μ
        else:           a = λ
        t += 1
    return (a+b)/2

print(golden(-1, 2, lambda x: x**2, 0.01))