#label: 二分查找 difficulty: medium

"""
思路：

二分查找找到离x最近的数，然后在附近搜索差最小的数

"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        self.res = []
        def find(arr, left, right, k, x):
            while k>0:
                k-=1
                if left<0:
                    self.res += arr[right:right+k+1]
                    break
                elif right>=len(arr):
                    self.res = arr[left-k:left+1] + self.res 
                    break
                elif abs(arr[left]-x) <= abs(arr[right]-x):
                    self.res = [arr[left]] + self.res
                    left -= 1
                else:
                    self.res += [arr[right]]
                    right += 1
           
        
        left, right = 0, len(arr)
        while left<right:
            mid = (left+right)//2
            if arr[mid] == x:
                self.res.append(x)
                find(arr, mid-1, mid+1, k-1, x)
                return self.res
            
            elif arr[mid]>x:
                right = mid
            else:
                left = mid+1
        find(arr, left-1, right, k, x)
        return self.res
