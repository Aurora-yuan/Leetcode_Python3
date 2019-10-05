# label: slidewindow difficulty: easy
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # 函数定义后的箭头：https://blog.csdn.net/sunt2018/article/details/83022493
        res = 0 # 总分
        s = sum(calories[:k])
        for start in range(len(calories)-k+1):
            if start !=0 :
                s += calories[start+k-1] - calories[start-1]  #采取累加的形式，每次往后加一天同时减去之前的一天，避免了在k天内再写一个循环,滑动窗口的思想！！！
            if s < lower:
                res -= 1
            if s > upper:
                res += 1
        return res
    
