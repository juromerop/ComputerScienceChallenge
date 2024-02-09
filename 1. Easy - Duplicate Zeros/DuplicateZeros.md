# Duplicate Zeros
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: O(n)
(O(1) to pop the last element of the list)

- Space complexity: O(1)

# Code
```
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        just_added = False
        for position in range(len(arr)):
            if arr[position] == 0 and not just_added:
                arr.insert(position, 0)
                just_added=True
                arr.pop()
            else:
                just_added=False
```