class LRUCache:
    # @param capacity, an integer
	def __init__(self, capacity):
		self.capacity = capacity
		self.count = 0
		self.value_map = dict()
		self.time_map = dict()
		self.least_used_key = -1

    # @return an integer
	def get(self, key):
		times = self.time_map.get(key) += 1
		return self.value_map.get(key, -1)

	# @param key, an integer
	# @param value, an integer
	# @return nothing
	def set(self, key, value):
		self.count += 1
		if self.count > self.capacity:
			key_list = self.time_map.keys()
			min_times = float("inf")
			min_time_key = -1
			for single in key_list:
				if self.time_map[single] < min_times:
					min_times = self.time_map[single]
					min_time_key = single
			del self.time_map[min_time_key]
			del self.value_map[min_time_key]

		self.value_map[key] = value
		self.time_map[key] = 1
