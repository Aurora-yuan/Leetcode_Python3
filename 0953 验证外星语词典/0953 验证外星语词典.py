#label: dictionary difficulty: easy

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n=len(words)
        m=len(order)
        dic={}
        for i in range(m):
            if order[i] not in dic:
                dic[order[i]]=i+1
        flag=1
        for i in range(0,n-1):
            s1=len(words[i])
            s2=len(words[i+1])
            if s1>s2 and words[i][0:s2]==words[i+1]:
                flag=0
                break
            k=0
            while k<s1 and k<s2:
                if dic[words[i][k]]<dic[words[i+1][k]]:
                    flag=1
                    break
                elif dic[words[i][k]]>dic[words[i+1][k]]:
                    flag=0
                    break
                k+=1
            if 0==flag:
                break
        if flag:
            return True
        else:
            return False
        


