def count(n):
    if n >= 1:
        print(n, end=' ')
        count(n-1)
    else:
        return

count(10)

def sum(n):
    if n ==1:
        return 1
    else:
        return n + sum(n-1)
print(sum(10))

def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(10))
