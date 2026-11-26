class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur_row, step = 0, -1

        for ch in s:
            rows[cur_row] += ch
            if cur_row == 0 or cur_row == numRows - 1:
                step *= -1
            cur_row += step

        return "".join(rows)



sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))  
print(sol.convert("PAYPALISHIRING", 4))  
print(sol.convert("A", 1))               
