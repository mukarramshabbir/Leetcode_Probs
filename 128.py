def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_set = set(nums)
    longest_sequence = 0

    for num in num_set:
        # Only process if num is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1

            # Check for consecutive elements in the positive direction
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1

            # Update longest_sequence if necessary
            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence
        
        
if __name__=="__main__":
    nums = [100,4,200,1,3,2]
    n = longestConsecutive(nums)
    print(n)