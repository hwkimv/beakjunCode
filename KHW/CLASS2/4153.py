while True:
    NUM= list(map(int, input().split()))
    C = max(NUM)
    NUM.remove(C)
    if sum(NUM)==0:
        break

    if NUM[0]**2 + NUM[1]**2 == C**2:
        print("right")
    else:
        print("wrong")
