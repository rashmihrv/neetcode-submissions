class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        ans = []
        for i in strs:
            
            if ''.join(sorted(i)) in hashMap.keys():
                hashMap[''.join(sorted(i))].append(i)
            else:
                hashMap[''.join(sorted(i))] = [i]
        
        for i,k in hashMap.items():
            ans.append(k)

        return ans



        