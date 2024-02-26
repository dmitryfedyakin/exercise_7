n = int(input())
ant_dict = {}

for _ in range(n):
    words = input().split()
    ant_dict[words[0]] = words[1]

word = input()
if word in ant_dict:
    print(ant_dict[word])
else:
    print(word)
