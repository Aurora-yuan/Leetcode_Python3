#label: 正则表达式 difficulty: difficult

import re
class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.match(r'\s*[+-]?([\d]+(\.[\d]*)?|\.[\d]+)(e[+-]?[\d]+)? *$', s))

