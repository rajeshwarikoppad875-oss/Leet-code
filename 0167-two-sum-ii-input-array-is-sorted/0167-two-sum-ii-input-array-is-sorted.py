class Solution(object):
    def twoSum(self, num, tar):
       l=0
       r=len(num)-1
       while l<r:
            sum=num[l]+num[r]
            if sum == tar:
                return [l + 1 , r + 1]
            elif sum < tar :
                l+=1
            else:
                r-=1       
        