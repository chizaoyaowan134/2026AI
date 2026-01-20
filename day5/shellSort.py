'''
希尔排序
'''

def shell_sort(nums):
    # 初始步长
    step = len(nums) // 2
    # 当步长大于0时，继续排序
    while step > 0:
        #---以下是希尔排序的步骤，只需要修改步长即可---
        # 遍历每个子列表的起始位置
        for i in range(step, len(nums)):
            # 记录当前元素
            current = nums[i]
            # 从本组中的前一个位置开始比较，下表为i-step
            j = i - step
            # 遍历本组中前面的所有元素，若本组中前面的元素大于current，则将其后移
            while j >= 0 and nums[j] > current:
                nums[j + step] = nums[j]
                j -= step
            # 将current放到正确位置
            nums[j + step] = current
        # 减小步长
        step //= 2
# 待排序列表
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("排序前：", nums)
shell_sort(nums)
print("排序后：", nums)