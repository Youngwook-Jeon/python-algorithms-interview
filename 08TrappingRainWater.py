# leetcode 42
# 막대의 높이들의 배열이 주어졌을때 담을 수 있는 물의 양 리턴
class Solution:
    # 투포인터 이용한 첫번째 방법
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volume = 0
        left = 0 
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        
        while (left < right):
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
    
    # 스택을 이용한 풀이
    def trap2(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break

                dist = i - stack[-1] - 1
                water = min(height[i], height[stack[-1]]) - height[top]
                volume += dist * water

            stack.append(i)
        return volume
        