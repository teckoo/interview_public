# Template

[Explaination Details](./summary.md) | [Template Index](../template_list.md)

```python
def rand10():
    """ rand7 to rand10 """
    n = rand7() + (rand7() - 1) * 7
    while n > 40:
        n = rand7() + (rand7() - 1) * 7
    return 1 + n % 10
```

LC:
* [470. Implement Rand10() Using Rand7()](../../leetcode/470-implement-rand10-using-rand7/solution.py)
