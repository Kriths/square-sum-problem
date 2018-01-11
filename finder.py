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


def find_paths(graph, get_count):
    cycles = 0
    if len(graph) == 1:
        return 1
    end_nodes = 0
    for node in graph:
        if len(graph[node]) == 0: # Check for nodes without paths
            return 0
        elif len(graph[node]) == 1: # Check for nodes with only 1 path
            if end_nodes == 2: # Only 2 end nodes allowed max
                return 0
            else:
                end_nodes += 1
    for startnode in graph:
        for endnode in graph:
            newpaths = find_all_paths(graph, startnode, endnode)
            for path in newpaths:
                if (len(path) == len(graph)):
                    cycles += 1
                    if not get_count:
                        return 1
    return cycles


def evaluate_current(graph, get_count):
    count = find_paths(graph, get_count)
    if get_count:
        print(len(graph), ": Number of Hamiltonian Paths=", count)
    else:
        print(len(graph), ": Hamiltonian Paths exist: ", count > 0)

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
    while check_node < node: # Check all existing nodes for connections
        if check_node+node in squares:
            graph[node].append(check_node)
            graph[check_node].append(node)
        check_node += 1


def calculate_up_to(number, get_count):
    squares = generate_squares_up_to(number * 2) # Cache square numbers
    print(squares)
    graph = { }
    node = 1
    while node < number:
        add_node(graph, node, squares)
        print("Network for ", node, ": ", graph)
        evaluate_current(graph, get_count)
        node += 1


if __name__ == "__main__":
    calculate_up_to(300, False)
