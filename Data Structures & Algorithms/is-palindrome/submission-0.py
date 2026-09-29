class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpnum = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        i,j = 0, len(alpnum)-1
        print(alpnum, i, j)
        while i==j or j>i:
            if alpnum[i] == alpnum[j]:
                i+=1
                j-=1
            else:
                return False
        return True