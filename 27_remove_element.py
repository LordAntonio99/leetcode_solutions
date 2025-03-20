# 27. Remove Element
# Se da un array de enteros y un valor entero.
# Se debe eliminar todas las ocurrencias del valor en el array.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
