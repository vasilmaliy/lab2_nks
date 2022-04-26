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


def min_path(graph, start, end):
    paths = find_all_paths(graph, start, end)
    mt = 10 ** 99
    mpath = []
    # print('\tAll paths:', paths);
    for path in paths:
        t = sum(graph[i][j] for i, j in zip(path, path[1::]))
        print('\t', path, t)

        if t < mt:
            mt = t
            mpath = path

    # e1 = ' '.join('{}->{}:{}'.format(i, j, graph[i][j]) for i, j in zip(mpath, mpath[1::]))
    # e2 = str(sum(graph[i][j] for i, j in zip(mpath, mpath[1::])))
    # print('Best path: ' + e1 + '   Total: ' + e2 + '\n')
    return paths

def print_table( elements, data):

    row_format = "{:>15}" * (len(elements) + 1)
    print(row_format.format("", *elements))
    for team, row in zip(elements, data):
        row_array = []
        for i in elements:
            if i in data[team]:
                row_array.append(1)
            else:
                row_array.append(0)

        print(row_format.format(team, *row_array))

def find_operating_conditions( P, paths, elements):
    probabilities_of_trouble_free = []
    for path in paths:
        p = 1
        for p_kay, element in zip(P, elements):
            if element in path:
                p = p * P[p_kay]
            else:
                p = p * (1 - P[p_kay])

        probabilities_of_trouble_free.append(p)

    return probabilities_of_trouble_free

if __name__ == "__main__":
    P = {'P1': 0.41, 'P2': 0.3, 'P3': 0.59, 'P4': 0.44, 'P5': 0.51, 'P6': 0.63, 'P7': 0.72, 'P8': 0.48}

    graph = {'E1': {'E3': 1, 'E5': 1},
             'E2': {'E4': 1, 'E7': 1},
             'E3': {'E4': 1, 'E5': 1},
             'E4': {'E3': 1, 'E7': 1},
             'E5': {'E6': 1},
             'E6': {},
             'E7': {'E8': 1},
             'E8': {}}

    elements = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8'];

    print('Таблиця зв’язків системи :\n')
    print_table(elements, graph)

    print('\nCхеми представленої системи, за допомогою алгоритму пошуку у глибину:\n')

    paths = [ *min_path(graph, 'E1', 'E6'), *min_path(graph, 'E1', 'E8'), *min_path(graph, 'E2', 'E8'), *min_path(graph, 'E2', 'E6')]

    print(find_operating_conditions(P, paths, elements));

