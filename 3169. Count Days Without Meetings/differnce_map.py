from collections import defaultdict

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        difference_map = defaultdict(int)
            
        for start, end in meetings:
            difference_map[start] += 1
            difference_map[end] -= 1

        events = sorted(difference_map.keys())

        free_days = 0

        in_meeting = 0
        last_end = 0
        for event in events:
            if in_meeting == 0:
                free_days += event - last_end - 1
            
            in_meeting += difference_map[event]
            if in_meeting == 0:
                last_end = event

        
        free_days += days - last_end

        return free_days

            

