def find (sample_n, find_n, start, end):
    if start > end:
        print(0)
        return
    mid = (start + end) // 2
    if sample_n[mid] == find_n:
        print(1)
        return
    elif sample_n[mid] > find_n:
        find(sample_n, find_n, start, mid - 1)
    else:
        find(sample_n, find_n, mid + 1, end)



sample_number_count = int(input())
sample_number = list(map(int, input().split()))
sort_sample_number = sorted(sample_number)

find_number_count = int(input())
find_number = list(map(int, input().split()))


for i in find_number:
    find(sort_sample_number, i, 0, sample_number_count - 1)