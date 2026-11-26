class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        
        full_weeks_sum = weeks * 28 + 7 * weeks * (weeks - 1) // 2
        start_val = weeks + 1
        remaining_days_sum = days * start_val + days * (days - 1) // 2
        
        return full_weeks_sum + remaining_days_sum