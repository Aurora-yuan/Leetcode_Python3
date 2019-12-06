#label: stack difficulty: medium

class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ""
        pathlist = path.split('/')
        stack = list()
        for path in pathlist:
            if path == '.' or path == "":
                continue
            elif path == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(path)
        return '/' + '/'.join(stack)
