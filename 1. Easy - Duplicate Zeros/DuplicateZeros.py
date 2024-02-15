'''
My solution to the problem iterates through the array and when it finds a zero, 
it adds a zero to the array and pops the last element, also I used a flag to avoid adding more than one zero.
'''
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