class MyHashMap:

	class Node(object):
		def __init__(self, key, val):
			self.key = key
			self.val = val
			self.next = None

	def __init__(self):
		self.Hashlist = [None] * 10000

	def h1(self, key):
		return key % len(self.Hashlist)
    
	def find_node(self, head, key):
		pointer = head
		while pointer.next != None and pointer.next.key != key:
			pointer = pointer.next
		return pointer      

	def put(self, key, value):
		
		if not self.Hashlist[self.h1(key)]:
			self.Hashlist[self.h1(key)] = self.Node(-1, -1)
		prev = self.find_node(self.Hashlist[self.h1(key)], key)

		if not prev.next:
			prev.next = self.Node(key, value)
		else:
			prev.next.val = value
	


	def get(self, key):
		if not self.Hashlist[self.h1(key)]:
			return -1
		prev = self.find_node(self.Hashlist[self.h1(key)], key)
		
		return -1 if prev.next == None else prev.next.val
	
	def remove(self, key):
		if self.Hashlist[self.h1(key)] == None:
			return
		prev = self.find_node(self.Hashlist[self.h1(key)], key)
		if prev.next == None:
			return None
		prev.next = prev.next.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)