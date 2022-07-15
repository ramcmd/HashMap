# TC: O(1)
# SC: O(n)

class MyHashMap:

    def __init__(self):
        self.bucketlen = 1000
        self.bucket = [None] * self.bucketlen
    
    def h1(self, key):
        return key%len(self.bucket)
    
    def h2(self, key):
        return key//self.bucketlen
        
    def put(self, key: int, value: int) -> None:
        if not self.bucket[self.h1(key)] and self.h1(key) == 0:
            self.bucket[self.h1(key)] = [-1] * (self.bucketlen+1)
        elif not self.bucket[self.h1(key)]:
            self.bucket[self.h1(key)] = [-1] * self.bucketlen
                    
        self.bucket[self.h1(key)][self.h2(key)] = value
        
    def get(self, key: int) -> int:
        if self.bucket[self.h1(key)]:
            return self.bucket[self.h1(key)][self.h2(key)]
        else:
            return -1

    def remove(self, key: int) -> None:
        if self.bucket[self.h1(key)]:
            self.bucket[self.h1(key)][self.h2(key)] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)