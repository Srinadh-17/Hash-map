class Solution(object):
    def groupAnagrams(self, strs):
        ans = {}
        for i in strs:
            srt = str(sorted(i))
            if srt in ans:
                ans[srt].append(i)
            else:
                ans[srt] = [i]
        return list(ans.values())
        