#label: sort difficulty: medium

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key = lambda x: [-len(x), x])#对字典d进行排序，第一关键字是长度升序，第二关键字是字符串本身字典序
        def f(c):                   #匹配函数
            i = 0
            for j in c:             #遍历单词里的字母
                k = s.find(j, i)    #查找函数，后一个参数是查找起点
                if k == -1:
                    return False    #查找失败就返回错误
                i = k + 1           #查找成功就更新查找起点
            return True
        for c in d:                 #遍历有序字典里的单词
            if f(c):                #如果匹配就返回单词
                return c
        return ''

