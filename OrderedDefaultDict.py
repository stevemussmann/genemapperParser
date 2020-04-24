import collections

#for infinite nesting of OrderedDict
class OrderedDefaultDict(collections.OrderedDict):
	def __missing__(self, key):
		self[key] = type(self)()
		return self[key]