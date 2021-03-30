# independent-set-fpt
Search tree algorithm for finding an independent set of a planar graph with parameterized time complexity.

#### INDEPENDENT SET
Input: A planar graph G = (V,E) and a non-negative integer k.
Output: A subset V' of V with at least k pairwise non-adjacent vertices.

The INDEPENDENT SET problem is fixed-parameter tractable (FPT) and this algorithm
follows a search tree approach with time complexity O(6^k * poly(n)) where n is the number
of vertices in G and poly(n) is a polynomial depending on n.
