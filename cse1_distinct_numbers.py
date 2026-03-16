#Distinct Numbers 

import sys

class Solution(object):
    def distinctNumbers(self, nums, n):
        """
        :type nums: List[int]
        :rtype: int
        """


        #solution 1 (using hashmap) -> timelimit exceeded

        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = hashmap.get(i, 0)+1
        # return len(hashmap)


        #solution 2 (using hashmap) -> timelimit exceeded

        # return len(set(nums))


        #solution 3 (using sorting) -> accepted

        nums.sort()
        count = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                count += 1
        return count

def main():
    input = sys.stdin.readline
    
    n = int(input())
    nums = list(map(int, input().split()))
    
    sol = Solution()
    result = sol.distinctNumbers(nums,n)
    
    print(result)

if __name__ == "__main__":
    main()