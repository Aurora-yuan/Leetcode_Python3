#label: stack difficulty: medium

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def nestedInteger(x):
            if isinstance(x, int):
                return NestedInteger(x)
            lst = NestedInteger()
            for y in x:
                lst.add(nestedInteger(y))
            return lst
    
        return nestedInteger(eval(s)) #eval(s) = [123, [456, [789]]]

