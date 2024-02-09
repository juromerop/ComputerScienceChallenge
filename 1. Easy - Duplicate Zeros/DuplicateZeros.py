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