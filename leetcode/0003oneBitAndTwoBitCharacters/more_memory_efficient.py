class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        state = 'A'
        for i in range(len(bits) - 1):
            if state == 'A':
                if bits[i] == 1:
                    state = 'B'
            elif state == 'B':
                state = 'A'
        return state == 'A'
