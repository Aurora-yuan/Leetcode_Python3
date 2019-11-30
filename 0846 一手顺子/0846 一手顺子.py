#label: Ordered Map difficulty: medium

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False
        hand.sort()
        tmp = collections.Counter(hand)
        for key in tmp:
            if tmp[key] > 0:
                count  = tmp[key]
                for i in range(W):
                    tmp[key+i] -= count
                    if tmp[key+i] < 0:
                        return False
                    
        return True
