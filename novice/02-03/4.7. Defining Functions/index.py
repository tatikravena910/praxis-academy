def fib(n):  
    # a, b = 0, 1
    a = 0
    b = 1
    while a < n:
        print(a, end="")
        a, b = b, a+b
    print()

fib(2000)
fib (0)
print (fib(0))