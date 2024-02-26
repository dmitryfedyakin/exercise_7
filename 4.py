n = int(input())
form_item_dict = {}

for i in range(n):
    words = input().split()
    for j in range(1, len(words)):
        form_item_dict[words[j]] =  words[0]
    
word = input()
if word in form_item_dict:
    print(form_item_dict[word])
else:
    print("Такого слова нет")
