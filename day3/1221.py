def max_balanced_substrings(s):
    count_L, count_R = 0, 0
    result = 0

    for char in s:
        if char == 'L':
            count_L += 1
        else:
            count_R += 1

        if count_L == count_R:
            result += 1

    return result

# Example usage
s = "RLRRRLLRLL"
output = max_balanced_substrings(s)
print(output)  # Output: 2

        
