class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = list(s)
        
        for i in range(len(li)):
            if not li[i].isalpha() and not li[i].isdigit():
                li[i] = ""
        reStr = "".join(li)
        reStr = reStr.lower()
        print(reStr)
        return reStr == reStr[::-1]
        