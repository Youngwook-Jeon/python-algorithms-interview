# leetcode 49
# 문자열 배열을 에너그램 단위로 그룹핑하기
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word) # sorted 함수는 결과를 리스트로 리턴
        return anagrams.values()