# Two pointers

## Squeeze to middle direction

```python
def partition(self, A, start, end):
    """ partition in quicksort """
    if start >= end: return
    left, right = start, end

    pivot = A[(start + end) // 2]
    while left <= right:
        while left <= right and A[left] < pivot:
                left += 1
        while left <= right and A[right] > pivot:
                right -= 1
        if left <= right: 
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
    return left
```

See also: [quick select](./sort/quickselect.py)

## Expand from the middle

```python
left = position
right = position + 1
while left >= 0 and right < len(s):
    if left and right are out of bound, or meeting condition:
        break
    left -= 1
    right += 1
```

## Same direction

```python
j = 0
for i in range(n):
    while j < n and not meet_condition(i, j):
        j += 1
    if meet_condition(i, j):
        process this [i, j]
```

## Merge two points

```python
def merge(list1, list2):
    new_list = []
    i, j = 0, 0
    # don't use list.pop() since it is O(n)
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
    # merge the rest
    while i < len(list1):
        new_list.append(list1[i])
        i += 1
    while j < len(list2):
        new_list.append(list2[j])
        j += 1
    return new_list
```
