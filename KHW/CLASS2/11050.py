def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)

def binomial_theorem(n,k):
    return fact(n) // (fact(k) * fact(n - k))

num1, num2 = map(int, input().split())

if num1 < num2:
    num1, num2 = num2, num1

print(binomial_theorem(num1, num2))