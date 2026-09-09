class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        state = 'A'
        def transition(c, state):
            if state == 'A':
                if c == 1:
                    return 'B'
                return state
            elif state == 'B':
                return 'A'
        for c in bits[:-1]:
            state = transition(c, state)
        return state == 'A'

