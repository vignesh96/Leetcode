class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        str_N = list(str(N))
        i=1
        while i < len(str_N) and str_N[i-1] <= str_N[i]:
            i += 1
        while 0 < i < len(str_N) and str_N[i] < str_N[i-1]:
            str_N[i-1] =  str(int(str_N[i-1]) - 1)
            i -= 1
        print(i)
        str_N[i+1:] = '9' * (len(str_N) - i - 1)
        return int("".join(str_N))
