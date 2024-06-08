open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

def check(myStr):
    stack = []
    for i, char in enumerate(myStr):
        if char in open_list:
            stack.append((char, i))
        elif char in close_list:
            pos = close_list.index(char)
            if stack and open_list[pos] == stack[-1][0]:
                stack.pop()
            else:
                return i
    if not stack:
        return -1
    else:
        return stack[-1][1]

s = input()
print(check(s))
