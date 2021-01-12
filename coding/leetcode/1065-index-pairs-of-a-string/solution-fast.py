class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res=[]
        for word in words:
            for i in range(len(text)-len(word)+1):
                if text[i:len(word)+i]==word:
                    res.append([i,i+len(word)-1])
        res.sort(key=lambda x:(x[0],x[1]))
        return res
