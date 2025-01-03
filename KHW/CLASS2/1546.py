
def average(score,sub):
    max_score = max(score)
    average_score = sum(score)/max_score*100/sub
    return average_score

subs = int(input())
sub_score = list(map(int, input().split()))
print(average(sub_score,subs))