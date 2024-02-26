'''
#1

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

'''


'''
#2

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

'''


'''
#3

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

'''

'''
#4

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

'''

'''
#5

def kids(gen_tree, name):
    if name not in gen_tree:
        return 0
    kids_count = len(gen_tree[name])
    for kid in gen_tree[name]:
        kids_count += kids(gen_tree, kid)
    return kids_count

n = int(input())
gen_tree = {}
for _ in range(n):
    par_child = input().split()
    if par_child[0] not in gen_tree:
        gen_tree[par_child[0]] = [par_child[1]]
    else:
        gen_tree[par_child[0]].append(par_child[1])

name = input()
print(kids(gen_tree, name))

'''

'''
#6

def lst_to_matrix(cities_list, n, cities_ind):
    m = []
    for _ in range(n):
        m.append([float('inf')] * n)
    for city_1, city_2, dist in cities_list:
        m[cities_ind[city_1]][cities_ind[city_2]] = int(dist)
        m[cities_ind[city_2]][cities_ind[city_1]] = int(dist)
    return m


def floyd(m):
    n = len(m)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if m[i][j] > m[i][k] + m[k][j]:
                    m[i][j] = min(m[i][j], m[i][k] + m[k][j])
    return m


n = int(input())
m = int(input())
cities_names = set()
cities_list = []
cities_ind = {}

for _ in range(m):
    info = input().split()
    cities_list.append(info)
    for cities in info[:-1]:
        cities_names.add(cities)

ind = 0
for city in cities_names:
    cities_ind[city] = ind
    ind += 1

matr = lst_to_matrix(cities_list, n, cities_ind)
matrix = floyd(matr)
    
shortest_dist = input().split() 
print(matrix[cities_ind[shortest_dist[0]]][cities_ind[shortest_dist[1]]])

'''