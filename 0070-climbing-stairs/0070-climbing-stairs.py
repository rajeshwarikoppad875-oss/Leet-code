class Solution(object):
    def climbStairs(self, n):
        if n==1:
           return 1
        if n==2:
           return 2
        c=1
        r=2   
        for i in range(3, n + 1):
            p =c+r
            c = r
            r = p
        return r

        