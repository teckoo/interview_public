class Solution:
    def numSquares(self, n: int) -> int:
        # list of squre numbers < n
        square_nums = [i * i for i in range(1, int(n**0.5) + 1)]
        
        level = 0
        que = {n}
        while que:
            level += 1
            # important to use set() to remove redundency
            next_que = set()
            for remainder in que:
                if remainder in square_nums:
                    return level  # find the node
                # construct the next level
                for square_num in square_nums:
                    if remainder > square_num:
                        next_que.add(remainder - square_num)
            que = next_que           
        return level
