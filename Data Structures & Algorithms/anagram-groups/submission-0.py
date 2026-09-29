class Solution:
    # def checkAnagrams(self, s: str, t: str) -> bool:
    #     if len(s) != len(t): return False
    #     d={}
    #     for c in s:
    #         d[c] = 1 + d.get(c,0)
        
    #     for j in t:
    #         if d.get(j): d[c] = d[c] - 1
    #         else: return False 
    #     return True       
    def arr_strings (self, s:str) -> List[int]:
        arr = [0] * 26

        for c in s:
            arr[ord(c)-97] = arr[ord(c)-97] + 1

        return arr

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d={}
        # res=[]
        # final=[]
        # for i in range(len(strs)):
        #     for j in range(i+1, len(strs)):
        #         if self.checkAnagrams(strs[i],strs[j]) : 
        #             res.append(strs[j])
        #             # strs.pop(j)
        #         print(self.checkAnagrams(strs[i],strs[j]))
        #     res.append(strs[i])
        #     final.append([res])

        # return final
        d={}
        for i in range(len(strs)):
            item = tuple(self.arr_strings(strs[i]))
            # d.update({item : d.get(item,[]).append(strs[i])})
            if item in d:
                d[item].append(strs[i])
            else:
                d[item] = [strs[i]]
         
        return list(d.values())
        


