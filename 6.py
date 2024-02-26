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
