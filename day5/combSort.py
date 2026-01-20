def comb_sort(nums):
    """
    梳排序：引入希尔排序“步长递减”思想的冒泡排序改进版
    """
    length = len(nums)
    gap = length
    # 递减因子，经验证 1.3 是最佳值
    shrink_factor = 1.3
    sorted = False

    # 只要 gap > 1 或者还没排好序（sorted为False），就继续循环
    while gap > 1 or not sorted:
        # 1. 更新步长 (向下取整)
        gap = int(gap / shrink_factor)
        # 步长最小不能小于 1
        if gap < 1:
            gap = 1

        # 2. 假设这一轮排好了（如果发生交换则置为False）
        # 这一步对于 gap=1 时非常重要，相当于冒泡排序的优化标志位
        sorted = True

        # 3. 执行“带步长的冒泡”
        i = 0
        while i + gap < length:
            # 比较跨度为 gap 的两个元素
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                sorted = False  # 发生了交换，说明没排好
            i += 1

    return nums


# --- 测试代码 ---
import random

# 生成随机数据
data = [random.randint(1, 100) for _ in range(15)]
print(f"原始列表: {data}")

comb_sort(data)
print(f"排序结果: {data}")