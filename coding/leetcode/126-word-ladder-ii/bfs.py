class Solution:
    def findLadders(self, beginWord: str, endWord: str, 
                    wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordSet = set(wordList) # faster checks against dictionary
        layer = {}
        # stores current word and all possible sequences how we got to it
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            # returns [] on missing keys, just to simplify code

            for word in layer:
                if word == endWord:
                    # return all found sequences
                    return layer[word] 
                for i in range(len(word)): 
                    # change every possible letter and check if it's in dictionary
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord =  word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            # add new word to all sequences and form new layer element
                            newlayer[newWord] += [j + [newWord] for j in layer[word]] 
            wordSet -= set(newlayer.keys()) # remove from dictionary to prevent loops
            layer = newlayer # move down to new layer

        return []
