def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])  # Sort intervals by ending time
    end = intervals[0][1]
    count = 0

    for i in range(1, len(intervals)):
        if intervals[i][0] < end:  # Overlapping interval
            count += 1
        else:
            end = intervals[i][1]  # Update non-overlapping ending time

    return count

if __name__=="__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    res=eraseOverlapIntervals(intervals)
    print(res)