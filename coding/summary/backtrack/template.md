# Template

[Explaination Details](./summary.md) | [Template Index](../template_list.md)

```python
result = []
def backtrack(path, candidate_list):
    if meet_condition:
        result.add(path)
        return

    for choice in candidate_list:
        # make choice
        backtrack(path, new_candidate_list)
        # restore choice
```
