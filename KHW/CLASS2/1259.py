def palindrome_number(num):
    if num == num[::-1]:
        print("yes")
    else:
        print("no")

while True:
    try:
        number = str(input())

        if number == "0":
            break

        elif number[0] == "0":
            print("다시 입력하세요")
            continue

        else:
            palindrome_number(number)

    except EOFError:
        break
