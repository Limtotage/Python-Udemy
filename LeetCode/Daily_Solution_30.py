class Daily_Solution_30:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        curr_start=curr_end=-1
        meeting_days_counter=0
        for start,end in meetings:
            if start>curr_end:
                if curr_end!=-1:
                    meeting_days_counter+=curr_end-curr_start+1
                curr_end,curr_start=end,start    
            else:
                curr_end=max(curr_end,end)
        if curr_end !=-1:
            meeting_days_counter+=curr_end-curr_start+1
        return days-meeting_days_counter
        """
        merged_meetings=[]
        for meeting in meetings:
            if not merged_meetings or meeting[0]>merged_meetings[-1][1]:
                merged_meetings.append(meeting)
            else:
                merged_meetings[-1][1] = max(merged_meetings[-1][1],meeting[1])
        meeting_days_c=0
        for start,end in merged_meetings:
            meeting_days_c+=end-start+1
        return days-meeting_days_c"""
        
