# 1181

def sorting_func(list):
    return (len(list), list)

N = int(input())
words = set()
for _ in range(N):
    word = input()
    words.add(word)

new_words = sorted(words, key=sorting_func)
for word in new_words:
    print(word)