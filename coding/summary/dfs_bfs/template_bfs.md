# Template

[Explaination Details](./summary.md) | [Template Index](../template_list.md)

1. topo sort
2. find-union
3. level traverse
4. MST, graph
5. games, state search

```python
# 计算从起点 start 到终点 target 的最近距离
def BFS(Node start, Node target):
    q = collections.deque()  # 核心数据结构
    visited = set() # 避免走回头路

    q.append(start)  # 将起点加入队列
    visited.add(start)
    step = 0  # 记录扩散的步数

    while not q: 
        sz = len(q)
        # 将当前队列中的所有节点向四周扩散
        for _ in range(sz):
            cur = q.popleft()  # poll
            # 划重点：这里判断是否到达终点 
            if cur is target: return step

            # 将 cur 的相邻节点加入队列 
            for x in cur.adj():
                if (x not in visited):
                    q.append(x)
                    visited.add(x)
        step += 1  # 划重点：更新步数在这里
```
