class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # find the item reach the boundary
        idx, count, size = 0, 0, len(arr)
        while count < size:
            if arr[idx] == 0:
                count += 1
            count += 1
            if count >= size:
                break
            idx += 1
        # print(f"arr[{idx}] = {arr[idx]}, {count}")    
        overflow = count > size
        if arr[idx] == 0 and overflow:
            arr[-1] = 0
            idx -= 1
            pos = size - 2
        else:
            pos = size - 1

        for i in range(idx, -1, -1):
            if arr[i] == 0:
                arr[pos], arr[pos - 1] = 0, 0
                pos -= 2
            else:
                arr[pos] = arr[i]
                pos -= 1
