class Solution:
    def oddString(self, words: List[str]) -> str:
        diff = []
        nestlst = []
        for i in words:
            for j in range(len(i)-1):
                var1 = ord(i[j])-97
                var2 = ord(i[j+1])-97
                nestlst.append(var2-var1)
            diff.append(nestlst)
            nestlst = []
        ind = [list(x) for x in set(tuple(x) for x in diff if diff.count(x) == 1)]
        return words[diff.index(ind[0])]
