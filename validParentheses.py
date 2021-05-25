class Solution:
    def isValid(self, s: str) -> bool:

        # This acts as a stack to track the open characters '([{'
        open_chars = []

        # Loop through the given string
        for char in s:

            # if there is an open character add it to the top of the 'stack'
            if char in '({[':
                open_chars.append(char)
            elif len(open_chars) == 0:
                # This conditional takes care of the case that there is a close character with nothing on the stack
                return False

            # In these conditionals if a close character is found the top of the stack is checked for the corresponding
            # open character, which if found is popped off the stack
            if char == ')':
                if open_chars[-1] == '(':
                    open_chars.pop()
                else:
                    return False
            if char == ']':
                if open_chars[-1] == '[':
                    open_chars.pop()
                else:
                    return False
            if char == '}':
                if open_chars[-1] == '{':
                    open_chars.pop()
                else:
                    return False

        # if any characters are left on the stack then there existed open characters that were not closed
        if len(open_chars) > 0:
            return False
        else:
            return True