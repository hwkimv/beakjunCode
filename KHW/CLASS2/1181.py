def arrange_words(arr_word):
    arr_word = list(set(arr_word)) # 중복 제거

    arr_word.sort(key=lambda x:(len(x),x))# 길이순 정렬
    return arr_word

n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)

for i in arrange_words(words):
    print(i)