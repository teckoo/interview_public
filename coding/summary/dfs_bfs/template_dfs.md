# DFS - Template I: recursive

[Explaination Details](./summary.md) | [Template Index](../template_list.md)

```python
def DFS(Node cur, Node target, Set<Node> visited):
    return True if cur is target
    for next in each_neighbor_of_cur:
        if next not in visited:
            add next to visted
            return true if DFS(next, target, visited)
    return False
}
```

## DFS - Template II: iteration

```python
def DFS(root, target):
    Set<Node> visited = set()
    stack = collections.deque()
    stack.append(root)
    while s is not empty:
        Node cur = stack.pop()
        if cur is target: return result 
        for next in cur.neighbors:
            if next not in visited: 
                visited.add(next)
                stack.append(next)
    return result
```
