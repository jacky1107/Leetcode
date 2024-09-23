x = "1*2*3-4/3-2"
x = "1-2-3-4" #-3-2"

l1 = []
l2 = []

for i in x:
    if i in "+-*/":
        l2.append(i)
    else:
        l1.append(i)

print(l1, l2)

total = 0
i1 = len(l1) - 1
i2 = len(l2) - 1
while len(l2) != 0:
    v1 = l1[i1]
    op = l2[i2]
    if op in "*/":
        v2 = l1[i1-1]
        total = (float(v1) + float(v2))
        l1 = l1[:i1] + [str(total)] + l1[i1+1:]
        l2 = l2[:i2] + l2[i2+1:]
    elif i2 == 0:
        v2 = l1[i1-1]
        total = (float(v1) + float(v2))
        l1 = l1[:i1] + [str(total)]
        l2 = l2[:i2] + l2[i2+1:]
        i1 += 1
        i2 += 1
    else:
        i1 -= 1
        i2 -= 1

    print(l1, l2)
    print(i1, i2)
print(total)