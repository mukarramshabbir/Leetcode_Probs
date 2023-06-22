def isMatch(s, p):
    # Recursive function for backtracking
    def backtrack(s_index, p_index):
        # Base case: If both indices reach the end, it's a match
        if s_index == len(s) and p_index == len(p):
            return True

        # Check if the indices are within bounds
        if s_index >= len(s) or p_index >= len(p):
            return False

        # Check the current characters for a match
        current_match = s[s_index] == p[p_index] or p[p_index] == '.'

        # Check if the next character is '*'
        if p_index + 1 < len(p) and p[p_index + 1] == '*':
            # Case 1: Zero occurrences of the preceding element
            if backtrack(s_index, p_index + 2):
                return True
            # Case 2: One or more occurrences of the preceding element
            while current_match and s_index < len(s):
                if backtrack(s_index + 1, p_index + 2):
                    return True
                s_index += 1
                current_match = s_index < len(s) and (s[s_index] == p[p_index] or p[p_index] == '.')
        elif current_match:
            # If the current characters match, move to the next indices
            return backtrack(s_index + 1, p_index + 1)

        return False

    # Start the backtracking from the first indices
    return backtrack(0, 0)


    
            
if __name__=="__main__":
    s = 'a'
    p='ab*'
    result = isMatch(s,p)
    print(result) 