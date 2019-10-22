#label: maths difficulty: easy

"""
思路：

排列组合题，

只需要找到1~n的质数的个数prime_cnt， 就可以得知质数合法的排列顺序 prime_cnt !,

非质数同理，得到个数之后阶乘就可以知道组合总数，

然后两部分相乘就是整体的方案总数。

"""

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime_cnt = 0
        for i in range(1,n+1):
            if self.prime(i):
                prime_cnt += 1
        return (math.factorial(prime_cnt) * math.factorial(n-prime_cnt)) % (10**9+7)

    def prime(self,n):
        if n == 1:
            return False
        elif n == 2 or n == 3 or n==5:
            return True
        else:
            for i in range(2,int(n**0.5)+1):
                if n % i ==0:
                    return False      
            return True
