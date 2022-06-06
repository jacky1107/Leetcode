def depth_first_print(start_node, hashMap):
    stack = [start_node]

    while len(stack) > 0:
        current_node = stack.pop()
        print(current_node)
        neighboring_nodes = hashMap[current_node]
        for node in neighboring_nodes:
            stack.append(node)


def depth_first_print_recursive(start_node, hashMap):
    print(start_node)
    neighboring_nodes = hashMap[start_node]
    for node in neighboring_nodes:
        depth_first_print_recursive(node, hashMap)


def breadth_first_print(start_node, hashMap):
    queue = [start_node]

    while len(queue) > 0:
        current_node = queue[0]
        print(current_node)
        neighboring_nodes = hashMap[current_node]
        for node in neighboring_nodes:
            queue.append(node)
        queue.remove(current_node)

def breadth_first_print_recursive(start_node, hashMap):
    print(start_node)
    neighboring_nodes = hashMap[start_node]
    for node in neighboring_nodes:
        breadth_first_print_recursive(node, hashMap)

hashMap = {
    "a": ['c', 'b'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": [],
}

depth_first_print("a", hashMap)
print("")
depth_first_print_recursive("a", hashMap)
print("")
breadth_first_print("a", hashMap)
print("")
breadth_first_print_recursive("a", hashMap)