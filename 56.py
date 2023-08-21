def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x:x[0])
    merged_intervals=[intervals[0]]
    for i in range(1,len(intervals)):
        current_intervals=intervals[i]
        previous_interval=merged_intervals[-1]
        if current_intervals[0]<=previous_interval[1]:
            merged_intervals[-1]=[previous_interval[0],max(previous_interval[1],current_intervals[1])]
        else:
            merged_intervals.append(current_intervals)
    return merged_intervals
    
if __name__=="__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    res=merge(intervals)
    print(res)