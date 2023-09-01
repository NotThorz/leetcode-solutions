#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#

# @lc code=start
class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.d = defaultdict(set)

    def insert(self, val: int) -> bool:
        if val in self.d and len(self.d[val]) > 0:
            res = False
        else:
            res = True

        self.nums.append(val)
        self.d[val].add(len(self.nums)-1)

        return res
        

    def remove(self, val: int) -> bool:

        if val in self.d and len(self.d[val]) > 0:
            pos = self.d[val].pop()

            lpos = len(self.nums) - 1
            lval = self.nums[-1]

            self.d[lval].add(pos)
            self.d[lval].remove(lpos)

            self.nums[pos], self.nums[lpos] = self.nums[lpos], self.nums[pos]

            self.nums.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:

        size = len(self.nums)

        idx = int(random.random() * size)
        
        return self.nums[idx]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

