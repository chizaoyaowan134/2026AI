def quick_sort(nums, start, end):

    # 如果开始的索引小于结束的索引，说明范围内有两个或以上的元素需要排序
    if start < end:

        # 选择第一个元素作为基准值
        pivot = nums[start]
        low = start
        high = end

        # 两下标未相遇时继续循环
        while low < high:
            # 从右向左移动high指针，找到第一个小于基准值的元素
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]      # 将找到的元素放到low位置

            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]

        nums[low] = pivot

        quick_sort(nums, start, low - 1)
        quick_sort(nums, low + 1, end)




# --- 测试代码 ---
import random
# 生成随机数据
data = [random.randint(1, 100) for _ in range(15)]
print(f"原始列表: {data}")
quick_sort(data, 0, len(data) - 1)
print(f"排序结果: {data}")
