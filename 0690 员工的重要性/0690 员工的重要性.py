#label: BFS/DFS difficulty: easy

"""
第一种思路：

BFS实现。

"""

class Solution(object):
    def getImportance(self, employees, i):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        res = 0
        hashmap = dict()
        
        for employee in employees:
            hashmap[employee.id] = [employee.importance, employee.subordinates]
        
        queue = [i]
        while(queue):
            next_queue = []
            for item in queue:
                res += hashmap[item][0]
                next_queue += hashmap[item][1] #把下属列表加入下一次的queue                
            queue = next_queue[:]
            
        return res

“”“
第二种思路：

DFS，res每次先加自己的importance，再去找下属。

”“”

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, i):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        self.res = 0
        
        def dfs(subs):          
            for sub in subs:
                for employee in employees:
                    if employee.id == sub:#就是这个要找的员工
                        self.res += employee.importance                
                        dfs(employee.subordinates)#找他的下属员工
                
        dfs([i])       
        return self.res

“”“
第三种思路：

在第一种思路的基础上优化，不需要每次都从employees里遍历查找importance和subordinates，

而是用一个hashmap先记录好所有需要的结果，这样可以极大地提高查找速度。

”“”

class Solution(object):
    def getImportance(self, employees, i):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        self.res = 0
        hashmap = dict()
        
        for employee in employees:
            hashmap[employee.id] = [employee.importance, employee.subordinates]
        
        def dfs(subs):          
            for sub in subs:               
                self.res += hashmap[sub][0]                
                dfs(hashmap[sub][1])#找他的下属员工
 
        dfs([i])       
        return self.res

