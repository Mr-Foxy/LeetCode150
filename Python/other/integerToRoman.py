import pdb
class Solution:
  # @return a string
  def intToRoman(self, num):
		res = ""
		while num != 0:
			#pdb.set_trace()
			if num >= 1000:
				res += "M"
				num -= 1000
			if num >= 500 and num < 1000 :
				res += "D"
				num -= 500
			if num >= 100 and num < 500:
				res += "C"
				num -= 100
			if num >= 50 and num < 100:
				res += "L"
				num -= 50
			if num >= 10 and num < 50:
				res += "X"
				num -= 10
			if num >= 5 and num < 10:
				res += "V"
				num -= 5
			if num >= 1 and num < 5:
				res += "I"
				num -= 1
		res = res.replace("VIIII", "IX")
		res = res.replace("IIII", "IV")
		res = res.replace("LXXXX", "XC")
		res = res.replace("XXXX", "XL")
		res = res.replace("DCCCC", "CM")
		res = res.replace("CCCC", "CD")
		return res
	

a = Solution()
print a.intToRoman(9)
