class Graph:
    def __init__(self):
        self.graph_dict = {}

    def addEdge(self,node,neighbour):  
        if node not in self.graph_dict:
            self.graph_dict[node]=[neighbour]
        else:
            self.graph_dict[node].append(neighbour)

    def show_edges(self):
        result = {}
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                result.update({ node: neighbour })
        print(result)

g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'C')
g.addEdge('B', 'A')
g.addEdge('C', 'A')
g.addEdge('C', 'B')
g.addEdge('C', 'D')
g.addEdge('D', 'C')
g.show_edges() # C A D C