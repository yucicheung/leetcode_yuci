class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_start = 0
        str_end = 1
        #longest_str = ''
        ch_dict = {}
        longest_length = 0
        
        str_length = len(s)
        if str_length:
            longest_length = 1
            ch_dict[s[0]] = 0
        while str_end < str_length:
            ch = s[str_end]
            string = s[str_start:str_end]
            if ch not in string:
                longest_length = max(str_end - str_start + 1, longest_length)
                #longest_str = string+ch
            else:
                str_start = ch_dict[ch] + 1
            ch_dict[ch] = str_end
            str_end += 1
            
        return longest_length
        
while True:
	string = raw_input('The string you want to test:')
	print Solution().lengthOfLongestSubstring(string)

        
