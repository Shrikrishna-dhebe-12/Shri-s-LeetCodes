class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        original, reversed_num = x, 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return original == reversed_num



sol = Solution()
print(sol.isPalindrome(121))  
print(sol.isPalindrome(-121))  
print(sol.isPalindrome(10))    
