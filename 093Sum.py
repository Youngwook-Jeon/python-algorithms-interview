# leetcode 15
# 세 수를 더해서 0이 되는 3개의 원소 출력하기
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                summ = nums[left] + nums[right] + nums[i]
                if summ < 0:
                    left += 1
                elif summ > 0:
                    right -= 1
                else:
                    ans.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans