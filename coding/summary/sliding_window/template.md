# Template

[Explaination Details](./summary.md) | [Template Index](../template_list.md)

```python
# for LC Problem 76
# window is [left, right) [close and open)
def sliding_window(s, t):
    """ s, t are iterable """
    need, window = {}, {}  # counters
    [need.setdefault(c, 1) for c in t]
    # need = {A: 1, B: 1, C: 1}
    left = right = 0
    valid = 0
    while right < len(s):
        c = s[right]
        right += 1  # move right window
        # ... update window

        print(f"left={left}, right={right}")
        # check left window
        while window needs shrink:
            d = s[left]
            left += 1
            # ... update window
```

LC: 76, 567, 438, 3