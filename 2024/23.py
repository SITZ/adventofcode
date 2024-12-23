# Problem: https://adventofcode.com/2024/day/22

from itertools import combinations
from collections import defaultdict

network = defaultdict(set)
for line in open('input.txt'):
    computer1, computer2 = line.strip().split('-')
    network[computer1].add(computer2)
    network[computer2].add(computer1)

triangles = set()
for computer1 in network:
    neighbors = network[computer1]
    for computer2, computer3 in combinations(neighbors, 2):
        if computer3 in network[computer2]:
            triangles.add(tuple(sorted([computer1, computer2, computer3])))

print("Part 1:", len([triangle for triangle in triangles if any(computer.startswith('t') for computer in triangle)]))


def bron_kerbosch(R, P, X, cliques):
    if not P and not X:
        cliques.append(R)
        return
    for v in list(P):
        bron_kerbosch(R | {v}, P & network[v], X & network[v], cliques)
        P.remove(v)
        X.add(v)


cliques = []
bron_kerbosch(set(), set(network.keys()), set(), cliques)
largest_clique = max(cliques, key=len)
print("Part 2:", ','.join(sorted(largest_clique)))
