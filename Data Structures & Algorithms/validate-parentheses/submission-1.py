class Solution:
    def isValid(self, s: str) -> bool:

        hashMap = {}
        hashMap["{"] = "}"
        hashMap["["] = "]"
        hashMap["("] = ")"
        stack = []
        for i in s:
            
            if not stack and i in hashMap.values():
                return False

            elif i in hashMap.values() and i == hashMap[stack[-1]]:
                stack.pop()

            elif stack and i in hashMap.values() and hashMap[stack[-1]] != i:
                return False

            elif i in hashMap.keys():
                stack.append(i)
        
        
        return len(stack) == 0

        