from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self):

        indegree_dict = defaultdict(int)

        for _, adjancency_list in self.graph.items():
            for adjancency in adjancency_list:
                indegree_dict[adjancency] += 1

        zero_indegree_list = list(set(self.graph.keys()) - set(indegree_dict.keys()))

        ret = []
        while zero_indegree_list:
            v = zero_indegree_list.pop()
            ret.append(v)
            
            for adj in self.graph[v]:
                indegree_dict[adj] -= 1
                if indegree_dict[adj] == 0:
                    zero_indegree_list.append(adj)

        print(ret)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topologicalSort()



