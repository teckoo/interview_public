class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map_1 = {}
        min_index = len(list1) + len(list2)
        result = []
        for i, dinner in enumerate(list1):
            map_1[dinner] = i

        for j, dinner in enumerate(list2):
            if dinner in map_1:
                if map_1[dinner] + j < min_index:
                    min_index = map_1[dinner] + j
                    result = [dinner]
                elif map_1[dinner] + j == min_index:
                    result.append(dinner)

        return result
