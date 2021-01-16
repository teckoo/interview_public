class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # print(sea.hasShips(Point(1, 1,), Point(0, 0)))
        
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y: return 0
        if not sea.hasShips(topRight, bottomLeft): return 0
        if bottomLeft.x == topRight.x and bottomLeft.y == topRight.y and sea.hasShips(topRight, bottomLeft):
            # print(f"found a ship at ({bottomLeft.x}, {bottomLeft.y})")
            return 1
            
        x_md = (bottomLeft.x + topRight.x) // 2
        y_md = (bottomLeft.y + topRight.y) // 2
        mid_pt = Point(x_md, y_md)
        return self.countShips(sea, mid_pt, bottomLeft) + \
                self.countShips(sea, Point(x_md, topRight.y), Point(bottomLeft.x, y_md + 1)) + \
                self.countShips(sea, Point(topRight.x, y_md), Point(x_md + 1, bottomLeft.y)) + \
                self.countShips(sea, topRight, Point(x_md + 1, y_md + 1))
