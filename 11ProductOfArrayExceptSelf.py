# leetcode: 238
# 배열을 입력받아 새로운 배열 arr을 리턴하는데, arr[i]는 nums[i]를 제외한 나머지 모든 요소의 곱셈값이 되도록 출력하기
# Remark: 나눗셈을 하지않고 O(n)에 풀기

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]
        prod = 1
        for i in range(len(nums) - 1): # 오른쪽으로 한칸 밀어서 곱해나가기
            prod *= nums[i] 
            arr.append(prod)
        prod = 1
        for i in range(len(nums) - 1, -1, -1): # 왼쪽으로 한칸 밀어서 곱하기
            arr[i] *= prod
            prod *= nums[i] # 그 두 결과를 곱해서 원하는 값 만들기
        return arr