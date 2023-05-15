

def validate_brackets(s: str) -> bool:
    stack = []
    for c in s:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            if not stack:
                return False
            if (c == ")" and stack[-1] == "(") or \
               (c == "]" and stack[-1] == "[") or \
               (c == "}" and stack[-1] == "{"):
                stack.pop()
            else:
                return False
    return not stack
