class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        stu_score = {}
        result = []
        for id, score in items:
            stu = stu_score.setdefault(id, [])
            stu.append(score)
        for id in sorted(stu_score):
            scores = stu_score[id]
            score = sum(sorted(scores, reverse=True)[:5])//5
            result.append([id, score])
        return result
