class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        array = []
        negative = False
        if x < 0:
            negative = True
            x = abs(x)
        while x != 0:
            array.append(x % 10)
            x = (x - abs(x%10))/10
        result = 0
        i = 0
        while(len(array) > 0):
            result += array[-1]*(10**i)
            array.pop()
            i += 1
        if result < -2**31 or result > 2**31-1:
            return 0
        if negative:
            return -int(result)
        return int(result)
