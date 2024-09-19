import sys

trees = set()
tree_count = dict()
tree_percents = list()
while True:
    tree = sys.stdin.readline().rstrip()
    if tree:
        if tree in trees: 
            tree_count[tree] += 1
        else:
            trees.add(tree) 
            tree_count[tree] = 1
    else:
        break
tree_sum = sum(tree_count.values())
sort_tree = sorted(tree_count.items())

for count in sort_tree:
    value = count[1]
    percent = value / tree_sum
    tree_percents.append((count[0], percent))

for tree_percent in tree_percents:
    print('%s %.4f' %(tree_percent[0], tree_percent[1] * 100))
