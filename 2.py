n = int(input())
rus_eng_dict = {}

for _ in range(n):
    words = input().split()
    rus_eng_dict[words[0]] = words[1]

sentence = input().split()
translation = ''
for word in sentence:
    if word in rus_eng_dict:
        translation += rus_eng_dict[word] + ' '
    else:
        translation += word + ' '

print(translation)
