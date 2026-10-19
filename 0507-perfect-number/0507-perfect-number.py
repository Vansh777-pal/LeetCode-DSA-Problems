class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if (num <= 1):
            return False
        divisor = 1
        i = 2
        while i * i <= num:
            if (num % i == 0):
                divisor +=i
                if (i != num//i):
                    divisor += num//i
            i += 1
        return divisor == num