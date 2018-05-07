#Queue
import heapq as h
import itertools

class QueuePriorityClass:
	heap = []
	entry_finder = {}
	REMOVED = '<removed-item>'
	counter = itertools.count()

	def add_item(self, item, function=0):
		if item.position in self.entry_finder:
			self.remove_item(item)
		count = next(self.counter)
		entry = [function, count, item]
		self.entry_finder[item.position] = entry
		h.heappush(self.heap, entry)

	def remove_item(self, item):
		entry = self.entry_finder.pop(item.position)
		entry[-1] = self.REMOVED

	def pop_item(self):
		while self.heap:
			function, count, item = h.heappop(self.heap)
			if item is not self.REMOVED:
				del self.entry_finder[item.position]
				return item
		raise KeyError('Pop from an empty priority queue!!!')

	def contains(self, position):
		return position in self.entry_finder

	def is_empty(self):
		return self.heap

	def reorder(self):
		return h.heapify(self.heap)

	def __repr__(self):
		return str(self.heap[0][2])

			