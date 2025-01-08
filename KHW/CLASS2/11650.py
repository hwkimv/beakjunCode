n = int(input())
coordinate = []

for i in range(n):
    x,y = input().split()
    coordinate.append((int(x), int(y)))

set_coordinate = list(set(coordinate))
sorted_coordinate = sorted(set_coordinate, key=lambda z:(z[0], z[1]))

for i in sorted_coordinate:
    print(i[0],i[1])