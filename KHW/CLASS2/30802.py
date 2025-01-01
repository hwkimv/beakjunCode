def t_shirt(tshirt_count, tshirt_bundle):
    if tshirt_count == 0:
        return 0

    else:
        tshirt_bundle_count = tshirt_count // tshirt_bundle
        tshirt_one = tshirt_count % tshirt_bundle

        if tshirt_one == 0:
            return tshirt_bundle_count

        else:
            return tshirt_bundle_count + 1

N = int(input())
t_shirt_list = list(map(int,input().split()))
T,P = map(int,input().split())
all_tshirt_bundle = 0

for i in t_shirt_list:
    all_tshirt_bundle += t_shirt(i,T)

pan_bundle = N // P
pan_one = N % P

print(all_tshirt_bundle)
print(pan_bundle, pan_one)