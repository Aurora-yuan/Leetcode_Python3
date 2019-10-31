#label: array difficulty: easy

"""
第一种思路：

马上就能想到的比较麻瓜的思路：

每次查询后就改变对应的值，然后sum一下数组里的偶数元素，

这种思路问题是太慢了我就没有实现，参考评论区会出现超时的情况

"""

"""
第二种思路：

 先sum一下数组里所有的偶数元素，把这个值设为sumOfEven的初始值，

 然后线性扫描queries里的每个元素，可以得到每次查询的数组元素下标和数组元素下标对应值的改变的值

 如果查询之前是奇数，查询之后也是奇数，就直接PASS，这种情况跟结果无关，

 如果查询之前是奇数，查询之后变成了偶数，就需要把数组元素的值和改变的值都加在res上，

 如果查询之前是偶数，查询之后还是偶数，就只需把改变的值加在res上，

 如果查询之前是偶数，查询之后变成了奇数，就从res里减去数组元素的值。
 
"""

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sumOfEven = sum(num for num in A if  not num % 2)
        result = []
        
        for item in queries:
            value = item[0]
            index = item[1]
            newvalue = A[index] + value
            
            if not A[index] % 2 and not newvalue % 2: # even and even
                sumOfEven += value
            elif not A[index] % 2 and newvalue % 2:  # even and odd
                sumOfEven -= A[index] 
            elif A[index] % 2 and not newvalue % 2:  # odd and even
                sumOfEven += newvalue
                
            result.append(sumOfEven)            
            A[index] = newvalue
            
        return result

