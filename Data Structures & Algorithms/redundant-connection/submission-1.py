class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph_size = len(edges)

        parents = [i for i in range(graph_size + 1)]
        rank = [1 for _ in range(graph_size + 1)]
        
        
        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            
            return parents[node]


        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return False

            if parent1 != parent2:
                if rank[parent1] > rank[parent2]:
                    parents[parent2] = parent1
                elif rank[parent2] > rank[parent1]:
                    parents[parent1] = parent2
                else:
                    parents[parent2] = parent1
                    rank[parent1] += 1
            
            return True

        

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
        
        return []
