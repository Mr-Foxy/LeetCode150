import pdb
class Solution:
  # @param path, a string
  # @return a string
  def simplifyPath(self, path):
		res = []
		b = path.replace("/", " ")
		b = b.split()
		pdb.set_trace()
		for i in b:
			if i == "..":
				if res:
					del res[-1]
			elif i == ".":
				continue
			else:
				res.append(i)
		# Create Layout
		str_res = ""
		if not res:
			str_res = "/"
		for str in res:
			str_res += "/" + str 

		return str_res

a = Solution()
test_str = "/abc/..."
print a.simplifyPath(test_str)
        
