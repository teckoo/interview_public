class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        res = 0
        right, top = topRight.x, topRight.y
        left, bottom = bottomLeft.x, bottomLeft.y
        q = [(right, top, left, bottom)]
        while len(q) > 0:
            right, top, left, bottom = q.pop(0)

            if left > right or bottom > top:
                continue

            hasShip = sea.hasShips(Point(right, top), Point(left, bottom))
            if hasShip == False:
                continue
            if left == right and top == bottom:
                res += 1
            else:
                midX = (left + right) // 2
                midY = (top + bottom) // 2
                q.append((right, top, midX+1, midY+1))  # top right
                q.append((right, midY, midX+1, bottom))  # bottom right
                q.append((midX, midY, left, bottom))    # bottom left
                q.append((midX, top, left, midY+1))     # top left
        return res
