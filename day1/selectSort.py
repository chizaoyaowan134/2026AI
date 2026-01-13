'''
直接选择排序
'''

def insertionSort(nums):
    for i in range(0, len(nums)):
        minIndex = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j
        if minIndex != i:
            temp = nums[i]
            nums[i] = nums[minIndex]
            nums[minIndex] = temp

list = [3, 5, 1, 8, 6, 9, 7, 0, 2]
insertionSort(list)
print(list)