def get_int(string, index):
    temp = ""
    while index < len(string):
        if string[index] == "," or string[index] == "]":
            print(temp)
            return int(temp), index
        elif string[index].isnumeric():
            temp += string[index]
        index += 1
    return -1, index

i = 0
j = 0
strings = ["[5, 2, 3]", "[2,2,3,10,6]"]
min_len = min(len(strings[0]), len(strings[1]))
prev_i = 1
while i < min_len or j < min_len:
    if strings[0][i] == "]" or strings[1][j] == "]": break
    v1, i = get_int(strings[0], i)
    v2, j = get_int(strings[1], j)
    strings[0] = strings[0][:prev_i] + str(v1 + v2) + strings[0][i:]

    i += 1
    j += 1
    prev_i = i

    print(strings[0][:-1] + strings[1][j-1:])

