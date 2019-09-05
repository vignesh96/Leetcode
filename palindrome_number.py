class Solution:
    def reverse(self, x: int) -> int:
        """ No string conversion """
        reverse_num = 0
        if x >= 0:
            reverse_num =  int(str(x)[::-1])
        else:
            reverse_num =  int("-" + str(x)[::-1][:-1])
        
        if reverse_num >= (-1) * (2 ** 31) and reverse_num <= (2 ** 31) - 1:
            return reverse_num
        
        return 0
        
 class Solution:
    def reverse(self, x: int) -> int:
        """ With String function """
        return str(x)[::-1] == str(x)
