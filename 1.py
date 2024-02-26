sentence = input().split()
word_freq = {}

for word in sentence:
    word_count = sentence.count(word)
    word_freq[word_count] = word

for i in range(max(word_freq), min(word_freq) - 1, -1):
    if i in word_freq:
        print(word_freq[i])
    else:
        continue
