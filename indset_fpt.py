# INDEPENDENT SET
# Input: A planar graph G = (V,E) and a non-negative integer k.
# Output: A subset V' of V with least k pairwise non-adjacent vertices.
#
# The INDEPENDENT SET problem is fixed-parameter tractable and the following algorithm
# follows a search tree approach with time complexity O(6^k * poly(n)) where n is the number
# of vertices in G and poly(n) is a polynomial depending on n.

from graph import *
import copy
import sys

def is_solution(g: Graph, sol_candidate: list) -> bool:
    for v in sol_candidate:
        for u in sol_candidate:
            if g.is_adjacent(v, u):
                return False
    return True

# Finds an independent set (size at least k) of the given Graph g
# and returns it as a list of vertices. If there is no such set, the empty list is
# returned.
#
# The behavior is undefined if the given graph is not planar.
#
# The parameters sol and orig are used internally and do not have to be specified
# when calling find_independent_set initially. They are given because this is a
# recursive procedure.
def find_independent_set(g: Graph, k: int, sol: list = [], orig: Graph = None) -> list:
    if k < 0:
        sys.exit("find_independent_set ERROR: k needs to be >= 0")
    # This is a hack to be able to set orig equal to g in the first recursion, 
    # which we cannot do in the parameter declaration.
    if orig == None:
        orig = g

    if k == 0:
        if is_solution(orig, sol):
            return sol
        return []
    
    # Get a vertex v of minimal degree
    if g.get_number_of_vertices() == 0:
        # We have k > 0 as the k == 0 case is handled above.
        # Therefore, we still need to add at least k > 0 vertices to get a solution.
        # However, if we have no more vertices in the graph, there cannot be a solution.
        return []
    deg_dict = dict()
    for vertex in g.vertices:
        deg_dict[vertex] = g.get_degree(vertex)
    v = min(deg_dict, key=deg_dict.get)

    # Branching: Put v or one of its neighbors into the solution
    g_minus_v = copy.deepcopy(g)
    # We put v into the solution, so delete v and its neighbors from the graph
    # (The neighbors of v cannot be in the solution if we take v)
    v_neighbors = g.get_neighbors(v)
    g_minus_v.remove_vertex(v)
    for v_n in v_neighbors:
        g_minus_v.remove_vertex(v_n)
    sol_v = find_independent_set(g_minus_v, k - 1, sol + [v], orig)
    if sol_v != []:
        return sol_v
    for u in g.get_neighbors(v):
        g_minus_u = copy.deepcopy(g)
        # We put u into the solution, so delete u and its neighbors from the graph
        u_neighbors = g.get_neighbors(u)
        g_minus_u.remove_vertex(u)
        for u_n in u_neighbors:
            g_minus_u.remove_vertex(u_n)
        sol_u = find_independent_set(g_minus_u, k - 1, sol + [u], orig)
        if sol_u != []:
            return sol_u
    return []   # there is no solution

def main():
    # Test graph 1
    gstr = "a:b,c,d; b:a,c; c:a,b; d:a;;"
    graph = get_graph_from_str(gstr)
    print(graph)
    indset = find_independent_set(graph, k=2)
    print("indset (k=2): ", indset)

    # Test graph 2 (induced path with five vertices)
    gstr = "a:b; b:a,c; c:b,d; d:c,e; e:d;;"
    graph = get_graph_from_str(gstr)
    print(graph)
    indset = find_independent_set(graph, k=0)
    print("indset (k=0): ", indset)
    indset = find_independent_set(graph, k=1)
    print("indset (k=1): ", indset)
    indset = find_independent_set(graph, k=2)
    print("indset (k=2): ", indset)
    indset = find_independent_set(graph, k=3)
    print("indset (k=3): ", indset)
    indset = find_independent_set(graph, k=4)
    print("indset (k=4): ", indset)

    # Test graph 3
    gstr = "a:b,c,d,e,f; b:a,c,f; c:a,b,d,e; d:a,c,e; e:a,c,d,f; f:a,b,e;;"
    graph = get_graph_from_str(gstr)
    print(graph)
    indset = find_independent_set(graph, k=2)
    print("indset (k=2): ", indset)
    indset = find_independent_set(graph, k=3)
    print("indset (k=3): ", indset)

    # Test graph 4
    gstr = "a:;;"
    graph = get_graph_from_str(gstr)
    print(graph)
    indset = find_independent_set(graph, k=1)
    print("indset (k=1): ", indset)

if __name__ == "__main__":
    main()
