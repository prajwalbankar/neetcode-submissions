class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets_dict = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        for bracket in s:
            if bracket not in brackets_dict.keys():
                stack.append(bracket)
            else:
                if len(stack)==0:
                    return False
                if stack[-1]==brackets_dict[bracket]:
                    stack.pop()
                else: 
                    return False

        if len(stack)==0:
            return True
        else: return False