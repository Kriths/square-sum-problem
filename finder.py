# Path finding methods based on:
# http://www.ieor.berkeley.edu/~faridani/python.htm
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_paths(graph):
    cycles = []
    for startnode in graph:
        for endnode in graph:
            newpaths = find_all_paths(graph, startnode, endnode)
            for path in newpaths:
                if (len(path) == len(graph)):
                    cycles.append(path)
    return cycles


def evaluate_current(graph):
    a = find_paths(graph)
    print(len(graph), ": Number of Hamiltonian Paths=", len(a))


def generate_squares_up_to(max):
    set = []
    current = 1
    while current ** 2 <= max:
        set.append(current ** 2)
        current += 1
    return set


def add_node(graph, node, squares):
    graph[node] = []
    check_node = 1
    while check_node < node:
        if check_node+node in squares:
            graph[node].append(check_node)
            graph[check_node].append(node)
        check_node += 1


def calculate_up_to(number):
    squares = generate_squares_up_to(number * 2)
    print(squares)
    graph = { }
    node = 1
    while node < number:
        add_node(graph, node, squares)
        print("Network for ", node, ": ", graph)
        evaluate_current(graph)
        node += 1


if __name__ == "__main__":
    calculate_up_to(300)
