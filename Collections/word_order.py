from collections import defaultdict

n = int(input())
words = defaultdict(int)
for _ in range(n):
    word = input()
    words[word] = 1 + words.get(word, 0)

print(len(words))
print(' '.join(map(str, words.values())))
