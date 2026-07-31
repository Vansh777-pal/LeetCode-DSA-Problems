class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
            if v not in graph:
                graph[v] = []
            graph[v].append(u)

        visited = [False] * n
        queue = []
        queue.append(source)
        visited[source] = True

        while queue:
            vertex = queue.pop(0)

            if vertex == destination:
                return True
            for neighbour in graph[vertex]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
        return False