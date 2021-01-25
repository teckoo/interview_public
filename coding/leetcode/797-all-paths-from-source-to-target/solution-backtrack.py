class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        
        def bt(node, path):
            if node == target:
                res.append(list(path))
                return
            
            for n in graph[node]:
                path.append(n)
                bt(n, path)
                path.pop()
        
        path = deque([0])
        bt(0, path)
        return res
