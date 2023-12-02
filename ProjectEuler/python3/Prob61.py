from typing import Tuple, Set, List, Dict


def polygonal(i, base=None):
    """
    P_3_n = n(n + 1) / 2    = n( n - -1) / 2
    P_4_n = n^2             = n(2n - 0) / 2
    P_5_n = n(3n - 1) / 2   = n(3n - 1) / 2
    P_6_n = n(2n - 1)       = n(4n - 2) / 2
    P_7_n = n(5n - 3) / 2   = n(5n - 3) / 2
    P_8_n = n(3n - 2)       = n(6n - 4) / 2
    """

    multiplier = base - 2
    constant = base - 4

    # Order of operations helps!
    return i * (multiplier * i - constant) // 2

def get_polygonals(up_to, base=None):
    polygonals = set()

    i = 1

    while polygonal(i, base) <= up_to:
        polygonals.add(polygonal(i, base))

        i += 1

    return polygonals

def truncate_to_range(values: set, start, end_exclusive):
    return set(v for v in values if start <= v < end_exclusive)

def prefix(n, digits):
    return str(n)[:digits]

def suffix(n, digits):
    return str(n)[-digits:]

class PolygonalManager:
    def __init__(self, *, digits):
        self.polygonal_sets = {i: truncate_to_range(get_polygonals(10 ** digits, i), 10 ** (digits - 1), 10 ** digits) for i in range(3, 8 + 1)}

    def get_bases(self, n):
        return set(i for i in range(3, 8 + 1) if n in self.polygonal_sets[i])

    def all(self):
        return sorted(set.union(*list(self.polygonal_sets.values())))

class FixedPrefixMap:
    def __init__(self, *, length, values):
        self.prefix_map = self._build_prefix_map(length, values)

    def for_prefix(self, prefix):
        return self.prefix_map[prefix] if prefix in self.prefix_map else set()

    def _build_prefix_map(self, length, values):
        prefix_map = {}

        for i in range(10 ** (length - 1), 10 ** length):
            prefix_map[prefix(i, length)] = set()

        for v in values:
            prefix_map[prefix(v, length)].add(v)

        return prefix_map

class Node:
    def __init__(self, _id: Tuple[int, int]):
        self._id = _id
        self.n = _id[0]
        self.base = _id[1]
        self.edges = []  # List of other node IDs that can come after this one

    def __repr__(self):
        return str(self._id)

def cyclical_figurate_numbers():
    # First, build graph
    # Nodes are polygonal numbers, edges are all possible following numbers in the sequence
    polygonal_manager = PolygonalManager(digits=4)
    fixed_prefix_maps = { base: FixedPrefixMap(length=2, values=polygonal_set) for base, polygonal_set in polygonal_manager.polygonal_sets.items()}

    nodes = {(n, base): Node((n, base)) for base, polygonal_set in polygonal_manager.polygonal_sets.items() for n in polygonal_set}

    for (n, base), node in nodes.items():
        if base == 8:
            continue

        for chained_p in fixed_prefix_maps[base + 1].for_prefix(suffix(n, 2)):
            node.edges.append((chained_p, base + 1))

    result = None

    # Next, conduct DFS from each number to see if we can find a path which contains all polygonal bases
    for (n, base), node in nodes.items():
        if base != 3:
            continue

        stack = [n]

        if dfs((n, base), nodes, stack, { n }):
            result = stack
            break

    print(result)

    return sum(result)

def dfs(
    _id: Tuple[int, int],
    nodes: Dict[Tuple[int, int], Node],
    stack: List[int],
    seen: Set[int]
):
    n, base = _id

    print(stack, base)

    if len(stack) == 3:
        if suffix(stack[-1], 2) == prefix(stack[0], 2):
            return True
    else:
        for (edge_n, edge_base) in nodes[_id].edges:
            if edge_n in seen:
                continue

            stack.append(edge_n)
            seen.add(edge_n)

            if dfs((edge_n, edge_base), nodes, stack, seen):
                return True

            stack.pop()
            seen.remove(edge_n)

    return False


print(cyclical_figurate_numbers())





