#label: maths difficulty: easy

"""
用dpx和dpy两个数组分别存小于bound的x和y的可能的幂倍数，然后双重循环组合即可。

注意当x 或者y 为 1 的时候，需要手动设定dpx， dpy。
"""

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        dpx = list()
        dpy = list()
        res = list()
        if x != 1:
            t = 0
            while( x **t < bound):
                dpx.append(x **t)
                t += 1
        else:
            dpx.append(1)
            
        if y != 1:
            t = 0
            while(y **t < bound):
                dpy.append(y ** t)
                t += 1
        else:
            dpy.append(1)
 

        for p in dpx:
            for q in dpy:
                t = p + q
                if t <= bound:
                    res.append(t)
        
        return list(set(res))


