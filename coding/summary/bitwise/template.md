# Template

[Explaination Details](./summary.md) | [Template Index](../template_list.md)

```python
def find_rightmost_1(number):
    if not number: return 0
    rightmost_set_bit = 1
    while (rightmost_set_bit & number) == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    return rightmost_set_bit

def find_rightmost_0(number):
    if not number: return 0
    cnt = 0
    while (number & 1) == 1:
        number >>= 1
        cnt += 1
    return cnt  # or return 1 << cnt

    # result for reference
    (0, 0), (1, 1), (2, 0), (3, 2), (4, 0),
    (5, 1), (6, 0), (7, 3), (8, 0), (9, 1),
```

This can be used as a trick to separate numbers into two groups based this bit. E.g.

```python
    num1, num2 = 0, 0

    for num in nums:
        if (num & rightmost_set_bit) != 0:  # the bit is set
            num1 ^= num
        else:  # the bit is not set
            num2 ^= num
```

[Bitwise to find the missing number](./find_missing_number.py)