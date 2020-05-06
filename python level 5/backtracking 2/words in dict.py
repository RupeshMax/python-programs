import collections
def wordBreak( s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    res = collections.defaultdict(list)
    res[0] = [[""]]        

    def dfs(i):
        if i<0:
            return
        else:
            for w in wordDict:
                if s[i-len(w):i]==w:
                    if i-len(w) not in res:
                        dfs(i-len(w))
                    for prefix in res[i-len(w)]:
                        res[i].append(prefix+[w])

    dfs(len(s))
    return [" ".join(words[1:]) for words in res[len(s)]]

for i in range(int(input())):
    n = input()
    dic = input().split()
    s= input()
    for i in wordBreak(s,dic)[::-1]:
        print(i)
