"""Way overkill implementation because it's a bit of a tricky problem to express cleanly!"""

from typing import Dict
from collections import defaultdict


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
        self.all = self._build_numbers(digits)
        self.by_tuple = {pn.tup(): pn for pn in self.all}
        self.by_number = self._build_by_number()

    def _build_numbers(self, digits):
        sets = {i: truncate_to_range(get_polygonals(10 ** digits, i), 10 ** (digits - 1), 10 ** digits) for i in self.all_bases()}

        return sorted([PolygonalNumber(i, base) for base, ps in list(sets.items()) for i in ps])

    def _build_by_number(self):
        v = defaultdict(set)

        for pn in self.all:
            v[pn.n].add(pn)

        return v

    def get_bases(self, n):
        return set(pn.base for pn in self.by_number[n])

    def all_bases(self):
        return list(range(3, 8 + 1))

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

class PolygonalNumber:
    def __init__(self, n: int, base: int):
        self.n = n
        self.base = base

    def tup(self):
        return self.n, self.base

    def __repr__(self):
        return f"PN({self.n}, {self.base})"

    def __hash__(self):
        return hash(self.tup())

    def __lt__(self, other: 'PolygonalNumber'):
        return self.tup() < other.tup()

class Node:
    def __init__(self, pn: PolygonalNumber):
        self.pn = pn
        self.edges = []  # List of other node IDs that can come after this one

    def __repr__(self):
        return f"Node({str(self.pn)})"

class DFSState:
    def __init__(self):
        self.stack: [Node] = []
        self.seen_numbers = set()
        self.seen_bases = set()
        self.saved = []

    def step(self, node: Node):
        self.stack.append(node)
        self.seen_numbers.add(node.pn.n)
        self.seen_bases.add(node.pn.base)

    def pop(self):
        popped = self.stack.pop()
        self.seen_numbers.remove(popped.pn.n)
        self.seen_bases.remove(popped.pn.base)

    def current(self) -> Node:
        return self.stack[-1]

    def first(self) -> Node:
        return self.stack[0]

    def sum(self):
        return sum(self.seen_numbers)

    def stack_pns(self):
        return [node.pn for node in self.stack]

    def save_stack_pns(self):
        self.saved.append(self.stack_pns())

    def __repr__(self):
        return str(self.stack_pns())

def cyclical_figurate_numbers():
    # First, build graph
    # Nodes are polygonal numbers, edges are all possible following numbers in the sequence
    polygonal_manager = PolygonalManager(digits=4)
    fixed_prefix_map = FixedPrefixMap(length=2, values=[pn.n for pn in polygonal_manager.all])

    nodes: Dict[PolygonalNumber, Node] = {n: Node(n) for n in polygonal_manager.all}

    for pn, node in list(nodes.items()):
        for chained_p in fixed_prefix_map.for_prefix(suffix(pn.n, 2)):
            for base in polygonal_manager.get_bases(chained_p):
                if base != pn.base:
                    edge = nodes[polygonal_manager.by_tuple[(chained_p, base)]]
                    node.edges.append(edge)

    dfs_state = DFSState()

    # Next, conduct DFS from each number to see if we can find a path which contains all polygonal bases
    for node in list(nodes.values()):
        # There's only one, and it's a cycle, so we should be able to limit to starting from a base of 3
        if node.pn.base != 3:
            continue

        dfs_state.step(node)

        dfs(dfs_state, nodes)

        dfs_state.pop()

    for saved in dfs_state.saved:
        print((saved, sum(pn.n for pn in saved)))

def dfs(
    s: DFSState,
    nodes: Dict[PolygonalNumber, Node],
):
    if len(s.stack) == 6:
        if suffix(s.current().pn.n, 2) == prefix(s.first().pn.n, 2):
            s.save_stack_pns()
    else:
        for edge in s.current().edges:
            if edge.pn.n in s.seen_numbers or edge.pn.base in s.seen_bases:
                continue

            s.step(edge)

            dfs(s, nodes)

            s.pop()


cyclical_figurate_numbers()





