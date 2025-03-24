class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x: (x[0], x[1]))

        free_days = 0
        latest_end = 0

        for start, end in meetings:
            if start > latest_end + 1:
                free_days += start - latest_end - 1
            
            latest_end = max(latest_end, end)

        free_days += days - latest_end

        return free_days


            

