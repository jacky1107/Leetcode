def findAll(x, target=100):
    table = {}
    res = []
    for i in range(len(x)):
        if x[i] not in table:
            table[target - x[i]] = [i, x[i]]
        else:
            res.append([table[x[i]], [i, x[i]]]) 

    print(table)
    print(res)


x = [38, 2, 2, 3, 62]
findAll(x, target=100)

import random

print(random.random() * 400)
