def comb_sort(nums):

    length = len(nums)

    gap = length

    shrink_factor = 1.3
    sorted = False

    while gap > 1 or not sorted:
        gap = int(gap / shrink_factor)

        if gap < 1:
            gap = 1


        sorted = True

        i = 0
        while i + gap < length:
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                sorted = False

            i += 1

    return nums



#---测试代码---
import random
data = [random.randint(1, 100) for _ in range(15)]
print(f"原始列表: {data}")
comb_sort(data)
print(f"排序结果: {data}")

