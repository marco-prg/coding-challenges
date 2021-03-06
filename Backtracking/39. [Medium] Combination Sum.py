# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return 

            for item in candidates:
                if item > remain:
                    break
                if stack and item < stack[-1]:
                    continue
                
                dfs(remain - item, stack + [item])

        dfs(target, [])
        return result


# Array - Backtracking