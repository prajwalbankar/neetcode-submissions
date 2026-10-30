class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_alnum = ''.join([c for c in s if c.isalnum()]).lower()

        i=0
        j=len(s_alnum)-1

        while i <= j:
            if s_alnum[i] == s_alnum[j]:
                i+=1
                j-=1
                continue
            return False
        return True