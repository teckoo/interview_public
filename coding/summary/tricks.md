# Coding triks

## Initialize a 2-D array

```python
rows = len(grid)
cols = len(grid[0])
dp = [[-1 for _ in range(cols)] for _ in range(rows)]
```

## Define diagonals

Useful in checking matrix, board games.

1. "hill" diagonals（正斜线 in math `y=-x+b`): in coding, `row + column = const`

2. "dale" diagonals (反斜线 in math `y=x+b`): in coding, `row - column = const`

See: LC 52 N-Queens

```python

rows = [0] * n
hills = [0] * (2 * n -1)
dales = [0] * (2 * n -1)

# place
rows[col] = 1
hills[row + col] = 1
dales[row - col] = 1

# remove
rows[col] = 0
hills[row + col] = 0
dales[row - col] = 0

# checking
return not (rows[col] or hills[row + col] or dales[row - col])
```
