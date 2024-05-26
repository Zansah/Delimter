def isValid(given_string):
    mapping = {")": "(", "]": "[", "}": "{"}    
    stack = []

    for char in given_string:
        if char in mapping:
            if stack:
                top_element = stack.pop()
            else:
                top_element = "dummy"
            
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    if not stack:
        return True # checks if the stack is empty is so that brackets were matched correctly
    else:
        return False

print(isValid("()[]{}"))
print(isValid("([)]")) 