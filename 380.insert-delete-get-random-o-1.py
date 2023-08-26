#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.values=[]
        self.values_to_index={}

    def insert(self, val: int) -> bool:
        if val in self.values_to_index:
            return False
        self.values.append(val)
        self.values_to_index[val]=len(self.values)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values_to_index:
            return False

        index_to_remove = self.values_to_index[val]
        last_val = self.values[-1]

        self.values[index_to_remove] = last_val
        self.values_to_index[last_val] = index_to_remove
        del self.values_to_index[val]
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

