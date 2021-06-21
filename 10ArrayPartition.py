# leetcode 561
# n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하기

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])