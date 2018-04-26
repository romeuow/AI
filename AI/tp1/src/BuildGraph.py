import importlib


def remove_item(valid_nodes, i, j):
    r = dict(valid_nodes)
    del r[(i, j)]
    return r


def del_diagonal_v(valid_nodes, i, j):
    try:
        print('removendo: ', i-1, j)
        print('removendo: ', i+1, j)
        remove_item(valid_nodes, i-1, j)
        remove_item(valid_nodes, i+1, j)
    except KeyError:
        pass


def del_diagonal_h(valid_nodes, i, j):
    try:
        print('removendo: ', i, j-1)
        print('removendo: ', i, j+1)
        remove_item(valid_nodes, i, j-1)
        remove_item(valid_nodes, i, j+1)
    except KeyError:
        pass


def valid_paths(i, j):
    if not cell_free(i, j):
        return []
    valid_nodes = {}
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if cell_free(k, l) and not (k == i and l == j):
                valid_nodes.update({(k, l): (i, j)})
    print(valid_nodes)
    if not cell_free(i-1, j):
        del_diagonal_h(valid_nodes, i-1, j)
    if not cell_free(i+1, j):
        del_diagonal_h(valid_nodes, i+1, j)
    if not cell_free(i, j-1):
        del_diagonal_v(valid_nodes, i, j-1)
    if not cell_free(i, j+1):
        del_diagonal_v(valid_nodes, i, j+1)

    return valid_nodes


def cell_free(i, j):
    try:
        if hash_map[(i, j)] == '.':
            return True
        else:
            return False
    except KeyError:
            return False


BuildMap = importlib.import_module('BuildMap')
hash_map = BuildMap.build_map()
print(valid_paths(8, 7))
