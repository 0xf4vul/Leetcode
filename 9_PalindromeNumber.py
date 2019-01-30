class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        array = []
        y = x
        while x != 0:
            array.append(x % 10)
            x = (x - x%10)/10
        result = 0
        i = 0
        while(len(array) > 0):
            result += array[-1]*(10**i)
            array.pop()
            i += 1
        if y == result:
            return True
        return False

    def adv(self, x):
        return (str(x)==str(x)[::-1])