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
