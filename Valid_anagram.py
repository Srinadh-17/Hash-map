class Solution(object):
    def isAnagram(self, s, t):
        dictionary={}
        if len(s)!=len(t):
            return False
        for i in t:
            if i not in dictionary:
                dictionary[i]=1
            else:
                dictionary[i]+=1
        for char in s:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False
        
        return True