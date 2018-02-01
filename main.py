#!/usr/bin/python

class Solution:
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
        :rtype: int
		"""
		li = list(s)
		if len(li) == 0:
			return 0
		sonLi = [li[0]]
		num = 0
		for i in range(len(li)):
			sonLi.pop(0)
			tmpAdd = 0
			for j in range(i+num,len(li)):
				sonLi.append(li[j])
				if len(sonLi) == len(list(set(sonLi))):
					num = num + 1
				else:
					break
		return num 
				
so = Solution()
print(so.lengthOfLongestSubstring('abcabcbb'))
