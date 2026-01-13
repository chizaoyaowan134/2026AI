'''
插入排序
'''

def insertionSort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp

list = [7, 4, 3, 8, 0, 4, 3, 5, 1, 6]
insertionSort(list)
print(list)