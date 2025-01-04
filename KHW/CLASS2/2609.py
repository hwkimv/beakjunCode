def gcd(a, b):
    for i in range(a,1,-1):
        if b % i == 0:
            if a % i == 0:
                return i

    return 1

def lcm(a, b):
    return a * b // gcd(a, b)

num1, num2 = map(int, input().split())

if num1 > num2:
    num1, num2 = num2, num1

print(gcd(num1, num2))
print(lcm(num1, num2))