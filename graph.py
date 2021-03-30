class Graph:
    """
    vertices: list
        A list of str representing the vertices
    adj_list: dict
        A dict mapping vertices (str) to list of str representing the neighbors (adjacency list)
    """
    def __init__(self, vertices: list, adj_list: dict):
        self.vertices = vertices
        self.adj_list = adj_list

    def __str__(self):
        graphstr = ""
        for (i, vertex) in enumerate(self.vertices):
            graphstr += vertex + ":"
            for (j, neighbor) in enumerate(self.adj_list[vertex]):
                graphstr += neighbor
                if j != len(self.adj_list[vertex]) - 1:
                    graphstr += "," # there are still more neighbors to print
            graphstr += ";" # finished printing current vertex
            if i != len(self.vertices) - 1:
                graphstr += " " # there are still more vertices to print
        graphstr += ";" # finished printing the graph
        return graphstr

    def get_degree(self, vertex: str) -> int:
        return len(self.adj_list[vertex])

    def get_number_of_vertices(self) -> int:
        return len(self.vertices)

    # If you have an undirected graph, divide this value by 2
    def get_number_of_edges(self) -> int:
        num_edges = 0
        for v in self.vertices:
            num_edges += self.get_degree(v)
        return num_edges

    def get_neighbors(self, vertex: str) -> list:
        return self.adj_list[vertex]

    def is_adjacent(self, vertex_a: str, vertex_b: str) -> bool:
        return vertex_b in self.adj_list[vertex_a]

    def remove_vertex(self, vertex: str):
        for neighbor in self.adj_list[vertex]:
            self.adj_list[neighbor].remove(vertex)
        del self.adj_list[vertex]
        self.vertices.remove(vertex)

def get_graph_from_str(graphstr: str) -> Graph:
    vertices = []
    adj_list = dict()

    # GRAPH STRING PARSER (FINITE STATE MACHINE)
    # 0: initial, 1: adding new vertex, 2: adding new neighbor
    parser_state = 0
    # auxiliary variables
    vertex_name = ""
    neighbor_name = ""
    for c in graphstr:
        if c == " ": # skip spaces
            continue

        if parser_state == 0:
            current_vertex = ""
            if c.isalnum():
                vertex_name += c
                parser_state = 1
            elif c == ";":
                # success
                pass
        elif parser_state == 1:
            if c.isalnum():
                vertex_name += c
            elif c == ":":
                current_vertex = vertex_name
                vertices.append(current_vertex)
                adj_list[current_vertex] = []
                vertex_name = ""
                parser_state = 2
        elif parser_state == 2:
            if c.isalnum():
                neighbor_name += c
            elif c == ",":
                adj_list[current_vertex].append(neighbor_name)
                neighbor_name = ""
            elif c == ";":
                if neighbor_name != "":
                    adj_list[current_vertex].append(neighbor_name)
                neighbor_name = ""
                parser_state = 0

    return Graph(vertices, adj_list)
