def find_primenumbers(numbers):
    result = []
    for number in numbers:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                result.append(number)
    return result

N = int(input())
numbers_list = list(map(int, input().split()))
prime_number = find_primenumbers(numbers_list)

print(len(prime_number))