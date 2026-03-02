class Solution:
    def judgeCircle(self, m: str) -> bool:
        return (m.count('R')-m.count('L'),m.count('U')-m.count('D'))==(0,0)