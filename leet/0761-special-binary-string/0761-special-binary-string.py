class Solution:
    def makeLargestSpecial(self, s: str) -> str:
     
        if len(s) <= 2:
            return s

        substrings = []
        count = 0
        start = 0

      
        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
               
                inner = self.makeLargestSpecial(s[start + 1:i])
                substrings.append("1" + inner + "0")
                start = i + 1

      
        substrings.sort(reverse=True)

        
        return "".join(substrings)



if __name__ == "__main__":
    sol = Solution()
    print(sol.makeLargestSpecial("11011000"))  
    print(sol.makeLargestSpecial("10"))        
