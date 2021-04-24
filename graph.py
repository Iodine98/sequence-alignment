class Vertex:
    def __init__(self, id_prop):
        self.id = id_prop


class Graph:
    def __init__(self, graph_obj):
        self.vertices = [Vertex(v) for v in graph_obj.keys()]
        self.edges = graph_obj.values()


if __name__ == '__main__':
    graph_object = {
        'a': ['b', 'c'],
        'b': ['a', 'c'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['c', 'e'],
        'e': ['c', 'd']
    }
    print(graph_object)
