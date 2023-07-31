def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0 or x == 1:
        return x

    left, right = 1, x
    result = 0

    while left <= right:
        mid = left + (right - left) // 2

        # If the square of mid is equal to x, mid is the square root
        if mid * mid == x:
            return mid

        # If the square of mid is less than x, update the result and narrow the search to the right half
        if mid * mid < x:
            left = mid + 1
            result = mid
        else:
            # If the square of mid is greater than x, narrow the search to the left half
            right = mid - 1

    return result

if __name__=="__main__":
    nums = 8
    result = mySqrt(nums)
    print(result)