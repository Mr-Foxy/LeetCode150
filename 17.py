class Solution:
	# @param ratings, a list of integer
	# @return an integer
	def candy(self, ratings):
		total_candy = 1
		prev_candy = 1
		seq_len = 1
		max_seq_cnt = 0
		peak_cnt = 0

		for i in range(1, len(ratings)):
			if ratings[i] > ratings[i - 1]:
				if max_seq_cnt != 0:
					prev_candy = 1
				max_seq_cnt = 0
				total_candy += prev_candy + 1
				prev_candy += 1
				seq_len = 1
				peak_cnt = 0
			elif ratings[i] == ratings[i - 1]:
				total_candy += 1
				prev_candy = 1
				seq_len = 1
			else:
				max_seq_cnt = prev_candy
				if seq_len >= max_seq_cnt:
					peak_cnt = 1
				total_candy += seq_len + peak_cnt
				seq_len += 1

		return total_candy

list = [5,4] #3
list2 = [4,5,7,6,4,3,2,4,5,6,3,2] #30
list3 = [1,2,2,1] #6 
list4 = [5,3,1] #6
list5 = [5,6,5] #4
a = Solution()
print a.candy(list)
print a.candy(list2)
print a.candy(list3)
print a.candy(list4)
print a.candy(list5)
