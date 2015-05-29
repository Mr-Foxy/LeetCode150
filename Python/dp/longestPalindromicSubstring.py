class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        l = len(s)
        table = [[0 for i in range(l)] for j in range(l)]
        for i in range(l):
            table[i][i] = 1
        #print table
        for sub_l  in range(2, l + 1):
            for i in range(l - sub_l + 1):
                sub_str = s[i: i+sub_l]
                #print sub_str
                if self.isPalindrome(sub_str):
                    table[i][i+sub_l - 1] = sub_l
                #print i, sub_l
                candidate_list = []
                table[i][i+sub_l - 1] = max(table[i][i+sub_l - 1], table[i+1][i+sub_l - 1], table[i][i+sub_l-2])
        #print table
        return table[0][l - 1]

    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False;
            i += 1
            j -= 1
        return True

A = Solution()
print A.longestPalindrome("accacc")
#print A.isPalindrome("a")
            
